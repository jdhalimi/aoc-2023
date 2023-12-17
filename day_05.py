sample = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def decode_map(content):
    data = content.splitlines()
    data = [x.strip() for x in data if x.strip()]

    maps = {}
    current = []
    for line in data:
        if line.startswith("seeds:"):
            maps['seeds'] = [int(x) for x in line.split(":")[1].strip().split()]
            continue
        if line.endswith("map:"):
            current = []
            maps[line.split(":")[0].replace(" map", "").strip()] = current
            continue

        r = [int(x) for x in line.strip().split()]
        current.append(r)

    return maps


def test_decode_map():
    assert decode_map(sample) == {
        'seeds': [79, 14, 55, 13],
        'seed-to-soil': [[50, 98, 2], [52, 50, 48]],
        'soil-to-fertilizer': [[0, 15, 37], [37, 52, 2], [39, 0, 15]],
        'fertilizer-to-water': [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]],
        'water-to-light': [[88, 18, 7], [18, 25, 70]],
        'light-to-temperature': [[45, 77, 23], [81, 45, 19], [68, 64, 13]],
        'temperature-to-humidity': [[0, 69, 1], [1, 0, 69]],
        'humidity-to-location': [[60, 56, 37], [56, 93, 4]]
    }


def calc_destination(n, translations):
    """ calculates destination """
    for destination, start, window in translations:
        if start <= n < start + window:
            return destination + n - start
    return n


def test_calc_destination():
    mappings = decode_map(sample)
    assert calc_destination(79, mappings['seed-to-soil']) == 81
    assert calc_destination(14, mappings['seed-to-soil']) == 14
    assert calc_destination(55, mappings['seed-to-soil']) == 57
    assert calc_destination(13, mappings['seed-to-soil']) == 13


def find_location(n, mappings):
    """ finds location """
    for k in ('seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature',
              'temperature-to-humidity', 'humidity-to-location'):
        n = calc_destination(n, mappings[k])
    return n


def test_find_location():
    mappings = decode_map(sample)
    assert find_location(79, mappings) == 82
    assert find_location(14, mappings) == 43
    assert find_location(55, mappings) == 86
    assert find_location(13, mappings) == 35

    assert min([find_location(s, mappings) for s in mappings['seeds']]) == 35


def calc_file_location(file_name):
    """ reads file and calculates score """
    with open(file_name, 'r') as f:
        mappings = decode_map(f.read())
    return min([find_location(s, mappings) for s in mappings['seeds']])


def test_calc_file_location():
    """ tests calc_file_score function """
    assert calc_file_location("data/05.txt") == 1181555926
