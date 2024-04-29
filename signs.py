import pandas as pd
from sklearn import preprocessing


def process_signs(df):

    # delete numbering
    df = df.drop(df.columns[0], axis=1)
    # del df[None]

    # subject id
    # leave as it is, its identifier to the case, not required in modelling

    # visit id
    # leave as it is, required to assoc with other sheets

    # medical_test_jaundice
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["medical_test_jaundice"] == 'Yes'), 'medical_test_jaundice'] = 1
    df.loc[(df["medical_test_jaundice"] == 'No'), 'medical_test_jaundice'] = 0
    df.loc[(df["medical_test_jaundice"] == 'Unknown'), 'medical_test_jaundice'] = 0.5
    df.loc[(df["medical_test_jaundice"].isnull()), 'medical_test_jaundice'] = 0.5
    # print(df['medical_test_jaundice'])

    # medical_test_jaundice_note
    # leave for bert
    del df['medical_test_jaundice_note']

    # medical_test_abdoMass
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["medical_test_abdoMass"] == 'Yes'), 'medical_test_abdoMass'] = 1
    df.loc[(df["medical_test_abdoMass"] == 'No'), 'medical_test_abdoMass'] = 0
    df.loc[(df["medical_test_abdoMass"] == 'Unknown'), 'medical_test_abdoMass'] = 0.5
    df.loc[(df["medical_test_abdoMass"].isnull()), 'medical_test_abdoMass'] = 0.5
    # print(df['medical_test_abdoMass'])

    # medical_test_abdoMass_note
    # leave for bert
    del df['medical_test_abdoMass_note']

    # medical_test_lymphNode
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["medical_test_lymphNode"] == 'Yes'), 'medical_test_lymphNode'] = 1
    df.loc[(df["medical_test_lymphNode"] == 'No'), 'medical_test_lymphNode'] = 0
    df.loc[(df["medical_test_lymphNode"] == 'Unknown'), 'medical_test_lymphNode'] = 0.5
    df.loc[(df["medical_test_lymphNode"].isnull()), 'medical_test_lymphNode'] = 0.5
    # print(df['medical_test_lymphNode'])

    # medical_test_lymphNode_note
    # leave for bert
    del df['medical_test_lymphNode_note']

    return df