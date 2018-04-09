endpoints = {}


def endpoint(name):
    def register_endpoint(fn):
        endpoints['agent/' + name] = fn
    return register_endpoint
