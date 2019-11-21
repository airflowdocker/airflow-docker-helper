import argparse

from airflow_docker_helper import client


def call():
    parser = argparse.ArgumentParser()
    parser.add_argument("--call", type=str, required=True)
    parser.add_argument("--args", type=str, required=True)
    parser.add_argument("--kwargs", type=str, required=True)
    options = parser.parse_args()

    args = client.codec.decode(options.args)
    kwargs = client.codec.decode(options.kwargs)

    module_path, symbol = options.call.split(":", 1)
    module = __import__(module_path)
    callable = getattr(module, symbol)
    return callable(*args, **kwargs)
