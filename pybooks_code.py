from flask import Flask, render_template, request
import requests


app = Flask("PyBooks")


@app.route('/search', methods=["POST"])
def search_books():
    form_data = request.form
    search_term = form_data["text"]
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q={}&key=AIzaSyCbhIgJKBPeTDIhAF4MCY0VXOZoTX3IcAc".format(search_term))
    results = search(r)
    return render_template('searchResults.html', results=results)


def search(data):
    results = []
    book_data = data.json()
    books = book_data['items']

    for book in books:
        result = {}
        volumeInfo = book.get('volumeInfo')
        result["title"] = volumeInfo['title']
        result['authors'] = volumeInfo['authors'][0]
        result["description"] = volumeInfo.get('description')
        imageLink = volumeInfo.get('imageLinks')
        result["imageLinks"] = imageLink.get("thumbnail")
        result["infoLink"] = volumeInfo.get("infoLink")
        result["previewLink"] = volumeInfo.get("previewLink")

        results.append(result)

    return results


@app.route('/')
def home():
    return render_template('homePage.html')


app.run(debug=True)


def find(data):
    results = []
    titles = []
    results = []
    book_data = data.json()
    books = book_data['items']

    for book in books:
        result = {}
        volumeInfo = book.get('volumeInfo')
        result["title"] = volumeInfo.get('title')
        # result["author"] = volumeInfo.get('authors')[0]
        # result["description"] = volumeInfo.get('description')
        results.append(result)

    return results


def search_books(title):
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q={}&key=AIzaSyCbhIgJKBPeTDIhAF4MCY0VXOZoTX3IcAc".format(title))
    book_list = find(r)

    return book_list