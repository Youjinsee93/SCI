from flask import Flask, jsonify, Response, abort, send_file, request
from flask_cors import CORS
import json
import os

from utils.display import *
from utils.problem import *

from datetime import datetime
from pytz import timezone

app = Flask(__name__)

import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def root_dir():  # pragma: no cover
    return os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        '..', 'frontend', 'dist',
    )


def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        return open(src, encoding='UTF8').read()
    except IOError as exc:
        return str(exc)



def get_time():
    return datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')


@app.route('/', methods=['GET'])
def metrics():  # pragma: no cover
    content = get_file('index.html')
    return Response(content, mimetype="text/html")


@app.route('/register', methods=['POST'])
def register():
    params = json.loads(request.get_data())

    if not os.path.isfile(os.path.join('.', 'results', 'users.tsv')):
        make_user_sheet()

    user_id = get_next_user_number()

    with open(os.path.join('.', 'results', 'users.tsv'), 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow([user_id, params['name'], params['sex'], params['age'], params['disabled_degree'],
                         params['disabled_type'], params['communication_type'], params['communication_input']])

    return Response(str(user_id), mimetype="text/html")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_resource(path):  # pragma: no cover
    mimetypes = {
        ".css": "text/css",
        ".html": "text/html",
        ".js": "application/javascript",
    }
    complete_path = os.path.join(root_dir(), path)
    ext = os.path.splitext(path)[1]
    mimetype = mimetypes.get(ext, "text/html")
    content = get_file(complete_path)
    return Response(content, mimetype=mimetype)


@app.route('/favicon.ico', methods=['GET'])
def get_favicon():
    return Response('')


@app.route('/experiment-desc', methods=['GET'])
def get_experiment_desc():
    with open(os.path.join(ROOT_PATH, 'variables', 'description.md'), 'r',  encoding='UTF8') as f:
        data = jsonify(markdown_to_html(f.read()))
    return data


@app.route('/attachments/<path:file_name>', methods=['GET'], strict_slashes=False)
def get_public_attachment(file_name):
    try:
        return send_file(os.path.join('.', 'public_attachments', file_name), download_name=file_name)
    except:
        return abort(404)


@app.route('/type1/problems', methods=['GET'])
def get_proto2_problems():
    user_id = request.args.get('user_id', default=None, type=str)
    if user_id is None: abort(400, 'User ID not passed')

    available_problems = []
    solved_problems = []
    genre_dict = dict()

    from variables.problem_type1_list import problems
    for problem in problems:
        available_problems.append(problem['num'])
        genre_dict[problem['num']] = problem['genre'] if 'genre' in problem.keys() else 'N/A'

    try:
        with open(os.path.join(ROOT_PATH, 'results', str(user_id), 'answers2.tsv'), 'r', encoding='UTF8') as f:
            reader = csv.reader(f, delimiter='\t')

            for line in reader:
                if len(line) == 0: continue

                if line[0] == 'question_num':
                    continue
                else:
                    problem_num = int(line[0])
                    solved_problems.append(problem_num)

        solved_problems = list(set(solved_problems).intersection(set(available_problems)))
    except:
        make_answer2_sheet(uid=user_id)

    return jsonify({'available': available_problems, 'solved': solved_problems, 'genre': genre_dict})


@app.route('/type1/problems/<problem_num>', methods=['GET'])
def get_proto2_problem(problem_num):
    problem = None

    from variables.problem_type1_list import problems
    for p_iter in problems:
        if p_iter['num'] == int(problem_num):
            problem = p_iter
            break

    if problem is not None:
        return jsonify(problem)
    else:
        return abort(404)


@app.route('/type1/problems/<problem_num>/answers', methods=['POST'])
def add_proto2_answer(problem_num):

    params = json.loads(request.get_data(), encoding='utf-8')
    user_id = params['user_id']
    if user_id is None: abort(400, 'User ID not passed')

    with open(os.path.join(ROOT_PATH, 'results', str(user_id), 'answers2.tsv'), 'a+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow([problem_num, json.dumps(params['answer']), params['answer_input'], get_time(), params['elapse_time']])

    return Response('OK', mimetype="text/html")


@app.route('/type1/problems/<problem_num>/answers', methods=['GET'])
def get_proto2_recent_answer(problem_num):
    user_id = request.args.get('user_id', default=None, type=str)
    if user_id is None: abort(400, 'User ID not passed')

    answers = list()
    answers_input = list()
    with open(os.path.join(ROOT_PATH, 'results', str(user_id), 'answers2.tsv'), 'r', encoding='UTF8') as f:
        reader = csv.reader(f, delimiter='\t')

        for line in reader:
            if len(line) == 0: continue

            if line[0] == 'question_num':
                continue

            if line[0] == problem_num:
                answers.append(line[1])
                answers_input.append(line[2])
    if len(answers):
        return jsonify({'answer': json.loads(answers[-1]), 'answer_input': answers_input[-1]})
    else:
        return abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('FLASK_RUN_PORT'), debug=False)