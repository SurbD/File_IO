import json
from random import randint

class Verify:
    """ Collects data from json file (it creates one if there's none), then it verifies the identity of user using the users ID,
    and stores new changes back to .json file """

    database = 'data_files/database.json'

    def __init__(self):
        self.db = self.db_retrive()
        self.__user_id = ''
        self.username = ''
        self.recent_file = ''
        self.user_info = ''


    def recover(self, user_id):
        ''' This method requires a user id as a parameter, so it can verify that its an existing id. '''

        if self.db:
            self.id_list  = [key for data in self.db for key in data]
            for data in self.db:
                for key in data:
                    if user_id == key:
                        print('Match!')
                        # self.id_list = key
                        self.__user_id = user_id
                        self.user_info = data
                        self.username = self.user_info.get(user_id).get('username')
                        break
        else:
            print('No data Found!, To Generate your unique id... use the [generate_id] method.')
        

    def generate_id(self, username):
        """Generate ID Method: it takes one argument which is the 'username' uses it to creates a new id for the user and 
        saves it to the data file ('.json file'). """
        loop_duration = 0
            
        while loop_duration <= 100:
            digit = ''.join([str(randint(0,9)) for i in range(4)])
            char = '#' 
            user_id = (username + char + digit).strip()
            loop_duration += 1

            if self.db:
                if user_id in self.id_list:
                    print('Username Exists, Try another username!')
                    continue
                else:
                    self.username = username
                    self.__user_id = user_id
                    self.save_progress()
                    
                    break
                    # user_data = {
                    #     self.__user_id: {
                    #         'username': username,
                    #         'recent_file': 'Null for now',
                    #     }

                    # }

                    # self.db.append(user_data)
            else:
                self.__user_id = user_id
                self.save_progress()
                # user_data = {
                #         self.user_id: {
                #             'username': username,
                #             'recent_file': 'Null for now',
                #         }

                #     }
                # self.db.append(user_data)
                break

                    
        hidden = self.__user_id[: user_id.index('#')]+ '*'*5

        print(f"This is your Unique ID -- '{hidden}'. _____ NB: To get ID call the user_id variable '[className().user_id]'")
        self.Save()

    def db_retrive(self):

        try:

            with open(self.database) as db_obj:
                db = json.load(db_obj)

        except (json.JSONDecodeError): 
            print("DataBase is empty... No present user!. [Run the 'generate_id' function to get your id]")
            return []
        
        else:
            return db

    def Save(self):
        
        with open(self.database, 'w') as db_obj:
            json.dump(self.db, db_obj)
        
        print('Done!')

    def save_progress(self):
        user_data = {
            self.__user_id: {
                'username': self.username,
                'recent_file': self.recent_file,
                }
            }
        for data in self.db:
            if self.__user_id in data:
                locator = self.db.index(data)
                self.db[locator] = user_data
                break

        else:
            self.db.append(user_data)

        # Finally...

        with open(self.database, 'w') as db_obj:
            json.dump(self.db, db_obj)
