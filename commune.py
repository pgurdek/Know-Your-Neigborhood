from communetype import CommuneType
from location import Location


class Commune(Location):
    def __init__(self, provinceId, countyId, communeType, name, locationType):
        super(Commune, self).__init__(name, locationType)
        self.countyId = countyId
        self.provinceId = provinceId
        self.communeType = communeType

    def __str__(self):
        return "{} {} {}".format(self.countyId, self.communeType, self.name)
