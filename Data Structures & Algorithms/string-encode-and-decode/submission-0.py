class Solution:
    # we need to find something to distinguish where is the separator
    # meaning where does each word in the list of string end
    # if cant be like a character because the string could contain all ascii
    # so we cant use a character to ssay this is where it ends
    # we could not also use something like 

    # couldnt think of the solution without hint for this question


    def encode(self, strs: List[str]) -> str:
        str_arr = []
        for st in strs:
            length = len(st)

            str_arr.append(str(length))
            str_arr.append("#")
            str_arr.append(st)

        return "".join(str_arr)

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            arr.append(word)

            i = j + 1 + length

        return arr


