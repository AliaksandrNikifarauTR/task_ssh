from iperf.parser import parse_result
from sshpass import Sshpass


class IperfClient:
    def __init__(self, ip_client, username_client, password_client):
        self.ip_client = ip_client
        self.username_client = username_client
        self.password_client = password_client

    def start(self, target_ip_server):
        ssh_client = Sshpass(self.ip_client, self.password_client, self.username_client)
        result = ssh_client.execute(f'iperf3 -c {target_ip_server}')
        return parse_result(result)

