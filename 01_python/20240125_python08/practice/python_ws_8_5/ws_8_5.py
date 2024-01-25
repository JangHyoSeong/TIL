# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    pass


class Dog(Animal):
    sound = '멍멍'

    def __init__(self):
        Animal.num_of_animal += 1

    def bark(self):
        print('멍멍!')


class Cat(Animal):
    sound = '야옹'

    def __init__(self):
        Animal.num_of_animal += 1

    def meow(self):
        print('야옹!')



class Pet(Dog, Cat):

    def __init__(self):
        pass

    def __str__(self):
        return f'애완 동물은 {self.sound}소리를 냅니다.'


    def play(self):
        print('애완동물과 놀기')

    def make_sound(self):
        print(f'{self.sound}')
    


pet1 = Pet()
print(pet1)
