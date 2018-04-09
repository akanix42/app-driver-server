from endpoints import endpoint
import connections


@endpoint('send-test')
def send_test(client, data):
    target_client = connections.get_client(data['clientIndex'])
    target_client.send_message({
        'endpoint': 'receive-test',
        'message': 'hello world',
    })
