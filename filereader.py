import random
#All of the below is to remain the same, only build using the WordFileReader class!!!
class FileReader:

    def __init__(self, filename): #This is the constructor which will be called when an instance of the class is created.
        self.__filename = None #Initially setting file name to None, will be changed later
        self.set_filename(filename) #Will then set the filename
        print("instance of FileReader class created!") #Let's us know that an instance has been created successfully
    
    def read_all(self): #Opens file, reads all lines and returns them
        try:
            file_1 = open(self.__filename) #Opens the file
            lines = file_1.readlines() #Reads all lines
            file_1.close() #Closes the file
            return lines #Returns the lines
        except:
            print("file not opened. Terminating method") #If the file isn't opened
            return False

    def line_count(self): #Returns the amount of lines in the file
        lines = self.read_all() #Calls the read_all method
        line_amount = len(lines) #Gets the amount of lines
        return line_amount   #Returns the amount of lines

    def get_filename(self): #Returns the filename
        return self.__filename 

    def set_filename(self, new_filename): #Sets the filename
        if type(new_filename) == str: #If the new filename is a string
            self.__filename = new_filename #Set the filename to the new filename

#Only change the code below
class WordFileReader(FileReader): #Inherits from the FileReader class
    def __init__(self, filename): #Constructor
        super().__init__(filename)  #Calls the constructor of the parent class!!!

    def all_rounds(self): #Returns a dictionary of all the rounds
        nested_dict = {} #Initialises an empty dictionary
        file_content = self.read_all() 
        for i in range(0, len(file_content), 2): #Iterates through the file content
            round_number = (i // 2) + 1 #Calculates the round number
            english_line = file_content[i].strip().split(',')[2:] #Splits the english line
            non_english_line = file_content[i + 1].strip().split(',')[2:] #Splits the non-english line
            nested_dict[round_number] = { 
                'english': english_line,
                'non-english': non_english_line
            } #Adds the round number and the english and non-english lines to the dictionary
        return nested_dict #Returns the dictionary
        
    def __str__(self): #Returns a string representation of the object
        return f"WordFileReader({self.get_filename()}), reading contents from this file and converting it into a specified dictionary format."
    
    def get_rounds_at(self, round_num_list): #Returns a dictionary of the rounds at the specified round numbers
        all_rounds_dict = self.all_rounds() #Gets all the rounds
        selected_rounds = {} #Initialises an empty dictionary
        for idx, round_num in enumerate(round_num_list, start=1): #Iterates through the round numbers
            if round_num in all_rounds_dict: #If the round number is in the dictionary
                selected_rounds[idx] = all_rounds_dict[round_num] #Add the round to the selected rounds dictionary
        return selected_rounds #Return the selected rounds dictionary

    def get_round_range(self, ran_rounds): #Returns a dictionary of the rounds within the specified range
        if not isinstance(ran_rounds, list) or len(ran_rounds) != 2: #If the range is not a list of two integers
            print("Error: ran_rounds should be a list of two integers.") #Print an error message
            return None

        start_round, end_round = ran_rounds #Get the start and end round
        if start_round > end_round or start_round < 1: 
            print("Error: Invalid range. Ensure start_round <= end_round and both are positive.")
            return None

        all_rounds_dict = self.all_rounds()
        total_rounds = len(all_rounds_dict)
        
        if end_round > total_rounds: #If the end round is greater than the total rounds
            print(f"Error: end_round exceeds the available rounds. Maximum round is {total_rounds}.")
            return None
        selected_rounds = {} #Initialises an empty dictionary
        new_round_number = 1 #Initialises a new round number
        for round_num in range(start_round, end_round + 1): #Iterates through the range
            if round_num in all_rounds_dict: #If the round number is in the dictionary
                selected_rounds[new_round_number] = all_rounds_dict[round_num] #Adds the round to the selected rounds dictionary
                new_round_number += 1 #Increments the new round number
        return selected_rounds #Returns the selected rounds dictionary

    def random_rounds(self): #Returns a dictionary of a random range of rounds
        all_rounds_dict = self.all_rounds() #Gets all the rounds
        total_rounds = len(all_rounds_dict) #Gets the total rounds

        if total_rounds == 0: #If there are no rounds
            print("No rounds available to select from.")
            return None
        start_round = random.randint(1, total_rounds) #Gets a random start round
        end_round = random.randint(start_round, total_rounds) #Gets a random end round
        selected_rounds = {} #Initialises an empty dictionary
        new_round_number = 1 #Initialises a new round number
        for round_num in range(start_round, end_round + 1): #Iterates through the range
            if round_num in all_rounds_dict: #If the round number is in the dictionary
                selected_rounds[new_round_number] = all_rounds_dict[round_num] #Adds the round to the selected rounds dictionary
                new_round_number += 1 #Increments the new round number

        return selected_rounds
    
    def exclude_rounds_at(self, round_nums_list): #Returns a dictionary of all rounds except the specified round numbers
            all_rounds_dict = self.all_rounds() #Gets all the rounds
            filtered_rounds = {} #Initialises an empty dictionary
            new_round_number = 1  #Initialises a new round number

            for round_num, round_data in all_rounds_dict.items(): #Iterates through the rounds
                if round_num not in round_nums_list: #If the round number is not in the list
                    filtered_rounds[new_round_number] = round_data #Adds the round to the filtered rounds dictionary
                    new_round_number += 1  #Increments the new round number
            return filtered_rounds #Returns the filtered rounds dictionary
    
    def exclude_round_range(self, ran_rounds): #Returns a dictionary of all rounds except the specified range
        if not isinstance(ran_rounds, list) or len(ran_rounds) != 2: #If the range is not a list of two integers
            print("Error: ran_rounds should be a list of two integers.")
            return None

        start_round, end_round = ran_rounds #Gets the start and end round
        if start_round > end_round or start_round < 1: #If the start round is greater than the end round or less than 1
            print("Error: Invalid range. Ensure start_round <= end_round and both are positive.")
            return None

        all_rounds_dict = self.all_rounds() #Gets all the rounds
        total_rounds = len(all_rounds_dict) #Gets the total rounds
        
        if end_round > total_rounds: #If the end round is greater than the total rounds
            print(f"Error: end_round exceeds the available rounds. Maximum round is {total_rounds}.")
            return None

        filtered_rounds = {} 
        new_round_number = 1 

        for round_num, round_data in all_rounds_dict.items(): #Iterates through the rounds
            if round_num < start_round or round_num > end_round: #If the round number is not within the range
                filtered_rounds[new_round_number] = round_data #Adds the round to the filtered rounds dictionary
                new_round_number += 1
        return filtered_rounds
    
    def generate_new_words(self, filename):
        new_word_reader = WordFileReader(filename)
        return new_word_reader.all_rounds()
    
if __name__ == "__main__": #This will only run if the file is run directly
    file_1 = WordFileReader("words.txt")