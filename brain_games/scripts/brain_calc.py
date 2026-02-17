#!/usr/bin/env python3


from brain_games.games import brain_calc
from brain_games.engine import run_games


def main():
    run_games(brain_calc)


if __name__ == '__main__':
    main()