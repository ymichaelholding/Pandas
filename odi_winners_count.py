import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'E:\Learning\python\project_wrk\Datasets\odi-cricket-matches-19712017\originalDataset.csv',index_col='Match Date')

def date_parsing(date):
    if date.find('-')==-1:
        return date
    elif date.find('-')==6:
        return date[:5] + date[8:]
    elif date.find('-')==5:
        return date[:5] + date[8:]

def date_string():
    index_list = []
    index_list = list(df.index)
    new_index = []
    for i in index_list:
        test = date_parsing(i)
        new_index.append(test)
    df.insert(0, column='Match', value=new_index)

date_string();

# resetting index
df.reset_index(inplace = True)
df['Match'] = pd.to_datetime(df['Match'])
#df.set_index("Match",inplace = True)
del df['Match Date']
#print(df[['Team 1', 'Team 2','Winner']])
df1 = df.groupby(['Winner']).count()

print(df1["Scorecard"])
print(df1.index)
plt.bar(df1.index,df1["Scorecard"], align='center')
plt.title('Odi winning bar chart')
plt.ylabel('Winning count')
plt.xlabel('Teams')
plt.show()