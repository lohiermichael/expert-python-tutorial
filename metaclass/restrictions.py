from functools import wraps


class MetaRestrict(type):
    """
    Metclass that restricts the creation of new attributes
    """
    def __new__(meta, class_name, bases, attrs):
        def _setattr(self, name, value):
            if not hasattr(self, name):
                raise AttributeError(
                    f'Name {name} is not an attribute of {class_name} object. You cannot add new attributes to {class_name}')
            object.__setattr__(self, name, value)

        def override_setattr_after(fn):
            @wraps(fn)
            def _wrapper(*args, **kwargs):
                cls.__setattr__ = object.__setattr__
                fn(*args, **kwargs)
                cls.__setattr__ = _setattr
            return _wrapper

        cls = type.__new__(meta, class_name, bases, attrs)
        cls.__init__ = override_setattr_after(cls.__init__)
        return cls


class Dog(metaclass=MetaRestrict):

    def __init__(self, gender, name):
        self.gender = gender
        self.name = name

    def bark(self):
        print("Wouah!")


class Cat:
    def __init__(self, name, gender):
        self.gender = gender
        self.name = name

    def mew(self):
        print("Miaou!")


if __name__ == "__main__":
    cat = Cat(name='Lili', gender='female')
    print(cat.gender)
    cat.mew()
    cat.love = True
    print(cat.love)

    dog = Dog(name='Lili', gender='female')
    dog.love = True
    print(dog.love)
