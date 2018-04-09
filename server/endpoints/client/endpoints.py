endpoints = {}


def endpoint(name):
    def register_endpoint(fn):
        endpoints['client/' + name] = fn
    return register_endpoint
