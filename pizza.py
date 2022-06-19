class Pizza:
    def __init__(self,ingredients) -> None:
        self.ingredients = ingredients

    def __repr__(self) :
        #ส่งคืนค่าที่สามารถพิมพ์ได้
        return f'Pizza({self.ingredients})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarrella','tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarrella','tomatoes','ham'])

    @staticmethod
    #มักใช้เป็น utility หรือ helper function เพื่อทำให้ code เป็น modular
    def size(ch):
        ch=ch.upper()
        if ch == 'S':
            return 'small: 6 inches, 4 slices'
        elif ch == 'L' :
            return 'large: 14 inches, 10 slices'
        else:
            return 'Default Medium: 12 inches, 8 slices'
    
    # create instance
    my_pizza = Pizza('Cheese, Meat')
    print(my_pizza)
    print(my_pizza.margherita())

    #static method
    print('---- Static Method ----')
    print(Pizza.size('L'))

    # clsaa method
    print('---- class Method ----')
    print(pizza.margherita())
    print(pizza.prosciuttu())
    print(my_pizza.margherita())
    print(Pizza.ingredients) # cannot access instance vatiable