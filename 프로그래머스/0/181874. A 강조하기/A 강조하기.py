def solution(myString):
    answer = ''
    #for i in range (len(myString)):
     #   if 'a' in myString[i]:
    #        answer+=myString[i].replace(myString[i],myString[i].upper())
   #     elif myString[i].isupper():
  #          if myString[i]!='A':
#                answer+=myString[i].replace(myString[i],myString[i].lower())
#            else:
#                answer+=myString[i]
#        else:
 #           answer+=myString[i]
    answer=myString.lower().replace('a','A')
    return answer