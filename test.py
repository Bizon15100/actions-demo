from __future__ import annotations
import sys


def greet(name: str) -> str:
    """
    Zwraca tekst powitania dla podanego imienia.

    :param name: Imię osoby do przywitania.
    :return: Napis z powitaniem.
    """
    return f"Cześć, {name}!"


def main(args: list[str]) -> None:
    if len(args) >= 2:
        name = args[1]
    else:
        name = "Świecie"
    print(greet(name))


if __name__ == "__main__":
    main(sys.argv)
