_connections_set = set()
_connections = list()


def add_client(client):
    number_of_connections = len(_connections_set)
    _connections_set.add(client)
    if len(_connections_set) > number_of_connections:
        _connections.append(client)
    print(len(_connections))


def get_client(client_index):
    return _connections[client_index]
