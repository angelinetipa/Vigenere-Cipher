print("*" * 55)
# a variable for alphabetical letters
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# input for the plaintext and keyword, remove space and change to uppercase
message = input("\n\033[3m\033[1m" "Message: \n> " "\033[0m").strip().upper()
keyword = input("\n\033[3m\033[1m" "Key: \n> " "\033[0m").strip().upper()
# list for message indices
message_indices = []
# find the index of each letter in message then add to list
for j in range(len(message)):
    message_indices.append(alphabet.find(message[j]))
# list for keyword indices
# find the index of each letter in message then add to list
# list for mod of sum of message's and keyword's indices
# for every message indices a keyword indices will add
# if sum less than the len of alphabet, add to list, otherwise take mod then add to list
# if index2 on last index of keyword, bring it back to zero
# take the index from list mod message keyword to the variable alphabet
# output for ciphertext/print the result