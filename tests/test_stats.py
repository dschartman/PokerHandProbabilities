from itertools import combinations, permutations, product
from math import comb, pow
from pprint import pprint

import pytest

SUITS = [("s", "black"), ("c", "black"), ("h", "red"), ("d", "red")]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
POSSIBLE_HANDS = 2598960


@pytest.fixture(scope="module")
def cards():
    yield [p for p in list(product(RANKS, SUITS))]


def test_print_cards(cards):
    expected_cards = 52

    assert len(cards) == expected_cards


def test_possible_hands(cards):
    expected_combinations = 2598960
    c = combinations(cards, 5)
    assert len(list(c)) == expected_combinations


def test_probability_high_card(cards):
    expected_combinations = 1302540

    distinct_ranks = 5
    single_rank_possible_straights = 10
    single_suit_possible_flushes = 4

    ranks = comb(13, distinct_ranks) - single_rank_possible_straights
    suits = pow(comb(4, 1), distinct_ranks) - single_suit_possible_flushes

    total = ranks * suits

    assert total == expected_combinations


def test_probability_pair(cards):
    ranks = comb(13, 1)
    suits = comb(4, 2)
    remaining_ranks = comb(12, 3)
    remaining_suits = pow(comb(4, 1), 3)

    total = ranks * suits * remaining_ranks * remaining_suits
    print(total)


def test_probability_two_pair(cards):
    ranks = comb(13, 2)
    suits = pow(comb(4, 2), 2)
    remaining_ranks = comb(11, 1)
    remaining_suits = pow(comb(4, 1), 1)

    total = ranks * suits * remaining_ranks * remaining_suits
    print(total)


def test_probability_three_of_a_kind(cards):
    ranks = comb(13, 1)
    suits = comb(4, 3)
    remaining_ranks = comb(12, 2)
    remaining_suits = pow(comb(4, 1), 2)

    total = ranks * suits * remaining_ranks * remaining_suits
    print(total)


def test_probability_straight(cards):
    ranks = 10
    suits = pow(comb(4, 1), 5)

    total = ranks * (suits - 4)
    print(total)


def test_probability_flush(cards):
    ranks = comb(13, 5) - 10
    suits = comb(4, 1)

    total = ranks * suits
    print(total)


def test_probability_full_house(cards):
    ranks = comb(13, 1)
    suits = comb(4, 3)
    remaining_ranks = comb(12, 1)
    remaining_suits = comb(4, 2)

    total = ranks * suits * remaining_ranks * remaining_suits
    print(total)


def test_probability_4_of_a_kind(cards):
    ranks = comb(13, 1)
    suits = comb(4, 4)
    remaining_ranks = comb(12, 1)
    remaining_suits = comb(4, 1)

    total = ranks * suits * remaining_ranks * remaining_suits
    print(total)


def test_probability_straight_flush(cards):
    ranks = 10
    suits = comb(4, 1)

    total = ranks * suits - 4
    print(total)


def test_probability_royal_flush(cards):
    ranks = 1
    suits = comb(4, 1)

    total = ranks * suits
    print(total)


STRAIGHTS = [
    "14 2 3 4 5",
    "2 3 4 5 6",
    "3 4 5 6 7",
    "4 5 6 7 8",
    "5 6 7 8 9",
    "6 7 8 9 10",
    "7 8 9 10 11",
    "8 9 10 11 12",
    "9 10 11 12 13",
    "10 11 12 13 14",
]

scores = {
    "high_card": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    "pair": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
}

sample = {
    "cards": "14.s 2.s 3.h 4.d 5.c",
    "type": "straight",
    "strength": "5 4 3 2 14",
    "meta": {
        "cards": "2.s 3.h 4.d 5.c 14.s 7.h 8.d",
        "high": "14",
        "pairs": None,
        "trips": None,
        "straight": "14.s 2.s 3.h 4.d 5.c",
        "flush": None,
        "quads": None,
        "broadway": None,
    },
}
