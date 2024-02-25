#!/usr/bin/python3
"""
index file
"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def get_status():
    """status of the request"""
    return jsonify({"status": "OK"})
