import csv


class Database():
    @staticmethod
    def read_file(filename):
        """
        Read file content
        :param filename:
        :return: list
        """
        convertedList = []

        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')

            for index, element in enumerate(reader):

                if index > 0:
                    convertedList.append(element)

        return convertedList
