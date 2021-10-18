import os
import csv

RESULTS_DIR = os.path.join('.', 'results')
os.makedirs(RESULTS_DIR, exist_ok=True)


def make_user_sheet():
    with open(os.path.join(RESULTS_DIR, 'users.tsv'), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['user_id', 'name', 'sex', 'age', 'disabled_degree', 'disabled_type', 'communication_type',
                         'communication_input'])


def make_answer1_sheet(uid):
    os.makedirs(os.path.join(RESULTS_DIR, str(uid)), exist_ok=True)

    with open(os.path.join(RESULTS_DIR, str(uid), 'answers1.tsv'), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['question_num', 'answer', 'submit_time', 'elapse_time'])


def make_answer2_sheet(uid):
    os.makedirs(os.path.join(RESULTS_DIR, str(uid)), exist_ok=True)

    with open(os.path.join(RESULTS_DIR, str(uid), 'answers2.tsv'), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['question_num', 'answer', 'answer_input', 'submit_time', 'elapse_time'])


def get_next_user_number():
    user_ids = list()

    with open(os.path.join(RESULTS_DIR, 'users.tsv'), 'r', encoding='UTF8') as f:
        reader = csv.reader(f, delimiter='\t')

        for line in reader:
            if len(line) == 0: continue

            if line[0] == 'user_id':
                continue
            else:
                user_ids.append(int(line[0]))

    if len(user_ids):
        return max(user_ids) + 1
    else:
        return 1

def problem1_array_to_json(arr):
    return {
        'problem_num': arr[0],
        'emotion_select': arr[1],
        'image_select': arr[2],
    }

