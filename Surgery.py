import numpy as np
import pandas as pd
from sklearn import preprocessing

from extract_features import extract_bert_features


def process_surgery(df):

    # delete numbering
    df = df.drop(df.columns[0], axis=1)
    # del df[None]

    # print('Number of rows surgery',  df.count)
    # exit()
    # subject id
    # leave as it is, its identifier to the case, not required in modelling

    # visit id
    # leave as it is, required to assoc with other sheets

    # surgery_done
    # print(df['surgery_done'])
    df.loc[(df["surgery_done"].isnull()), 'note'] = 'NA'
    df = pd.concat([df, pd.get_dummies(df['surgery_done'],
                                       prefix='surgery_done',
                                       dummy_na=True)], axis=1).drop(['surgery_done'], axis=1)
    # print(df['surgery_done'])

    # surgery date
    # sort later

    # surgery_organ
    # print(df['surgery_organ'])
    df.loc[(df["surgery_organ"].isnull()), 'note'] = 'NA'
    df = pd.concat([df, pd.get_dummies(df['surgery_organ'],
                                       prefix='surgery_organ',
                                       dummy_na=True)], axis=1).drop(['surgery_organ'], axis=1)
    # print(df['surgery_organ'])

    # surgery_subtype
    # print(df['surgery_subtype'])
    df.loc[(df["surgery_subtype"].isnull()), 'note'] = 'NA'
    df = pd.concat([df, pd.get_dummies(df['surgery_subtype'],
                                       prefix='surgery_subtype',
                                       dummy_na=True)], axis=1).drop(['surgery_subtype'], axis=1)
    # print(df['surgery_subtype'])

    # surgery_days
    df['surgery_stay'] = df['surgery_stay'].replace(to_replace=r'days', value='', regex=True)
    df['surgery_stay'] = df['surgery_stay'].replace(to_replace=r'day', value='', regex=True)
    df['surgery_stay'] = df['surgery_stay'].replace(to_replace=r' ', value='', regex=True)
    df['surgery_stay'] = df['surgery_stay'].replace(to_replace=r'>', value='', regex=True)
    df.loc[(df["surgery_stay"].isnull()), 'surgery_stay'] = 0
    df = df.astype({'surgery_stay': int})

    # surgery_complications
    # print(df['surgery_complications'])
    df.loc[(df["surgery_complications"].isnull()), 'note'] = 'NA'
    df = pd.concat([df, pd.get_dummies(df['surgery_complications'],
                                       prefix='surgery_complications',
                                       dummy_na=True)], axis=1).drop(['surgery_complications'], axis=1)
    # print(df['surgery_complications'])

    # surgery note

    # save bert features to numpy array
    # df.loc[(df["surgery_note"].isnull()), 'surgery_note'] = 'NA'
    # surgery_note = df['surgery_note']
    # print(surgery_note[1])
    # surgery_note = extract_bert_features(surgery_note)
    # np.save('surgery_note', surgery_note)

    # load to dataframe, each feature a column
    # surgery_note = np.load('surgery_note.npy')
    # print('surgery_note.shape', surgery_note.shape)
    # df_surgery_note = pd.DataFrame(surgery_note.reshape(326, -1))
    # print('surgery_note.shape', surgery_note.shape)
    # del df['surgery_note']
    # df = pd.concat([df, df_surgery_note], axis=1)

    # all features in one column
    surgery_note = np.load('surgery_note.npy').tolist()
    # print(surgery_note[0][0])
    df['surgery_note'] = surgery_note
    # print(df['surgery_note'][0])
    # exit()

    return df
