from location import Location


class Province(Location):
    def __init__(self, id, name, locationType):
        super(Province, self).__init__(name, locationType)
        self.id = id
        self.countyList = []
