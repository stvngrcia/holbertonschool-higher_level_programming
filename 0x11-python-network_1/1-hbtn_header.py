#!/usr/bin/python3
import sys
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)
    with urlopen(req) as response:
        headers = response.getheaders()

    for data in headers:
        if data[0] == "X-Request-Id":
            print(data[1])
