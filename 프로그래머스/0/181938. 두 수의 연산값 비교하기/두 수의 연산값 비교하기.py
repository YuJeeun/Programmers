def solution(a, b):
    #answer=0
    #list_ab=[]
    #list_ab.append(a)
    #list_ab.append(b)
    #list_ab=map(str,list_ab)
    #join_ab=''.join(list_ab)
    #mul_ab=2*a*b
    #if int(join_ab)>=mul_ab:
        #answer=int(join_ab)
    #elif int(join_ab)<mul_ab:
        #answer=mul_ab
    return max(int(str(a) + str(b)), 2 * a * b)