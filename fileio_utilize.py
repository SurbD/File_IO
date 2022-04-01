import json
import string
from random import choice, randint


class UtilityFileIO:
    """This is a draft for the FileIO project, No GUI yet.... coming soon """
    recent_files = []
    default_usrn = ['Divi', 'jkpol', 'userx', 'Mini', 'Yuga_lab']
    id_log = ['divine#9147', 'sam#2324', 'miami#0991']
    
    def __init__(self, filepath):
        # self.filepath = filepath
        self.filepath = self.valid_path(filepath)


    def read_all(self, lines=None):
        """This prints out all the information in the text file, or print out the text with the total number of lines if specified.
        Enter an Integer for the lines
        """

        
        text_lines = []
        with open(self.filepath) as file_object:
            if lines:
                text_lines = file_object.readlines()[:lines]
            else:
                text_lines = file_object.readlines()

        for line in text_lines:
            print(line.strip())

    def search(self, target_text):
        """
            This method searches for text, sentences, or even words and return an Output of all the lines the text appears,
            with the target text all in UPPERCASE.
            Note: The search is case sensitive.
                                                    """

        # target_text = target_text.lower()
        result = []

        with open(self.filepath) as file_object:
            full_text = file_object.readlines()

        for line in full_text:
            if target_text in line:
                line = line.replace(target_text, target_text.upper())
                result.append(line)
            else:
                pass

        if result:
            print(''.join([ln for ln in result]))
        else:
            print('No Match Found')


    def valid_path(self, filepath):

        try:
            open(filepath)

        except FileNotFoundError as err:
            print(f'{err} check path and try again!\n [PROGRAM ENDED].')
            quit()
        else:
            return filepath 


class WordScraping(UtilityFileIO):

    ''' This Class is Mainly for word(s) mainpulation or collection, Just getting more data on the text in the document.

                ++++++ Coming Soon... ++++++
    '''

    def __init__(self, filepath):
        super().__init__(filepath)






        

util_ = UtilityFileIO('food.txt')
wow = WordScraping('food.txt')
# util_.read_all()
util_.search('Rice')
