import re

from sshpass import Sshpass


class IperfServer:
    def __init__(self, ip_server, username_server, password_server):
        self.ip_server = ip_server
        self.username_server = username_server
        self.password_server = password_server
        self.pid = None

    def start(self):
        ssh_server = Sshpass(self.ip_server, self.password_server, self.username_server)
        res, err = ssh_server.execute('iperf3 -s &')
        self.pid = self.get_pid(res)
        return self.pid

    def exit(self):
        ssh_server = Sshpass(self.ip_server, self.password_server, self.username_server)
        res, _ = ssh_server.execute(f'kill -9 {self.pid}')

    @staticmethod
    def get_pid(res):
        print(res)
        pid = re.findall(r'\[1] \d{5}', res)[0].split(' ')[1]
        return pid
