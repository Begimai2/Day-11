year = int(input())
if year % 4 != 0:
    print('Regular year')
elif year % 100 == 0:
    # print('Regular year')

    if year % 400 == 0:
        print('intercalary year')
    else:
        print('Regular year')    
else:
    print('intercalary year')    