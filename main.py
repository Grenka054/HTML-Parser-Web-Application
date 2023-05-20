from flask import Flask, render_template,request,send_file
import requests
import parser
import logging

app = Flask(__name__)

@app.route("/")

@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/download")
def download():
    return send_file('result.csv',as_attachment=True)


@app.route("/parse", methods=['POST'])
def parse():
    try:
        if request.method == 'POST':
            url = request.form["url_input"]

            parser.parse()

            return download()

    except requests.exceptions.MissingSchema: 
        app.logger.error("url is empty")
        return index()
