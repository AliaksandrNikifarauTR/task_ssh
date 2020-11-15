from unittest.mock import patch, call

from iperf import iperf_server


@patch.object(iperf_server.Sshpass, 'execute', return_value=('[1] 11111', ''))
def test_iperf_server(iperf_server_mock):
    _iperf_server = iperf_server.IperfServer('ip', 'username', 'password')
    pid = _iperf_server.start()
    _iperf_server.exit()
    assert pid == '11111'
    assert iperf_server_mock.call_count == 2
    iperf_server_mock.assert_has_calls([call('iperf3 -s &'), call('kill -9 11111')])
