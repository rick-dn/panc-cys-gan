import pandas as pd
from sklearn import preprocessing
import numpy as np


def process_urine(df):

    # delete numbering
    df = df.drop(df.columns[0], axis=1)
    # del df[None]

    # subject id
    # leave as it is, its identifier to the case, not required in modelling

    # visit id
    # use number_of_days_to_visit and visit_id elsewhere to assoc data
    # print('process_demogra subject ids: ', len(np.unique(np.asarray(df['subject_id'].tolist()))))
    # exit()

    # diptest_done
    # print(df['diptest_done'])
    df = pd.concat([df, pd.get_dummies(df['diptest_done'],
                                       prefix='diptest_done',
                                       dummy_na=True)], axis=1).drop(['diptest_done'], axis=1)

    # diptest_date
    # ignore

    # leu
    # print(df['leu'])
    df = pd.concat([df, pd.get_dummies(df['leu'],
                                       prefix='leu',
                                       dummy_na=True)], axis=1).drop(['leu'], axis=1)

    # nit
    # print(df['nit'])
    df = pd.concat([df, pd.get_dummies(df['nit'],
                                       prefix='nit',
                                       dummy_na=True)], axis=1).drop(['nit'], axis=1)
    # pro
    # print(df['pro'])
    df = pd.concat([df, pd.get_dummies(df['pro'],
                                       prefix='pro',
                                       dummy_na=True)], axis=1).drop(['pro'], axis=1)

    # ph
    df.loc[(df["ph"].isnull()), 'ph'] = np.nan
    # print(df["ph"].mean())
    # exit()

    avg_ph = np.nanmean(np.asarray(df["ph"].array, dtype=np.float32))
    df.loc[(df["ph"].isna()), 'ph'] = avg_ph
    # print('avg_ph: ', avg_ph)

    ph = df['ph']
    # print('ph', ph.values)
    ph = preprocessing.minmax_scale(ph.values)
    df['ph'] = ph
    # print(df['ph'].tolist())

    # blo
    # print(df['blo'])
    df = pd.concat([df, pd.get_dummies(df['blo'],
                                       prefix='blo',
                                       dummy_na=True)], axis=1).drop(['blo'], axis=1)

    # ket
    # print(df['ket'])
    df = pd.concat([df, pd.get_dummies(df['ket'],
                                       prefix='ket',
                                       dummy_na=True)], axis=1).drop(['ket'], axis=1)

    # glu
    # print(df['glu'])
    df = pd.concat([df, pd.get_dummies(df['glu'],
                                       prefix='glu',
                                       dummy_na=True)], axis=1).drop(['glu'], axis=1)

    # sg
    df['sg'] = df['sg'].replace(to_replace=r'<=', value='', regex=True)
    df.loc[(df["sg"] == 'Negative'), 'sg'] = 0
    df.loc[(df["sg"].isnull()), 'sg'] = 0

    sg = df['sg']
    # print('sg', sg.values)
    sg = preprocessing.minmax_scale(sg.values)
    df['sg'] = sg
    # print(df['sg'].tolist())

    return df