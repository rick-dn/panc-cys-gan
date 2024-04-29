import pandas as pd


def merge_df(df_list):

    merged_df = None
    for df in df_list:
        if merged_df is None:
            merged_df = df
        else:
            print('while merging', df.columns.tolist())
            # merged_df = pd.merge(merged_df, df, on=['visit_id'], how='outer')
            merged_df = pd.merge(merged_df, df, on=['visit_id'], how='left')
            print('merged')

    print(merged_df.columns.tolist())
    return merged_df

