from flask import Flask, render_template, request, make_response
from configparser import ConfigParser
import apihandler
import qrcodeprinter


config = ConfigParser()
config.read("settings.cfg")

app = Flask(__name__)

# Serve the page
@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")

# Separate endpoint for the API
@app.route("/api", methods=["POST"])
def api_handler():
    if request.method == "POST":
        postrequest = request.get_json()
    # TODO: understand why return is necessary
    return make_response()


if __name__ == "__main__":
    HOST = config["general"]["HOST"]
    PORT = config["general"]["PORT"]
    qrcodeprinter.prepare_qr_code_info(HOST, PORT)
    app.run(host=HOST, port=PORT, debug=True)