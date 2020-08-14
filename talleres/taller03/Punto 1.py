def hanoi(topN, a = "Tower1", b = "Tower2", c = "Tower3"):
    if topN == 1:
        # de la torre en la que lo tenga a la última torre
        print (a + " -> " + c)
    else:
        hanoi(topN - 1 ,a , c ,b)
        hanoi(1 , a , b , c)
        hanoi(topN - 1 ,b , a ,c)
       
hanoi(16)
