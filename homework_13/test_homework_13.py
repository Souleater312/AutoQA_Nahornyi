from homework_13.homework_13 import JSONConverter
import pytest

@pytest.fixture
def converter():
    return JSONConverter()


"""def test_add_row_to_csv(converter, tmp_path):
    # Підготовка даних та виклик функції
    converter.read_file('example.json')

    # Використовуємо tmp_path для створення тимчасового файла
    csv_file_path = tmp_path / 'example.csv'

    converter.write_file(str(csv_file_path))
    converter.add_row_to_csv(str(csv_file_path), ['John', 'Doe', '30', 'Male', '3000'])

    # Перевірка результатів
    # Зчитуємо дані з файлу, щоб перевірити кількість рядків
    with open(csv_file_path, 'r') as csv_file:
        lines = csv_file.readlines()

    assert len(lines) == 5  # Перевірка кількості рядків у файлі після додавання
    """

def test_add_row_to_csv(converter):
    # Підготовка даних та виклик функції
    converter.read_file('example.json')
    converter.write_file('example.csv')
    converter.add_row_to_csv('example.csv', ['John', 'Doe', '30', 'Male', '3000'])

    # Перевірка результатів
    assert len(converter._JSONConverter__lines) == 3  # Перевірка довжини __lines
    assert converter._JSONConverter__lines[3]['first_name'] == 'John'  # Перевірка конкретного значення


def test_remove_row_from_csv(converter):
    # Підготовка даних та виклик функції
    converter.read_file('example.json')
    converter.write_file('example.csv')
    converter.remove_row_from_csv('example.csv', 0)

    # Перевірка результатів
    assert len(converter._JSONConverter__lines) == 0  # Перевірка довжини __lines після видалення