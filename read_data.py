import pandas as pd
import xlwings as xw
from openpyxl import Workbook, load_workbook

from Blood import process_blood
from Demogra import process_demogra
from LifeStyle import process_lifestyle
from MedHist import process_medhist
from signs import process_signs
from symptoms import process_symptoms

# PATH = '/Volumes/mydrive/localdrive/datasets/panc_cys_gan/panc_cys_gan.xlsx'
PATH = './panc_cys_gan_pl.xlsx'


# wb = xw.Book(PATH)
wb = load_workbook(filename=PATH)
# wb = pd.read_excel(PATH)

# process sheet Demogra
# demogra = wb.sheets['demogra']
# demogra_df = demogra['A1:L327'].options(pd.DataFrame, index=False, header=True).value
# # print(df)
# demogra_df = process_demogra(demogra_df)
# print(demogra_df.columns.tolist())

# # process sheet symptoms
# symptoms = wb.sheets['symptoms']
# symptoms_df = symptoms['A1:AC327'].options(pd.DataFrame, index=False, header=True).value
# # print(df)
# symptoms_df = process_symptoms(symptoms_df)
# print(symptoms_df.columns.tolist())

# process sheet signs
# signs = wb.sheets['signs']
# signs_df = signs['A1:I327'].options(pd.DataFrame, index=False, header=True).value
# # print(df)
# signs_df = process_signs(signs_df)
# print(signs_df.columns.tolist())

# process sheet MedHist
# medhist = wb.sheets['MedHist']
# medhist_df = medhist['A1:AR327'].options(pd.DataFrame, index=False, header=True).value
# # print(df)
# medhist_df = process_medhist(medhist_df)
# print(medhist_df.columns.tolist())

# process sheet MedHist
# lifestyle = wb.sheets['LifeStyle']
# lifestyle = lifestyle['A1:L327'].options(pd.DataFrame, index=False, header=True).value
# # print(df)
# lifestyle_df = process_lifestyle(lifestyle)
# print(lifestyle_df.columns.tolist())

# process sheet MedHist
blood = wb.sheets['Blood']
blood = blood['A1:DZ327'].options(pd.DataFrame, index=False, header=True).value
# print(df)
blood_df = process_blood(blood)
print(blood_df.columns.tolist())
