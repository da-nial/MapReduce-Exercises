# Map-Reduce Exercises
This repository contains solutions for three Hadoop map-reduce exercises. They were the third assignment in my undergraduate cloud computing course.

You can find the full project description in [instructions.pdf](instructions.pdf) and [report.pdf](report.pdf) (in Persian).

## Dataset

A subset of the [US Election 2020 Tweets](https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets) dataset is
used for this assignment. The subset has 1.72 million tweet records related to the election, with the original 21 features.

## Exercises

1. **Likes, Retweets, and Source Frequency**

   Create a map-reduce program that calculates the number of likes, retweets, and the frequency of different source platforms (Android/iOS/Web) for each candidate individually, as well as for both candidates combined. 
   - You can find the results of this calculation in [output/part-00000_1](output/part-00000_1).

2. **Tweets Percentage and Counts in Specific States and Time**

   Develop a map-reduce program that calculates the percentage of tweets posted between 9 AM to 5 PM in specific states related to the first candidate, the second candidate, and both of them. Additionally, count the total number of tweets posted in those states during the specified time period. The states include New York, Texas, California, and Florida. The search should be case insensitive. 
   - You can find the results in [output/part-00000_2](output/part-00000_2).

3. **Filtering Tweets by Geographic Coordinates**

    Build a map-reduce program similar to the previous exercise, but this time use geographic coordinates to filter the tweets related to the mentioned states. The states' coordinates are:
   - New York: [-79.7624 < Lon < -71.7517] | [40.47772 < Lat < 45.0153]
   - California: [-124.6509 < Lon < -114.1315] | [32.5121 < Lat < 42.0126]
   - The reasons for the different results between exercises 2 and 3 are also explained in the report. You can find the results in [output/part-00000_3](output/part-00000_3).

Hadoop was set up as part of the exercise to run these codes on the dataset.

## Course Information

- **Course**: Cloud Computing
- **University**: Amirkabir University of Technology
- **Semester**: Spring 2022

Let me know if you have any questions!
