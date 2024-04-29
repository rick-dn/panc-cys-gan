# surgery_complications
# print(df['surgery_complications'])
df.loc[(df["surgery_complications"].isnull()), 'note'] = 'NA'
df = pd.concat([df, pd.get_dummies(df['surgery_complications'],
                                   prefix='surgery_complications',
                                   dummy_na=True)], axis=1).drop(['surgery_complications'], axis=1)
# print(df['surgery_complications'])