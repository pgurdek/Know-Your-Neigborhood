from location import Location


class County(Location):
    def __init__(self, id, provinceId, name, locationType):
        super(County, self).__init__(name, locationType)
        self.id = id
        self.provinceId = provinceId
        self.communeList = []
