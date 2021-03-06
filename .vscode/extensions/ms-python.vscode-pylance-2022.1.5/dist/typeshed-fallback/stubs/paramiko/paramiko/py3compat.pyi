import sys
from typing import Any, Iterable, Sequence, Text, TypeVar

_T = TypeVar("_T")

PY2: bool

string_types: type[Any] | Sequence[type[Any]]
text_type: type[Any] | Sequence[type[Any]]
bytes_types: type[Any] | Sequence[type[Any]]
integer_types: type[Any] | Sequence[type[Any]]
long = int

def input(prompt: Any) -> str: ...
def decodebytes(s: bytes) -> bytes: ...
def encodebytes(s: bytes) -> bytes: ...

if sys.version_info >= (3, 0):
    import builtins as builtins
    import io

    StringIO = io.StringIO
    BytesIO = io.BytesIO
else:
    import __builtin__ as builtins
    import cStringIO

    StringIO = cStringIO.StringIO
    BytesIO = StringIO

bytes = builtins.bytes

def byte_ord(c: int | str) -> int: ...
def byte_chr(c: int) -> bytes: ...
def byte_mask(c: int, mask: int) -> bytes: ...
def b(s: bytes | str, encoding: str = ...) -> bytes: ...
def u(s: bytes | str, encoding: str = ...) -> Text: ...
def b2s(s: bytes | str) -> str: ...
def is_callable(c: Any) -> bool: ...
def next(c: Iterable[_T]) -> _T: ...

MAXSIZE: int
