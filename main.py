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
