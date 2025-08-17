from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Engima

# historical enigma rotors and reflectors
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II  = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# keyboards and plugboards
KB = Keyboard()
PB = Plugboard(["AB", "CD", "EF"])

# encipher a letter
ENGIMA = Engima(B, IV, II, I, PB, KB)

# set message key
ENGIMA.set_key("CAT")
ENGIMA.rotor1.show()

message = "TEST"
cipher_text = ""
for letter in message:
    cipher_text = cipher_text + ENGIMA.encipher(letter)
print(cipher_text)
# print(ENGIMA.encipher("A"))