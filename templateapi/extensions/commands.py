from templateapi.extensions.database import db


def create_db():
    """Creates database"""
    db.create_all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db]:
        app.cli.add_command(app.cli.command()(command))
