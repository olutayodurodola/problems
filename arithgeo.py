'''def arith_geo(myarray):
  if (myarray == []):
    return 0
  if (myarray[1] - myarray[0]) == (myarray[2] - myarray[1]) and (myarray[1] - myarray[0]) == (myarray[3] - myarray[2]):
      count1 = 0
      count2= 0
      for i in range(0,len(myarray)-1):
          count1 = myarray[i+1] - myarray[i]
          if i+2 < len(myarray) and i+3 < len(myarray):
            count2 = myarray[i+3] -myarray[i+2]
          else:
            
        if count1 == count2:
          return "Arithmetic"
        else:
          return "unknown"
  elif (myarray[1] / myarray[0]) == (myarray[2] / myarray[1]):
    return "Geometric"
  else:
    return -1
    
print arith_geo([1,2,3,4,5,7])'''

def arith_geo(myarray):
  if (myarray == []):
    return 0
  if (myarray[1] - myarray[0]) == (myarray[2] - myarray[1]) and (myarray[1] - myarray[0]) == (myarray[3] - myarray[2]):
    count1 = 0
    count2 = 0
    for i in range(0,len(myarray)-1):
      if (i+2 < len(myarray)) and (i+3 < len(myarray)):
        count1 = myarray[i+1] - myarray[i]
        print count1,"count1"
        count2 = myarray[i+3] -myarray[i+2]
        print count2, "count2"
    if count1 == count2:
      return "Arithmetic"
    else:
      return -1
  elif (myarray[1] / myarray[0]) == (myarray[2] / myarray[1]):
    count1 = 0
    count2 = 0
    for i in range(0,len(myarray)-1):
      if (i+2 < len(myarray)) and (i+3 < len(myarray)):
        count1 = myarray[i+1] / myarray[i]
        print count1,"count1"
        count2 = myarray[i+3] / myarray[i+2]
        print count2, "count2"
    if count1 == count2:
      return "Geometric"
    else:
      return -1
  else:
    return -1
    
print arith_geo([1,2,4,8,16,32])
