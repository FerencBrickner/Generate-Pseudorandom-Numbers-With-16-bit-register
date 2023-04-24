from typing import Final, Generator, Iterator, Literal, TypeAlias


def generate_pseudorandom_numbers_with_16_bit_register(
    *, STARTING_STATE: Final[Literal[int]] = 14_950
) -> Generator[int, None, None]:
    NUMBER_OF_BITS: Final[Literal[int]] = 16
    
    Taps: TypeAlias = Final[list[Literal[int]]]
    TAPS: Taps = [16, 15, 13, 4]

    state: int = STARTING_STATE

    while 1:
        shifted_states: Iterator[int] = map(lambda x: state >> NUMBER_OF_BITS - x, TAPS)
        from functools import reduce

        new_bit: int = reduce(lambda x, y: x ^ y, shifted_states)
        del shifted_states
        new_bit &= 1
        state >>= 1
        state |= new_bit << (NUMBER_OF_BITS - 1)
        pseudorandom_number = state & 1
        yield pseudorandom_number
