import pandas as pd
from pandas import DataFrame

def read_population_data(file_path: str) -> DataFrame:
    data = pd.read_csv(file_path, header=None, names=['Country', 'Year', 'Population'])
    return data

def calculate_population_change(data: DataFrame) -> DataFrame:
    grouped = data.sort_values(by=['Country', 'Year'])
    grouped['Population Change'] = grouped.groupby('Country')['Population'].diff().fillna(0)
    return grouped

def write_changes_to_file(data: DataFrame, output_path: str) -> None:
    data.to_csv(output_path, index=False)

def process_population_data(input_path: str, output_path: str) -> None:
    data = read_population_data(input_path)
    changed_data = calculate_population_change(data)
    write_changes_to_file(changed_data, output_path)
    print(f"Data processed and written to {output_path}")

if __name__ == "__main__":
    input_file: str = input("Please enter the path to the input data file: ")
    output_file: str = input("Please enter the path to the output data file: ")
    process_population_data(input_file, output_file)
