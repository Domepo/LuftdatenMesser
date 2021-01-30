# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = data_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Sensordatavalue:
    value_type: str
    value: str

    @staticmethod
    def from_dict(obj: Any) -> 'Sensordatavalue':
        assert isinstance(obj, dict)
        value_type = from_str(obj.get("value_type"))
        value = from_str(obj.get("value"))
        return Sensordatavalue(value_type, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value_type"] = from_str(self.value_type)
        result["value"] = from_str(self.value)
        return result


@dataclass
class Data:
    software_version: str
    age: int
    sensordatavalues: List[Sensordatavalue]

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        software_version = from_str(obj.get("software_version"))
        age = int(from_str(obj.get("age")))
        sensordatavalues = from_list(Sensordatavalue.from_dict, obj.get("sensordatavalues"))
        return Data(software_version, age, sensordatavalues)

    def to_dict(self) -> dict:
        result: dict = {}
        result["software_version"] = from_str(self.software_version)
        result["age"] = from_str(str(self.age))
        result["sensordatavalues"] = from_list(lambda x: to_class(Sensordatavalue, x), self.sensordatavalues)
        return result


def data_from_dict(s: Any) -> Data:
    return Data.from_dict(s)


def data_to_dict(x: Data) -> Any:
    return to_class(Data, x)
