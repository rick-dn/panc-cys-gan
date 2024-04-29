import pandas as pd
from sklearn import preprocessing


def process_symptoms(df):

    # delete numbering
    df = df.drop(df.columns[0], axis=1)
    # del df[None]

    # subject id
    # leave as it is, its identifier to the case, not required in modelling

    # visit id
    # leave as it is, required to assoc with other sheets

    # pain
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["pain"] == 'Yes'), 'pain'] = 1
    df.loc[(df["pain"] == 'No'), 'pain'] = 0
    df.loc[(df["pain"] == 'unknown'), 'pain'] = 0.5
    df.loc[(df["pain"].isnull()), 'pain'] = 0.5
    # print(df['pain'])

    # pain duration
    df['pain_duration'] = df['pain_duration'].replace(to_replace=r'weeks', value='', regex=True)
    df['pain_duration'] = df['pain_duration'].replace(to_replace=r'>', value='', regex=True)
    df['pain_duration'] = df['pain_duration'].replace(to_replace=r'<', value='', regex=True)
    df['pain_duration'] = df['pain_duration'].replace(to_replace=r'week', value='', regex=True)
    df['pain_duration'] = df['pain_duration'].replace(to_replace=r' ', value='', regex=True)
    df['pain_duration'] = df['pain_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["pain_duration"].isnull()), 'pain_duration'] = 0
    df = df.astype({'pain_duration': int})
    df['pain_duration'] = df['pain_duration'] * 7
    # print(df['pain_duration'])

    ###### pain duration nomralisation? ##############
    pain_duration = df['pain_duration']
    pain_duration = preprocessing.minmax_scale(pain_duration.values)
    df['pain_duration'] = pain_duration

    # pain site
    # leave for now, need to change it consistent site terminology
    # print(df['pain_site'])
    df = pd.concat([df, pd.get_dummies(df['pain_site'],
                                       prefix='pain_site',
                                       dummy_na=True)], axis=1).drop(['pain_site'], axis=1)

    # pain note
    # to be processed by bert
    del df['pain_note']

    # jaundice
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["jaundice"] == 'Yes'), 'jaundice'] = 1
    df.loc[(df["jaundice"] == 'No'), 'jaundice'] = 0
    df.loc[(df["jaundice"] == 'unknown'), 'jaundice'] = 0.5
    df.loc[(df["jaundice"].isnull()), 'jaundice'] = 0.5
    # print(df['pain'])

    # jaundice duration
    # fully empty leave for now
    df['jaundice_duration'] = df['jaundice_duration'].replace(to_replace=r'weeks', value='', regex=True)
    df['jaundice_duration'] = df['jaundice_duration'].replace(to_replace=r'>', value='', regex=True)
    df['jaundice_duration'] = df['jaundice_duration'].replace(to_replace=r'<', value='', regex=True)
    df['jaundice_duration'] = df['jaundice_duration'].replace(to_replace=r'week', value='', regex=True)
    df['jaundice_duration'] = df['jaundice_duration'].replace(to_replace=r' ', value='', regex=True)
    df['jaundice_duration'] = df['jaundice_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["jaundice_duration"].isnull()), 'jaundice_duration'] = 0
    df = df.astype({'jaundice_duration': int})
    df['jaundice_duration'] = df['jaundice_duration'] * 7
    # print(df['jaundice_duration'])

    ###### jaundice duration nomralisation? ##############
    jaundice_duration = df['jaundice_duration']
    jaundice_duration = preprocessing.minmax_scale(jaundice_duration.values)
    df['jaundice_duration'] = jaundice_duration

    # jaundice note
    # all columns empty for now
    del df['jaundice_note']

    # weightLoss
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["weightLoss"] == 'Yes'), 'weightLoss'] = 1
    df.loc[(df["weightLoss"] == 'No'), 'weightLoss'] = 0
    df.loc[(df["weightLoss"] == 'unknown'), 'weightLoss'] = 0.5
    df.loc[(df["weightLoss"].isnull()), 'weightLoss'] = 0.5
    # print(df['weightLoss'])

    # weightLoss duration
    # fully empty leave for now
    df['weightLoss_duration'] = df['weightLoss_duration'].replace(to_replace=r'weeks', value='', regex=True)
    df['weightLoss_duration'] = df['weightLoss_duration'].replace(to_replace=r'>', value='', regex=True)
    df['weightLoss_duration'] = df['weightLoss_duration'].replace(to_replace=r'<', value='', regex=True)
    df['weightLoss_duration'] = df['weightLoss_duration'].replace(to_replace=r'week', value='', regex=True)
    df['weightLoss_duration'] = df['weightLoss_duration'].replace(to_replace=r' ', value='', regex=True)
    df['weightLoss_duration'] = df['weightLoss_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["weightLoss_duration"].isnull()), 'weightLoss_duration'] = 0
    df = df.astype({'weightLoss_duration': int})
    df['weightLoss_duration'] = df['weightLoss_duration'] * 7
    # print(df['weightLoss_duration'])

    ###### weightLoss duration nomralisation? ##############
    weightLoss_duration = df['weightLoss_duration']
    weightLoss_duration = preprocessing.minmax_scale(weightLoss_duration.values)
    df['weightLoss_duration'] = weightLoss_duration
    # print(df['weightLoss_duration'].values)

    # weightLoss amount
    df.loc[(df["weightLoss_amount"].isnull()), 'weightLoss_amount'] = 0
    weightLoss_amount = df['weightLoss_amount']
    weightLoss_amount = preprocessing.minmax_scale(weightLoss_amount.values)
    df['weightLoss_amount'] = weightLoss_amount

    # weightLoss note
    # columns empty for now
    del df['weightLoss_note']

    # nausea
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df['nausea'] == 'Yes'), 'nausea'] = 1
    df.loc[(df["nausea"] == 'No'), 'nausea'] = 0
    df.loc[(df["nausea"] == 'unknown'), 'nausea'] = 0.5
    df.loc[(df["nausea"].isnull()), 'nausea'] = 0.5
    # print(df['nausea'])

    # nausea duration
    # fully empty leave for now
    df['nausea_duration'] = df['nausea_duration'].replace(to_replace=r'weeks', value='', regex=True)
    df['nausea_duration'] = df['nausea_duration'].replace(to_replace=r'>', value='', regex=True)
    df['nausea_duration'] = df['nausea_duration'].replace(to_replace=r'<', value='', regex=True)
    df['nausea_duration'] = df['nausea_duration'].replace(to_replace=r'week', value='', regex=True)
    df['nausea_duration'] = df['nausea_duration'].replace(to_replace=r' ', value='', regex=True)
    df['nausea_duration'] = df['nausea_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["nausea_duration"].isnull()), 'nausea_duration'] = 0
    df = df.astype({'nausea_duration': int})
    df['nausea_duration'] = df['nausea_duration'] * 7
    # print(df['nausea_duration'])

    ###### nausea duration nomralisation? ##############
    weightLoss_amount = df['weightLoss_amount']
    weightLoss_amount = preprocessing.minmax_scale(weightLoss_amount.values)
    df['weightLoss_amount'] = weightLoss_amount

    # nausea note
    # all columns empty for now
    del df['nausea_note']

    # vomit
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["vomit"] == 'Yes'), 'vomit'] = 1
    df.loc[(df["vomit"] == 'No'), 'vomit'] = 0
    df.loc[(df["vomit"] == 'unknown'), 'vomit'] = 0.5
    df.loc[(df["vomit"].isnull()), 'vomit'] = 0.5
    # print(df['vomit'])

    # vomit duration
    # fully empty leave for now
    df['vomit_duration'] = df['vomit_duration'].replace(to_replace=r'weeks', value='', regex=True)
    df['vomit_duration'] = df['vomit_duration'].replace(to_replace=r'>', value='', regex=True)
    df['vomit_duration'] = df['vomit_duration'].replace(to_replace=r'<', value='', regex=True)
    df['vomit_duration'] = df['vomit_duration'].replace(to_replace=r'week', value='', regex=True)
    df['vomit_duration'] = df['vomit_duration'].replace(to_replace=r' ', value='', regex=True)
    df['vomit_duration'] = df['vomit_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["vomit_duration"].isnull()), 'vomit_duration'] = 0
    df = df.astype({'vomit_duration': int})
    df['vomit_duration'] = df['vomit_duration'] * 7
    # print(df['vomit_duration'])

    ###### vomit duration nomralisation? ##############
    vomit_duration = df['vomit_duration']
    vomit_duration = preprocessing.minmax_scale(vomit_duration.values)
    df['weightLoss_amount'] = vomit_duration

    # vomit note
    # all columns empty for now
    del df['vomit_note']

    # diarrhoea
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["diarrhoea"] == 'Yes'), 'diarrhoea'] = 1
    df.loc[(df["diarrhoea"] == 'No'), 'diarrhoea'] = 0
    df.loc[(df["diarrhoea"] == 'unknown'), 'diarrhoea'] = 0.5
    df.loc[(df["diarrhoea"].isnull()), 'diarrhoea'] = 0.5
    # print(df['diarrhoea'])

    # diarrhoea duration
    # fully empty leave for now
    df['diarrhoea_duration'] = df['diarrhoea_duration'].replace(to_replace=r'weeks', value='', regex=True)
    df['diarrhoea_duration'] = df['diarrhoea_duration'].replace(to_replace=r'>', value='', regex=True)
    df['diarrhoea_duration'] = df['diarrhoea_duration'].replace(to_replace=r'<', value='', regex=True)
    df['diarrhoea_duration'] = df['diarrhoea_duration'].replace(to_replace=r'week', value='', regex=True)
    df['diarrhoea_duration'] = df['diarrhoea_duration'].replace(to_replace=r' ', value='', regex=True)
    df['diarrhoea_duration'] = df['diarrhoea_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["diarrhoea_duration"].isnull()), 'diarrhoea_duration'] = 0
    df = df.astype({'diarrhoea_duration': int})
    df['diarrhoea_duration'] = df['diarrhoea_duration'] * 7
    # print(df['diarrhoea_duration'])

    ###### diarrhoea duration nomralisation? ##############
    diarrhoea_duration = df['diarrhoea_duration']
    diarrhoea_duration = preprocessing.minmax_scale(diarrhoea_duration.values)
    df['weightLoss_amount'] = diarrhoea_duration

    # diarrhoea note
    # all columns empty for now
    del df['diarrhoea_note']

    # constipation
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["constipation"] == 'Yes'), 'other'] = 1
    df.loc[(df["constipation"] == 'No'), 'other'] = 0
    df.loc[(df["constipation"] == 'unknown'), 'other'] = 0.5
    df.loc[(df["constipation"].isnull()), 'other'] = 0.5
    # print(df['other'])

    # constipation_duration duration
    # fully empty leave for now
    df['constipation_duration'] = df['constipation_duration'].replace(to_replace=r'weeks', value='', regex=True)
    df['constipation_duration'] = df['constipation_duration'].replace(to_replace=r'>', value='', regex=True)
    df['constipation_duration'] = df['constipation_duration'].replace(to_replace=r'<', value='', regex=True)
    df['constipation_duration'] = df['constipation_duration'].replace(to_replace=r'week', value='', regex=True)
    df['constipation_duration'] = df['constipation_duration'].replace(to_replace=r' ', value='', regex=True)
    df['constipation_duration'] = df['constipation_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["constipation_duration"].isnull()), 'constipation_duration'] = 0
    df = df.astype({'constipation_duration': int})
    df['constipation_duration'] = df['constipation_duration'] * 7
    # print(df['other_duration'])

    ###### constipation_duration nomralisation? ##############
    constipation_duration = df['constipation_duration']
    constipation_duration = preprocessing.minmax_scale(constipation_duration.values)
    df['constipation_duration'] = constipation_duration

    # constipation_note
    # all columns empty for now
    del df['constipation_note']

    # other
    # 1: yes, 0: no, 0.5 unknown
    df.loc[(df["other"] == 'Yes'), 'other'] = 1
    df.loc[(df["other"] == 'No'), 'other'] = 0
    df.loc[(df["other"] == 'unknown'), 'other'] = 0.5
    df.loc[(df["other"].isnull()), 'other'] = 0.5
    # print(df['other'])

    # other duration
    # fully empty leave for now
    df['other_duration'] = df['other_duration'].replace(to_replace=r'weeks', value='', regex=True)
    df['other_duration'] = df['other_duration'].replace(to_replace=r'>', value='', regex=True)
    df['other_duration'] = df['other_duration'].replace(to_replace=r'<', value='', regex=True)
    df['other_duration'] = df['other_duration'].replace(to_replace=r'week', value='', regex=True)
    df['other_duration'] = df['other_duration'].replace(to_replace=r' ', value='', regex=True)
    df['other_duration'] = df['other_duration'].replace(to_replace=r'^$', value=0, regex=True)
    df.loc[(df["other_duration"].isnull()), 'other_duration'] = 0
    df = df.astype({'other_duration': int})
    df['other_duration'] = df['other_duration'] * 7
    # print(df['other_duration'])

    ###### other duration nomralisation? ##############
    other_duration = df['other_duration']
    other_duration = preprocessing.minmax_scale(other_duration.values)
    df['weightLoss_amount'] = other_duration

    # other note
    # all columns empty for now
    del df['other_note']

    return df