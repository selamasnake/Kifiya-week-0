import pandas as pd 

def load_data(file_path):
    df = pd.read_csv(file_path)
    pd.set_option('display.max_columns', 20)
    return df

def explore_data(df):
    print("Shape of the data:", df.shape)
    print("Info of the data:", df.info())
    print("First 5 rows:", df.head(5))
    print("Data types of the columns:", df.dtypes)

#change to appropriate datatypes
def convert_datatypes(df):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    return df

#check for missing values
def handle_missing_values(df):
    if (df.isnull().sum()) > 0:
        print(df.isnull().sum() > 0)
    return df


def drop_columns(df):
    df = df.drop(['Comments'], axis=1).copy()
    return df

def remove_negative_values(df):
    df = df[df['GHI'] >= 0]
    df = df[df['DNI'] >= 0]
    df = df[df['DHI'] >= 0]
    return df

def main():
    file_path = 'data/benin-malanville.csv'
    df = load_data(file_path)
    explore_data(df)
    convert_datatypes(df)
    handle_missing_values(df)
    drop_columns(df)
    remove_negative_values(df)


if __name__ == "__main__":
    main()
    
