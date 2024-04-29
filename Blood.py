import pandas as pd
from sklearn import preprocessing


def process_blood(df):

    # subject id
    # leave as it is, its identifier to the case, not required in modelling

    # visit id
    # leave as it is, required to assoc with other sheets

    # delete empty column
    df = df.drop(df.columns[2], axis=1)

    # ALP Ignore for now, very few values
    del df['ALP']

    # ALT
    df['ALT_done'] = 1
    df.loc[df['ALT'].isnull(), 'ALT_done'] = 0

    avg_ALT = df['ALT'].mean()
    # print('average ALT: ', ALT)
    df.loc[(df["ALT"].isnull()), 'ALT'] = avg_ALT

    ALT = df['ALT']
    # print('ALT', ALT.values)
    ALT = preprocessing.minmax_scale(ALT.values)
    df['ALT'] = ALT
    # print(df['ALT'].tolist())

    # AST & AST_GG
    # Ignore, very few data
    del df['AST']
    del df['AST GGT']

    # Alb
    df['Alb_done'] = 1
    df.loc[df['Alb'].isnull(), 'Alb_done'] = 0

    avg_Alb = df['Alb'].mean()
    # print('average Alb: ', Alb)
    df.loc[(df["Alb"].isnull()), 'Alb'] = avg_Alb

    Alb = df['Alb']
    # print('Alb', Alb.values)
    Alb = preprocessing.minmax_scale(Alb.values)
    df['Alb'] = Alb
    # print(df['Alb'].tolist())

    # Alp
    df['Alp_done'] = 1
    df.loc[df['Alp'].isnull(), 'Alp_done'] = 0

    avg_Alp = df['Alp'].mean()
    # print('average Alp: ', Alp)
    df.loc[(df["Alp"].isnull()), 'Alp'] = avg_Alp

    Alp = df['Alp']
    # print('Alp', Alp.values)
    Alp = preprocessing.minmax_scale(Alp.values)
    df['Alp'] = Alp
    # print(df['Alp'].tolist())

    # Bil
    df['Bil_done'] = 1
    df.loc[df['Bil'].isnull(), 'Bil_done'] = 0

    avg_Bil = df['Bil'].mean()
    # print('average Bil: ', Bil)
    df.loc[(df["Bil"].isnull()), 'Bil'] = avg_Bil

    Bil = df['Bil']
    # print('Bil', Bil.values)
    Bil = preprocessing.minmax_scale(Bil.values)
    df['Bil'] = Bil
    # print(df['Bil'].tolist())

    # CA 19-9
    df['CA 19-9_done'] = 1
    df.loc[df['CA 19-9'].isnull(), 'CA 19-9_done'] = 0

    avg_Bil = df['CA 19-9'].mean()
    # print('average Bil: ', Bil)
    df.loc[(df["CA 19-9"].isnull()), 'CA 19-9'] = avg_Bil

    CA_19_9 = df['CA 19-9']
    # print('Bil', Bil.values)
    CA_19_9 = preprocessing.minmax_scale(CA_19_9.values)
    df['CA_19_9'] = CA_19_9
    # print(df['CA_19_9'].tolist())

    # CEA, COVID-19
    # ignore lot of missing values
    del df['CEA']
    del df['COVID-19']

    # CRP
    df['CRP_done'] = 1
    df.loc[df['CRP'].isnull(), 'CRP_done'] = 0

    # avg_Bil = df['CA 19-9'].mean()
    # print('average Bil: ', Bil)
    df.loc[(df["CRP"].isnull()), 'CRP'] = 0

    CRP = df['CRP']
    # print('Bil', Bil.values)
    CRP = preprocessing.minmax_scale(CRP.values)
    df['CRP'] = CRP
    # print(df['CA_19_9'].tolist())

    # Ca 19-9
    del df['Ca 19-9']

    # Creat
    df['Creat_done'] = 1
    df.loc[df['Creat'].isnull(), 'Creat_done'] = 0

    avg_Creat = df['Creat'].mean()
    # print('average Creat: ', Creat)
    df.loc[(df["Creat"].isnull()), 'Creat'] = avg_Creat

    Creat = df['Creat']
    # print('Creat', Creat.values)
    Creat = preprocessing.minmax_scale(Creat.values)
    df['Creat'] = Creat
    # print(df['Creat'].tolist())

    # GGT Ignore, too many missing values
    del df['GGT']

    # Hb
    df['Hb_done'] = 1
    df.loc[df['Hb'].isnull(), 'Hb_done'] = 0

    avg_Hb = df['Hb'].mean()
    # print('average Hb: ', Hb)
    df.loc[(df["Hb"].isnull()), 'Hb'] = avg_Hb

    Hb = df['Hb']
    # print('Hb', Hb.values)
    Hb = preprocessing.minmax_scale(Hb.values)
    df['Hb'] = Hb
    # print(df['Hb'].tolist())

    # K
    df['K_done'] = 1
    df.loc[df['K'].isnull(), 'K_done'] = 0

    avg_K = df['K'].mean()
    # print('average K: ', K)
    df.loc[(df["K"].isnull()), 'K'] = avg_K

    K = df['K']
    # print('K', K.values)
    K = preprocessing.minmax_scale(K.values)
    df['K'] = K
    # print(df['K'].tolist())

    # Na
    df['Na_done'] = 1
    df.loc[df['Na'].isnull(), 'Na_done'] = 0

    avg_Na = df['Na'].mean()
    # print('average Na: ', Na)
    df.loc[(df["Na"].isnull()), 'Na'] = avg_Na

    Na = df['Na']
    # print('Na', Na.values)
    Na = preprocessing.minmax_scale(Na.values)
    df['Na'] = Na
    # print(df['Na'].tolist())

    # Ingnore columns V to DS
    # Too many missing values
    df = df[df.columns.drop(list(df.filter(regex='Other')))]

    # Plt
    df['Plt_done'] = 1
    df.loc[df['Plt'].isnull(), 'Plt_done'] = 0

    avg_Plt = df['Plt'].mean()
    # print('average Plt: ', Plt)
    df.loc[(df["Plt"].isnull()), 'Plt'] = avg_Plt

    Plt = df['Plt']
    # print('Plt', Plt.values)
    Plt = preprocessing.minmax_scale(Plt.values)
    df['Plt'] = Plt
    # print(df['Plt'].tolist())

    # TProt
    df['TProt_done'] = 1
    df.loc[df['T Prot'].isnull(), 'TProt_done'] = 0

    avg_Plt = df['T Prot'].mean()
    # print('average Plt: ', Plt)
    df.loc[(df["T Prot"].isnull()), 'T Prot'] = avg_Plt

    TProt = df['T Prot']
    # print('Plt', Plt.values)
    TProt = preprocessing.minmax_scale(TProt.values)
    df['T Prot'] = TProt
    # print(df['TProt'].tolist())

    # Ignore Tprotein, Ur
    # Too many missing values
    del df['Tprotein']
    del df['Ur']

    # Urea
    df['Urea_done'] = 1
    df.loc[df['Urea'].isnull(), 'Urea_done'] = 0

    avg_Urea = df['Urea'].mean()
    # print('average Urea: ', Urea)
    df.loc[(df["Urea"].isnull()), 'Urea'] = avg_Urea

    Urea = df['Urea']
    # print('Urea', Urea.values)
    Urea = preprocessing.minmax_scale(Urea.values)
    df['Urea'] = Urea
    # print(df['Urea'].tolist())

    # WCC
    df['WCC_done'] = 1
    df.loc[df['WCC'].isnull(), 'WCC_done'] = 0

    avg_WCC = df['WCC'].mean()
    # print('average WCC: ', WCC)
    df.loc[(df["WCC"].isnull()), 'WCC'] = avg_WCC

    WCC = df['WCC']
    # print('WCC', WCC.values)
    WCC = preprocessing.minmax_scale(WCC.values)
    df['WCC'] = WCC
    # print(df['WCC'].tolist())

    # eGFR
    df['eGFR_done'] = 1
    df.loc[df['eGFR'].isnull(), 'eGFR_done'] = 0

    avg_eGFR = df['eGFR'].mean()
    # print('average eGFR: ', eGFR)
    df.loc[(df["eGFR"].isnull()), 'eGFR'] = avg_eGFR

    eGFR = df['eGFR']
    # print('eGFR', eGFR.values)
    eGFR = preprocessing.minmax_scale(eGFR.values)
    df['eGFR'] = eGFR
    # print(df['eGFR'].tolist())

    # print(df['ALT_done'])

    return df
