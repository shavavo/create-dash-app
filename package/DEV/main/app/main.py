import dash
import dash_auth

import flask
import base64

from app import *
import page

dash_app.layout = page.layout
dash_app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)