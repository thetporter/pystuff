que = str(input())
i = int(0)
j = int(0)
while(i < 4):
    match i:
        case 0:
            while j < len(que):
                if j == 3: 
                    j = j + 1
                    continue
                print(que[j], end="")
                j = j + 1
        case 1:
            while j < len(que):
                if que[j] == 'c':
                    print("\nFound a \'c\'!")
                print(que[j], end="")
                j = j + 1
        case 2:
            while j < len(que):
                print(que[j], end="")
                j = j + 1
            print(" Length:"+str(len(que)))
        case 3:
            while j < len(que)-1:
                print(que[j], end="")
                j = j + 1
    print()
    j = 0
    i = i+1
    
    