import flask


from . import home


@home.route("/", methods=["GET"])
def index():
    return flask.render_template(
        "home/index.html", page_title="Webinaire Flask"
    )
