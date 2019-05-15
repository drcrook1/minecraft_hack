from flask import Blueprint, request, jsonify
import sys
from bson.json_util import dumps
import json
from subprocess import Popen, PIPE

kubernetes = Blueprint('kubernetes', __name__, url_prefix='/api/v1/k8')

@kubernetes.route('/test', methods=['POST'])
def test():
    """
    Test endpoint
    """
    req_dict = request.get_json()
    print(req_dict)
    return json.dumps({"output":req_dict["input"]})

@kubernetes.route("/basichealth", methods=["GET"])
def basic_health():
    """
    gets some basic kubernetes health
    """
    process = Popen(["kubectl", "get", "pods"], stdout=PIPE)
    (output, err) = process.communicate()
    print(output)
    exit_code = process.wait()
    return json.dumps({"output" : output})
    