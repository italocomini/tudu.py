from flask import Blueprint

task_bp = Blueprint(
    'task_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/api/tasks'
)


@task_bp.route('/', methods=['GET'])
def index():
    return {'title': 'Task 1'}, 200
