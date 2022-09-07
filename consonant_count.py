#define function to count consonant in the given string
def countConsonants(string):
   num_consonants = [each for each in string if each not in "aeiouAEIOU "]
   print('Number of consonants:', len(num_consonants))

#this asks user to input the string
string = input('Enter any string: ')

#call function using input as string
countConsonants(string)