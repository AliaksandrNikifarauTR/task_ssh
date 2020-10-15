import subprocess


class Sshpass:
    def __init__(self, ip, password, username, file=False):
        self.ip = ip
        self.password = password
        self.username = username
        self.file = file

    def execute(self, cmd):
        if self.file:
            query = f"sshpass -f {self.password} ssh {self.username}@{self.ip}"
        else:
            query = f"sshpass -p '{self.password}' ssh {self.username}@{self.ip}"
        with subprocess.Popen(
                query.split(' '),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                bufsize=0,
                shell=False
        ) as p:
            out, err = p.communicate(f'{cmd}\n')
        return out, err
