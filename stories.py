"""Madlibs Stories."""
from random import choice

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text. answers contains a dictionary."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


'''story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
story2 = Story(
    ["adjective", "noun", "verb, past tense", "adverb", "adjective", "noun"], """Today I went to the zoo. I saw a(n) {adjective} {noun} jumping up and down in its tree.
He {verb, past tense} {adverb} through the large tunnel that led to its {adjective} {noun}."""
)
stories = [story1, story2]
story = stories[0]
madlib = story.generate({"place": "on a rainbow", "noun":"cat", "verb": "jump", "adjective": "fast", "plural_noun":"heads"})
#print("MADLIB1", madlib)
story = stories[1]
madlib = story.generate({"adjective": "fat", "noun": "cloud", "verb, past tense":"ate", "adverb":"hungrily", "adjective":"red", "noun":"ball"})
#print("MADLIB2", madlib)'''