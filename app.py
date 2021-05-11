import flask
from flask import Flask, render_template, request, redirect, json
import numpy as np

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/kohlicalls', methods=['GET', 'POST'])
def kohli():
    return render_template('toss-call-kohli.html')


@app.route('/kanecalls', methods=['GET', 'POST'])
def kane():
    return render_template('toss-call-kane.html')


@app.route('/kohlicalls/heads', methods=['GET', 'POST'])
def result_kohlih():
    return render_template('kohliheads.html')


@app.route('/kohlicalls/tails', methods=['GET', 'POST'])
def result_kohlit():
    return render_template('kohlitails.html')


@app.route('/kanecalls/heads', methods=['GET', 'POST'])
def result_kaneh():
    return render_template('kaneheads.html')


@app.route('/kanecalls/tails', methods=['GET', 'POST'])
def result_kanet():
    return render_template('kanetails.html')


if __name__ == "__main__":
    app.run(debug=True)
