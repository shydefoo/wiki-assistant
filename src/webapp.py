from flask import Flask
from flask import request, Response
from services import wiki_category
app = Flask(__name__)

@app.route('/')
def homepage():
    return Response("Hello world")

@app.route('/find_outdated_page/', methods=['POST'])
def find_outdated_cat():
    if request.method == 'POST':
        category = request.form.get('category', None)
        if category is not None:
            page_title = wiki_category.find_pages_under_cat(category)
            return Response(page_title)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False)
