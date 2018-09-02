# Normalize time series dat
import csv

import pandas as ps
import os
from sklearn.preprocessing import MinMaxScaler

# TODO: Replace  print statements with logger
original_data_dir = "original"
processed_data_dir = "processed"
cer_dataset_dir = "data/cer_dataset"
old_columnName = 'kwh_sum'
new_columnName = 'norm_kwh_sum'
dir_path_test = "C:/mine/ucd/Praticum/DataEngineering/DataCleaning/TMP"
dir_path = "C:/mine/ucd/Praticum/SMD_Data/meters"

def rescale_meter_readings(fileName, old_columnName, new_columnName):
    try:
        # Building the path of the file
        relative_fileName = cer_dataset_dir + "/" + original_data_dir + "/" + fileName
        absolute_file_name = dir_path+ "/" + fileName
        series = ps.read_csv( absolute_file_name , header=0, infer_datetime_format= True)
        #print(" Original Data set \n",series)
        # Getting the min max scaller handle
        min_max_scaler = MinMaxScaler()
        # Initializing Normalized data set with original data
        rowCount = series['kwh'].count()
        nonZerCount = series[(series['kwh']> 0)]['kwh'].count()
        zeroCount = rowCount - nonZerCount
        mean = series['kwh'].mean()
        newRow = [fileName, rowCount,zeroCount,nonZerCount,mean]
        print(newRow)
        with open('fileCount.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(newRow)


    except Exception as e:
        print("Exception while processing the file ", fileName)
        print(e)


def norm_all_meter_readinds(dirName):
    try:
        print("Reading all the files from the given directory : ", dirName)

        for file in os.listdir(dirName):
            rescale_meter_readings(file, old_columnName, new_columnName )
            print("Normalizing the data in ", file)
        # Call the Normalization function for the data set

    except Exception as e:
        print("Exception in processing the files under : ", dirName)
        print(e)

fileName = '1000.csv'
norm_all_meter_readinds(dir_path)
#rescale_meter_readings(fileName)

