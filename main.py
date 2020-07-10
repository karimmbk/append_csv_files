import os

import pandas as pd

file_list = []
# TODO: set environment variable with the directory path
path = os.environ['FILE_PATH']
for file in sorted(os.listdir(path)):

    if file.endswith('.csv') and file != 'all.csv':
        df = pd.read_csv(path + file, sep=",")
        df['filename'] = file
        file_list.append(df)

all_days = pd.concat(file_list, ignore_index=True)
all_days.to_csv(path + "all.csv")
