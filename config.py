# this is the configuration file

words_in_each_discover = 5
words_in_each_practise = 5
words_in_each_test = 5  # min=5

max_practises_for_each_word = 3  # min=2
# means if user x time answers to this question correctly so dont ask again this question.

min_difficulty_for_test = -3

scores_log_file_name = './scores.log'

practise_header = "\n -> practising <-\n"
test_header = "\n -> examination <-\n"
discover_header = "\n -> discovering <-\n"

message_for_ending_practicing = """:D  you don't have any words to practise.

press enter to continue..."""

message_for_ending_discover = """:D  you don't have any words to discover.

press enter to continue..."""

message_for_ending_test = """:(  first discover some new words.

press enter to continue..."""

question_text_before = 'wich one is the corret meaning for "'
question_text_after = '"'

version = '0.2'
menu = f"""
VOCAB EXTENDER\tversion:{version}

-> main menu <-
select one of these

  e  :\texit and save data
  d  :\tdiscover new words
  p  :\tpractise discovered words
  t  :\ttake an exam
  s  :\tshow a review of my current status


"""
menu_question = "your choise ? "
