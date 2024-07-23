def solution(date1, date2):
    yearDiff=date1[0]-date2[0] # date1이 앞서면 -
    monthDiff=date1[1]-date2[1] # date1이 앞서면 -
    dayDiff=date1[2]-date2[2] # date1이 앞서면 -
    
    # if yearDiff<0:
    #     return 1
    # elif yearDiff==0:
    #     if monthDiff<0:
    #         return 1
    #     elif monthDiff==0:
    #         if dayDiff<0:
    #             return 1
    #         elif dayDiff==0:
    #             return 0
    #         else:
    #             return 0
    #     else:
    #         return 0
    # else:
    #     return 0
    
    if yearDiff<0:
        return 1
    elif yearDiff>0:
        return 0
    
    if monthDiff<0:
        return 1
    elif monthDiff>0:
        return 0
    
    if dayDiff<0:
        return 1
    elif dayDiff>0:
        return 0
    
    else:
        return 0
            