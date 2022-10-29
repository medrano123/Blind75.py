
def isSubsequence(s, t):

    i, j = 0, 0

    while (i < len(s) and j < len(t)):
        if (s[i] == t[j]):
            i += 1
            j += 1
        else:
            j += 1
    if i == len(s):  # if we reached the end of s then that means it was a subsequence
        return True
    else:
        return False
        
        

def main():
    s = "axc"
    t = "ahbgdc"
    sol = isSubsequence(s, t)
    print(sol)


if __name__ == "__main__":
    main()
