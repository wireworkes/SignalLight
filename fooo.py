from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
@app.route("/all")
def all():
    urls = [
        "https://www.yahoo.co.jp/",
        "https://twitter.com/",
        "https://www.slideshare.net/"]
    status = []

    for url in urls:
        req = requests.get(url)
        status.append(req.status_code)

    return render_template('fooo.html', site_URL=urls, site_status=status)


app.run()
