import pandas as pd
from sklearn import preprocessing
import numpy as np


def process_lifestyle(df):

    # delete numbering
    df = df.drop(df.columns[0], axis=1)
    # del df[None]

    # subject id
    # leave as it is, its identifier to the case, not required in modelling
    # visit id
    # use number_of_days_to_visit and visit_id elsewhere to assoc data
    # print('process_lifestyle subject ids: ', len(np.unique(np.asarray(df['subject_id'].tolist()))))
    # exit()

    # visit id
    # leave as it is, required to assoc with other sheets

    # # smoking
    # # 1: yes, 0: no, 0.5 unknown
    # df.loc[(df["smoking"] == 'Yes'), 'smoking'] = 1
    # df.loc[(df["smoking"] == 'Past'), 'smoking'] = 1
    # df.loc[(df["smoking"] == 'No'), 'smoking'] = 0
    # df.loc[(df["smoking"] == 'Unknown'), 'smoking'] = 0.5
    # df.loc[(df["smoking"].isnull()), 'smoking'] = 0.5
    # print(df['smoking'].tolist())
    #
    # # smoking_duration
    # df['smoking_duration'] = df['smoking_duration'].replace(to_replace=r'years', value='', regex=True)
    # df['smoking_duration'] = df['smoking_duration'].replace(to_replace=r'>', value='', regex=True)
    # df['smoking_duration'] = df['smoking_duration'].replace(to_replace=r'<', value='', regex=True)
    # df['smoking_duration'] = df['smoking_duration'].replace(to_replace=r'year', value='', regex=True)
    # df['smoking_duration'] = df['smoking_duration'].replace(to_replace=r' ', value='', regex=True)
    # df['smoking_duration'] = df['smoking_duration'].replace(to_replace=r'^$', value=0, regex=True)
    # df.loc[(df["smoking_duration"].isnull()), 'smoking_duration'] = 0
    # df = df.astype({'smoking_duration': int})
    # df['smoking_duration'] = df['smoking_duration'] * 365
    # print(df['smoking_duration'].tolist())

    # smoking
    # print(df['smoking'])
    df = pd.concat([df, pd.get_dummies(df['smoking'],
                                       prefix='smoking',
                                       dummy_na=True)], axis=1).drop(['smoking'], axis=1)

    # # smoking_duration
    # # print(df['smoking_duration'])
    # df = pd.concat([df, pd.get_dummies(df['smoking_duration'],
    #                                    prefix='smoking_duration',
    #                                    dummy_na=True)], axis=1).drop(['smoking_duration'], axis=1)

    # smoking_duration
    df['smoking_duration'] = df['smoking_duration'].replace(to_replace=r'years', value='', regex=True)
    df['smoking_duration'] = df['smoking_duration'].replace(to_replace=r'>', value='', regex=True)
    df['smoking_duration'] = df['smoking_duration'].replace(to_replace=r'<', value='', regex=True)
    df['smoking_duration'] = df['smoking_duration'].replace(to_replace=r'year', value='', regex=True)
    df['smoking_duration'] = df['smoking_duration'].replace(to_replace=r' ', value='', regex=True)
    df['smoking_duration'] = df['smoking_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["smoking_duration"].isnull()), 'smoking_duration'] = 0
    df = df.astype({'smoking_duration': int})
    df['smoking_duration'] = df['smoking_duration'] * 365
    # print(df['smoking_duration'].tolist())

    # ##### smoking_duration nomralisation? ##############
    smoking_duration = df['smoking_duration']
    smoking_duration = preprocessing.minmax_scale(smoking_duration.values)
    df['smoking_duration'] = smoking_duration

    # smoking_unit
    # print(df['smoking_unit'])
    df = pd.concat([df, pd.get_dummies(df['smoking_unit'],
                                       prefix='smoking_unit',
                                       dummy_na=True)], axis=1).drop(['smoking_unit'], axis=1)

    # alcohol
    # print(df['alcohol'])
    df = pd.concat([df, pd.get_dummies(df['alcohol'],
                                       prefix='alcohol',
                                       dummy_na=True)], axis=1).drop(['alcohol'], axis=1)

    # smoking_duration
    df['alcohol_duration'] = df['alcohol_duration'].replace(to_replace=r'years', value='', regex=True)
    df['alcohol_duration'] = df['alcohol_duration'].replace(to_replace=r'>', value='', regex=True)
    df['alcohol_duration'] = df['alcohol_duration'].replace(to_replace=r'<', value='', regex=True)
    df['alcohol_duration'] = df['alcohol_duration'].replace(to_replace=r'year', value='', regex=True)
    df['alcohol_duration'] = df['alcohol_duration'].replace(to_replace=r' ', value='', regex=True)
    df['alcohol_duration'] = df['alcohol_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["alcohol_duration"].isnull()), 'alcohol_duration'] = 0
    df = df.astype({'alcohol_duration': int})
    df['alcohol_duration'] = df['alcohol_duration'] * 365
    # print(df['alcohol_duration'].tolist())

    # ##### smoking_duration nomralisation? ##############
    alcohol_duration = df['alcohol_duration']
    alcohol_duration = preprocessing.minmax_scale(alcohol_duration.values)
    df['alcohol_duration'] = alcohol_duration

    # # alcohol_duration
    # # print(df['alcohol_duration'])
    # df = pd.concat([df, pd.get_dummies(df['alcohol_duration'],
    #                                    prefix='alcohol_duration',
    #                                    dummy_na=True)], axis=1).drop(['alcohol_duration'], axis=1)

    # alcohol_unit
    # print(df['alcohol_unit'])
    df = pd.concat([df, pd.get_dummies(df['alcohol_unit'],
                                       prefix='alcohol_unit',
                                       dummy_na=True)], axis=1).drop(['alcohol_unit'], axis=1)

    # drugs
    # print(df['drugs'])
    df = pd.concat([df, pd.get_dummies(df['drugs'],
                                       prefix='drugs',
                                       dummy_na=True)], axis=1).drop(['drugs'], axis=1)

    # # drugs_duration
    # # print(df['drugs_duration'])
    # df = pd.concat([df, pd.get_dummies(df['drugs_duration'],
    #                                    prefix='drugs_duration',
    #                                    dummy_na=True)], axis=1).drop(['drugs_duration'], axis=1)

    # drugs_duration
    df['drugs_duration'] = df['drugs_duration'].replace(to_replace=r'years', value='', regex=True)
    df['drugs_duration'] = df['drugs_duration'].replace(to_replace=r'>', value='', regex=True)
    df['drugs_duration'] = df['drugs_duration'].replace(to_replace=r'<', value='', regex=True)
    df['drugs_duration'] = df['drugs_duration'].replace(to_replace=r'year', value='', regex=True)
    df['drugs_duration'] = df['drugs_duration'].replace(to_replace=r' ', value='', regex=True)
    df['drugs_duration'] = df['drugs_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["drugs_duration"].isnull()), 'drugs_duration'] = 0
    df = df.astype({'drugs_duration': int})
    df['drugs_duration'] = df['drugs_duration'] * 365
    # print(df['drugs_duration'].tolist())

    # ##### smoking_duration nomralisation? ##############
    drugs_duration = df['drugs_duration']
    drugs_duration = preprocessing.minmax_scale(drugs_duration.values)
    df['drugs_duration'] = drugs_duration

    # drugs_type
    # print(df['drugs_type'])
    # df = pd.concat([df, pd.get_dummies(df['drugs_type'],
    #                                    prefix='drugs_type',
    #                                    dummy_na=True)], axis=1).drop(['drugs_type'], axis=1)

    del df['drugs_type']

    return df
