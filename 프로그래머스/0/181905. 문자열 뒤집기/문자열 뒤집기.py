def solution(my_string, s, e): 
    return my_string[:s] + my_string[e:s:-1]+my_string[s] + my_string[e+1:]

# s가 0인 경우 if 0~5 