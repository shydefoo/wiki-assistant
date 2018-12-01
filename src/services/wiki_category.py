from db_setup.DBConnect import DBConnect
from utils.wiki_logger import WikiLogger

logger = WikiLogger().logger
db_instance = DBConnect()

def find_pages_under_cat(category):
    query = """SELECT t2.page_id, rev_table.rev_timestamp
            FROM 
            (SELECT cl.cl_from as cl_from FROM categorylinks cl WHERE cl.cl_to = %s) t1
            JOIN
            (SELECT p.page_id, p.page_title, p.page_latest FROM page p) t2
            ON t2.page_id = t1.cl_from
            JOIN
            (SELECT rev.rev_timestamp, rev.rev_id FROM revision rev) rev_table 
            ON rev_table.rev_id = t2.page_latest; """

    db_instance.cursor.execute(query, (category,))
    page_ids = []
    time_stamp = []
    outdatedness_list = []
    for item in db_instance.cursor:
        page_ids.append(item[0])
        time_stamp.append(int(item[1]))
    logger.debug("page_ids: {}, len: {}".format(page_ids, len(page_ids)))
    logger.debug("timestamp: {}, len: {}".format(time_stamp, len(time_stamp)))

    for page, timestamp in zip(page_ids, time_stamp):
        outdatedness = 0
        
        find_links = 'SELECT page_id, page_latest ' \
                     'FROM page ' \
                     'WHERE page_title IN ' \
                     '(SELECT pl_title FROM pagelinks WHERE pl_from = %s)'
        db_instance.cursor.execute(find_links, (page, ))
        links = db_instance.cursor.fetchall()
        if len(links)>0:
            new_link = []
            for link in links:
                get_timestamp = 'SELECT rev_timestamp ' \
                                'FROM revision ' \
                                'WHERE rev_id = %s'
                db_instance.cursor.execute(get_timestamp, (link[1],))
                link_timestamp = db_instance.cursor.fetchall()
                if len(link_timestamp)>0:
                    link_timestamp = int(link_timestamp[0][0])
                    new_link.append([link[0], link_timestamp])
                    diff = link_timestamp - timestamp # modified later means link_timestamp > timestamp i.e diff > 0
                    outdatedness = max(outdatedness, diff)
        outdatedness_list.append(outdatedness)
    logger.debug(outdatedness_list)
    outdated_page = page_ids[outdatedness_list.index(max(outdatedness_list))]
    db_instance.cursor.execute('SELECT page_title FROM page WHERE page_id = %s', (outdated_page,))
    page = db_instance.cursor.fetchone()
    page = str(page[0], 'utf-8')
    logger.debug(page)
    return page


if __name__ == "__main__":
    logger.debug(find_pages_under_cat('Yorkshire'))