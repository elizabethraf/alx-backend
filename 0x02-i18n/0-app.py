#!/usr/bin/env python3
"""display setup a basic Flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Display Hello world"""
    return render_template('0-index.html')
