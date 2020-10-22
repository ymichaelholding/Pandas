# import packages
import pandas as pd
import numpy as np

print("Hello World")

# get the source and target files to compare files.
source_df = pd.read_csv(r'D:\Learning\python\pandas\employees_new.csv')
target_df = pd.read_csv(r'D:\Learning\python\pandas\employees_new1.csv')

# join the two source and target dataframes using indexes.
# all the columns are extracted from source and target
# source columns are alias with _src
# target_columns are alias with _target
merge_df = source_df.join(target_df,
                              lsuffix='_src',
                              rsuffix='_target',
                              how='outer')


# compare the source and target columns compares
# if its matched then True
# if its matched then False
def column_compare(column_name):
    src_column_name = column_name + '_src'
    tar_column_name = column_name + '_target'
    diff_identifies_cols = column_name + '_DIFF_FLAG'
    merge_df[diff_identifies_cols] = np.where(merge_df[src_column_name] == merge_df[tar_column_name],
                                                  'True', 'False')


# final_result["SALARY_DIFF_FLAG"]=0

# taking only columns and converted into lists
df_cols = list(source_df.columns)

# excuecuted the functions for all columns
for i in df_cols:
    column_compare(i)

difference_records = ""
for i in df_cols:
    difference_records = difference_records + " " + i + '_DIFF_FLAG' + "==" + "'" + 'False' + "'" + 'or'

difference_records = difference_records + ' 1 == 2'

print(difference_records)

diff_df = merge_df.query(difference_records)

print(diff_df)

if __name__ == "__main__":
    diff_df.to_csv('D:\Learning\python\pandas\output.csv')
