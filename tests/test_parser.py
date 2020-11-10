import pytest

from iperf.parser import parse_result


def test_parse_correct_result(iperf_result):
    actual_data = parse_result((iperf_result, None))
    exp_data = {'status': 0,
                'error': None,
                'result': {'ip': '172.31.1.233', 'interval': '0.00-10.00 sec',
                           'transfer': '1.13 GBytes', 'bandwidth': '973 Mbits/sec'}}
    assert exp_data == actual_data


def test_parse_error_result(iperf_result):
    actual_data = parse_result((iperf_result, 'error_text'))
    exp_data = {'status': 255,
                'error': 'error_text',
                'result': {'ip': '172.31.1.233', 'interval': '0.00-10.00 sec',
                           'transfer': '1.13 GBytes', 'bandwidth': '973 Mbits/sec'}}
    assert exp_data == actual_data
