import os
from flask import Flask
from flask import request, Response, render_template, jsonify
from services import wiki_category, perform_query
app = Flask(__name__)



@app.route('/')
def homepage():
    return render_template('dashboard.html')

@app.route('/find_outdated_page', methods=['POST'])
def find_outdated_cat():
    if request.method == 'POST':
        category = request.form.get('category', None)
        if category is not None:
            result = wiki_category.find_outdatedness_sql(category)
            return jsonify(result)

@app.route('/query', methods=['POST'])
def perform_query():
    if request.method == 'POST':
        query = request.form.get('query', None)
        if query is not None:
            result = perform_query.execute_sql_query(query)
        return Response("Temp")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False)
