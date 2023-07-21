class Nikola():
    __slots__ = ['name', 'age']
    def __init__(self, param1: str,  param2: int):
        self.name = self.check(param1)
        self.age = param2
    def check(self, name):
        if name.capitalize() not in ("Николай", "Nikola"):
            print(f'Я не {name}, я Николай')
        else:
            print('Успешно!')
        return name

if __name__ == '__main__':
    while True:
        input_name = input('Имя - ')
        if input_name == '':
            raise KeyboardInterrupt
        input_age = input('Возраст - ')
        if input_age.isnumeric():
            input_age = int(input_age)
            Nikola(input_name, input_age)
        else:
            print('- - Возраст должен быть целым числом - -')



