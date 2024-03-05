from homework_13.homework_13 import JSONConverter
import pytest

@pytest.fixture
def converter():
    return JSONConverter()


def test_add_row_to_csv(converter):
    # Підготовка даних та виклик функції
    converter.read_json_file('example.json')
    converter.write_csv_file('example1.csv')
    converter.cleanup()
    converter.add_row_to_csv('example1.csv', ['John', 'Doe', '30', 'Male', '3000'])
    converter.read_csv_file('example1.csv')


    # Перевірка результатів
    assert len(converter._JSONConverter__lines) == 4
    assert converter._JSONConverter__lines[3]['first_name'] == 'John'


def test_remove_row_from_csv(converter):
    # Підготовка даних та виклик функції
    converter.read_json_file('example.json')
    converter.write_csv_file('example1.csv')
    converter.cleanup()
    converter.add_row_to_csv('example1.csv', ['John', 'Doe', '30', 'Male', '3000'])
    converter.read_csv_file('example1.csv')
    len_value = len(converter._JSONConverter__lines)
    converter.cleanup()
    converter.remove_row_from_csv('example1.csv', len_value)
    converter.read_csv_file('example1.csv')

    # Перевірка результатів
    assert len(converter._JSONConverter__lines) == 3  # Перевірка довжини __lines після видалення