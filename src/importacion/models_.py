 
from typing import NamedTuple, Optional
#from .database import connection


class Userx(NamedTuple):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[str] = None
    sexo: Optional[str] = None

class User(NamedTuple):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[str] = None
    sexo: Optional[str] = None

