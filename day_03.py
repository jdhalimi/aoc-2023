sample = ["467..114..",
          "...*......",
          "..35..633.",
          "......#...",
          "617*......",
          ".....+.58.",
          "..592.....",
          "......755.",
          "...$.*....",
          ".664.598.."]


def mult(iterable):
    res = 1
    for x in iterable:
        res *= x
    return res


def find_symbols(grid):
    symbols = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row.strip()):
            if not cell.isdigit() and cell != '.':
                symbols.append((x, y))
    return symbols


def test_find_symbols():
    assert find_symbols(sample) == [(3, 1), (6, 3), (3, 4), (5, 5), (3, 8), (5, 8)]


def adjacent_symbols(x, y, symbols):
    for sx, sy in symbols:
        if abs(x - sx) <= 1 and abs(y - sy) <= 1:
            return True
    return False


def test_adjacent_symbols():
    assert adjacent_symbols(2, 0, [(3, 1), (3, 4), (5, 4), (5, 7), (7, 7), (7, 9), (8, 9)]) is True
    assert adjacent_symbols(2, 4, [(3, 1), (3, 4), (5, 4), (5, 7), (7, 7), (7, 9), (8, 9)]) is True


def calc_adjacent_numbers(grid, symbols):
    numbers = []
    for y, row in enumerate(grid):
        n = 0
        test_adjacent = False
        for x, cell in enumerate(row.strip() + '.'):
            if cell.isdigit():
                if adjacent_symbols(x, y, symbols):
                    test_adjacent = True
                n = n * 10 + int(cell)
                continue
            if test_adjacent:
                numbers.append(n)
            n = 0
            test_adjacent = False

    return numbers


def test_calc_adjacent_numbers():
    symbols = find_symbols(sample)
    assert calc_adjacent_numbers(sample, symbols) == [467, 35, 633, 617, 592, 755, 664, 598]
    assert sum(calc_adjacent_numbers(sample, symbols)) == 4361


def calc_file_adjacent_numbers(file_name):
    """ reads file and calculates score """
    with open(file_name, 'r') as f:
        grid = [x.strip() for x in f.readlines() if x.strip()]
    symbols = find_symbols(grid)
    return calc_adjacent_numbers(grid, symbols)


def test_calc_file_adjacent_numbers():
    """ tests calc_file_adjacent_numbers function """
    numbers = calc_file_adjacent_numbers("data/03.txt")
    print(numbers)
    assert sum(numbers) == 528819


def find_gears(grid):
    symbols = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row.strip()):
            if cell == '*':
                symbols.append((x, y))
    return symbols


def calc_gear_power(grid):
    gears = find_gears(grid)
    power = 0
    for gear in gears:
        numbers = calc_adjacent_numbers(grid, [gear])
        if len(numbers) > 1:
            power += mult(numbers)
    return power


def test_calc_sample_gear_power():
    assert calc_gear_power(sample) == 467835


def test_calc_file_gear_power():
    """ tests calc_file_gear_power function """
    with open("data/03.txt", 'r') as f:
        grid = [x.strip() for x in f.readlines() if x.strip()]
    assert calc_gear_power(grid) == 80403602
