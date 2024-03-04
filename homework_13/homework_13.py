import csv
import json


class JSONConverter:
    def __init__(self):
        self.__lines = []

    def read_json_file(self, filename: str):
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            self.__lines.extend(data)
            print(self.__lines)

    def write_csv_file(self, filename: str):
        fieldnames = self.__lines[0].keys() if self.__lines else []
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.__lines)

    def read_csv_file(self, filename:str):
        with open(filename, 'r') as csv_file:
            lines = csv.DictReader(csv_file)
            for line in lines:
                self.__lines.append(line)
            print(self.__lines)

    def write_json_file(self, filename:str):
        with open(filename, 'w', newline='') as writer:
            json.dump(self.__lines, writer, indent=4)
            self.cleanup()


    def add_row_to_csv(self, filename, row_data):
        with open(filename, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(row_data)

    def remove_row_from_csv(self, filename, row_index):
        with open(filename, 'r', newline='') as csv_file:
            rows = list(csv.reader(csv_file))

        if 0 <= row_index < len(rows):
            del rows[row_index]

            with open(filename, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows(rows)
        else:
            print(f"Invalid row index: {row_index}")


if __name__ == '__main__':
    converter = JSONConverter()
    converter.read_json_file('example.json')
    converter.write_csv_file('example.csv')
    #converter.read_file('example.json')
    #converter.write_file('example2.csv')
    print(len(converter._JSONConverter__lines))
    converter.add_row_to_csv('example.csv', ['John', 'Doe', '30', 'Male', '3000'])
    converter.read_csv_file('example.csv')
    print(len(converter._JSONConverter__lines))

    # Домашнє не дороблено