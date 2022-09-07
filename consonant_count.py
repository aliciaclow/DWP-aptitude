def countConsonants(string):
   num_consonants = [each for each in string if each not in "aeiouAEIOU "]
   print('Number of consonants:', len(num_consonants))

string = input('Enter any string: ')
countConsonants(string)