from country import Country
from province import Province
from county import County
from commune import Commune
from communetype import CommuneType


class Converter():
    @staticmethod
    def converter(database_list, country="Poland"):

        """
        Convert List, and assign all/ Tree Structure
        :param database_list:
        """
        provinceList = []
        communeList = []
        countyList = []
        for index, element in enumerate(database_list):
            if element[1] == "":
                prov = Province(element[0], element[4], element[5])
                provinceList.append(prov)
            elif element[2] == "":
                county = County(element[1], element[0], element[4], element[5])
                countyList.append(county)
            else:
                commune = Commune(element[0], element[1], CommuneType(int(element[3])), element[4], element[5])
                # print(commune.__dict__)
                communeList.append(commune)

        for prov in provinceList:
            provCountyList = []
            for county in countyList:
                if county.provinceId == prov.id:
                    provCountyList.append(county)
                    countyCommuneList = []
                    for commune in communeList:
                        if commune.provinceId == prov.id and commune.countyId == county.id:
                            countyCommuneList.append(commune)
                    county.communeList = countyCommuneList

            prov.countyList = provCountyList

        return Country(country, provinceList)

    @staticmethod
    def flatData(country):
        """
        Flat object Country and its objects lists
        :param country:
        :return: list of objects
        """

        flat_list = [country]
        for provinces in country.provinces:
            flat_list.append(provinces)
            for county in provinces.countyList:
                flat_list.append(county)
                for commune in county.communeList:
                    flat_list.append(commune)

        return flat_list

    @staticmethod
    def flatProv(prov):
        """
        Flat object Province and its objects lists
        :param country:
        :return: list of objects
        """
        flat_list_prov = []

        for county in prov.countyList:
            flat_list_prov.append(county)
            for commune in county.communeList:
                flat_list_prov.append(commune)

        return flat_list_prov
