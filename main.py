import pandas as pd
from pandas import DataFrame

def read_population_data(file_path: str) -> DataFrame:
    """Зчитування даних про населення з файлу у DataFrame."""
    data: DataFrame = pd.read_csv(file_path, header=None, names=['Country', 'Year', 'Population'])
    return data

def calculate_population_change(data: DataFrame) -> DataFrame:
    """Обрахунок зміни населення за роками для кожної країни."""
    grouped: DataFrame = data.sort_values(by=['Country', 'Year'])
    grouped['Population Change'] = grouped.groupby('Country')['Population'].diff().fillna(0)
    return grouped

def write_changes_to_file(data: DataFrame, output_path: str) -> None:
    """Запис змінених даних у новий файл."""
    data.to_csv(output_path, index=False)

def process_population_data(input_path: str, output_path: str) -> None:
    """Основна функція для обробки даних про населення."""
    data = read_population_data(input_path)
    changed_data = calculate_population_change(data)
    write_changes_to_file(changed_data, output_path)
    print(f"Data processed and written to {output_path}")