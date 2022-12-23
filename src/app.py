from flask import Flask, render_template, request, make_response, url_for
from configparser import ConfigParser
import apihandler
import qrcodeprinter
import sys
if sys.platform.startswith("linux"):
    pass
if sys.platform.startswith("win32"):
    import threading
    import trayapp


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
        #print(postrequest)
        apihandler.api_handler(postrequest)
    # TODO: understand why return is necessary
    return make_response()


if __name__ == "__main__":
    HOST = config["general"]["HOST"]
    PORT = config["general"]["PORT"]
    qrcodeprinter.prepare_qr_code_info(HOST, PORT)
    if sys.platform == "win32":
        # Start the tray icon on a separate thread
        threading.Thread(target=trayapp.trayapp.run).start()
    # Then starting the webserver
    app.run(host=HOST, port=PORT, debug=False)