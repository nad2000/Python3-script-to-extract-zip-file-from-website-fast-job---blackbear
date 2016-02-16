#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

import os
import requests
from html.parser import HTMLParser
#from urllib.parse import urlencode

ROOT_URL = "http://www.eppo.go.th/info/cd-2015/"
DOC_URL = ROOT_URL + "index.html"


def download(href):
    url = ROOT_URL + href
    destination_filename = href

    os.makedirs(os.path.dirname(destination_filename), exist_ok=True)

    req = requests.get(url, stream=True)
    if req.status_code != 200:
        print("*** Failed to connect to {}. Status code: {}".format(url, req.status_code))
        return False

    with open(destination_filename, "wb") as f:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    print("*** {} downloaded into {}".format(url, destination_filename))
    return True


class Parser(HTMLParser):

    curret_chapter = None

    def handle_data(self, data):
        if "CHAPTER" in data and self.lasttag == 'b':
            self.curret_chapter = data
            print("** Start downloading:", data)

    def handle_starttag(self, tag, attrs):

        if tag=='a':
            for name, val in attrs:
                if name == "href":
                    href = val
                    break
            else:
                return  ## missiong 'href' attribute
            if "chapter" in href.lower() and href.endswith(".xls"):
                download(href)

def main():
    parser = Parser()
    page = requests.get(DOC_URL)
    parser.feed(page.text)


if __name__ == "__main__":
    main()

