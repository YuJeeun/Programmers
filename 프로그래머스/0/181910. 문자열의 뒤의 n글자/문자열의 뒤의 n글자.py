def solution(my_string, n):
    num = len(my_string) - n
    answer = ''.join(my_string[num:])
    return answer