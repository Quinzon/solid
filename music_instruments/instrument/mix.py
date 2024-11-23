from dataclasses import dataclass, field
from typing import List

from ..base import KeyInstrument, BrassInstrument, InstrumentTuning


@dataclass
class Organ(KeyInstrument, BrassInstrument):
    tone: List[InstrumentTuning] = field(default_factory=lambda: [InstrumentTuning.DO,
                                                                  InstrumentTuning.SO])

    def display(self) -> None:
        print(f"{self} (Тип духовой части: {', '.join(t for t in self.brass_instrument_type)}, "
              f"Тип клавишной части: {', '.join(t for t in self.key_instrument_type)})")
