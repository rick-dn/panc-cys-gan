import numpy as np
import pandas as pd
from sklearn import preprocessing

from extract_features import extract_bert_features


def process_histol_details(df):

    # delete numbering
    df = df.drop(df.columns[0], axis=1)
    # del df[None]

    # print('Number of rows Investig-CTMRI',  df.count)
    # exit()

    # subject id
    # leave as it is, its identifier to the case, not required in modelling

    # visit id
    # leave as it is, required to assoc with other sheets

    # histology_done
    # print(df['histology_done'])
    # df.loc[(df["histology_done"].isnull()), 'note'] = 'NA'
    df = pd.concat([df, pd.get_dummies(df['histology_done'],
                                       prefix='histology_done',
                                       dummy_na=True)], axis=1).drop(['histology_done'], axis=1)
    # print(df['histology_done'])

    # histology_source
    # print(df['histology_source'])
    # df.loc[(df["histology_source"].isnull()), 'note'] = 'NA'
    df = pd.concat([df, pd.get_dummies(df['histology_source'],
                                       prefix='histology_source',
                                       dummy_na=True)], axis=1).drop(['histology_source'], axis=1)
    # print(df['histology_source'])

    # histology date
    # leave as it is

    # histology_finding
    # print(df['histology_finding'])
    # df.loc[(df["histology_finding"].isnull()), 'note'] = 'NA'
    df = pd.concat([df, pd.get_dummies(df['histology_finding'],
                                       prefix='histology_finding',
                                       dummy_na=True)], axis=1).drop(['histology_finding'], axis=1)
    # print(df['histology_finding'])

    # histology_T
    # print(df['histology_T'])
    # df.loc[(df["histology_T"].isnull()), 'note'] = 'NA'
    df = pd.concat([df, pd.get_dummies(df['histology_T'],
                                       prefix='histology_T',
                                       dummy_na=True)], axis=1).drop(['histology_T'], axis=1)
    # print(df['histology_T'])

    # histology_N
    # print(df['histology_N'])
    # df.loc[(df["histology_N"].isnull()), 'note'] = 'NA'
    df = pd.concat([df, pd.get_dummies(df['histology_N'],
                                       prefix='histology_N',
                                       dummy_na=True)], axis=1).drop(['histology_N'], axis=1)
    # print(df['histology_N'])

    # histology_M
    # print(df['histology_M'])
    # df.loc[(df["histology_M"].isnull()), 'note'] = 'NA'
    df = pd.concat([df, pd.get_dummies(df['histology_M'],
                                       prefix='histology_M',
                                       dummy_na=True)], axis=1).drop(['histology_M'], axis=1)
    # print(df['histology_M'])

    # histology_TNM
    # print(df['histology_TNM'])
    # df.loc[(df["histology_TNM"].isnull()), 'note'] = 'NA'
    df = pd.concat([df, pd.get_dummies(df['histology_TNM'],
                                       prefix='histology_TNM',
                                       dummy_na=True)], axis=1).drop(['histology_TNM'], axis=1)
    # print(df['histology_TNM'])

    # histology_grading
    # print(df['histology_grading'])
    # df.loc[(df["histology_grading"].isnull()), 'note'] = 'NA'
    df = pd.concat([df, pd.get_dummies(df['histology_grading'],
                                       prefix='histology_grading',
                                       dummy_na=True)], axis=1).drop(['histology_grading'], axis=1)
    # print(df['histology_grading'])

    # histology_resection
    # print(df['histology_resection'])
    # df.loc[(df["histology_resection"].isnull()), 'note'] = 'NA'
    df = pd.concat([df, pd.get_dummies(df['histology_resection'],
                                       prefix='histology_resection',
                                       dummy_na=True)], axis=1).drop(['histology_resection'], axis=1)
    # print(df['histology_resection'])

    # histology_invasion
    # print(df['histology_invasion'])
    # df.loc[(df["histology_invasion"].isnull()), 'note'] = 'NA'
    df = pd.concat([df, pd.get_dummies(df['histology_invasion'],
                                       prefix='histology_invasion',
                                       dummy_na=True)], axis=1).drop(['histology_invasion'], axis=1)
    # print(df['histology_invasion'])

    # histology file
    del df['histology_file']

    # histology note
    # extract bert features
    # df.loc[(df["histology_note_clean"].isnull()), 'histology_note_clean'] = 'NA'
    # histology_note_clean = df['histology_note_clean']
    # print(histology_note_clean[0])
    # histology_note_clean = extract_bert_features(histology_note_clean)
    # np.save('histology_note_clean', histology_note_clean)

    # load to dataframe, each feature a column
    # histology_note_clean = np.load('histology_note_clean.npy')
    # print('histology_note_clean.shape', histology_note_clean.shape)
    # df_histology_note_clean = pd.DataFrame(histology_note_clean.reshape(326, -1))
    # del df['histology_note_clean']
    # df = pd.concat([df, df_histology_note_clean], axis=1)

    # all features in one column
    histology_note_clean = np.load('histology_note_clean.npy').tolist()
    # print(histology_note_clean[0][0])
    df['histology_note_clean'] = histology_note_clean
    # print(df['histology_note_clean'])

    del df['Unnamed: 16']
    del df['Unnamed: 17']
    del df['Unnamed: 18']

    return df
