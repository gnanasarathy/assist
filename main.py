from flask import Flask, request, render_template
from reader import reading
from creater import supplier, destroyer
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        update_val = request.form.get("val")
        supplier(update_val)
    return render_template("index.html")


@app.route('/view')
def viewer():
    txt = reading()
    rt = f"""<xmp>{txt}</xmp>"""
    return rt


@app.route('/refresh')
def destroy():
    destroyer()
    return "Ready for New data!!!"


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
