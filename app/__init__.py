from flask import Flask


def create_app(config):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config)

    with app.app_context():
        from .tasks import task
        app.register_blueprint(task.task_bp)

        return app
