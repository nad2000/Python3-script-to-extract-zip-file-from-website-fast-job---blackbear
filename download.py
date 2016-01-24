#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests

default_iea_user = ""
default_iea_pwd = ""

iea_user = os.environ.get("IEA_USER", default_iea_user)
iea_pwd = os.environ.get("IEA_PWD", default_iea_pwd)
source_url = "http://mods.iea.org/sdbs/supply.zip"
destination_filename = source_url.split('/')[-1]

req = requests.get(source_url, auth=(iea_user, iea_pwd), stream=True)
with open(destination_filename, "wb") as f:
    for chunk in req.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

print("*** {} downloaded into {}".format(source_url, destination_filename))


