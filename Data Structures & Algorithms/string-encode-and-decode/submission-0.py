class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''

        for string in strs:

            for char in string:
                output += str(ord(char))
                output += '_'

            output += ' '
        
        return output

    def decode(self, s: str) -> List[str]:
        return_arr = []
        words = s.split(' ')

        for code in words:
            decoded_word = ''
            letters = code.split('_')

            for decode in letters:
                if decode != '':
                    decoded_word += chr(int(decode))

            return_arr.append(decoded_word)
        return_arr.pop()
        return return_arr

