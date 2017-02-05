from converter import Converter
from database import Database
from menu import Menu


def main():
    data = Database.read_file('malopolska.csv') # import data and assign it to list
    country = Converter.converter(data) # convert data to objects / Country object ini
    session = Menu(country) # crate new object Menu
    session.operate_data() #operate data


if __name__ == '__main__':
    main()