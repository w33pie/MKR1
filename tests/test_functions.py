import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from main import read_population_data, calculate_population_change, write_changes_to_file


@pytest.fixture
def sample_population_data():
    return pd.DataFrame({'Country': ['A', 'A', 'B', 'B'],
                         'Year': [2020, 2021, 2020, 2021],
                         'Population': [100, 110, 200, 220]})


def test_read_population_data(tmp_path, sample_population_data):
    file_path = tmp_path / "population.csv"
    sample_population_data.to_csv(file_path, header=None, index=None)

    expected_result = sample_population_data
    actual_result = read_population_data(file_path)

    assert_frame_equal(actual_result, expected_result)


def test_calculate_population_change(sample_population_data):
    expected_result = pd.DataFrame({'Country': ['A', 'A', 'B', 'B'],
                                    'Year': [2020, 2021, 2020, 2021],
                                    'Population': [100, 110, 200, 220],
                                    'Population Change': [0, 10, 0, 20]})
    actual_result = calculate_population_change(sample_population_data)

    actual_result['Population Change'] = actual_result['Population Change'].astype('int64')

    assert_frame_equal(actual_result, expected_result)


def test_write_changes_to_file(tmp_path, sample_population_data):
    output_path = tmp_path / "output.csv"

    expected_result = sample_population_data
    write_changes_to_file(expected_result, output_path)

    actual_result = pd.read_csv(output_path)

    assert_frame_equal(actual_result, expected_result)