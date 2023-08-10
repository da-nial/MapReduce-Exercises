import sys
import csv
import datetime
import json

STATES = ["new york", "texas", "california", "florida"]


def use_file():
    input_file = open('../light_dataset.csv', encoding='utf8')
    sys.stdin = input_file
    output_file = open('mapper_output.txt', mode='w')
    sys.stdout = output_file
    error_file = open('mapper_error.txt', mode='w')
    sys.stderr = error_file


class Subject:
    Trump = 'Trump'
    Biden = 'Biden'
    Common = 'Common'
    Other = 'Other'


def get_subject(tweet: str) -> str:
    if ("#Trump" in tweet or "#DonaldTrump" in tweet) and ("#Biden" in tweet or "#JoeBiden" in tweet):
        return Subject.Common

    # Donald Trump
    elif "#Trump" in tweet or "#DonaldTrump" in tweet:
        return Subject.Trump

    # Joe Biden
    elif "#Biden" in tweet or "#JoeBiden" in tweet:
        return Subject.Biden

    return Subject.Other


def is_datetime_9_to_5(created_at: str):
    created_at_obj = datetime.datetime.strptime(
        created_at, '%Y-%m-%d %H:%M:%S'
    )

    return (
            datetime.time(9, 0) < created_at_obj.time() < datetime.time(17, 0)
    )


def is_state_in_target_states(state: str):
    return state in STATES


def mapper(row):
    created_at, tweet, state = row[0], row[2], row[18]

    state = state.lower()

    if not is_datetime_9_to_5(created_at):
        return

    if not is_state_in_target_states(state):
        return

    subject = get_subject(tweet)

    data = {
        'subject': subject,
        'state': state,
    }
    data_json = json.dumps(data)
    print(data_json)


def main():
    # use_file()
    rows = csv.reader(sys.stdin)

    next(rows, None)  # skip the headers

    for row in rows:
        try:
            mapper(row)
        except Exception as e:
            print(f'Error parsing row: {row}, exception: {e}', file=sys.stderr)


if __name__ == '__main__':
    main()
