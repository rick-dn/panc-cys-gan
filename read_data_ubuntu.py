import joblib
import pandas as pd
import xlwings as xw
from openpyxl import Workbook, load_workbook

from Blood import process_blood
from Demogra import process_demogra
from FamLife import process_famlife
from FamilyHCanc import process_fam_h_canc
from HistolDetails import process_histol_details
from LifeStyle import process_lifestyle
from MedHist import process_medhist
from Meds import process_meds
from Surgery import process_surgery
from Urine import process_urine
from investing_ctmri import process_investing_ctmri
from merge_df import merge_df
from signs import process_signs
from symptoms import process_symptoms

# PATH = '/Volumes/mydrive/localdrive/datasets/panc_cys_gan/panc_cys_gan.xlsx'
PATH = './panc_cys_gan_pl.xlsx'

wb = pd.read_excel(PATH, engine='openpyxl', sheet_name=None)
df_list = []

# # process sheet Demogra
# demogra = wb['Demogra']
# # demogra_df = demogra['A1:L327'].options(pd.DataFrame, index=False, header=True).value
# # print(df)
# demogra_df = process_demogra(demogra)
# print(demogra_df.columns.tolist())
# df_list.append(demogra_df)
#
# # process sheet symptoms
# symptoms = wb['symptoms']
# # symptoms_df = symptoms['A1:AC327'].options(pd.DataFrame, index=False, header=True).value
# # print(df)
# symptoms_df = process_symptoms(symptoms)
# print(symptoms_df.columns.tolist())
# df_list.append(symptoms_df)
#
# # process sheet signs
# signs = wb['signs']
# # signs_df = signs['A1:I327'].options(pd.DataFrame, index=False, header=True).value
# # print(df)
# signs_df = process_signs(signs)
# print(signs_df.columns.tolist())
# df_list.append(signs_df)
#
# # process sheet MedHist
# medhist = wb['MedHist']
# # medhist_df = medhist['A1:AR327'].options(pd.DataFrame, index=False, header=True).value
# # print(df)
# medhist_df = process_medhist(medhist)
# print(medhist_df.columns.tolist())
# df_list.append(medhist_df)

# # process sheet Meds
# meds = wb['Meds']
# # meds_df = Meds['A1:AR327'].options(pd.DataFrame, index=False, header=True).value
# # print(df)
# meds_df = process_meds(meds)
# print(meds_df.columns.tolist())
# df_list.append(meds_df)
#
# # process sheet LifeStyle
# lifestyle = wb['Lifestyle']
# # lifestyle = lifestyle['A1:L327'].options(pd.DataFrame, index=False, header=True).value
# # print(df)
# lifestyle_df = process_lifestyle(lifestyle)
# print(lifestyle_df.columns.tolist())
# df_list.append(lifestyle_df)
#
# # process sheet FamLife
# famlife = wb['FamLife']
# # famlife = famlife['A1:F327'].options(pd.DataFrame, index=False, header=True).value
# # famlife.__delitem__(None)
# # print(famlife.columns.tolist())
# # print(df)
# famlife_df = process_famlife(famlife)
# print(famlife_df.columns.tolist())
# df_list.append(famlife_df)
#
# # process sheet FamHCanc
# fam_h_canc = wb['FamHCanc']
# # fam_h_canc = fam_h_canc['A1:F122'].options(pd.DataFrame, index=False, header=True).value
# # print(fam_h_canc.columns.tolist())
# # print(df)
# fam_h_canc_df = process_fam_h_canc(fam_h_canc)
# print(fam_h_canc_df.columns.tolist())
# df_list.append(fam_h_canc_df)
#
# # process sheet Blood
# blood = wb['Blood']
# # blood = blood['A1:DZ327'].options(pd.DataFrame, index=False, header=True).value
# # print(df)
# blood_df = process_blood(blood)
# print(blood_df.columns.tolist())
# df_list.append(blood_df)
#
# # process sheet Urine
# urine = wb['Urine']
# # urine = urine['A1:M327'].options(pd.DataFrame, index=False, header=True).value
# # print(df)
# urine_df = process_urine(urine)
# print(urine_df.columns.tolist())
# df_list.append(urine_df)
#
# process sheet Investig-CTMRI
investing_ctmri = wb['Investig-CTMRI']
# blood = blood['A1:DZ327'].options(pd.DataFrame, index=False, header=True).value
# print(df)
investing_ctmri_df = process_investing_ctmri(investing_ctmri)
print(investing_ctmri_df.columns.tolist())
df_list.append(investing_ctmri_df)

# process sheet HistolDetails
histol_details = wb['HistolDetails']
# blood = blood['A1:DZ327'].options(pd.DataFrame, index=False, header=True).value
# print(df)
histol_details_df = process_histol_details(histol_details)
print(histol_details_df.columns.tolist())
df_list.append(histol_details_df)

# process sheet Surgery
Surgery = wb['Surgery']
# blood = blood['A1:DZ327'].options(pd.DataFrame, index=False, header=True).value
# print(df)
surgery_df = process_surgery(Surgery)
print(surgery_df.columns.tolist())
df_list.append(surgery_df)

# save the lists
# joblib.dump(df_list, filename='df_list.joblib')
# df_list = joblib.load('df_list.joblib')
# print(df_list)

# merged_df = merge_df(df_list)
# print('total columns: ', merged_df.count())
# merged_df.to_csv('merged_panc_cys_gan_inner.csv')
