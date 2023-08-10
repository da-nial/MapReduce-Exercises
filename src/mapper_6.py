import sys
import csv
import datetime
import json

STATES = ["new york", "california"]

STATES_GEO = {
    "new york": {
        "min_long": -79.7624, "max_long": -71.7517,
        "min_lat": 40.4772, "max_lat": 45.0153
    },
    "california": {
        "min_long": -124.6509, "max_long": -114.1315,
        "min_lat": 32.5121, "max_lat": 42.0126
    }
}


def use_file():
    input_file = open('../light_dataset.csv', encoding='utf8')
    sys.stdin = input_file
    # output_file = open('mapper_output.txt', mode='w')
    # sys.stdout = output_file
    # error_file = open('mapper_error.txt', mode='w')
    # sys.stderr = error_file


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


def get_state(lat, long):
    if (STATES_GEO["new york"]["min_long"] < long < STATES_GEO["new york"]["max_long"]) and \
            (STATES_GEO["new york"]["min_lat"] < lat < STATES_GEO["new york"]["max_lat"]):
        return "new york"
    elif (STATES_GEO["california"]["min_long"] < long < STATES_GEO["california"]["max_long"]) and \
            (STATES_GEO["california"]["min_lat"] < lat < STATES_GEO["california"]["max_lat"]):
        return "california"


def mapper(row):
    created_at, tweet, lat, long = row[0], row[2], row[13], row[14]

    try:
        lat, long = float(lat), float(long)
    except ValueError:
        return

    state = get_state(lat, long)

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
        mapper(row)


if __name__ == '__main__':
    main()
