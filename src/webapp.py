import os
from utils.wiki_logger import WikiLogger
from flask import Flask
from flask import request, Response, render_template, jsonify
from services import wiki_cateogry_service, normal_sql_service
from db_setup.load_sql_scripts import *
app = Flask(__name__)
from threading import Thread

logger = WikiLogger(__name__).logger

@app.route('/')
def homepage():
    return render_template('dashboard.html')

@app.route('/find_outdated_page', methods=['POST'])
def find_outdated_cat():
    if request.method == 'POST':
        category = request.form.get('category', None)
        if category is not None:
            try:
                service = wiki_cateogry_service.OutdatednessByCat()
                result, time = service.get_result(category)
                logger.info("Query time: {}".format(time))
                return Response(time + result)
            except Exception as e:
                return Response(str(e))
        else:
            return Response("")

@app.route('/query', methods=['POST'])
def perform_query():
    logger.info(request.form)
    query = request.form.get('query', None)
    if query is not None and len(query)>0 :
        service = normal_sql_service.ExecuteQuery()
        try:
            result, time = service.get_result(query)
            logger.info("Query time: {}".format(time))
            return Response(time + result)
        except Exception as e:
            return Response(str(e))
    else:
        return Response("Empty Query")

@app.route('/load_pages')
def load_wiki_pages():
    try:
        p = Thread(target=load_page)
        p.start()
        # load_page()
        return Response('Load Page Completed')
    except Exception as e:
        return Response(str(e))

@app.route('/load_cat')
def load_wiki_cat():
    try:
        load_cat()
        return Response('Load Cat Completed')
    except Exception as e:
        return Response(str(e))

@app.route('/load_pagelinks')
def load_wiki_pagelinks():
    try:
        p = Thread(target=load_pagelinks)
        # load_pagelinks()
        p.start()
        return Response('Load Pagelinks')
    except Exception as e:
        return Response(str(e))

@app.route('/load_catlinks')
def load_wiki_catlinks():
    try:
        p = Thread(target=load_catlinks)
        p.start()
        # load_catlinks()
        return Response('Load catlinks completed')
    except Exception as e:
        return Response(str(e))

@app.route('/load_revisions')
def load_wiki_revision():
    try:
        p = Thread(target=load_revisions)
        p.start()
        # load_revisions()
        return Response('Load Revisions')
    except Exception as e:
        return Response(str(e))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False)
