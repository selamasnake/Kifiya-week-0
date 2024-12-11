import pandas as pd 

def load_data(file_path):
    df = pd.read_csv(file_path)
    pd.set_option('display.max_columns', 20)
    return df

def convert_datatypes(df):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

def summary_statistics(df):
    return df.describe()

def resample_data_h(df):
    df.set_index('Timestamp', inplace=True)
    hourly_data = df.resample('h').mean()
    return hourly_data

def resample_data_m(df):
    df.set_index('Timestamp')
    monthly_data = df.resample('h').mean()
    return df



def main():
    file_path = 'data/prepared/benin_prepared.csv'
    df = load_data(file_path)
    convert_datatypes(df)
    summary_statistics(df)
    resample_data_h(df)
    resample_data_m(df)

if __name__ == "__main__":
    main()