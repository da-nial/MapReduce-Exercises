import sys
import csv
import json


def use_file():
    input_file = open('../light_dataset.csv', encoding='utf8')
    output_file = open('mapper_output.txt', mode='w')
    error_file = open('mapper_error.txt', mode='w')
    sys.stdin = input_file
    sys.stdout = output_file
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


def get_subject(tweet: str) -> str:
    if ("#Trump" in tweet or "#DonaldTrump" in tweet) and ("#Biden" in tweet or "#JoeBiden" in tweet):
        return Subject.Common

    # Donald Trump
    elif "#Trump" in tweet or "#DonaldTrump" in tweet:
        return Subject.Trump

    # Joe Biden
    elif "#Biden" in tweet or "#JoeBiden" in tweet:
        return Subject.Biden

    else:
        return Subject.Other


def get_source(source: str) -> str:
    if "Twitter Web App" in source:
        return Source.Web
    elif "Twitter for iPhone" in source:
        return Source.IPhone
    elif "Twitter for Android" in source:
        return Source.Android


def mapper(row):
    tweet, likes, retweets, source_raw = row[2], row[3], row[4], row[5]

    subject = get_subject(tweet)
    source = get_source(source_raw)

    data = {
        'subject': subject,
        'likes': int(float(likes)),
        'retweets': int(float(retweets)),
        'source': source
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
