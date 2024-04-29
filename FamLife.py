import pandas as pd
from sklearn import preprocessing


def process_famlife(df):

    # delete numbering
    df = df.drop(df.columns[0], axis=1)
    # del df[None]

    # subject id
    # leave as it is, its identifier to the case, not required in modelling

    # visit id
    # leave as it is, required to assoc with other sheets

    # spouse
    # print(df['spouse'])
    df = pd.concat([df, pd.get_dummies(df['spouse'],
                                       prefix='spouse',
                                       dummy_na=True)], axis=1).drop(['spouse'], axis=1)

    # children
    # print(df['children'])
    df = pd.concat([df, pd.get_dummies(df['children'],
                                       prefix='children',
                                       dummy_na=True)], axis=1).drop(['children'], axis=1)

    # no_of_child
    # print(df['no_of_child'])
    # df = pd.concat([df, pd.get_dummies(df['no_of_child'],
    #                                    prefix='no_of_child',
    #                                    dummy_na=True)], axis=1).drop(['no_of_child'], axis=1)

    df.loc[df["no_of_child"].isnull(), 'no_of_child'] = 0
    no_of_child = df['no_of_child']
    # print('Number_days_to_visit', Number_days_to_visit.values)
    no_of_child = preprocessing.minmax_scale(no_of_child.values)
    df['no_of_child'] = no_of_child
    # print(df['Number_days_to_visit'].values)

    return df
