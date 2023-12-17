def encode_game(txt):
    """ encodes game """
    desc = txt.replace("Game ", "")
    n, desc = desc.split(":")
    n = int(n)
    draws = desc.split(";")
    draws = [x.strip() for x in draws if x.strip()]

    state = {"red": 0, "blue": 0, "green": 0}
    for draw in draws:
        cubes = draw.split(",")
        cubes = [x.strip() for x in cubes if x.strip()]
        for cube in cubes:
            number, color = cube.split(" ")
            assert color in state.keys()
            state[color] = max(int(number), state[color])

    return n, state


def test_encode_game():
    txt = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert encode_game(txt) == (1, {'red': 4, 'blue': 6, 'green': 2})


def is_possible(state, bench):
    """ checks if game is possible """

    for k in ("red", "blue", "green"):
        if state[k] > bench[k]:
            return False

    return True


def calc_score(games, bench):
    """ calculates score """
    score = 0
    for game in games:
        n, state = encode_game(game)
        if is_possible(state, bench):
            score += n
    return score


def test_sample_score():
    sample = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    ]

    bench = {'red': 12, 'green': 13, 'blue': 14}
    assert calc_score(sample, bench) == 8


def calc_file_score(file_name):
    """ reads file and calculates score """
    with open(file_name, 'r') as f:
        games = [x.strip() for x in f.readlines() if x.strip()]
    bench = {'red': 12, 'green': 13, 'blue': 14}
    return calc_score(games, bench)


def test_calc_file_score():
    """ tests calc_file_score function """
    assert calc_file_score("data/02.txt") == 2679


def calc_game_power(game):
    """ calculates power """
    n, state = encode_game(game)

    def mult(iterable):
        res = 1
        for x in iterable:
            res *= x
        return res

    return mult(state.values())


def test_calc_game_power():
    """ tests calc_power function """
    game = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert calc_game_power(game) == 48


def calc_power(games):
    """ calculates power """
    return sum([calc_game_power(x) for x in games])


def test_sample_power():
    sample = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    ]

    assert calc_power(sample) == 2286


def calc_file_power(file_name):
    """ reads file and calculates score """
    with open(file_name, 'r') as f:
        games = [x.strip() for x in f.readlines() if x.strip()]
    return calc_power(games)


def test_calc_file_power():
    """ tests calc_file_power function """
    assert calc_file_power("data/02.txt") == 77607
