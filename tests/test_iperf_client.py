from unittest.mock import patch, call

from iperf import iperf_client


@patch.object(iperf_client, 'parse_result')
@patch.object(iperf_client.Sshpass, 'execute')
def test_iperf_server(iperf_server_mock, parse_result_mock):
    iperf_server_mock.return_value = 'iperf_server_mock'
    parse_result_mock.return_value = 'parse_res_mock'
    _iperf_server = iperf_client.IperfClient('ip', 'username', 'password')
    actual_result = _iperf_server.start('test_ip_server')
    assert actual_result == 'parse_res_mock'
    iperf_server_mock.assert_called_once_with('iperf3 -c test_ip_server')
    parse_result_mock.assert_called_once_with('iperf_server_mock')
