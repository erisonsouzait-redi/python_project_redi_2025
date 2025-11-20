import csv
import random

class GameData:

    def __init__(self):
    
        def gender_nominativ(self, genus):
            """This function returns the gender of the noun receeiin info from the column genus on the csv file"""
            
            gender = 'Der' #by default gender is male

            if genus == 'f': #if the value is f changes to female
                gender = 'Die'
            elif genus == 'n':
                gender = 'Das' #if the value is n changes to neuter

            return gender
    
