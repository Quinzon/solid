from typing import Callable

from music_instruments.base import Instrument


class Container(list):
    def rem(self, condition: Callable[[Instrument], bool]) -> None:
        """Удаляет элементы из контейнера, удовлетворяющие заданному условию."""
        self[:] = [item for item in self if not condition(item)]
