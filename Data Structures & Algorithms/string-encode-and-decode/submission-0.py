class Solution:

    def encode(self, strs: List[str]) -> str:
        eString = ""
        # i am creating a header which would store the lengths of the string
        # then the header would end with $.
        # after that the strings would be just laid like that.
        for n in strs:
            eString+= f"{len(n)}#"
        eString+= "$"
        # header created. Now I can add the elements of the string
        for n in strs:
            eString += n
        return eString
            
            

    def decode(self, s: str) -> List[str]:
        res = []
        right = s.find("$")
        lbuf = ""
        lens  = 0
        nStart = right+1
        for n in range(right):
            if s[n] != "#":
                lbuf+= s[n]
            else:
                lens = int(lbuf)
                lbuf = ""
                dString = ""
                for n in range(nStart, lens+nStart):
                    dString+=s[n]
                nStart += lens
                res.append(dString)
        return res
        