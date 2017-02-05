from location import Location
from province import Province


class Country(Location):
    def __init__(self, name="Poland", provinces=[], locationType="kraj"):
        super(Country, self).__init__(name, locationType)
        self.provinces = provinces
