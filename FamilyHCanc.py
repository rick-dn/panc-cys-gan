import pandas as pd
from sklearn import preprocessing


def process_fam_h_canc(df):

    # subject id
    # leave as it is, its identifier to the case, not required in modelling

    # visit id
    # leave as it is, required to assoc with other sheets

    # relation
    # print(df['relation'])
    df = pd.concat([df, pd.get_dummies(df['relation'],
                                       prefix='relation',
                                       dummy_na=True)], axis=1).drop(['relation'], axis=1)

    # relation_subtype
    # print(df['relation_subtype'])
    df = pd.concat([df, pd.get_dummies(df['relation_subtype'],
                                       prefix='relation_subtype',
                                       dummy_na=True)], axis=1).drop(['relation_subtype'], axis=1)

    # cancer
    # print(df['cancer'])
    df = pd.concat([df, pd.get_dummies(df['cancer'],
                                       prefix='cancer',
                                       dummy_na=True)], axis=1).drop(['cancer'], axis=1)

    # diag_age
    # print(df['diag_age'])
    df = pd.concat([df, pd.get_dummies(df['diag_age'],
                                       prefix='diag_age',
                                       dummy_na=True)], axis=1).drop(['diag_age'], axis=1)

    return df