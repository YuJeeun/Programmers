def solution(myString):
    answer = ''
    temp1=''
    temp2=''
    for i in range (len(myString)):
        if 'a' in myString[i]:
            answer+=myString[i].replace(myString[i],myString[i].upper())
        elif myString[i].isupper():
            if myString[i]!='A':
                answer+=myString[i].replace(myString[i],myString[i].lower())
            else:
                answer+=myString[i]
        else:
            answer+=myString[i]
    return answer