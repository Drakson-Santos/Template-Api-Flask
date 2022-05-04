

def init_app(app):
    @app.cli.command()
    def createdb():
        """Create sqlite database"""
        db.create_all()
