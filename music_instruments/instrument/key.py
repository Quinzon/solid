from dataclasses import dataclass, field
from typing import List

from ..base import KeyInstrument, InstrumentTuning


@dataclass
class Piano(KeyInstrument):
    tone: List[InstrumentTuning] = field(default_factory=lambda: [InstrumentTuning.MI,
                                                                  InstrumentTuning.FA,
                                                                  InstrumentTuning.SO])

    def display(self) -> None:
        print(f"{self} (Тип клавишного инструмента: {', '.join(t for t in self.key_instrument_type)}, "
              f"Количество клавиш: {self.count_key})")
