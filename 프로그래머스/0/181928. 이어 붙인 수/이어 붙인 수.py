def solution(num_list):
    odd_list=[]
    even_list=[]
    for i in range(len(num_list)):
        if num_list[i]%2!=0:
            odd_list.append(num_list[i])
        if num_list[i]%2==0:
            even_list.append(num_list[i])
    odd=''.join(map(str,odd_list))
    even=''.join(map(str,even_list))
    result=int(odd)+int(even)
    answer = result
    return answer