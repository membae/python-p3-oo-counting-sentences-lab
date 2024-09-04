import re

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ''

    def is_sentence(self):
        return self._value.endswith('.')
    def is_question(self):
      return self._value.endswith('?')
    def is_exclamation(self):
      return self._value.endswith('!')
  

    def count_sentences(self):
        sentences = re.split(r'[.!?]+', self._value)
        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(sentences)

# Example usage:
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())  # Output: 3
