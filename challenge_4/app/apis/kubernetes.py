from flask import Blueprint, request, jsonify
import sys
from bson.json_util import dumps
import json


kubernetes = Blueprint('kubernetes', __name__, url_prefix='/api/v1/k8')

@kubernetes.route('/test', methods=['POST'])
def test():
    """
    Test endpoint
    """
    req_dict = request.get_json()
    print(req_dict)
    return json.dumps({"output":req_dict["input"]})