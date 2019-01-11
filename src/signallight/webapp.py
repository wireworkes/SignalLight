from flask import Flask, render_template
from requests import RequestException
import requests

app = Flask(__name__)


class Service:
    def __init__(self, url, status='err'):
        self.url = url
        self.status = status


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
    services = [Service(url) for url in urls]

    for service in services:
        try:
            req = requests.get(service.url)
            service.status = req.status_code
        except RequestException:
            pass

    return render_template('all.html', services=services)


app.run()
