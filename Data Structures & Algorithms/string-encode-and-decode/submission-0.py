class Solution:

    def encode(self, strs: List[str]) -> str:
        eString = ""
        lens = [len(n) for n in strs]
        # i am creating a header which would store the lengths of the string
        # then the header would end with $.
        # after that the strings would be just laid like that.
        for n in lens:
            eString+= f"{n}#"
        eString+= "$"
        # header created. Now I can add the elements of the string
        for n in strs:
            eString += n
        return eString
            
            

    def decode(self, s: str) -> List[str]:
        res = []
        right = s.find("$")+1
        lbuf = ""
        lens  = 0
        nStart = right
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
        