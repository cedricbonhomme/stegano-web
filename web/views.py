#! /usr/bin/env python
# -*- coding: utf-8 -*-

import io
from flask import render_template, redirect, jsonify, request, flash, send_file
from stegano import lsb

from web import app, allowed_file


@app.route("/", methods=["GET", "POST"])
def index():
    """Returns the main page which will handle the hiding and revealing of
    the message.
    """
    action = "hide"
    message = ""

    if request.method == "POST":
        action = request.args.get("action", None)

        if action not in ("hide", "reveal"):
            flash("Action not specified.", "danger")
            return render_template("index.html")

        if "file" not in request.files:
            # check if the post request has the file part
            flash("File is missing.", "danger")
            return redirect(request.url)
        file = request.files["file"]

        if file.filename == "":
            # if user does not select file, browser also
            # submit an empty part without filename
            flash("File is missing.", "danger")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # an appropriate file has been submitted
            # now, checks the requested action
            if "reveal" == action:
                # reveal the secret
                message = lsb.reveal(file)
            elif "hide" == action:
                # hide the secret
                secret_to_hide = request.form.get("secret")
                image = lsb.hide(file, secret_to_hide)
                # convert the result to BytesIO
                outputBytes = io.BytesIO()
                image.save(outputBytes, "PNG")
                outputBytes.seek(0)
                # returns the image as an attachment
                return send_file(
                    outputBytes,
                    mimetype="image/png",
                    as_attachment=True,
                    attachment_filename="secret.png",
                )
        elif not allowed_file(file.filename):
            flash("File type not allowed (only png or jpeg).", "danger")

    return render_template("index.html", action=action, message=message)


@app.errorhandler(404)
def not_found(error=None):
    """
    Handles 404 errors.
    """
    message = {
        "status": 404,
        "message": "Not Found: " + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
