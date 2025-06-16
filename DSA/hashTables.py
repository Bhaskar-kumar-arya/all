from collections import defaultdict


def Counter (nums : list) :
    o = defaultdict(lambda : 0)
    for val in nums :
        o[val] += 1 
    return dict(o)      

def CountCharFrequncy (word : str) :
    freq = [0]*26
    for c in word :
        freq[ord(c) - ord("a")] += 1
    return tuple(freq)          
       
def is_anagram(s1, s2):
   return len(s1) == len(s2)  and  Counter(s1) == Counter(s2)

def Sort_Word (word : str) -> str :
    freq = [0]*26
    for c in word :
        freq[ord(c) - ord("a")] += 1
    output = []
    for i in range(26) :
        output.append(chr(i + ord("a"))*freq[i])
    return "".join(output)    


def group_anagrams(words : list[str]): 
    o = defaultdict(list) 
    for word in words :
        o[Sort_Word(word)].append(word)
        #o[CountCharFrequncy(word)].append(word)
    return list(o.values())    

def isAllUniqueInTable (Board : list[list[str]]) :
    freq = defaultdict(int) 
    for i in range(3) :
        for j in range(3) :
            if Board[i][j] != "." and freq[Board[i][j]] == 1 :
                return False
            freq[Board[i][j]] = 1
    return True        
    
# for 9x9 board    
# no repeatitions in row/column 
# no repeatition in 3x3 tables
def isSudokuTableValid (Board : list[list[str]]) :
    # check all rows :
    for i in range(9) :
        freq = defaultdict(int)
        for j in range(9) :
            if Board[i][j] == "." :
                continue
            if freq[Board[i][j]] == 1 :
                return False
            freq[Board[i][j]] = 1
    # check all cols 
    for i in range(9) :
        freq = defaultdict(int)
        for j in range(9) :
            if Board[j][i] == "." :
                continue
            if freq[Board[j][i]] == 1 :
                return False
            freq[Board[j][i]] = 1         
    # construct 3x3 tables
    # check each 3x3 table
    for i in range(0,9,3) :
        for j in range(0,9,3) :
           if not isAllUniqueInTable([row[i:i + 3] for row in Board[j:j + 3]]) :
            return False
    return True        
            
