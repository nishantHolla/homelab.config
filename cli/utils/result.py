from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

T = TypeVar("T")
E = TypeVar("E")


@dataclass
class Ok(Generic[T]):
    value: T

    def unwrap(self) -> T:
        return self.value

    def unwrap_or(self, default: T) -> T:
        return self.value

    def unwrap_or_else(self, f: Callable[[E], T]) -> T:
        return self.value


@dataclass
class Err(Generic[E]):
    error: E

    def unwrap(self):
        raise RuntimeError(f"Called unwrap on Err: {self.error}")

    def unwrap_or(self, default):
        return default

    def unwrap_or_else(self, f):
        return f(self.error)


Result = Ok[T] | Err[E]
