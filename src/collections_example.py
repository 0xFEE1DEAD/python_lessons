r"""

Распаковка кортежей:

    >>> lax_coordinates = (33.9425, -118.408)
    >>> latitude, longitude = lax_coordinates
    >>> latitude
    33.9425
    >>> longitude
    -118.408

Использование * для выборки лишних элементов:

    >>> a, b, *rest = range(5)
    >>> a, b, rest
    (0, 1, [2, 3, 4])

Распаковка с помощью * в вызовах функций и литеральных последовательностях:

    >>> def func(a, b, c, d, *rest):
    ...     return a, b, c, d, rest
    ...
    >>> func(*[1, 2], 3, *range(4, 7))
    (1, 2, 3, 4, (5, 6))

Срезы:

    >>> l = list(range(10))
    >>> l
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> l[2:5] = [20, 30]
    >>> l
    [0, 1, 20, 30, 5, 6, 7, 8, 9]
    >>> del l[5:7]
    >>> l
    [0, 1, 20, 30, 5, 8, 9]
    >>> l = [1, 2, 3]
    >>> l * 2
    [1, 2, 3, 1, 2, 3]
"""


def unpacking_nested_structures():
    """
    Распаковка вложенных структур
    >>> unpacking_nested_structures()
                    |  latitude | longitude
    Tokyo           |   35.6897 |  139.6917
    Delhi NCR       |   28.6139 |   77.2089
    """
    metro_areas = [
        ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
        ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ]

    print(f"{'':15} | {'latitude':>9} | {'longitude':>9}")  # noqa: T201
    for name, _, _, (lat, lon) in metro_areas:
        print(f"{name:15} | {lat:9.4f} | {lon:9.4f}")  # noqa: T201


class Robot:
    """
    Сопоставление с последовательностями образцами

    >>> r = Robot()
    >>> r.handle_command(("BEEPER", 10, 5))
    beep 5 10
    >>> r.handle_command(["BEEPER", 10, 5])
    beep 5 10
    >>> r.handle_command(["BEEPER", "10", "5"])
    Invalid beep arg types
    """

    def beep(self, times: int, frequency: int):
        print(f"beep {times} {frequency}")  # noqa: T201

    def handle_command(self, message: tuple[str | int] | list[str | int]):
        match message:
            case ["BEEPER", int(frequency), int(times)]:
                self.beep(times, frequency)
            case ["BEEPER", str(frequency), str(times)]:
                print("Invalid beep arg types")  # noqa: T201
            case _:
                msg = "Invalid Command"
                raise RuntimeError(msg)
