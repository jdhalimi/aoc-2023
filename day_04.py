sample = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]


def card_id(card):
    n, _ = card.split(":")
    return int(n.split()[1])


def worth(card):
    n, values = card.split(":")
    wining, numbers = values.split("|")
    wining = [int(x) for x in wining.strip().split()]
    numbers = [int(x) for x in numbers.strip().split()]
    w = 0
    for x in numbers:
        if x in wining:
            w = 2 * w if w else 1
    return w


def test_worth():
    assert worth("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53") == 8
    assert sum([worth(x) for x in sample]) == 13


def calc_file_worth(file_name):
    """ reads file and calculates score """
    with open(file_name, 'r') as f:
        games = [x.strip() for x in f.readlines() if x.strip()]
    return sum([worth(x) for x in games])


def test_calc_file_worth():
    """ tests calc_file_score function """
    assert calc_file_worth("data/04.txt") == 21558


def calc_match_numbers(card):
    n, values = card.split(":")
    wining, numbers = values.split("|")
    wining = [int(x) for x in wining.strip().split()]
    numbers = [int(x) for x in numbers.strip().split()]
    return len([x for x in numbers if x in wining])


def test_calc_match_numbers():
    assert calc_match_numbers("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53") == 4


def expand_game(game):
    data = {card_id(x): [calc_match_numbers(x), 1] for x in game}
    for i, x in data.items():
        nb, sz = x
        for j in range(nb):
            if i + j + 1 in data:
                data[i + j + 1][1] = data[i + j + 1][1] + sz

    return [[i, n, w] for (i, (n, w)) in data.items()]


def test_expand_game():
    assert expand_game(sample) == [
        [1,4, 1],
        [2, 2, 2],
        [3, 2, 4],
        [4, 1, 8],
        [5, 0, 14],
        [6, 0, 1]]

    assert sum([x[2] for x in expand_game(sample)]) == 30


def test_file_expand_score():
    """ reads file and calculates score """
    with open("data/04.txt", 'r') as f:
        cards = [x.strip() for x in f.readlines() if x.strip()]
    assert sum([x[2] for x in expand_game(cards)]) == 10425665
