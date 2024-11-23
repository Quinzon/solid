from dataclasses import dataclass, field
from typing import List

from ..base import BrassInstrument, InstrumentTuning


@dataclass
class Saxophone(BrassInstrument):
    tone: List[InstrumentTuning] = field(default_factory=lambda: [InstrumentTuning.DO,
                                                                  InstrumentTuning.RE,
                                                                  InstrumentTuning.MI])

    def display(self) -> None:
        print(f"{self} Тип саксофона: {', '.join(t for t in self.brass_instrument_type)}")
