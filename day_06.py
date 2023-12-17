sample = """
Time:      7  15   30
Distance:  9  40  200
"""


def decode_data(content):
    times = []
    distances = []
    for line in content.splitlines():
        if line.startswith("Time:"):
            times = [int(x) for x in line.split(":")[1].strip().split()]
        if line.startswith("Distance:"):
            distances = [int(x) for x in line.split(":")[1].strip().split()]
    return times, distances


def test_decode_data():
    assert decode_data(sample) == ([7, 15, 30], [9, 40, 200])


def ways_to_beat(time, distance):
    count = 0
    for n in range(1, time):
        speed = n
        d = speed * (time - n)
        if d > distance:
            count += 1
    return count


def test_ways_to_beat():
    assert ways_to_beat(7, 9) == 4
    assert ways_to_beat(15, 40) == 8
    assert ways_to_beat(30, 200) == 9


def calc_ways_to_beat(times, distances):
    result = 1
    for time, distance in zip(times, distances):
        result *= ways_to_beat(time, distance)
    return result


def test_all_ways_to_beat():
    times, distances = decode_data(sample)
    assert calc_ways_to_beat(times, distances) == 288


def test_calc_ways_to_beat():
    """ brute force """
    times, distances = decode_data(open("data/06.txt").read())
    assert calc_ways_to_beat(times, distances) == 281600


def test_calc_ways_to_beat_part_2():
    """ brute force works for part 2 too"""
    times, distances = decode_data(open("data/06.txt").read().replace(" ", ""))
    assert calc_ways_to_beat(times, distances) == 33875953
