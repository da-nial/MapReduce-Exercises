import sys
import json


def use_file():
    input_file = open('mapper_output.txt', encoding='utf8')
    sys.stdin = input_file
    # output_file = open('reducer_output.txt', mode='w')
    # sys.stdout = output_file
    # error_file = open('reducer_error.txt', mode='w')
    # sys.stderr = error_file


class Subject:
    Trump = 'Trump'
    Biden = 'Biden'
    Common = 'Common'
    Other = 'Other'


stats = {
    "new york": {
        Subject.Common: 0, Subject.Biden: 0, Subject.Trump: 0, Subject.Other: 0
    },
    "texas": {
        Subject.Common: 0, Subject.Biden: 0, Subject.Trump: 0, Subject.Other: 0
    },
    "california": {
        Subject.Common: 0, Subject.Biden: 0, Subject.Trump: 0, Subject.Other: 0
    },
    "florida": {
        Subject.Common: 0, Subject.Biden: 0, Subject.Trump: 0, Subject.Other: 0
    }
}


def reduce(line: str):
    line.strip()
    data = json.loads(line)

    subject = data['subject']
    state = data['state']

    stats[state][subject] += 1


def main():
    # use_file()

    for line in sys.stdin:
        reduce(line)

    # stats_json = json.dumps(stats, indent=4)
    # print(stats_json)

    results = {}
    for state, state_info in stats.items():
        num_all_tweets = state_info[Subject.Trump] + state_info[Subject.Biden] + \
                         state_info[Subject.Common] + state_info[Subject.Other]
        results.update({
            state: {
                Subject.Biden: (state_info[Subject.Biden] / num_all_tweets),
                Subject.Trump: (state_info[Subject.Trump] / num_all_tweets),
                Subject.Common: (state_info[Subject.Common] / num_all_tweets),
                'ALL': num_all_tweets
            }
        })

    results_json = json.dumps(results, indent=4)
    print(results_json)


if __name__ == '__main__':
    main()
