from range_key_dict import RangeKeyDict
maxScore = 40 #int(input("Enter max score: "))
dec = 't'
grades = RangeKeyDict({
        (0, 40): "ndst",
        (40, 50): "dop",
        (50, 70): "dst",
        (70, 85): 'db',
        (85, 100): 'bdb',
    })
while dec == 't':
    myScore = int(input("Enter your score: "))
    percent = myScore/maxScore*100
    if percent < 100:
        grade = grades[myScore/maxScore*100]
    elif percent == 100:
        grade = 'cel'
    print("Dostałeś {}".format(grade))
    dec = input("t/n: ")


