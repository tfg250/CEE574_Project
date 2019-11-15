import os.path
import pandas as pd

DataItems = ['swe','snowdepth','snowdensity','snowfall']
years = range(2003,2020) 
months = range(1,13) 
days =  range(1,32)  




#loop through each year
for item in DataItems:
    print(item)
    all_files = []
    for yr in years:
       for mo in months:
           for day in days:
               filename = "Data_{}_{}_{}_{}.csv"
               thisfilename=filename.format(item,yr,mo,day)
               if os.path.isfile(thisfilename):
                   all_files.append(thisfilename)
    df_from_each_file = (pd.read_csv(f) for f in all_files)
    Data = pd.concat(df_from_each_file, ignore_index=True) 
    Data.to_csv(item+".csv") 
