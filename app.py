#!/usr/bin/env python3
"""
simple flask application to display hello world
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    show hello world text
    """
    return "Hello world"
