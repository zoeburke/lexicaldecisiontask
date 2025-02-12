import random

class TrialParticipant:
    instances_of_participants = 0

    def __init__(self, words):
        print("\n" * 3)
        self.first_name = input("Please enter your first name: ")
        self.last_name = input("Please enter your last name: ")
        print("\n" * 3)

        TrialParticipant.instances_of_participants += 1
        self.participant_num = TrialParticipant.instances_of_participants

        self.possible_selections = {"english": "y", "non-english": "n"}
        self.position = 1
        self.correct_choices = 0
        self.incorrect_choices = 0
        self.word_type = "english", "non-english"
        self.words = words  # Use the words passed to the constructor

    def get_correct(self):
        return self.correct_choices
    
    def get_incorrect(self):
        return self.incorrect_choices

    def increment_correct(self):
        self.correct_choices += 1

    def increment_incorrect(self):
        self.incorrect_choices += 1

    def increment_position(self):
        self.position += 1
        if self.position > 6:
            return False
        return True

    def response(self, selection):
        key_association = self.possible_selections[self.word_type]
        if selection == key_association:
            if self.correct_choices > 4:
                print("That's correct, wow you're good at this!")
            else:
                print("That's correct!")
            self.increment_correct()
            print("You selected: %s" % selection)
            print("The correct response for this was: %s" % key_association)
            print(f"Your score is: {self.correct_choices}")
            return True
        else:
            print("That's incorrect :(")
            self.increment_incorrect()
            print("You selected: %s" % selection)
            print("The correct response for this was: %s" % key_association)
            return False

    def select_words(self):
        self.word_type = random.choice(["english", "non-english"])
        words_at_type = self.words[self.position][self.word_type]
        return words_at_type

    def reset(self):
        self.position = 1

    def get_firstname(self):
        return self.first_name

    def set_firstname(self, new_firstname):
        self.first_name = new_firstname

    def get_lastname(self):
        return self.last_name

    def set_lastname(self, new_lastname):
        self.last_name = new_lastname

    def set_words(self, new_words):
        if not isinstance(new_words, dict):
            return "Error: New Words must be in a dictionary"
        if not all(isinstance(key, int) for key in new_words.keys()):
            return "Error: All keys in new_words must be integers"
        for key, value in new_words.items():
            if not isinstance(value, dict):
                return f"Error: The value for key {key} must be a dictionary."
            if not all(isinstance(k, str) for k in value.keys()):
                return f"Error: All nested keys for word set {key} must be strings."
            for k, v in value.items():
                if not isinstance(v, list) or len(v) < 2:
                    return f"Error: The value for '{k}' in word set {key} must be a list of length 2 or greater."
        self.words = new_words
        self.reset()  # Reset the position to 1
        return "Success: Words have been reset and the position is set to 1."

    def get_position(self):
        return self.position