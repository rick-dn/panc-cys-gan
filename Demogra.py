import pandas as pd
from sklearn import preprocessing
import numpy as np


def unique_id(list1):
    unique_list = []
    for x in list1:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)

    print('total subjejct ids: ')


def process_demogra(df):

    # delete numbering
    df = df.drop(df.columns[0], axis=1)
    # del df[None]

    # subject id
    # leave as it is, its identifier to the case, not required in modelling

    # visit id
    # use number_of_days_to_visit and visit_id elsewhere to assoc data
    # print('process_demogra subject ids: ', len(np.unique(np.asarray(df['subject_id'].tolist()))))
    # exit()

    # visit date
    # not required, use number_of_days_to_visit
    # del df['visit_date']

    # age
    age = df['age']
    # print('age', age.values)
    age = preprocessing.minmax_scale(age.values)
    df['age'] = age
    # print(df['age'].values)

    # height_cm
    avg_female = df.loc[df['gender'] == 'Female']['height_cm'].mean()
    # print('average female height: ', avg_female)
    df.loc[(df["height_cm"].isnull()) & (df["gender"] == 'Female'), 'height_cm'] = avg_female

    avg_male = df.loc[df['gender'] == 'Male']['height_cm'].mean()
    # print('average male height: ', avg_male)
    df.loc[(df["height_cm"].isnull()) & (df["gender"] == 'Male'), 'height_cm'] = avg_male

    height_cm = df['height_cm']
    # print('height', height_cm.values)
    height_cm = preprocessing.minmax_scale(height_cm.values)
    df['height_cm'] = height_cm
    # print(df['height_cm'].values)

    # height_in
    # use height_cm
    del df['height_in']

    # gender
    # print(df['gender'])
    df = pd.concat([df, pd.get_dummies(df['gender'],
                                       prefix='gender',
                                       dummy_na=True)], axis=1).drop(['gender'], axis=1)
    # print(df['gender_Male'])

    # weight_kg
    weight_kg = df['weight_kg']
    # print('weight_kg', weight_kg.values)
    weight_kg = preprocessing.minmax_scale(weight_kg.values)
    df['weight_kg'] = weight_kg
    # print(df['weight_kg'].values)

    # race
    # print(df['race'])
    df = pd.concat([df, pd.get_dummies(df['race'],
                                       prefix='race',
                                       dummy_na=True)], axis=1).drop(['race'], axis=1)
    # print(df['race_Caucasian: Eastern European'])

    # bmi
    bmi = df['bmi']
    # print('bmi', bmi.values)
    bmi = preprocessing.minmax_scale(bmi.values)
    df['bmi'] = bmi
    # print(df['bmi'].values)

    # Number_days_to_visit
    Number_days_to_visit = df['Number_days_to_visit']
    # print('Number_days_to_visit', Number_days_to_visit.values)
    Number_days_to_visit = preprocessing.minmax_scale(Number_days_to_visit.values)
    df['Number_days_to_visit'] = Number_days_to_visit
    # print(df['Number_days_to_visit'].values)

    return df
