def solution(my_string, index_list):
    num=len(index_list)
    my_list=[]
    for i in range(num):
        my_list.append(my_string[index_list[i]])
    answer = ''.join(my_list)
    return answer