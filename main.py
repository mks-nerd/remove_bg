from io import BytesIO

from flask import Flask, render_template, request, send_file
from rembg import remove
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def remove_bg():
    if request.method == "POST":
        file = request.files["file"]
        data = file.read()
        data_no_bg = remove(data)
        return send_file(BytesIO(data_no_bg), download_name=file.filename, as_attachment=True)
    return render_template("index.html")
