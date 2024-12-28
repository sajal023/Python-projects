from cipher_art import logo
import string

print(logo)


def caesar(command, t, s):
    cipher_text = ""
    if command == 'D':
        s = s * -1
    for i in t:
        if i in alphabet:
            pos_letter = alphabet.index(i)
            new_pos = pos_letter + s
            cipher_text += alphabet[new_pos]
        else:
            cipher_text += i
    print(f"the coded text is {cipher_text}")


alphabet = list(string.ascii_letters + string.ascii_letters)
end = 0

while not end:
    command = input("Enter 'E' for encoding or 'D' for decoding: ")
    text = input("enter the text for operation")
    shift_no = int(input("Enter the shift number: "))
    shift_no %= 26
    caesar(command, text, shift_no)
    choice = input("Enter 'again' to begin operation or 'end' to exit: ")
    if choice == 'end':
        end = 1
