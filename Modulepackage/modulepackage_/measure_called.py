#วิธีที่ 1
from measure import Measure

if __name__ == '__main__':
    mobj = Measure()
    #print (f'5 cm = {mobj.cm_inch(5):.2f} inch')
    #print (f'18.5 inch = {mobj.inch_cm(18.5):.2f} cm')
    choice = input('choose type (1: inch, 2: cm): ')

    number = float(input('Enter number: '))

    if choice == '1':
        print (f'{number}inch = {mobj.inch_cm(number):.2f} cm')
    elif choice == '2':
        print (f'{number} cm = {mobj.cm_inch(number):.2f} inch')
    else:
        print('choose wrong type')