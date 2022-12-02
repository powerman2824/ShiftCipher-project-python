class ShiftCipher:
    def __init__(self, shift, string):
        self.shift = shift
        self.string = string
    def encrypt(self):
        turnLowerCase = self.string.lower()
        emptyArr = []
        for letter in turnLowerCase:
            emptyArr.append(ord(letter))
        fullArr = []
        for letter in emptyArr:
            if letter < 97:
                fullArr.append(letter)
            elif letter + self.shift > 122:
                fullArr.append(letter + self.shift - 122 + 97)
            else:
                fullArr.append(letter + self.shift)
        message = []
        for letter in fullArr:
            message.append(chr(letter))
        print('Your message is now encrypted:')
        print(''.join(str(x).upper() for x in message))
    
    def dencrypt(self):
        turnLowerCase = self.string.lower()
        emptyArr = []
        for letter in turnLowerCase:
            emptyArr.append(ord(letter))
        fullArr = []
        for letter in emptyArr:
            if letter < 64 or letter >= 32:
                fullArr.append(letter)
            elif letter + self.shift < 97:
                fullArr.append(123 - (97 - (letter + self.shift)))
            elif letter + self.shift > 122:
                fullArr.append(letter)
            else:
                fullArr.append(letter + self.shift)
        message = []
        for letter in fullArr:
            message.append(chr(letter))
        print('Your message is now dencrypted:')
        print(''.join(str(x).lower() for x in message))

print('Welcome to the Encryption Machine')
print('Would you like to encrypt your message or decrypt')

userChoice = int(input('Please select 1 for encryption or 2 for decryption\n--> '))
userShiftCode = int(input('Please enter the shift for your message\n--> '))
userMessage = input('Please enter your message:\n--> ')

newMessage = ShiftCipher(userShiftCode, userMessage)

if userChoice == 1:
    newMessage.encrypt()
elif userChoice == 2:
    newMessage.dencrypt()
else:
    print('Please only select 1 or 2')
