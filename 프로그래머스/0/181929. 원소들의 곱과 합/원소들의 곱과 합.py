def solution(num_list):
    sum=0
    mul=1
    for i in range (len(num_list)):        
        sum+=num_list[i]
        mul*=num_list[i]
    if mul < sum**2:
        result=1
    elif mul > sum**2:
        result=0
    answer = result
    return answer