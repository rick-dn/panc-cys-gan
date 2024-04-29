import numpy as np
import pandas as pd
from sklearn import preprocessing

from extract_features import extract_bert_features


def process_medhist(df):

    # delete numbering
    df = df.drop(df.columns[0], axis=1)
    # del df[None]

    # subject id
    # leave as it is, its identifier to the case, not required in modelling

    # visit id
    # leave as it is, required to assoc with other sheets

    # diabetes
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["diabetes"] == 'Yes'), 'diabetes'] = 1
    df.loc[(df["diabetes"] == 'No'), 'diabetes'] = 0
    df.loc[(df["diabetes"] == 'Unknown'), 'diabetes'] = 0.5
    df.loc[(df["diabetes"] == 'No change'), 'diabetes'] = 0.5
    df.loc[(df["diabetes"].isnull()), 'diabetes'] = 0.5
    # print(df['diabetes'].tolist())

    # diabetes duration
    df['diabetes_duration'] = df['diabetes_duration'].replace(to_replace=r'years', value='', regex=True)
    df['diabetes_duration'] = df['diabetes_duration'].replace(to_replace=r'>', value='', regex=True)
    df['diabetes_duration'] = df['diabetes_duration'].replace(to_replace=r'<', value='', regex=True)
    df['diabetes_duration'] = df['diabetes_duration'].replace(to_replace=r'year', value='', regex=True)
    df['diabetes_duration'] = df['diabetes_duration'].replace(to_replace=r' ', value='', regex=True)
    df['diabetes_duration'] = df['diabetes_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["diabetes_duration"].isnull()), 'diabetes_duration'] = 0
    df = df.astype({'diabetes_duration': int})
    df['diabetes_duration'] = df['diabetes_duration'] * 365
    # print(df['diabetes_duration'].tolist())

    ###### diabetes_duration nomralisation? ##############
    diabetes_duration = df['diabetes_duration']
    diabetes_duration = preprocessing.minmax_scale(diabetes_duration.values)
    df['diabetes_duration'] = diabetes_duration

    # diabetes_treatment
    # print(df['diabetes_treatment'])
    df = pd.concat([df, pd.get_dummies(df['diabetes_treatment'],
                                       prefix='diabetes_treatment',
                                       dummy_na=True)], axis=1).drop(['diabetes_treatment'], axis=1)

    # diabetes_treatment_2
    # leave for now try to go for one hot encoding
    del df['diabetes_treatment_2']

    # diabetes_note
    # leave for now try to go for one hot encoding
    del df['diabetes_note']

    # asthma
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["asthma"] == 'Yes'), 'asthma'] = 1
    df.loc[(df["asthma"] == 'No'), 'asthma'] = 0
    df.loc[(df["asthma"] == 'Unknown'), 'asthma'] = 0.5
    df.loc[(df["asthma"] == 'No change'), 'asthma'] = 0.5
    df.loc[(df["asthma"].isnull()), 'asthma'] = 0.5
    # print(df['asthma'].tolist())

    # asthma duration
    df['asthma_duration'] = df['asthma_duration'].replace(to_replace=r'years', value='', regex=True)
    df['asthma_duration'] = df['asthma_duration'].replace(to_replace=r'>', value='', regex=True)
    df['asthma_duration'] = df['asthma_duration'].replace(to_replace=r'<', value='', regex=True)
    df['asthma_duration'] = df['asthma_duration'].replace(to_replace=r'year', value='', regex=True)
    df['asthma_duration'] = df['asthma_duration'].replace(to_replace=r' ', value='', regex=True)
    df['asthma_duration'] = df['asthma_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["asthma_duration"].isnull()), 'asthma_duration'] = 0
    df = df.astype({'asthma_duration': int})
    df['asthma_duration'] = df['asthma_duration'] * 365
    # print(df['asthma_duration'].tolist())

    ###### diabetes_duration nomralisation? ##############
    asthma_duration = df['asthma_duration']
    asthma_duration = preprocessing.minmax_scale(asthma_duration.values)
    df['asthma_duration'] = asthma_duration

    # asthma_treatment
    # leave for now try to go for one hot encoding
    del df['asthma_treatment']

    # asthma_note
    # leave for now try to go for one hot encoding
    del df['ashtma_note']

    # cholesterol
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["cholesterol"] == 'Yes'), 'cholesterol'] = 1
    df.loc[(df["cholesterol"] == 'No'), 'cholesterol'] = 0
    df.loc[(df["cholesterol"] == 'Unknown'), 'cholesterol'] = 0.5
    df.loc[(df["cholesterol"] == 'No change'), 'cholesterol'] = 0.5
    df.loc[(df["cholesterol"].isnull()), 'cholesterol'] = 0.5
    # print(df['cholesterol'].tolist())

    # cholesterol duration
    df['cholesterol_duration'] = df['cholesterol_duration'].replace(to_replace=r'years', value='', regex=True)
    df['cholesterol_duration'] = df['cholesterol_duration'].replace(to_replace=r'>', value='', regex=True)
    df['cholesterol_duration'] = df['cholesterol_duration'].replace(to_replace=r'<', value='', regex=True)
    df['cholesterol_duration'] = df['cholesterol_duration'].replace(to_replace=r'year', value='', regex=True)
    df['cholesterol_duration'] = df['cholesterol_duration'].replace(to_replace=r' ', value='', regex=True)
    df['cholesterol_duration'] = df['cholesterol_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["cholesterol_duration"].isnull()), 'cholesterol_duration'] = 0
    df = df.astype({'cholesterol_duration': int})
    df['cholesterol_duration'] = df['cholesterol_duration'] * 365
    # print(df['cholesterol_duration'].tolist())

    ###### cholesterol_duration nomralisation? ##############
    cholesterol_duration = df['cholesterol_duration']
    cholesterol_duration = preprocessing.minmax_scale(cholesterol_duration.values)
    df['cholesterol_duration'] = cholesterol_duration

    # cholesterol_treatment
    # leave for now try to go for one hot encoding
    del df['cholesterol_treatment']

    # cholesterol_note
    # leave for now try to go for one hot encoding
    del df['cholesterol_note']

    # hypertension
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["hypertension"] == 'Yes'), 'hypertension'] = 1
    df.loc[(df["hypertension"] == 'No'), 'hypertension'] = 0
    df.loc[(df["hypertension"] == 'Unknown'), 'hypertension'] = 0.5
    df.loc[(df["hypertension"] == 'No change'), 'hypertension'] = 0.5
    df.loc[(df["hypertension"].isnull()), 'hypertension'] = 0.5
    # print(df['hypertension'].tolist())

    # hypertension duration
    df['hypertension_duration'] = df['hypertension_duration'].replace(to_replace=r'years', value='', regex=True)
    df['hypertension_duration'] = df['hypertension_duration'].replace(to_replace=r'>', value='', regex=True)
    df['hypertension_duration'] = df['hypertension_duration'].replace(to_replace=r'<', value='', regex=True)
    df['hypertension_duration'] = df['hypertension_duration'].replace(to_replace=r'year', value='', regex=True)
    df['hypertension_duration'] = df['hypertension_duration'].replace(to_replace=r' ', value='', regex=True)
    df['hypertension_duration'] = df['hypertension_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["hypertension_duration"].isnull()), 'hypertension_duration'] = 0
    df = df.astype({'hypertension_duration': int})
    df['hypertension_duration'] = df['hypertension_duration'] * 365
    # print(df['hypertension_duration'].tolist())

    ###### hypertension_duration nomralisation? ##############
    hypertension_duration = df['hypertension_duration']
    hypertension_duration = preprocessing.minmax_scale(hypertension_duration.values)
    df['hypertension_duration'] = hypertension_duration

    # hypertension_treatment
    # leave for now try to go for one hot encoding
    del df['hypertension_treatment']

    # hypertension_note
    # leave for now try to go for one hot encoding
    del df['hypertension_note']

    # heart
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["heart"] == 'Yes'), 'heart'] = 1
    df.loc[(df["heart"] == 'No'), 'heart'] = 0
    df.loc[(df["heart"] == 'Unknown'), 'heart'] = 0.5
    df.loc[(df["heart"] == 'No change'), 'heart'] = 0.5
    df.loc[(df["heart"].isnull()), 'heart'] = 0.5
    # print(df['heart'].tolist())

    # heart duration
    df['heart_duration'] = df['heart_duration'].replace(to_replace=r'years', value='', regex=True)
    df['heart_duration'] = df['heart_duration'].replace(to_replace=r'>', value='', regex=True)
    df['heart_duration'] = df['heart_duration'].replace(to_replace=r'<', value='', regex=True)
    df['heart_duration'] = df['heart_duration'].replace(to_replace=r'year', value='', regex=True)
    df['heart_duration'] = df['heart_duration'].replace(to_replace=r' ', value='', regex=True)
    df['heart_duration'] = df['heart_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["heart_duration"].isnull()), 'heart_duration'] = 0
    df = df.astype({'heart_duration': int})
    df['heart_duration'] = df['heart_duration'] * 365
    # print(df['heart_duration'].tolist())

    ###### heart_duration nomralisation? ##############
    heart_duration = df['heart_duration']
    heart_duration = preprocessing.minmax_scale(heart_duration.values)
    df['heart_duration'] = heart_duration

    # heart_treatment
    # leave for now try to go for one hot encoding
    del df['heart_treatment']

    # heart_note
    # leave for now try to go for one hot encoding
    del df['heart_note']

    # kidney
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["kidney"] == 'Yes'), 'kidney'] = 1
    df.loc[(df["kidney"] == 'No'), 'kidney'] = 0
    df.loc[(df["kidney"] == 'Unknown'), 'kidney'] = 0.5
    df.loc[(df["kidney"] == 'No change'), 'kidney'] = 0.5
    df.loc[(df["kidney"].isnull()), 'kidney'] = 0.5
    # print(df['kidney'].tolist())

    # kidney duration
    df['kidney_duration'] = df['kidney_duration'].replace(to_replace=r'years', value='', regex=True)
    df['kidney_duration'] = df['kidney_duration'].replace(to_replace=r'>', value='', regex=True)
    df['kidney_duration'] = df['kidney_duration'].replace(to_replace=r'<', value='', regex=True)
    df['kidney_duration'] = df['kidney_duration'].replace(to_replace=r'year', value='', regex=True)
    df['kidney_duration'] = df['kidney_duration'].replace(to_replace=r' ', value='', regex=True)
    df['kidney_duration'] = df['kidney_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["kidney_duration"].isnull()), 'kidney_duration'] = 0
    df = df.astype({'kidney_duration': int})
    df['kidney_duration'] = df['kidney_duration'] * 365
    # print(df['kidney_duration'].tolist())

    ###### kidney_duration nomralisation? ##############
    kidney_duration = df['kidney_duration']
    kidney_duration = preprocessing.minmax_scale(kidney_duration.values)
    df['kidney_duration'] = kidney_duration

    # kidney_treatment
    # leave for now try to go for one hot encoding
    del df['kidney_treatment']

    # kidney_note
    # leave for now try to go for one hot encoding
    del df['kidney_note']

    # lung
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["lung"] == 'Yes'), 'lung'] = 1
    df.loc[(df["lung"] == 'No'), 'lung'] = 0
    df.loc[(df["lung"] == 'Unknown'), 'lung'] = 0.5
    df.loc[(df["lung"] == 'No change'), 'lung'] = 0.5
    df.loc[(df["lung"].isnull()), 'lung'] = 0.5
    # print(df['lung'].tolist())

    # lung duration
    df['lung_duration'] = df['lung_duration'].replace(to_replace=r'years', value='', regex=True)
    df['lung_duration'] = df['lung_duration'].replace(to_replace=r'>', value='', regex=True)
    df['lung_duration'] = df['lung_duration'].replace(to_replace=r'<', value='', regex=True)
    df['lung_duration'] = df['lung_duration'].replace(to_replace=r'year', value='', regex=True)
    df['lung_duration'] = df['lung_duration'].replace(to_replace=r' ', value='', regex=True)
    df['lung_duration'] = df['lung_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["lung_duration"].isnull()), 'lung_duration'] = 0
    df = df.astype({'lung_duration': int})
    df['lung_duration'] = df['lung_duration'] * 365
    # print(df['lung_duration'].tolist())

    ###### lung_duration nomralisation? ##############
    lung_duration = df['lung_duration']
    lung_duration = preprocessing.minmax_scale(lung_duration.values)
    df['lung_duration'] = lung_duration

    # lung_treatment
    # leave for now try to go for one hot encoding
    del df['lung_treatment']

    # lung_note
    # leave for now try to go for one hot encoding
    del df['lung_note']

    # liver
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["liver"] == 'Yes'), 'liver'] = 1
    df.loc[(df["liver"] == 'No'), 'liver'] = 0
    df.loc[(df["liver"] == 'Unknown'), 'liver'] = 0.5
    df.loc[(df["liver"] == 'No change'), 'liver'] = 0.5
    df.loc[(df["liver"].isnull()), 'liver'] = 0.5
    # print(df['liver'].tolist())

    # liver duration
    df['liver_duration'] = df['liver_duration'].replace(to_replace=r'years', value='', regex=True)
    df['liver_duration'] = df['liver_duration'].replace(to_replace=r'>', value='', regex=True)
    df['liver_duration'] = df['liver_duration'].replace(to_replace=r'<', value='', regex=True)
    df['liver_duration'] = df['liver_duration'].replace(to_replace=r'year', value='', regex=True)
    df['liver_duration'] = df['liver_duration'].replace(to_replace=r' ', value='', regex=True)
    df['liver_duration'] = df['liver_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["liver_duration"].isnull()), 'liver_duration'] = 0
    df = df.astype({'liver_duration': int})
    df['liver_duration'] = df['liver_duration'] * 365
    # print(df['liver_duration'].tolist())

    ###### liver_duration nomralisation? ##############
    liver_duration = df['liver_duration']
    liver_duration = preprocessing.minmax_scale(liver_duration.values)
    df['liver_duration'] = liver_duration

    # liver_treatment
    # leave for now try to go for one hot encoding
    del df['liver_treatment']

    # liver_note
    # leave for now try to go for one hot encoding
    del df['liver_note']

    # stroke
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["stroke"] == 'Yes'), 'stroke'] = 1
    df.loc[(df["stroke"] == 'No'), 'stroke'] = 0
    df.loc[(df["stroke"] == 'Unknown'), 'stroke'] = 0.5
    df.loc[(df["stroke"] == 'No change'), 'stroke'] = 0.5
    df.loc[(df["stroke"].isnull()), 'stroke'] = 0.5
    # print(df['stroke'].tolist())

    # stroke duration
    df['stroke_duration'] = df['stroke_duration'].replace(to_replace=r'years', value='', regex=True)
    df['stroke_duration'] = df['stroke_duration'].replace(to_replace=r'>', value='', regex=True)
    df['stroke_duration'] = df['stroke_duration'].replace(to_replace=r'<', value='', regex=True)
    df['stroke_duration'] = df['stroke_duration'].replace(to_replace=r'year', value='', regex=True)
    df['stroke_duration'] = df['stroke_duration'].replace(to_replace=r' ', value='', regex=True)
    df['stroke_duration'] = df['stroke_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["stroke_duration"].isnull()), 'stroke_duration'] = 0
    df = df.astype({'stroke_duration': int})
    df['stroke_duration'] = df['stroke_duration'] * 365
    # print(df['stroke_duration'].tolist())

    # ##### stroke_duration nomralisation? ##############
    stroke_duration = df['stroke_duration']
    stroke_duration = preprocessing.minmax_scale(stroke_duration.values)
    df['stroke_duration'] = stroke_duration

    # stroke_treatment
    # leave for now try to go for one hot encoding
    del df['stroke_treatment']

    # stroke_note
    # leave for now try to go for one hot encoding
    del df['stroke_note']

    # other
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["other"] == 'Yes'), 'other'] = 1
    df.loc[(df["other"] == 'No'), 'other'] = 0
    df.loc[(df["other"] == 'Unknown'), 'other'] = 0.5
    df.loc[(df["other"] == 'No change'), 'other'] = 0.5
    df.loc[(df["other"].isnull()), 'other'] = 0.5
    # print(df['other'].tolist())

    # other duration
    df['other_duration'] = df['other_duration'].replace(to_replace=r'years', value='', regex=True)
    df['other_duration'] = df['other_duration'].replace(to_replace=r'>', value='', regex=True)
    df['other_duration'] = df['other_duration'].replace(to_replace=r'<', value='', regex=True)
    df['other_duration'] = df['other_duration'].replace(to_replace=r'year', value='', regex=True)
    df['other_duration'] = df['other_duration'].replace(to_replace=r' ', value='', regex=True)
    df['other_duration'] = df['other_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["other_duration"].isnull()), 'other_duration'] = 0
    df = df.astype({'other_duration': int})
    df['other_duration'] = df['other_duration'] * 365
    # print(df['other_duration'].tolist())

    # ##### other_duration nomralisation? ##############
    other_duration = df['other_duration']
    other_duration = preprocessing.minmax_scale(other_duration.values)
    df['other_duration'] = other_duration

    # other_treatment
    # extract bert features
    # df.loc[(df["other_treatment"].isnull()), 'other_treatment'] = 'NA'
    # other_treatment = df['other_treatment']
    # # print(other_treatment[1])
    # other_treatment = extract_bert_features(other_treatment)
    # np.save('other_treatment', other_treatment)

    # load to dataframe, each feature a column
    # other_treatment = np.load('other_treatment.npy')
    # print('other_treatment.shape', other_treatment.shape)
    # df_other_treatment = pd.DataFrame(other_treatment.reshape(326, -1))
    # print('surgery_note.shape', other_treatment.shape)
    # del df['other_treatment']
    # df = pd.concat([df, df_other_treatment], axis=1)

    # all features in one column
    other_treatment = np.load('other_treatment.npy').tolist()
    # print(other_treatment[0][0])
    df['other_treatment'] = other_treatment
    # print(df['other_treatment'])

    # other_note
    # leave for now try to go for one hot encoding
    del df['other_note']

    return df
