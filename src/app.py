from flask import Flask, redirect, url_for, render_template, request, make_response

app = Flask(__name__)

# Serve the page
@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/api", methods=["POST"])
def api_handler():
    if request.method == "POST":
        print("POST works")
        print(request.get_json())
    # TODO: understand why return is necessary
    return make_response()

if __name__ == "__main__":
    app.run(debug=True)