class Solution:

    def encode(self, strs: List[str]) -> str:
        # My answer 
        #output = ''

        #for string in strs:

        #    for char in string:
        #        output += str(ord(char))
        #        output += '_'

        #    output += ' '
        
        #return output
        output = ''

        for s in strs:
            output += str(len(s)) + '#' + s

        return output

    def decode(self, s: str) -> List[str]:
        # My answer 
        #return_arr = []
        #words = s.split(' ')

        #for code in words:
        #    decoded_word = ''
        #    letters = code.split('_')

        #    for decode in letters:
        #        if decode != '':
        #            decoded_word += chr(int(decode))

        #    return_arr.append(decoded_word)
        #return_arr.pop()
        #return return_arr
        
        
        #
        output = []
        i = 0

        while i < len(s):
            j = i
            val = ''

            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            output.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return output




