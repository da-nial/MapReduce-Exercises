import sys
import json


def use_file():
    input_file = open('mapper_output.txt', encoding='utf8')
    sys.stdin = input_file
    output_file = open('reducer_output.txt', mode='w')
    sys.stdout = output_file
    error_file = open('reducer_error.txt', mode='w')
    sys.stderr = error_file


class Source:
    Web = 'Web'
    IPhone = 'IPhone'
    Android = 'Android'


class Subject:
    Trump = 'Trump'
    Biden = 'Biden'
    Common = 'Common'
    Other = 'Other'


stats = {
    Subject.Trump: {
        "likes": 0, "retweets": 0, Source.Web: 0, Source.IPhone: 0, Source.Android: 0
    },
    Subject.Biden: {
        "likes": 0, "retweets": 0, Source.Web: 0, Source.IPhone: 0, Source.Android: 0
    },
    Subject.Common: {
        "likes": 0, "retweets": 0, Source.Web: 0, Source.IPhone: 0, Source.Android: 0
    }
}


def reduce(line: str):
    line.strip()
    data = json.loads(line)

    subject = data['subject']
    likes = data['likes']
    retweets = data['retweets']
    source = data['source']

    if subject == Subject.Other:
        return

    stats[subject]['likes'] += likes
    stats[subject]['retweets'] += retweets
    if source is not None:
        stats[subject][source] += 1


def main():
    # use_file()

    for line in sys.stdin:
        reduce(line)

    stats_json = json.dumps(stats, indent=4)
    print(stats_json)


if __name__ == '__main__':
    main()
