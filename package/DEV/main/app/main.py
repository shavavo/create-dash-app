import dash, dash_auth, flask, base64, page
from app import *

dash_app.layout = page.layout
dash_app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
