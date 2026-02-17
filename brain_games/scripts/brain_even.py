#!/usr/bin/env python3


from brain_games.games import brain_even
from brain_games.engine import run_games


def main():
    run_games(brain_even)

if __name__ == "__main__":
    main()
