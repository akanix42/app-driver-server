from endpoints import endpoint
import connections


@endpoint('register')
def register_client(client, data):
    connections.add_client(client)
    client.send_message({
        'response': 'test'
    })
    print('register')
