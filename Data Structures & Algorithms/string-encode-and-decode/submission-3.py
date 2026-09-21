class Solution:

    def encode(self, strs: List[str]) -> str:
        eString = []
        # i am creating a header which would store the lengths of the string
        # then the header would end with $.
        # after that the strings would be just laid like that.
        lens = [str(len(n)) for n in strs]
        for n in strs:
            eString.append(f"{len(n)}#")
        eString.append("$")
        # header created. Now I can add the elements of the string
        for n in strs:
            eString.append(n)
        return "#".join(lens) + "$" + "".join(strs)
            
            

    def decode(self, s: str) -> List[str]:
        header, data = s.split("$", 1)
        lens = [] if not header else map(int, header.split("#"))
        res = []
        pos = 0
        for n in lens:
            res.append(data[pos:pos+n])
            pos+=n
        return res