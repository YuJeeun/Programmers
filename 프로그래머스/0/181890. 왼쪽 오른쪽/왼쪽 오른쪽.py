def solution(str_list):
    answer = []
    if 'r' in str_list and 'l' in str_list:
        if str_list.index('l') < str_list.index('r'):
            return str_list[:str_list.index('l')]
        else:
            return str_list[str_list.index('r')+1:]
    elif 'r' in str_list:
        return str_list[str_list.index('r')+1:]
    elif 'l' in str_list:
        return str_list[:str_list.index('l')]
    else:
        return []