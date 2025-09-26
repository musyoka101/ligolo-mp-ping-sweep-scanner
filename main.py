import functions
import argparse

def main(proxying):
    live_hosts = functions.network_scan(proxying)
    if live_hosts:
        print("\nLive Hosts:")
        for host, status in live_hosts:
            print(f"{host} --> {status}")
    else:
        print("\nNo devices up and running in the given range of network.")


if __name__ == "__main__":
    args = argparse.ArgumentParser(description="Ping Sweep Network Scanner")
    args.add_argument("-l", "--ligolo-mp-proxy", help="proxying through ligolo-mp", default=False, type=bool)
    arguments = args.parse_args()
    functions.instructions()
    main(arguments.ligolo_mp_proxy)
