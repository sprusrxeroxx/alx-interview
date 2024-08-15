#!/usr/bin/python3

'''A module for parsing log data and computing metrics'''

import re
import sys

def logParser():
    for line in sys.stdin:
        match = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)', sys.stdin.readline())

        if match:
            ip_address, date, status_code, file_size = match.groups()
            print(ip_address)
            print(date)
            print(status_code)
            print(file_size)