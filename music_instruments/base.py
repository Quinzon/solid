from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class InstrumentTuning(str, Enum):
    DO = 'Do'
    RE = 'Re'
    MI = 'Mi'
    FA = 'Fa'
    SO = 'So'
    LA = 'La'
    SI = 'Si'


class StringTyping(str, Enum):
    NYLON = 'Nylon'
    METAL = 'Metal'


class KeyInstrumentType(str, Enum):
    KEYBOARD = 'Keyboard'
    KEYBRASS = 'Keyboard and brass'


class BrassInstrumentType(str, Enum):
    WOOD = 'Wood'
    COPPER = 'Copper'


@dataclass
class Instrument(ABC):
    year: Optional[int]
    tone: Optional[List[InstrumentTuning]] = field(default_factory=list)

    @abstractmethod
    def display(self) -> None:
        pass

    def __str__(self):
        """Возвращает строковое представление объекта."""
        tones = ', '.join(tone for tone in self.tone)
        return f"Инструмент: {self.__class__.__name__}, Тональности: [{tones}], Год: {self.year}"


@dataclass
class StringInstrument(Instrument):
    type_string: Optional[List[StringTyping]] = field(default_factory=list)
    count_string: int = 0

    def display(self) -> None:
        print(self)


@dataclass
class KeyInstrument(Instrument):
    key_instrument_type: Optional[List[KeyInstrumentType]] = field(default_factory=list)
    count_key: int = 0

    def display(self) -> None:
        print(self)


@dataclass
class BrassInstrument(Instrument):
    brass_instrument_type: Optional[List[BrassInstrumentType]] = field(default_factory=list)

    def display(self) -> None:
        print(self)
