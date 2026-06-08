from __future__ import annotations
import sys


def greet(name: str) -> str:
    return f"Cześć, {name}!"


def main(args: list[str]) -> None:
    if len(args) >= 2:
        name = args[1]
    else:
        name = "Świecie"
    print(greet(name))


if __name__ == "__main__":
    main(sys.argv)
