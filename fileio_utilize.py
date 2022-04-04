from verification import Verify

class UtilityFileIO(Verify):
    """This is a draft for the FileIO project, No GUI yet.... coming soon . NB: Always Run the [save()] method to keep track of your file changes """
    recent_files = ''
    
    def __init__(self, filepath):
        super().__init__()
        self.filepath = self.valid_path(filepath)
        self.recent_files += self.filepath

    def read_all(self, lines=None):
        """This prints out all the information in the text file, or print out the text with the total number of lines if specified.
        Enter an Integer for the lines
        """

        self.check_id()
        text_lines = []
        with open(self.filepath) as file_object:
            if lines:
                text_lines = file_object.readlines()[:lines]
            else:
                text_lines = file_object.readlines()

        for line in text_lines:
            print(line.strip())

    def search(self, target_text):
        """ This method searches for text, sentences, or even words and return an Output of all the lines the text appears,
            with the target text all in UPPERCASE.
            Note: The search is case sensitive. """

        self.check_id()
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
            print(f'{err} check path and try again.\n [PROGRAM ENDED]')
            quit()
        else:
            return filepath 

    def check_id(self):
        try:
            if self.username:
                print(f'Welcome back {self.username.capitalize()}')
            else:
                raise ValueError
        
        except ValueError:
            print('Run [recover(user_id) or generate_id(username) if New]')
            exit()


class WordScraping(UtilityFileIO):

    ''' This Class is Mainly for word(s) mainpulation or collection, Just getting more data on the text in the document.

                ++++++ Coming Soon... ++++++
    '''

    def __init__(self, filepath):
        super().__init__(filepath)

    def phrase_freqency(self, phrase): # Word or Phrase frequency
        """ Counts how many times the word argument appears in your file, and return the number. """

        self.check_id()
        with open(self.filepath) as f_obj:
            content = f_obj.read()
            frequency = content.count(phrase)

        if int(frequency):
            return None
        else:
            return frequency

    def find_line(self, line_number):
        """ This program accepts a 'line_number'(must be an integer(1 -> nth line)) argument that signifies a line in the file and returns that line only.
        NB: if line value is greater than the initial line length in the file, the last line is returned. """

        self.check_id()
        line = ''

        with open(self.filepath) as f_obj:
            lines = f_obj.readlines()
        
        try:
            line += lines[line_number-1]
        except IndexError:
            line += lines[-1]
            line_number = lines.index(lines[-1]) + 1
            return f'{line_number}. {line.strip()}'
        else:
            return f'{line_number}. {line.strip()}'
    

util_ = UtilityFileIO('data_files/food.txt')
util_.recover("Paul#5274")

print(util_.recent_file)
util_.save_progress()
print(util_.recent_file)