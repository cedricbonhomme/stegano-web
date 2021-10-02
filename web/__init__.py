#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.urandom(25)

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


import web.views
