import pytest


@pytest.fixture()
def iperf_result():
    with open('tests/iperf_out_correct.txt') as f:
        res = f.read()
    yield res

