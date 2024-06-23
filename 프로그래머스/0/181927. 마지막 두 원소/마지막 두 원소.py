def solution(num_list):
    num=len(num_list)
    if num_list[num-1] > num_list[num-2]:
        result=num_list[num-1] - num_list[num-2]
        num_list.append(result)
    elif num_list[num-1] <= num_list[num-2]:
        result=num_list[num-1]*2
        num_list.append(result)
    answer = num_list
    return answer