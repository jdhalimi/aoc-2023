from functools import cmp_to_key
from collections import defaultdict

CARDS = "AKQJT98765432"

sample = """
    32T3K 765
    T55J5 684
    KK677 28
    KTJJT 220
    QQQJA 483
    """


def decode_data(content):
    data = []
    for line in content.splitlines():
        if line.strip():
            cards, score = line.split()
            data.append((cards, int(score)))
    return data


def five_of_a_kind(cards):
    """Returns True if the hand has five of a kind."""
    return any(cards.count(card) == 5 for card in cards)


def four_of_a_kind(cards):
    """Returns True if the hand has four of a kind."""
    return any(cards.count(card) == 4 for card in cards)


def three_of_a_kind(cards):
    """Returns True if the hand has three of a kind."""
    return any(cards.count(card) == 3 for card in cards)


def two_pairs(cards):
    """Returns True if the hand has two pairs."""
    return len(set(cards)) == 3


def one_pair(cards):
    """Returns True if the hand has one pair."""
    return len(set(cards)) == 4


def high_card(cards):
    """Returns True if the hand has one pair."""
    return len(set(cards)) == 5


def test_hands():
    assert five_of_a_kind("AAAAA")
    assert not five_of_a_kind("AAAA2")
    assert four_of_a_kind("AAAA4")
    assert not four_of_a_kind("AAA14")
    assert three_of_a_kind("AAA24")
    assert not three_of_a_kind("AA234")
    assert not three_of_a_kind("AA234")
    assert two_pairs("AA233")
    assert not two_pairs("A2345")
    assert one_pair("A2245")
    assert not one_pair("23456")


def compare_values(cards, other_cards):
    """Returns True if the hand has one pair."""
    for x, y in zip(cards, other_cards):
        if CARDS.index(x) < CARDS.index(y):
            return 1
        elif CARDS.index(x) > CARDS.index(y):
            return -1
    return -1


def test_compare_values():
    assert compare_values("A2345", "A2344") > 0
    assert compare_values("A2344", "A2345") < 0
    assert compare_values("A2345", "A2245") > 0
    assert compare_values("A2245", "A2345") < 0
    assert compare_values("A2345", "A2344") > 0
    assert compare_values("A2345", "A2345") == 0


def weight(cards):
    c = defaultdict(int)
    for card in cards:
        c[card] += 1
    amount = sorted(c.values(), reverse=True)
    if amount == [5]:
        return 5
    elif amount == [4, 1]:
        return 4
    elif amount == [3, 2]:
        return 3
    elif amount == [3, 1, 1]:
        return 2.5
    elif amount == [2, 2, 1]:
        return 2
    elif amount == [2, 1, 1, 1]:
        return 1
    return 0


def compare(cards, other_cards):
    if weight(cards) > weight(other_cards):
        return 1
    elif weight(cards) < weight(other_cards):
        return -1
    elif weight(cards) == weight(other_cards):
        if cards == other_cards:
            return 0
        else:
            return compare_values(cards, other_cards)


def test_compare():
    assert compare("AAAAA", "AAAA2") > 0
    assert compare("AAAA2", "AAAAA") < 0
    assert compare("AAAA4", "AAA14") > 0
    assert compare("AAA14", "AAAA4") < 0


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    def __str__(self):
        return self.cards


def calc_score(hands):
    score = 0

    prv_hand = None
    for i, hand in enumerate(hands):
        score += (i + 1) * hand.bid
        prv_hand = hand
    return score


def test_calc_score():
    data = decode_data(sample)

    hands = [Hand(hand, score) for hand, score in data]
    hands.sort(key=cmp_to_key(lambda x, y: compare(x.cards, y.cards)))

    cards = [str(hand) for hand in hands]
    assert cards == ['32T3K', 'KTJJT', 'KK677', 'T55J5', 'QQQJA']

    assert calc_score(hands) == 6440


def test_calc_file_score():
    data = decode_data(open("data/07.txt").read())
    hands_map = {hand for hand, _ in data}
    assert len(hands_map) == len(data)

    hands = [Hand(hand, score) for hand, score in data]
    hands.sort(key=cmp_to_key(lambda x, y: compare(x.cards, y.cards)))
    assert len(hands) == 1000
    assert calc_score(hands) == 249204891


2448
