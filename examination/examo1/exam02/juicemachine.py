class JuiceOrder:
    total = 0

    def __init__(self,menu:str,size='R',) -> None:
        self.menu = menu
        self.size = size.upper()
        self.price = 0

    def check_menu(self):
        menu_dictionary = {
            'OJ':25,
            'AJ':25,
            'WJ':30,
            'PL':30
         } 
        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)

    
    def comput_price(self):
        if self.size == 'L':
            self.price += 5
        else:
            self.price

        JuiceOrder.total = self.price * 1

    def display_order(self):
        self.check_menu()
        self.comput_price()
        return (f'{self.menu}({self.size} * {self.price}) => {JuiceOrder.total}')

if __name__ == "__main__":
    order1 = JuiceOrder ("WJ","L")
    order2 = JuiceOrder ("OJ",)
    order3 = JuiceOrder ("PJ","L")

    print(order1.display_order())
    print(order2.display_order())
    print(order3.display_order())