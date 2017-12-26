from typing import Any, Optional, Union


class Semaphore:
    def __init__(self, value: int = ...) -> None: ...
    def acquire(self, blocking: bool = ..., timeout: Optional[int] = ...) -> bool: ...
    def release(self) -> None: ...
    def __exit__(self, t: Any, v: Any, tb: Any) -> None: ...
    @property
    def counter(self) -> int: ...

class BoundedSemaphore(Semaphore):
    def __init__(self, value: int = ...) -> None: ...
    def release(self) -> None: ...

class DummySemaphore(object):
    def __init__(self, value: Optional[int] = ...) -> None: ...
    def acquire(self, blocking: bool = ..., timeout: Optional[int] = ...) -> bool: ...
    def release(self) -> None: ...

class MaxWaitersBoundedSemaphore(object):
    def __init__(self, semaphore_class: Semaphore, value: int = ..., max_waiters: int = ...) -> None: ...
    def acquire(self, blocking: bool = ..., timeout: Optional[int] = ...) -> bool: ...
    def __getattr__(self, name: str) -> Any: ...

class MaxWaitersBoundedSemaphoreThread(MaxWaitersBoundedSemaphore):
    def __init__(self, value: int = ..., max_waiters: int = ...) -> None: ...

def create_semaphore(max_size: int, max_waiters: int) -> Union[Semaphore, MaxWaitersBoundedSemaphore]: ...
