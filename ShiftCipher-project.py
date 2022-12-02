class ShiftCipher:
    def __init__(self, shift, string):
        self.shift = shift
        self.string = string
    def encrypt(self):
        # print('You have selected to encryt your message:')
        # self.string = input('Enter your message:\n--> ')
        print(self.shift)
        print(self.string)

print('Welcome to the Encryption Machine')
print('Would you like to encrypt your message or decrypt')

userChoice = int(input('Please select 1 for encryption or 2 for decryption\n--> '))
userShiftCode = input('Please enter the shift for your message\n--> ')
userMessage = input('Please enter your message:\n--> ')

newMessage = ShiftCipher(userShiftCode, userMessage)

if userChoice == 1:
    newMessage.encrypt()
elif userChoice == 2:
    newMessage.dencrypt()
else:
    print('Please only select 1 or 2')
