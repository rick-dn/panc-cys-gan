import pandas as pd
import xlwings as xw

PATH = '/Volumes/mydrive/localdrive/datasets/panc_cys_gan/panc_cys_gan.xlsx'

wb = xw.Book(PATH)
sheet = wb.sheets['demogra']

df = sheet['A1:L327'].options(pd.DataFrame, index=False, header=True).value
# print(df)

# for column in df:
#     print(column)

# visit_id = []

# visit_ids = df['visit_id'].tolist()

# print(visit_ids)

# df = pd.read_excel(open(PATH, 'r'), sheet_name='Demogra')

# print(df)

# print(df['height_cm'])

# print(df['height_cm'].mean())

# df['height_cm'] = df['height_cm'].fillna(df['height_cm'].mean())

# print(df['height_cm'])

# print(df.loc[df['gender'] == 'Female']['height_cm'])
avg_female = df.loc[df['gender'] == 'Female']['height_cm'].mean()
print('average female height: ', avg_female)

# df.loc[df['foo'].isnull(), 'foo'] = df['bar']

# print(df.loc[df['gender'] == 'Female'])
# print(df.loc[df['height_cm'].isnull()])

# print(df.loc[df['gender'] == 'Female'])
# print(df.loc[df['height_cm'].isnull()])

# print(df["height_cm"][(df["height_cm"].isnull()) & (df["gender"] == 'Female')])

# works
df.loc[(df["height_cm"].isnull()) & (df["gender"] == 'Female'), 'height_cm'] = avg_female

# df.loc[[(df["height_cm"].isnull()) & (df["gender"] == 'Female')], 'height_cm'] = avg_female

# print(df.loc[(df["gender"] == 'Female'), 'height_cm'])

# df.loc[df.loc[df['gender'] == 'Female'] & df.loc[df['height_cm'].isnull()]] = avg_female

print(df.loc[df['gender'] == 'Female', 'height_cm'])

