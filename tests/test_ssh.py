from unittest import mock

from sshpass import Sshpass
from tests.mock_popen import MockedPopen


@mock.patch('subprocess.Popen', MockedPopen)
def test_ssh(iperf_result):
    test_sshpass = Sshpass('ip', 'password', 'username')
    actual_res = test_sshpass.execute('ls')
    expected_res = ('output', 'error')
    assert actual_res == expected_res

