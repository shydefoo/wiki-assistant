import os
from utils.wiki_logger import WikiLogger
from flask import Flask
from flask import request, Response, render_template, jsonify
from services import wiki_cateogry_service, normal_sql_service
app = Flask(__name__)

logger = WikiLogger(__name__).logger

@app.route('/')
def homepage():
    return render_template('dashboard.html')

@app.route('/find_outdated_page', methods=['POST'])
def find_outdated_cat():
    if request.method == 'POST':
        category = request.form.get('category', None)
        if category is not None:
            service = wiki_cateogry_service.OutdatednessByCat()
            result, time = service.get_result(category)
            logger.info("Query time: {}".format(time))
            return Response(time + result)

@app.route('/query', methods=['POST'])
def perform_query():
    logger.info(request.form)
    query = request.form.get('query', None)
    if query is not None:
        service = normal_sql_service.ExecuteQuery()
        try:
            result, time = service.get_result(query)
            logger.info("Query time: {}".format(time))
            return Response(time + result)
        except Exception as e:
            return Response(str(e))
    else:
        return Response("Empty Query")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False)
