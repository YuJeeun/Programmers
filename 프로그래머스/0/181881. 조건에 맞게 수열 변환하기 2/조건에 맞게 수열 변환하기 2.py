def solution(arr):
    count = 0
    
    while(True):
        test = []
        for i in range(len(arr)):
            if (arr[i]>=50 and arr[i]%2==0):
                test.append(int(arr[i]/2))
            elif (arr[i]<50 and arr[i]%2!=0):
                test.append(int(arr[i]*2+1))
            else :
                test.append(arr[i])
        if (test == arr) :
            return count
        else :
            arr = test.copy()
            count+=1