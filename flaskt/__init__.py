import os
from importlib import import_module

import flask


def create_app():
    """Factory function responsible for lazy app creation."""
    app = flask.Flask(__name__)
    app.config.from_object(os.getenv('FLASK_SETTINGS_MODULE'))

    for blueprint in app.config['INSTALLED_BLUEPRINTS']:
        module = import_module(blueprint['module'])
        app.register_blueprint(
            getattr(module, blueprint.get("name", "blueprint")),
            url_prefix=blueprint.get("prefix", ""),
        )

    return app
