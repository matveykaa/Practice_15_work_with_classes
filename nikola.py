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

    def __setattr__(self, name, value):
        if name in self.__slots__:
            super().__setattr__(name, value)
        else:
            raise AttributeError("Невозможно добавить новый атрибут или переопределить существующий атрибут.")

if __name__ == '__main__':
    while True:
        input_name = input('Имя - ')
        if input_name == '':
            raise KeyboardInterrupt
        input_age = input('Возраст - ')
        if input_age.isnumeric():
            input_age = int(input_age)
            person = Nikola(input_name, input_age)
        else:
            print('- - Возраст должен быть целым числом - -')

        try:
            person.surname = 'Петров'
        except AttributeError as e:
            print(e)



