class Product:
    def init(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return (f"{self.name}: ${self.price:.2f}")


class Customer:
    def init(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{product.name} додано до кошика.")

    def show_cart(self):
        if not self.cart:
            print("Кошик порожній.")
            return
        total = sum(product.price for product in self.cart)
        print(f"Кошик {self.name}:")
        for product in self.cart:
            print(f" - {product.info()}")
        print(f"Загальна вартість: ${total:.2f}")


apple = Product("Яблоко", 1.5)
banana = Product("Банан", 2.0)
customer = Customer("Іван")
customer.add_to_cart(apple)
customer.add_to_cart(banana)
customer.show_cart()


class Animal:
    def init(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} каже: {self.sound}")


class Dog(Animal):
    def init(self, name):
        super().init(name, "Гав-гав")

    def make_sound(self):
        print(f"{self.name} (собака) каже: {self.sound}! Я добрий пес!")


class Cat(Animal):
    def init(self, name):
        super().init(name, "Мяу-мяу")

    def make_sound(self):
        print(f"{self.name} (кіт) каже: {self.sound}! Я незалежний кіт!")


dog = Dog("Песик")
cat = Cat("котик")
dog.make_sound()
cat.make_sound()
