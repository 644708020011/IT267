class Bird:
    global bird_type            #------global variable ------#
    #ถ้าไม่ใส่ ิglobal bird _type จะกลายเป็น class variable
    bird_type ="parrot" 
    bird_name = 'lory'          #------ class variable ------#
    def __init__(self,color) -> None:
        self.color = color
        name = "Peter"          #------Local variable ------#
        print(f'(name) in init')

if __name__ == '__main__':
    my_bird = Bird('Green,blue')

    print (my_bird.color)

    print(Bird.bird_name)

    print(bird_type)

    #Error
    #พยายามเรียก Local variable
    #print(name)    #NameError: 'name' is not defined

    #พยายามเรียก gobal variable ผ่าน class
    #print(Bird.bird_type)