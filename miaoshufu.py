import abc


def prop_factory(name):
    """特性工程函数"""
    def get_prop(instance):
        return instance.__dict__[name]

    def set_prop(instance,value):
        if value > 0:                           # 此处排查条件根据具体需要设置
            instance.__dict__[name] = value
        else:
            print('error value')
    return property(get_prop, set_prop)


# class Quantity:
#
#     def __init__(self,storage_name):
#         self.storage = storage_name
#
#     def __set__(self,instance,value):
#         if value > 0:
#             instance.__dict__[self.storage] = value
#         else:
#             raise ValueError('the value is error')
class AutoStorage:

    def __init__(self):
        cls = self.__class__
        self.storage_name = ''

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)


class Validated(abc.ABC, AutoStorage):

    def __set__(self, instance, value):
        value = self.validate(instance,value)
        super().__set__(instance,value)
    @abc.abstractclassmethod
    def validate(self, instance, value):
        """retun validated value or raise ValueError"""



class Quantity(Validated):

    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('value must be > 0')
        return value


def entity(cls):
    for key, attr in cls.__dict__.items():
        if isinstance(attr, Validated):
            attr.storage_name = '_{}#{}'.format(type(attr).__name__, key)
        return cls


@entity
class Good:
    weight = Quantity()
    price = Quantity()

    def __init__(self,weight,price):
        self.weight = weight
        self.price = price

    def purase(self):
        return self.weight * self.price


class NonBlank(Validated):

    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('value cannot be empty or blank')
        return value




if __name__ == "__main__":
    good = Good(2,1)
    print(good.price, good.weight)