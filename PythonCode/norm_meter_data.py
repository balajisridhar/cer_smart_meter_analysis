# Normalize time series dat
import csv

import pandas as ps
import os
from sklearn.preprocessing import MinMaxScaler

# TODO: Replace  print statements with logger
original_data_dir = "original"
processed_data_dir = "processed"
cer_dataset_dir = "data/system_aggregated_data"
old_columnName = 'kwh_sum'
new_columnName = 'norm_kwh_sum'

def rescale_meter_readings(fileName, old_columnName, new_columnName):
    try:
        # Building the path of the file
        relative_fileName = cer_dataset_dir + "/" + original_data_dir + "/" + fileName
        series = ps.read_csv( relative_fileName , header=0, infer_datetime_format= True)
        print(" Original Data set \n",series)
        # Getting the min max scaller handle
        min_max_scaler = MinMaxScaler()
        # Initializing Normalized data set with original data
        normalized_data = series
        x = series[[old_columnName]]
        print("Selected values \n ",x)
        dx = min_max_scaler.fit_transform(x)
        norm_dx = ps.DataFrame(dx)
        print("Normalized column\n",norm_dx)
        normalized_data[[new_columnName]] = norm_dx
        print("Normalized Data set \n", normalized_data)
        # Writing to the csv dataset
        normFileName = fileName[:-4] + "_nm.csv"
        relative_normFileName = cer_dataset_dir + "/" + processed_data_dir + "/" + normFileName
        normalized_data.to_csv(relative_normFileName, index = False, float_format='%g')
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
norm_all_meter_readinds(cer_dataset_dir + "/" + original_data_dir)
#rescale_meter_readings(fileName)

