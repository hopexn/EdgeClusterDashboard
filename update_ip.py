import argparse
import socket
import time

import requests

parser = argparse.ArgumentParser()
parser.add_argument("--hostname", required=False, type=str, default=socket.gethostname())
parser.add_argument("--server", required=False, type=str, default="10.103.10.153")
args = parser.parse_args()

while True:
    try:
        req = requests.get("http://{}:8000/update_ip/{}".format(args.server, args.hostname))
        print(req.content)
        time.sleep(10)
    except KeyboardInterrupt:
        break
    except OSError:
        pass
