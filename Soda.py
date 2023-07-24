class Soda:
    def __init__(self, dobavka: str):
        self.dobavka = dobavka

    def show_my_drink(self):
        if self.dobavka is None:
            print('Обычная газировка')
        else:
            print(f'Газировка и {self.dobavka}')

if __name__ == '__main__':
    a = Soda()
    b = Soda('kjh')