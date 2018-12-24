from flask import Flask, render_template
from requests import RequestException
import requests

app = Flask(__name__)


@app.route("/")
@app.route("/all")
def all():
    urls = [
        "https://www.yahoo.co.jp/",
        "https://httpstat.us/200",
        "https://httpstat.us/300",
        "https://httpstat.us/404",
        "https://test.example.com/"
        ]
    status = []

    for url in urls:
        try:
            req = requests.get(url)
            status.append(req.status_code)
        except RequestException:
            status.append("err")

    return render_template('fooo.html', site_URL=urls, site_status=status)


app.run()
