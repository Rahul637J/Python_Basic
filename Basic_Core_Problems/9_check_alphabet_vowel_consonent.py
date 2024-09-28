'''
@Author: Rahul
@Date: 2024-07-29
@Last Modified by: Rahul
@Last Modified time: 2024-07-29
@Title: Checks the input alphabet is vowel or consonant

'''
def check_character_vowel_consonant(char):
     '''
    Description: 
        This function to find the character is vowel or consonant   
    Parameters:
        num: String :The user input 
    Return :
        None
    '''
     
     vowels=["a","e","i","o","u","A","E","I","O","U"]
     if char in vowels:
         print(char,"is a Vowel")
     else:
         print(char,"is a consonant")

def main():
    char=input("Enter the Alphabet to check: ")
    check_character_vowel_consonant(char)    

if __name__=="__main__":
    main()
