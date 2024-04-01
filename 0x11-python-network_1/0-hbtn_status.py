#!/usr/bin/python3
"""Retrieves https://intranet.hbtn.io/status"""
import urllib.request


def fetcher():
    """fetcher"""
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        webpage_content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(webpage_content)))
        print("\t- content: {}".format(webpage_content))
        print("\t- utf8 content: {}".format(webpage_content.decode("utf-8")))

if __name__ == "__main__":
    fetcher()

