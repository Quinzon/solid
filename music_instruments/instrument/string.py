from dataclasses import dataclass, field
from typing import List

from ..base import StringInstrument, InstrumentTuning


@dataclass
class Guitar(StringInstrument):
    tone: List[InstrumentTuning] = field(default_factory=lambda: [InstrumentTuning.DO,
                                                                  InstrumentTuning.RE,
                                                                  InstrumentTuning.MI])

    def display(self) -> None:
        print(f"{self} (Тип струн: {', '.join(t for t in self.type_string)}, Количество струн: {self.count_string})")
