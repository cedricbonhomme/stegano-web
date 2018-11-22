#! /usr/bin/env python
# -*- coding: utf-8 -*-

import io
from flask import render_template, jsonify, request, flash, send_file
from stegano import lsb

from web import app, allowed_file


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    """
    action = 'hide'
    message = ''
    base64Img = ''

    if request.method == 'POST':
        action = request.args.get('action', None)
        if action not in ('hide', 'reveal'):
            return render_template('index.html')

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            if 'reveal' == action:
                # reveal the secret
                message = lsb.reveal(file)
            elif 'hide' == action:
                # hide the secret
                secret_to_hide = request.form.get('secret')
                image = lsb.hide(file, secret_to_hide)
                # convert the result to BytesIO
                outputBytes = io.BytesIO()
                image.save(outputBytes, "PNG")
                outputBytes.seek(0)
                return send_file(outputBytes,
                                    mimetype='image/png',
                                    as_attachment=True,
                                    attachment_filename='secret.png')
        elif not allowed_file(file.filename):
            flash('File type not allowed (only png or jpeg).', 'danger')

    return render_template('index.html', action=action, message=message)


@app.route('/encode', methods=['POST'])
def encode():
    """
    """
    pass


@app.route('/decode', methods=['POST'])
def decode():
    """
    """
    print(request.files)
    return redirect(url_for('projects_bp.list_projects'))


@app.errorhandler(404)
def not_found(error=None):
    """
    Handles 404 errors.
    """
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
