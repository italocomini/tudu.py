from flask import Blueprint, jsonify, abort
from .tasks import get_tasks, get_task_by_id

task_bp = Blueprint(
    'task_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/api/tasks'
)


@task_bp.errorhandler(404)
def handle_invalid_usage(_):
    return {'error': 'task not found'}, 404


@task_bp.route('/', methods=['GET'])
def index():
    return jsonify(get_tasks()), 200


@task_bp.route('/<task_id>', methods=['GET'])
def get_task(task_id):
    task = get_task_by_id(task_id)
    if not task:
        abort(404)
    return jsonify(get_task_by_id(task_id)), 200
