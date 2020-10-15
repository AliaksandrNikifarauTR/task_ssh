import argparse

from iperf.iperf_client import IperfClient
from iperf.iperf_server import IperfServer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ic", "--ip_client")
    parser.add_argument("-is", "--ip_server")
    parser.add_argument("-uc", "--username_client")
    parser.add_argument("-us", "--username_server")
    parser.add_argument("-pc", "--password_client")
    parser.add_argument("-ps", "--password_server")
    args = parser.parse_args()
    iperf_client = IperfClient(
        args.ip_client,
        args.username_client,
        args.password_client
    )
    iperf_server = IperfServer(
        args.ip_server,
        args.username_server,
        args.password_client
    )
    iperf_server.start()
    result = iperf_client.start(args.ip_server)
    iperf_server.exit()
    print(result)


if __name__ == '__main__':
    main()
