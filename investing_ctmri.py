import numpy as np
import pandas as pd
from sklearn import preprocessing

from extract_features import extract_bert_features


def process_investing_ctmri(df):

    # delete numbering
    df = df.drop(df.columns[0], axis=1)
    # del df[None]

    # print('Number of rows Investig-CTMRI',  df.count)
    # exit()
    # subject id
    # leave as it is, its identifier to the case, not required in modelling

    # visit id
    # leave as it is, required to assoc with other sheets

    # type
    # print(df['type'])
    df.loc[(df["type"].isnull()), 'note'] = 'NA'
    df = pd.concat([df, pd.get_dummies(df['type'],
                                       prefix='type',
                                       dummy_na=True)], axis=1).drop(['type'], axis=1)
    # print(df['type'])

    # report date
    # ignore, use visit id

    # report file
    # ignore
    del df['report_file']

    # note, process with bert
    df.loc[(df["note"].isnull()), 'note'] = 'NA'
    note = df['note']
    # # print(note[1])
    # note = extract_bert_features(note)
    # print('saving note')
    # np.save('investing_ctmri_note', note)

    # load to dataframe, each feature a column
    # note = np.load('investing_ctmri_note.npy')
    # print('note.shape', note.shape)
    # note = note.reshape(769, -1)
    # print('note.shape', note.shape)
    # df_note = pd.DataFrame(note)
    # del df['note']
    # df = pd.concat([df, df_note], axis=1)

    # all features in one column
    # note = np.load('investing_ctmri_note.npy').tolist()
    # # print(note[0][0])
    # df['note'] = note
    # # print(df['note'])

    # scan_reports extract bert features
    df.loc[(df["Scan_Reports"].isnull()), 'Scan_Reports'] = 'NA'
    scan_reports = df['Scan_Reports']
    # print(note[1])
    # scan_reports = extract_bert_features(scan_reports)
    # np.save('investing_ctmri_scan_reports', scan_reports)

    # load to dataframe, each feature a column
    # scan_reports = np.load('investing_ctmri_scan_reports.npy')
    # # print('scan_reports.shape', scan_reports.shape)
    # scan_reports = scan_reports.reshape(769, -1)
    # df_scan = pd.DataFrame(scan_reports)
    # # df['Scan_Reports'] = scan_reports
    # del df['Scan_Reports']
    # # print(scan_reports.shape)
    # df = pd.concat([df, df_scan], axis=1)

    # all features in one column
    # scan_reports = np.load('investing_ctmri_scan_reports.npy').tolist()
    # # print(scan_reports[0][0])
    # df['Scan_Reports'] = scan_reports
    # # print(df['Scan_Reports'])

    # combine and extract
    combined_report = []
    for nt, scan_report in zip(note, scan_reports):
        print(nt)
        print(scan_report)
        combined_report.append(nt + ',' + scan_report)

    df['combined_report'] = combined_report
    # df.loc[(df["combined_report"].isnull()), 'combined_report'] = 'NA'
    combined_report = extract_bert_features(combined_report)
    # print('saving combined_report')
    np.save('investing_ctmri_combined_report', combined_report)

    # all features in one column
    combined_report = np.load('investing_ctmri_combined_report.npy').tolist()
    # print(scan_reports[0][0])
    df['combined_report'] = combined_report
    # print(df['investing_ctmri_combined_report'])
    del df['Scan_Reports']
    del df['note']

    print(df.columns.tolist())
    exit()

    return df
