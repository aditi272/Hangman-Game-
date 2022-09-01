from replit import clear
import random
import hangman_words
import hangman_art
lives = 6

# word_list = ["aardvark", "baboon", "camel"]
rand_word = random.choice(hangman_words.word_list)
#print(rand_word)


blank = []
for i in range(0,len(rand_word)):
  blank.append('_');

end_of_game = False;
print(hangman_art.logo)
while not end_of_game:

 
  guess_letter = (input('Guess a letter:')).lower();
  if(guess_letter in blank):
    print(f"You have already choosen letter {guess_letter}")
  for position in range(len(rand_word)):
    if(guess_letter == rand_word[position]):
      blank[position] = guess_letter;
  print(" ".join(blank))
  if(guess_letter not in rand_word):
    print(f"You choose {guess_letter} that is not in the word. You lose a life")
    # print(" ".join(blank))
    lives -= 1;
    
    if(lives == 0):
      end_of_game = True;
      print('You lose!')
    print(hangman_art.stages[lives])
    
  
  
    
      
    
  
  
  if "_" not in blank:
    end_of_game = True;
    print('You win')
  

    





    
  
    
 


  
