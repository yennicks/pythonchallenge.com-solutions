#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Site: http://www.pythonchallenge.com/pc/return/italy.html
# Username: huge / Password: file

import io
import requests
from requests.auth import HTTPBasicAuth
from PIL import Image


if __name__ == "__main__":
    url = "http://www.pythonchallenge.com/pc/return/wire.png"
    auth = HTTPBasicAuth('huge', 'file')

    response = requests.get(url, auth=auth)
    assert response.status_code != 401, "Login incorrect!"
    assert response.status_code == 200, "Incorrect HTTP request."

    image = io.BytesIO(response.raw.read())
    assert image.seekable(), "Image should be seekable before it can be opened by Pillow."
