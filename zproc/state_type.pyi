from typing import TypeVar, Iterator, overload, Optional, Mapping, Union, Tuple

T = TypeVar("T")
KT = TypeVar("KT")
VT = TypeVar("VT")

class StateDictMethodStub:
    def __contains__(self, o: object) -> bool: ...
    def __delitem__(self, v: KT) -> None: ...
    def __eq__(self, o: object) -> bool: ...
    def __getitem__(self, key: KT) -> VT: ...
    def __iter__(self) -> Iterator[KT]: ...
    def __len__(self) -> int: ...
    def __ne__(self, o: object) -> bool: ...
    def __setitem__(self, k: KT, v: VT) -> None: ...
    def clear(self) -> None: ...
    @overload
    def get(self, k: KT) -> Optional[VT]: ...
    @overload
    def get(self, k: KT, default: Union[KT, T]) -> Union[VT, T]: ...
    @overload
    def pop(self, k: KT) -> VT: ...
    @overload
    def pop(self, k: KT, default: Union[VT, T] = ...) -> Union[VT, T]: ...
    def pop(self, k: KT) -> VT: ...
    def popitem(self) -> Tuple[KT, VT]: ...
    def setdefault(self, k: KT, default: Optional[VT] = ...) -> VT: ...
    def update(self, a: Mapping[KT, VT]) -> None: ...
