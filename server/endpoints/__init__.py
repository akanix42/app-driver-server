from agent import endpoints as agent_endpoints
from client import endpoints as client_endpoints


def merge_dicts(a, b):
    c = a.copy()
    c.update(b)
    return c


endpoints = merge_dicts(agent_endpoints, client_endpoints)
