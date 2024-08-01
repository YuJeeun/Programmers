def solution(myStr): 
    myStr=' '.join(myStr.replace('a','?').replace('b','?').replace('c','?').split('?')).split()     
    if myStr==[]:
        return ["EMPTY"]
    return myStr