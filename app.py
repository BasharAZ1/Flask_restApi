from flask import Flask,jsonify,request


app = Flask(__name__)

Books=[
    {"id":1,"title":"1984","author":"George orwell"},
    {"id":2,"title":"To kill a mockgenbird","author":"Harper Lee"}
]

@app.route("/api/books",methods=["GET"])
def get_books():
    return jsonify(Books)

@app.route("/api/books/<int:book_id>")
def get_book(book_id):
    book = next((book for book in Books if book["id"] == book_id), None)
    return jsonify(book) if book else ("",404)


@app.route("/api/books/",methods=["POST"])
def create_book():
    new_book=request.get_json()
    new_book["id"]=Books[-1]["id"]+1 if Books else 1
    Books.append(new_book)
    return jsonify(new_book),201




@app.route("/api/books/<int:book_id>",methods=["PUT"])
def update_book(book_id):
    book = next((book for book in Books if book["id"] == book_id), None)
    if book:
        data=request.get_json()
        book.update(data)
        return jsonify(book)
    return ("",404)
    
    
if __name__ == "__main__":
    app.run(debug=True)