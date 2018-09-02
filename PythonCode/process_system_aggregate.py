import pandas as ps
import traceback
from sklearn.preprocessing import MinMaxScaler


# Reaading the csv file and loading in to the dataframe
ps.options.mode.chained_assignment = None
cer_dataset_dir = "data/system_aggregated_data"
original_data_dir = "original"
processed_data_dir = "processed"
aggregated_fileName = "SystemAggregate_WindPower_2009_cutdown.csv"
aggregated_file = cer_dataset_dir + "/" + original_data_dir +  "/" + aggregated_fileName

sys_aggregated = ps.read_csv(aggregated_file)
grouped_df  = sys_aggregated.groupby('Day')
# Grouping the data in the file based on the days


def process_aggr_system_data(int_day, df):
    try:

        # Normalizing the Wind and the Demand
        min_max_scaler = MinMaxScaler()
        x = df[['Demand']]
        print(x.shape)
        print(x)
        dx = min_max_scaler.fit_transform(x)
        print(dx)
        df['Norm_Demand'] = df[['Demand']]
        print(df)
        df['Norm_Demand'] = dx
        y = df[['Wind']]
        dy = min_max_scaler.fit_transform(y)
        df['Norm_Wind'] = dy
        df = df[(df.Subhour % 2 == 0)]
        df.loc[: ,'Subhour'] = df.loc[: ,'Subhour'].div(2).astype(int)

        print(df)
        relative_normFileName = cer_dataset_dir + "/" + processed_data_dir + "/" + str(int_day) + "_nm.csv"
        df.to_csv(relative_normFileName, index = False, float_format='%g')


    except Exception as e:
        print("Exception while processing aggregated demand records of " +  str(int_day) + "th day")
        print(e.with_traceback(traceback))


for int_day in range(330,366):
    df = sys_aggregated[(sys_aggregated.Day == int_day)]
    process_aggr_system_data(int_day, df)
    df = None