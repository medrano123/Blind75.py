
def isIsomorphic(s, t):
    mapST, mapTS = {},{}
    
    for i in range(len(s)):
        c1, c2 = s[i], t[i]
        
        if((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
            return False
        mapST[c1] = c2
        mapTS[c2] = c1   # if they have a different mapping then we stop our algorithm.
    return True

def main():
    s = "foo"
    t = "bar"
    sol = isIsomorphic(s, t)
    print(sol)


if __name__ == "__main__":
    main()
