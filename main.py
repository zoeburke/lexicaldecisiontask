from filereader import WordFileReader
from participant import TrialParticipant

if __name__ == "__main__":
    # Create an instance of WordFileReader
    file_1 = WordFileReader("words.txt")

    # Read all rounds from the file
    all_rounds_output = file_1.all_rounds()

    # Create an instance of TrialParticipant with the words
    trial_participant = TrialParticipant(all_rounds_output)

    # Print the introduction to the game
    print("\n" * 4)
    print(f"Welcome, to the Lexical Decision Task, {trial_participant.first_name} {trial_participant.last_name}!")
    print("In this task, you will be presented with four words.")
    print("Your task is to select whether all four words are of the English language!")
    print("---")

    # Ask the user for consent to engage with the game
    consent = input("Do you consent to engaging with the experiment? 1 for yes, 2 for no: ")
    print("\n" * 4)
    
    if consent == "1":
        run_game = True
    elif consent == "2":
        run_game = False
    else:
        print("Invalid Input!")
        run_game = False

    # Run the game
    while run_game:
        print("---")
        print("The word position is now at: %s" % trial_participant.get_position())

        words = trial_participant.select_words()
        print("The words are: ", words)

        participant_selection = input("Are all these words in English? Please select 'y' or 'n' to continue.")

        if participant_selection.lower() != "y" and participant_selection.lower() != "n":
            print("Please select a valid response...")
        else:
            correct = trial_participant.response(participant_selection.lower())
            next = trial_participant.increment_position()

            if next == False:
                run_game = False
                print("There are no more selections available. The experiment has ended.")
                print(f"Here are your results {trial_participant.first_name}: Correct = {trial_participant.correct_choices} Incorrect = {trial_participant.incorrect_choices}")
            elif trial_participant.get_position() == 4:
                # Prompt to change words after the third round
                change_words = input("Would you like to change the words? 1 for yes, 2 for no: ")
                if change_words == "1":
                    new_file = input("Please enter the filename for the new words: ")
                    new_word_reader = WordFileReader(new_file)
                    new_words = new_word_reader.all_rounds()
                    trial_participant.set_words(new_words)
                    print("Words have been changed.")