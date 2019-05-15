from flask import Blueprint, request, jsonify
import sys
from bson.json_util import dumps
import json
from subprocess import Popen, PIPE
from kubernetes import client, config, watch

kubernetes = Blueprint('kubernetes', __name__, url_prefix='/api/v1/k8')

@kubernetes.route('/test', methods=['POST'])
def test():
    """
    Test endpoint
    """
    req_dict = request.get_json()
    print(req_dict)
    return json.dumps({"output":req_dict["input"]})

@kubernetes.route("/pods", methods=['GET'])
def pods():
    """
    gets some basic kubernetes health
    """
    config.load_kube_config("/secrets/kubeconfig.txt")
    v1 = client.CoreV1Api()
    ret = v1.list_pod_for_all_namespaces(watch=False)
    print(ret.items)
    return json.dumps(ret.items)
