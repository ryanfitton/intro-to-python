# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")


def report_long_words(words):
  reported_words = ''

  for word in words:
    # store the word length
    word_length = len(word)

    # words not containing hyphens and greater than 10 characters
    if "-" not in word and word_length > 10:
      # and if greater than 15 characters, strip remaning words and replace with elipses
      if word_length > 15:
        word = word[0:15] + '...'

      # concatenate words
      reported_words = reported_words + word + ', '

  # Return and remove the last comma and space
  return "These words are quite long: " + reported_words.rstrip(', ')


check_that_these_are_equal(
    report_long_words([
        'hello', 'nonbiological', 'Kay', 'this-is-a-long-word',
        'antidisestablishmentarianism'
    ]), "These words are quite long: nonbiological, antidisestablis...")

check_that_these_are_equal(
    report_long_words(['cat', 'dog', 'rhinosaurus', 'rhinosaurus-rex',
                       'frog']), "These words are quite long: rhinosaurus")

check_that_these_are_equal(report_long_words(['cat']),
                           "These words are quite long: ")

# Once you're done, move on to 041_challenge_2_example.py

# Run
# python 040_challenge_1_exercise.py
