def nearestPoint(addressDic):
    temp = addressDic["route"]
    returnList = []
    i=0
    while i != -1:
        min = 40000000 #circunferencia da terra
        next = -1
        for j in range(0,len(temp)):
            if i != j and temp[chr(ord('a')+j)]["color"] == "white":
                if temp[chr(ord('a')+i)][chr(ord('a')+j)] < min:
                    next = j
                    min = temp[chr(ord('a')+i)][chr(ord('a')+j)]
        returnList.append(chr(ord('a')+i)) 
        temp[chr(ord('a')+i)].update({"color":"black"})
        i = next
    returnList.append('a')
    return returnList