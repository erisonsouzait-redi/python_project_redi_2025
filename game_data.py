import random
import pandas as pd

class GameData:
    """"This Class processes data from the CSV to play the game"""

    def __init__(self):
        
        #The file 'all_german_nouns.csv' is avaiable at https://github.com/gambolputty/german-nouns/blob/main/german_nouns/nouns.csv
        #originally it has all words in german extracted from https://www.wiktionary.org/ and it was filtered to only have nouns
        self.data_frame = pd.read_csv('all_german_nouns.csv', delimiter=';', dtype=str, low_memory=False)

        #the file most_used_german_nouns is avaiable at https://docs.google.com/spreadsheets/d/1r9HwvVpo35MFxnJ_5W6RKlDfx5VzmQVcnpJTgrNUY9I/edit?gid=1060626799#gid=1060626799
        #It is based on  the book A Frequency Dictionary of German: Core Vocabulary for Learners by Routledge - Taylor & Francis Group.
        self.data_frame_most_used_german_nouns = pd.read_csv('most_used_german_nouns.csv', delimiter=',', dtype=str, low_memory=False)
        
    
    def convert_genus_to_article(self, genus= str):
        """This function receives a string 'm', 'f' or 'n' from the column 'genus' [gender] and returns 
        'Der', 'Die' or 'Das' respectively"""
        
        gender = ''

        if genus == 'm':
            gender = 'Der'
        elif genus == 'f':
            gender = 'Die'
        elif genus == 'n':
            gender = 'Das'

        return gender
    
    def create_duplicate_free_list(self):
        """This functions extracts all nouns from the data on the CSV,
        removes the duplicates,  and returns a list with all of them.
        
        Some nouns in german have different articles. Ex.: Alphabet, See, Band
        depending on the article they have different meanings
        to simplify our game they will be left out"""

        #grabs all nouns
        data_frame_dropna = self.data_frame[['genus', 'lemma', 'pos']].dropna()
        data_frame_only_nouns = data_frame_dropna.loc[data_frame_dropna['pos'] == 'Substantiv']
        data_frame_only_nouns = data_frame_only_nouns[['genus', 'lemma']]

        return data_frame_only_nouns[~data_frame_only_nouns['lemma'].duplicated(keep=False)].values.tolist()
    
    def create_random_suffled_nouns_list(self, quantity=int, nouns_list=list):
        """This function receives a list of nouns and returns a shuffled list with the especified quantity"""
        
        return random.sample(nouns_list, quantity)
    
    def provide_suffix_dictionary(self):
        """This function returns a dictionary containing the suffixes and the most probable gender according to that suffix"""

        suffix_dict = {
                    'ant': 'm', #this list is found on https://germanwithlaura.com/german-articles/
                    'ast': 'm',
                    'ich': 'm',
                    'ig': 'm',
                    'ismus': 'm',
                    'ling': 'm',
                    'or': 'm',
                    'us': 'm',
                    'a': 'f',
                    'anz': 'f',
                    'enz': 'f',
                    'ei': 'f',
                    'ie': 'f',
                    'heit': 'f',
                    'keit': 'f',
                    'ik': 'f',
                    'sion': 'f',
                    'tion': 'f',
                    'sis': 'f',
                    'tät': 'f',
                    'ung': 'f',
                    'ur': 'f',
                    'schaft': 'f',
                    'chen': 'n',
                    'lein': 'n',
                    'icht': 'n',
                    'il': 'n',
                    'it': 'n',
                    'ma': 'n',
                    'ment': 'n',
                    'tel': 'n',
                    'tum': 'n',
                    'um': 'n'
                    }
        
        return suffix_dict
    
    def return_expected_gender(self, suffix= str):
        """Return the expected article acording to the noun suffix"""

        suffix_dict = self.provide_suffix_dictionary()
        
        for end, gender in suffix_dict.items():
            if suffix == end:
                expected_article = self.convert_genus_to_article(gender)
                return expected_article

    def create_noun_list_by_suffix(self, noun_list= list, suffix= str):
        """This function provides a list of random shuffled nouns in accordance 
        with the suffix provided. It return a list of lists containing:
        
        index 0 = nouns list to be used in the game (contains nouns follwingthe rule
            to the suffix and exceptions)

        index 1 = nouns list with all nouns containing the suffix

        index 2 = nouns list with all nouns that follow the rule"""

        all_nouns_with_suffix= [] 
        all_nouns_following_rule = [] 
        all_execeptions_to_rule = []

        expected_gender = self.return_expected_gender(suffix)

        #populate the tree lists
        for noun in noun_list:
            if noun[1].endswith(suffix):
                all_nouns_with_suffix.append(noun)
                if self.convert_genus_to_article(noun[0]) == expected_gender:
                    all_nouns_following_rule.append(noun)
                else:
                    all_execeptions_to_rule.append(noun)
        
        #balance of the quantities of nouns
        percentage_following_rule = len(all_nouns_following_rule) / len(all_nouns_with_suffix)

        quantity_following_rule = int(percentage_following_rule * 10 + 0.5)
        
        quantity_exception = 10 - quantity_following_rule
        
        #selects random nouns from each list
        random_list_following_rule = self.create_random_suffled_nouns_list(quantity_following_rule, all_nouns_following_rule)
        random_list_exception = self.create_random_suffled_nouns_list(quantity_exception, all_execeptions_to_rule)

        merged_list = []

        merged_list = random_list_following_rule + random_list_exception

        random.shuffle(merged_list)

        all_lists = []

        all_lists.append(merged_list)
        all_lists.append(all_nouns_with_suffix)
        all_lists.append(all_nouns_following_rule)

        return all_lists
    
    def create_game_nouns_list(self, game_mode= str, **kwargs):
        """This functions creates a list of nouns depending on the type of game.

        ***'game_mode' options***
        'random' returns a random list of nouns, the size of the list 'plays' must be given
        'suffix' returns a random list of 10 nouns with a provided 'suffix'
        'survive', returns a random list with all nouns avaiable
        'most_used' returns a random list of 10 nounts from the most used german nouns, 'quantity' must be given and
            determines the size of the list to sample
        """
        
        nouns_list = []

        if game_mode == 'random':
            nouns_list = self.create_random_suffled_nouns_list(kwargs.get('plays'), self.create_duplicate_free_list())

        elif game_mode == 'suffix':
            nouns_list = self.create_noun_list_by_suffix(self.create_duplicate_free_list(), kwargs.get('suffix'))[0]
    
        elif game_mode == 'survive':
            nouns_list = self.create_duplicate_free_list()
            random.shuffle(nouns_list)
        
        elif game_mode == 'most_used':
            duplicate_free_most_used = self.data_frame_most_used_german_nouns[~self.data_frame_most_used_german_nouns['lemma'].duplicated(keep=False)]
            nouns_list = duplicate_free_most_used.head(kwargs.get('quantity')).values.tolist()
            nouns_list = self.create_random_suffled_nouns_list(10, nouns_list)
        
        return nouns_list

    def generate_game_conclusion_message(self, streak=int, nouns_list=list):
        """This funcition generates a message depending on the player performance at the game"""

        if streak == len(nouns_list):
            return "Awesome! Perfect game!"
        else:
            return "Game complete."

    def provide_hint(self, noun_to_test=str):
        """This function analyses the percentage of chance of a noun to follow a rule according
        with the sufix and returns a string of text to help the player make a decision on what article
        to choose"""

        suffix_dict = self.provide_suffix_dictionary()
        suffix_list = []
        matching_suffix = ''

        for suffix in suffix_dict:
            if noun_to_test.endswith(suffix):
                matching_suffix = suffix
                suffix_list = self.create_noun_list_by_suffix(self.create_duplicate_free_list(), suffix)
        
        if matching_suffix == '':
            return "No hint found..."
        
        expected_gender = self.return_expected_gender(matching_suffix)

        percentage_follow_rule = (len(suffix_list[2]) * 100) / len(suffix_list[1])
        
        if percentage_follow_rule > 40:
            return f'Nouns with the suffix -{matching_suffix} take the article "{expected_gender}" with {percentage_follow_rule:.0f}% probability'
        else:
            return 'No hint found...'