class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        corres = {")":"(","}":"{","]":"["}
        for b in s:
            if b=='(' or b=='{' or b=="[":
                l.append(b)
            elif b==")" or b=="}" or b=="]":

                if not l or l.pop()!=corres[b]:
                    return False
        if not l:
            return True
        else:
            return False

