import logger
import requests
from flask import Flask, render_template, request, send_file

import html_parser

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/download")
def download():
    return send_file('result.csv', as_attachment=True)


@app.route("/parse", methods=['POST'])
def parse():
    try:
        if request.method == 'POST':
            url = request.form["url_input"]

            html_parser.parse(url)

            return download()

    except requests.exceptions.MissingSchema:
        app.logger.error("Url is empty")
        return index()

    except html_parser.BadResponse:
        app.logger.error("Bad response")
        return index()

    except html_parser.WrongWebsite:
        app.logger.error("The data was not found")
        return index()

    except html_parser.ParserError:
        app.logger.error(
            "Internal parser error. The site may have been updated")
        return index()
