from container import Container
from music_instruments.base import StringTyping, KeyInstrumentType, BrassInstrumentType, InstrumentTuning
from music_instruments.instrument.brass import Saxophone
from music_instruments.instrument.key import Piano
from music_instruments.instrument.string import Guitar
from music_instruments.instrument.mix import Organ



if __name__ == "__main__":
    container = Container()

    guitar = Guitar(year=2020, type_string=[StringTyping.NYLON, StringTyping.METAL], count_string=6)
    piano = Piano(year=2018, key_instrument_type=[KeyInstrumentType.KEYBOARD], count_key=88)
    trumpet = Saxophone(year=2015, brass_instrument_type=[BrassInstrumentType.WOOD])
    organ = Organ(year=1920, key_instrument_type=[KeyInstrumentType.KEYBRASS],
                  brass_instrument_type=[BrassInstrumentType.COPPER ], count_key = 40)

    container.extend([guitar, piano, trumpet, organ])
    print("Контейнер до удаления:")
    for instrument in container:
        instrument.display()

    container.rem(lambda x: x.year < 2016)
    print("\nКонтейнер после удаления (year < 2016):" )
    for instrument in container:
        instrument.display()

    container.extend([guitar, piano, trumpet, organ])
    print("\nКонтейнер до удаления:")
    for instrument in container:
        instrument.display()



    container.rem(lambda x: InstrumentTuning.DO in x.tone)
    print("\nКонтейнер до удаления (InstrumentTuning.RE in x.tone):")
    for instrument in container:
        instrument.display()