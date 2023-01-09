import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


lives = 6

#Generovanie náhodného slova
words = ["FUNCTION", "OBJECT", "VALUE", "VARIABLE", "CONSTANT", "INTEGER", "FLOAT", "PATH", "LANGUAGE", "SYNTAX", "STRING", "DIRECTORY", "SOFTWARE", "DEVELOPER"]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
choosed_word = words[random.randint(0, len(words) - 1)]

#Generovanie podtržítok
hidden_word = []
for letter in choosed_word:
    hidden_word.append("_")

#Zbieranie neuhádnutých písmen
nonguessed_words = []

#Vypísanie hádaného slova z listu do stringu
def list_to_string(s):
    return "".join(s)

print(stages[lives])
print(list_to_string(hidden_word))


#User's-input(guess) - pokusy hráča a kontrola inputu
while "_" in hidden_word:
    print("________________________________________________________")
    guess = input("Zadaj hádané písmeno: ").upper()
    if len(guess) > 1:
      print("Zadaj iba jedno písmeno.")
      continue
    elif guess not in alphabet or guess == "":
      print(f"Zadaj písmeno základnej abecedy: '{alphabet}'.")
      continue

    if guess in hidden_word:
      print(f"Zadané písmeno '{guess}' už bolo uhádnuté.")
      continue
    elif guess in nonguessed_words:
      print(f"Zadané písmeno '{guess}' si už hádal/a a bolo nesprávne.")
      continue

    for index in range(0, len(choosed_word)):
        if guess == choosed_word[index]:
            hidden_word[index] = guess

    if guess not in choosed_word:
        lives -= 1
        print(stages[lives])
        print(f"Nesprávne. Počet zostávajúcich životov: {lives}")
        if guess not in nonguessed_words:
          nonguessed_words.append(guess)

    elif guess in choosed_word:
        print(stages[lives])   
        print("Správne! Pokračuj.")
         
    if lives <= 0:
        print(list_to_string(hidden_word))
        print(f"Stratil/a si všetky pokusy. Hádané slovo bolo '{list_to_string(choosed_word)}'. Koniec hry")
        break
    print(list_to_string(hidden_word))

#kontrola víťazstva
if "_" not in hidden_word:
    print("Gratulujeme. Vyhral/a si!")