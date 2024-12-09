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


def main():
    file_path = 'data/benin-malanville.csv'
    df = load_data(file_path)
    explore_data(df)


if __name__ == "__main__":
    main()
    
