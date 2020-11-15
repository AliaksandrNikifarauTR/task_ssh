import pytest


@pytest.fixture()
def iperf_result():
    with open('tests/test_data/iperf_out_correct.txt') as f:
        res = f.read()
    yield res

