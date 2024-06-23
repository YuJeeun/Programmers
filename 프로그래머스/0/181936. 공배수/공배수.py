
def solution(number, n, m):
    result=0
    if number%n==0:
        if number%m==0:
            result=1
        elif number%m==0:
            result=0
        else: result=0
    
    answer = result
    return answer