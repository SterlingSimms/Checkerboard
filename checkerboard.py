def checkerboard():
    star = "*"
    space = " "
    line1 = 4*(star + space)
    line2 = 4*(space + star) 
    for count in range(0,5):
        print line1
        print line2
checkerboard()
