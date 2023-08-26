import dash, dash_auth, appCredentials, flask

app, dash_app = flask.Flask(__name__), dash.Dash(__name__, server = app)

dash_app.config.update({
        'suppress_callback_exceptions': True
})

auth = dash_auth.BasicAuth(
    dash_app,
    appCredentials.VALID_USERNAME_PASSWORD_PAIRS
)
