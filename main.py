import pandas as pd
from pandas import DataFrame

def read_population_data(file_path: str) -> DataFrame:
    """Зчитування даних про населення з файлу у DataFrame."""
    data: DataFrame = pd.read_csv(file_path, header=None, names=['Country', 'Year', 'Population'])
    return data


