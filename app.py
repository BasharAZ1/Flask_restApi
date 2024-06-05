from flask import Flask,jsonify,request


app = Flask(__name__)

Books=[
    {"id":1,"title":"1984","author":"George orwell"},
    {"id":2,"title":"To kill a mockgenbird","author":"Harper Lee"}
]

@app.route("/api/books")
def get_books():
    return jsonify(Books)


if __name__ == "__main__":
    app.run(debug=True)