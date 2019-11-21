import base64
import json


def decode(data):
    return base64.b64encode(json.dumps(data).encode("utf-8")).decode("ascii")


def encode(data):
    return base64.b64encode(json.dumps(data).encode("utf-8")).decode("ascii")
