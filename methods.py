class Methods:
    def __init__(self, encrypted_text):
        self.encrypted_text = encrypted_text

    def applyCaesarShift(self):
        while (True):
            try:
                shift_to_apply = int(
                    input(
                        "Enter the shift to apply ( -n if you want to go backwards, 0 if you want to test all possibilities ): "
                    ))
                break
            except:
                print('{}'.format(
                    'This is not a valid number. Please type a valid one.\n'))

        self.encrypted_text = self.encrypted_text.lower().split(' ')
        if shift_to_apply == 0:
            for shift_to_apply in range(-25, 25):
                decoded_text = []
                current_index = 0

                while current_index < len(self.encrypted_text):
                    decoded_text.append([])
                    for char in self.encrypted_text[current_index]:
                        if ord(char) + shift_to_apply < 97:
                            letter = 122 - (shift_to_apply - ord(char) - 97)

                        elif ord(char) + shift_to_apply > 122:
                            letter = 97 + (shift_to_apply + ord(char) - 122)

                        else:
                            letter = ord(char) + shift_to_apply

                        if letter > 96 and letter < 123:
                            decoded_text[current_index] += chr(letter)

                    decoded_text[current_index] = ''.join(
                        decoded_text[current_index])
                    current_index += 1

                print("Here's your decoded text with a Shift of {}: {}".format(
                    shift_to_apply, ' '.join(decoded_text)))

        else:

            decoded_text = []
            current_index = 0

            while current_index < len(self.encrypted_text):
                decoded_text.append([])
                for char in self.encrypted_text[current_index]:
                    if ord(char) + shift_to_apply < 97:
                        letter = 122 - (shift_to_apply - ord(char) - 97)

                    elif ord(char) + shift_to_apply > 122:
                        letter = 97 + (shift_to_apply + ord(char) - 122)

                    else:
                        letter = ord(char) + shift_to_apply

                    if letter > 96 and letter < 123:
                        decoded_text[current_index] += chr(letter)

                decoded_text[current_index] = ''.join(
                    decoded_text[current_index])
                current_index += 1

            print('{}: {}'.format("Here's your decoded text",
                                  ' '.join(decoded_text)))

    def applyROT13(self):

        self.encrypted_text = self.encrypted_text.lower().split(' ')

        decoded_text = []
        current_index = 0

        while current_index < len(self.encrypted_text):
            decoded_text.append([])
            for char in self.encrypted_text[current_index]:
                if ord(char) + 13 < 97:
                    letter = 122 - (12 - ord(char) - 97)

                elif ord(char) + 13 > 122:
                    letter = 97 + (12 + ord(char) - 122)

                else:
                    letter = ord(char) + 13

                if letter > 96 and letter < 123:
                    decoded_text[current_index] += chr(letter)

            decoded_text[current_index] = ''.join(decoded_text[current_index])
            current_index += 1

        print('{}: {}'.format("Here's your decoded text",
                              ' '.join(decoded_text)))
