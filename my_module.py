# Sebastian Galinski och Noor Fouad Raheem
# datum: 2024-02-XX
# DD1318 lab 3

import text_encryption_function


# uppgift 1
def copy_text_file(in_file, out_file):
    fr = open(in_file, "r")
    text = fr.read()  # stores in_file as text
    fr.close()

    fw = open(out_file, "w")
    fw.write(text)  # write the stored text in out_file
    fw.close()


"""
testing for uppgift 1
copy_text_file("namn.csv", "my_copy.csv")
"""


# uppgift 2
def encrypt_file(in_file, out_file):
    fr = open(in_file, "r")
    encrypted_text = text_encryption_function.encrypt(fr.read())  # encrypts what is written in in_file
    fr.close()

    fw = open(out_file, "w")
    fw.write(encrypted_text)
    fw.close()


"""
# testing for uppgift 2
encrypt_file("namn.csv", "secret_names.csv")
"""
# uppgift 3

def user_dialogue():
  while True:
     in_file = input(" ge name på ny encrypted fil: ")
     out_file = input("ge namn på fil som ska krypteras:")


     try:
        encrypt_file(in_file, out_file)
        print("Super! Kryptering är klart!")
        break
     except FileNotFoundError as error:
        print(f" Fel name du skrivit. var god försök igen! felet var: {error}")


user_dialogue()


# uppgift 4



# uppgift 5

# uppgift 6

# uppgift 7

# uppgift 8
