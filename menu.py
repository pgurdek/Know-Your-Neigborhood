import sys
from operator import itemgetter
from collections import Counter
from converter import Converter


class Menu():
    def __init__(self, country):

        self.country = country
        self.flatData = Converter.flatData(country)

    def operate_data(self):
        """
        Show menu and operate on its handle requests
        """
        while True:
            self.show_menu()
            user_output = self.get_input()
            if user_output == "0":
                sys.exit(0)
            elif user_output == "1":
                self.listStatistic()
            elif user_output == "2":
                self.cityLongestName()
            elif user_output == "3":
                self.maxCommunities()
            elif user_output == "4":
                self.multipleCategorys()
            elif user_output == "5":
                self.searchLocation()

    @staticmethod
    def show_menu():
        """
        Show menu
        :return:
        """
        """"""
        print("""What would you like to do:
   (1) List statistics
   (2) Display 3 cities with longest names
   (3) Display county's name with the largest number of communities
   (4) Display locations, that belong to more than one category
   (5) Advanced search
   (0) Exit program""")

    @staticmethod
    def get_input(msg=''):
        """Get input"""

        return input(msg)

    def listStatistic(self):
        """
        Print statistic list and sort it by name reverse(upgraded for all provinces)
        """
        print('===============', self.country.name, '====================')
        for province in self.country.provinces:
            print()
            print("============={}============".format(province.name))
            one_province_items = Converter.flatProv(province)
            cnt = Counter()
            for location_type in one_province_items:
                cnt[location_type.locationType] += 1

            for key in sorted(cnt, reverse=True):
                print("{} : {}".format(key, cnt[key]))

    def cityLongestName(self, number=3):
        """
        Get 3 longest occurrences
        :param number: number of occurrences
        :return: None
        """
        cityList = []
        for city in self.flatData:
            if city.locationType == "miasto":
                cityList.append([city.name, len(city.name)])  # crate list of citys and its length

        for index, item in enumerate(
                sorted(cityList, key=itemgetter(1), reverse=True)[:number]):  # sort Citys by its length, and get only first 3

            print("{} longest occurrence is : {}".format(index + 1, item[0]))

    def maxCommunities(self):
        """
        Get County with biggest number of communities
        :return:
        """
        countyList = []
        for province in self.country.provinces:
            for county in province.countyList:
                countyList.append([county.name, len(county.communeList)])
        print(max(countyList, key=lambda x: x[1])) # get County with biggest number of comm

    def multipleCategorys(self):
        """
        find Communities with more than 1 category
        :return:
        """
        locationCounter = Counter() # Init Counter
        for location in self.flatData:
            locationCounter[location.name] += 1 # Count and and it to Counter

        print('Locations which belongs to more than 1 category')
        for key in locationCounter:
            if locationCounter[key] > 1: # print all Name which occurred more than 1 time
                print('Name : {}, its linked to {} categorys'.format(key, locationCounter[key]))

    def searchLocation(self):
        """
        Search for expression
        :return:
        """
        searchExpression = self.get_input('What would you like to search?')
        searchResult = []
        for province in self.country.provinces: # Search in all objects and its childs
            if searchExpression in province.name:
                searchResult.append(province)
            for county in province.countyList:
                if searchExpression in county.name:
                    searchResult.append(county)
                for commune in county.communeList:
                    if searchExpression in commune.name:
                        searchResult.append(commune)
        simpleList = []
        for element in searchResult:
            simpleList.append([element.name, element.locationType]) # Simplify it and crate new list for sort

        for element in sorted(simpleList, key=lambda sl: (sl[0], sl[1])): # Sort List by its name first and then by it's Location
            print('Name {} , Location type: {}'.format(element[0], element[1]))
