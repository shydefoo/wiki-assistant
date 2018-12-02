SELECT page_title, outdatedness
FROM page
INNER JOIN
(
	SELECT pl_from, outdatedness
	FROM (
	    SELECT pl_from, max_rev_timestamp-rev_timestamp as outdatedness
	    FROM(
	        SELECT pl_from, max(rev_timestamp_link) as max_rev_timestamp
	        FROM
	        (
	            SELECT pl_from, page_id, rev_timestamp as rev_timestamp_link
	            FROM
	            (
	                SELECT pl_from, page_id, page_latest
	                FROM page
	                INNER JOIN
	                (
	                    SELECT pl_from, pl_title, pl_namespace, pl_from_namespace
	                    FROM pagelinks
	                    WHERE pl_from in (
	                        SELECT page_id FROM (
								SELECT t1.page_id
								FROM(
									SELECT page.page_id, page.page_title, page.page_latest
									FROM page
									WHERE page_id in(
										SELECT cl_from FROM categorylinks where cl_to = %s
									)
								) t1
							)t2_1
	                    )
	                )t3
	                ON t3.pl_title = page.page_title and page.page_namespace = t3.pl_namespace
	            )t4
	            INNER JOIN
	            (
	                SELECT rev_page, rev_timestamp
	                FROM revision
	            )t5
	            ON t5.rev_page = t4.page_id
	        ) t6
	        GROUP BY pl_from
	    ) t7
	    INNER JOIN
	    (
	        SELECT page_id, rev_timestamp
	        FROM (
				SELECT t1.page_id, t2.rev_timestamp
				FROM
					(SELECT page.page_id, page.page_title, page.page_latest
					FROM page
					WHERE page_id in(
						SELECT cl_from FROM categorylinks where cl_to = %s
					)) t1
				INNER JOIN (
						SELECT rev_timestamp, rev_id FROM revision
					)t2
				ON rev_id = page_latest
			)t2_1
	    ) t8
	    on t7.pl_from = t8.page_id
	)t10
	WHERE outdatedness in (
	    SELECT max(outdatedness) as maximum_outdated
	    FROM
	    (
	        SELECT pl_from, max_rev_timestamp-rev_timestamp as outdatedness
		    FROM(
		        SELECT pl_from, max(rev_timestamp_link) as max_rev_timestamp
		        FROM
		        (
		            SELECT pl_from, page_id, rev_timestamp as rev_timestamp_link
		            FROM
		            (
		                SELECT pl_from, page_id, page_latest
		                FROM page
		                INNER JOIN
		                (
		                    SELECT pl_from, pl_title, pl_namespace, pl_from_namespace
		                    FROM pagelinks
		                    WHERE pl_from in (
		                        SELECT page_id FROM (
									SELECT t1.page_id
									FROM(
										SELECT page.page_id, page.page_title, page.page_latest
										FROM page
										WHERE page_id in(
											SELECT cl_from FROM categorylinks where cl_to = %s
										)
									) t1
								)t2_1
		                    )
		                )t3
		                ON t3.pl_title = page.page_title and page.page_namespace = t3.pl_namespace
		            )t4
		            INNER JOIN
		            (
		                SELECT rev_page, rev_timestamp
		                FROM revision
		            )t5
		            ON t5.rev_page = t4.page_id
		        ) t6
		        GROUP BY pl_from
		    ) t7
		    INNER JOIN
		    (
		        SELECT page_id, rev_timestamp
		        FROM (
					SELECT t1.page_id, t2.rev_timestamp
					FROM
						(SELECT page.page_id, page.page_title, page.page_latest
						FROM page
						WHERE page_id in(
							SELECT cl_from FROM categorylinks where cl_to = %s
						)) t1
					INNER JOIN (
							SELECT rev_timestamp, rev_id FROM revision
						)t2
					ON rev_id = page_latest
				)t2_1
		    ) t8
		    on t7.pl_from = t8.page_id
	    ) t9
	)
)combined
WHERE page.page_id = combined.pl_from