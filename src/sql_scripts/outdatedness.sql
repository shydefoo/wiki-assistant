
SELECT final.page_title, max_rev_timestamp-rev_timestamp as outdatedness
FROM(
    SELECT pl_from, max(rev_timestamp) as max_rev_timestamp
    FROM page
    INNER JOIN
    (
        SELECT pl_from, pl_title, pl_namespace, pl_from_namespace
        FROM pagelinks
        WHERE pl_from in (
			SELECT page.page_id
			FROM page
			WHERE page_id in(
				SELECT cl_from FROM categorylinks where cl_to = %s
			)
		)
     )t3
     ON t3.pl_title = page.page_title and page.page_namespace = t3.pl_namespace
     INNER JOIN revision t5
     ON t5.rev_page = page.page_id
     GROUP BY pl_from
) t7
INNER JOIN
(
    SELECT page_id, rev_timestamp
	FROM (
		SELECT page.page_id, page.page_title, page.page_latest
		FROM page
		WHERE page_id in(
			SELECT cl_from FROM categorylinks where cl_to = %s
			)
	) t1
	INNER JOIN revision
	ON rev_id = page_latest
) t8
on t7.pl_from = t8.page_id
INNER JOIN page final
ON final.page_id = pl_from
ORDER BY outdatedness DESC
LIMIT 1;
