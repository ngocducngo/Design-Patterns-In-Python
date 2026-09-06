# pylint: disable=too-few-public-methods
"Abstract Factory Concept Sample Code"
from abc import ABCMeta, abstractmethod
from factory_a import FactoryA
from factory_b import FactoryB


class IAbstractFactory(metaclass=ABCMeta): #lớp trừu tượng định nghĩa giao diện cho Abstract Factory, dùng ABCMeta và abstractmethod để ép các class con phải triển khai method create_object
    "Abstract Factory Interface"

    @staticmethod #method nhận vào 1 chuỗi như 'ab', 'bc','ca'
    @abstractmethod
    def create_object(factory): #method quyết định dùng factoryA hay factoryB
        "The static Abstract factory interface method"


class AbstractFactory(IAbstractFactory):
    "The Abstract Factory Concrete Class"

    @staticmethod
    def create_object(factory):
        "Static get_factory method"
        try:
            if factory in ['aa', 'ab', 'ac']:
                return FactoryA.create_object(factory[1])
            if factory in ['ba', 'bb', 'bc']:
                return FactoryB.create_object(factory[1])
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None


# The Client. client không biết class nào được tạo, chỉ cần 1 điểm giao tiếp là AbstractFactory và các factory con (fac A, fac B # # tạo product phù hợp
PRODUCT = AbstractFactory.create_object('ab')
print(f"{PRODUCT.__class__}")

PRODUCT = AbstractFactory.create_object('bc')
print(f"{PRODUCT.__class__}")
