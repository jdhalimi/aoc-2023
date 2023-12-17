def decode(txt):
    """ finds fist numer in txt and returns it as int """
    x, y = 0, 0
    for i in txt:
        if i.isdigit():
            x = int(i)
            break
    for j in txt[::-1]:
        if j.isdigit():
            y = int(j)
            break
    return 10 * x + y


def test_decode():
    """ tests decode function """
    assert decode("a123b") == 13
    assert decode("a12b") == 12
    assert decode("a1b") == 11


def test_sample_decode():
    sample = ["one1two2three3", "1abc2pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    res = [decode(x) for x in sample]
    assert sum(res) == 123


def calc_file(file_name):
    """ reads file and calculates sum of first and last number in each line """
    with open(file_name, 'r') as f:
        return [decode(x) for x in f]


def test_calc_file():
    """ tests calc_file function """
    res = calc_file("data/01.txt")
    assert sum(res) == 54081


def decode_2(txt):
    d_digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    r_digits = {k[::-1]: v for k, v in d_digits.items()}

    def is_digit(s, digits):
        if s[0].isdigit():
            return int(s[0])
        for k, v in digits.items():
            if s.startswith(k):
                return v
        return None

    for i in range(len(txt)):
        x = is_digit(txt[i:], d_digits)
        if x is not None:
            break
    txt = txt[::-1]
    for i in range(len(txt)):
        y = is_digit(txt[i::], r_digits)
        if y is not None:
            break
    return 10 * x + y


def test_decode_2():
    assert decode_2("one123two") == 12
    assert decode_2("one12two") == 12
    assert decode_2("7one12two") == 72
    assert decode_2("one1two3") == 13


def test_sample_decode_2():
    sample = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234",
              "7pqrstsixteen"]
    res = [decode_2(x) for x in sample]
    assert sum(res) == 281


def calc_file_2(file_name):
    """ reads file and calculates sum of first and last number in each line """
    with open(file_name, 'r') as f:
        return [decode_2(x) for x in f]


def test_calc_file_2():
    """ tests calc_file function """
    res = calc_file_2("data/01.txt")
    assert sum(res) == 54649
