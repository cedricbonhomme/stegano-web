#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from flask import Flask


app = Flask(__name__)
app.config.from_object(__name__)



import web.views
