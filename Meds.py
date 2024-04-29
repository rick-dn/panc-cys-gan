import pandas as pd
from sklearn import preprocessing


def process_meds(df):

    # # delete numbering
    df = df.drop(df.columns[0], axis=1)
    # del df[None]

    # subject id
    # leave as it is, its identifier to the case, not required in modelling

    # visit id
    # leave as it is, required to assoc with other sheets

    # medication
    # print(df['medication'])
    df = pd.concat([df, pd.get_dummies(df['medication'],
                                       prefix='medication',
                                       dummy_na=True)], axis=1).drop(['medication'], axis=1)

    # medication_reason
    # print(df['medication_reason'])
    df = pd.concat([df, pd.get_dummies(df['medication_reason'],
                                       prefix='medication_reason',
                                       dummy_na=True)], axis=1).drop(['medication_reason'], axis=1)

    # medication_duration
    df['medication_duration'] = df['medication_duration'].replace(to_replace=r'years', value='', regex=True)
    df['medication_duration'] = df['medication_duration'].replace(to_replace=r'>', value='', regex=True)
    df['medication_duration'] = df['medication_duration'].replace(to_replace=r'<', value='', regex=True)
    df['medication_duration'] = df['medication_duration'].replace(to_replace=r'year', value='', regex=True)
    df['medication_duration'] = df['medication_duration'].replace(to_replace=r' ', value='', regex=True)
    df['medication_duration'] = df['medication_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["medication_duration"].isnull()), 'medication_duration'] = 0
    df = df.astype({'medication_duration': int})
    df['medication_duration'] = df['medication_duration'] * 365
    # print(df['medication_duration'].tolist())

    # ##### diabetes_duration nomralisation? ##############
    medication_duration = df['medication_duration']
    medication_duration = preprocessing.minmax_scale(medication_duration.values)
    df['medication_duration'] = medication_duration

    return df
