"""
Module: psa9_tester

Test cases for critters project.

DO NOT MODIFY THIS FILE IN ANY WAY!

Author: Sat Garcia (sat@sandiego.edu)
"""

from unittest.mock import Mock, MagicMock, mock_open, patch, call
from critters import *
import io

def run_tests():

    try:
        # test all of the bear's methods
        test_bear_init()
        test_bear_str()
        test_bear_get_color()
        test_bear_eat()
        test_bear_fight()
        test_bear_get_move()

        # test all of the lion's methods
        test_lion_init()
        test_lion_str()
        test_lion_get_color()
        test_lion_eat()
        test_lion_fight()
        test_lion_get_move()

        # test all of the cheetah's methods
        test_cheetah_init()
        test_cheetah_str()
        test_cheetah_get_color()
        test_cheetah_eat()
        test_cheetah_fight()
        test_cheetah_get_move()

    except AssertionError as e:
        print("\nTest FAILED :(\n")
        raise e

    print("Congratulations: All tests PASSED!")


def test_bear_init():
    print("\nTesting Bear's __init__ method")
    b = Bear((5, 3), True)

    assert 'x' in b.__dict__ and 'y' in b.__dict__, \
        "x and y instance variables not set. Did you call the parent's constructor?"

    assert b.x == 5 and b.y == 3, \
        "Bear's x and y not set correctly. Did you call the super constructor?"

    print("\nTest of Bear.__init__ passed")

def test_bear_str():
    print("\nTesting Bear's __str__ method")
    b = Bear((0, 0), True)

    # test __str__ 10 times to make sure it doesn't vary
    for _ in range(10):
        assert str(b) == "B", \
            "Bear should always return 'B' from __str__"

    print("\nTest of Bear.__str__ passed")

def test_bear_get_color():
    print("\nTesting Bear's get_color method")

    for is_grizzly, expected_color in [(True, "brown"), (False, "snow")]:
        b = Bear((0, 0), is_grizzly)

        # test 10 times to make sure it doesn't vary
        for _ in range(10):
            assert b.get_color() == expected_color, \
                "When is_grizzly is %s, always return %s from get_color" \
                % (is_grizzly, expected_color)

    print("\nTest of Bear.get_color passed")

def test_bear_eat():
    print("\nTesting Bear's eat method")
    b = Bear((0, 0), True)

    # test 10 times to make sure it doesn't vary
    for _ in range(10):
        assert b.eat() == True

    print("\nTest of Bear.eat passed")

def test_bear_fight():
    print("\nTesting Bear's fight method")
    b = Bear((0, 0), True)

    # try with several different opponents to make sure it always returns
    # scratch
    print("\tTesting attack against a Lion.")
    assert b.fight("L") == Attack.SCRATCH, \
        "fight should always return Attack.SCRATCH"

    print("\tTesting attack against a Cheetah.")
    assert b.fight("0") == Attack.SCRATCH, \
        "fight should always return Attack.SCRATCH"
    assert b.fight("1") == Attack.SCRATCH, \
        "fight should always return Attack.SCRATCH"

    print("\tTesting attack against another critter (Torero?).")
    assert b.fight("T") == Attack.SCRATCH, \
        "fight should always return Attack.SCRATCH"

    print("\nTest of Bear.fight passed")

def test_bear_get_move():
    print("\nTesting Bear's get_move method")
    b = Bear((0, 0), True)

    neighbors = {Direction.NORTH: "L",
                 Direction.EAST: "L",
                 Direction.SOUTH: "L",
                 Direction.WEST: "L"}

    print("\tTesting movement of new Bear for 10 turns.")

    expected_moves = [Direction.NORTH, Direction.WEST] * 5
    actual_moves = [b.get_move(neighbors) for _ in range(10)]

    assert actual_moves == expected_moves, \
        "Expected first 10 moves: %s\nActual first 10 moves: %s" % (expected_moves, actual_moves)

    print("\nTest of Bear.get_move passed")


def test_lion_init():
    print("\nTesting Lion's __init__ method")
    l = Lion((5, 3))

    assert 'x' in l.__dict__ and 'y' in l.__dict__, \
        "x and y instance variables not set. Did you call the parent's constructor?"

    assert l.x == 5 and l.y == 3, \
        "x and y not set correctly. Did you call the parent's constructor?"

    print("\nTest of Lion.__init__ passed")

def test_lion_str():
    print("\nTesting Lion's __str__ method")
    l = Lion((0, 0))

    # test __str__ 10 times to make sure it doesn't vary
    for _ in range(10):
        assert str(l) == "L", \
            "Lion should always return 'L' from __str__"

    print("\nTest of Lion.__str__ passed")

def test_lion_get_color():
    print("\nTesting Lion's get_color method")

    l = Lion((0, 0))

    expected_color = "goldenrod3"

    # test 10 times to make sure it doesn't vary
    for _ in range(10):
        assert l.get_color() == expected_color, \
            "Lion always return 'goldenrod3' from get_color"

    print("\nTest of Lion.get_color passed")

def test_lion_eat():
    print("\nTesting Lion's eat method")
    l = Lion((0, 0))

    print("\tTesting scenario where new Lion is asked to eat")
    # test 10 times to make sure it doesn't vary
    for _ in range(3):
        assert l.eat() == False, \
            "Lion should not have eaten."

    print("\tTesting scenario where lion fights then is asked twice about eating")
    l.fight("0")

    assert l.eat() == True, \
        "Lion should have eaten right after a fight."

    assert l.eat() == False, \
        "Lion just ate. Shouldn't try to eat again."

    print("\tTesting scenario where lion fights twice then is asked to eat twice.")
    l.fight("0")
    l.fight("0")

    assert l.eat() == True, \
        "Lion should have eaten right after a fight."

    assert l.eat() == False, \
        "Lion just ate. Shouldn't try to eat again."

    print("\nTest of Lion.eat passed")

def test_lion_fight():
    print("\nTesting Lion's fight method")
    l = Lion((0, 0))

    print("\tTesting attack against a Bear")

    # try with several different opponents to make sure it always returns
    # scratch
    for _ in range(3):
        actual_attack = l.fight("B")
        assert actual_attack == Attack.ROAR, \
            "Lion did a %s against a bear when it should have done Attak.ROAR" % actual_attack

    print("\tTesting attack against a Cheetah")
    actual_attack = l.fight("0")
    assert actual_attack == Attack.POUNCE, \
        "Lion did %s against a non-Bear critter ('0') instead of Attack.POUNCE" \
        % actual_attack

    actual_attack = l.fight("3")
    assert actual_attack == Attack.POUNCE, \
        "Lion did %s against a non-Bear critter ('3') instead of Attack.POUNCE" \
        % actual_attack

    print("\tTesting attack against another critter (Torero?)")
    actual_attack = l.fight("T")
    assert actual_attack == Attack.POUNCE, \
        "Lion did %s against a non-Bear critter ('T') instead of Attack.POUNCE" \
        % actual_attack

    print("\nTest of Lion.fight passed")

def test_lion_get_move():
    print("\nTesting Lion's get_move method")
    l = Lion((0, 0))

    neighbors = {Direction.NORTH: "B",
                 Direction.EAST: "L",
                 Direction.SOUTH: "0",
                 Direction.WEST: "3"}

    print("\tTesting movement of new Lion for 40 turns.")

    expected_moves = ([Direction.SOUTH] * 5 + [Direction.WEST] * 5 \
        + [Direction.NORTH] * 5 + [Direction.EAST] * 5) * 2

    actual_moves = [l.get_move(neighbors) for _ in range(40)]

    pairs = zip(expected_moves, actual_moves)

    for i, (expected, actual) in enumerate(pairs):
        assert expected == actual, \
            "In turn %d, expected %s but got %s" % (i+1, expected, actual)

    print("\nTest of Lion.get_move passed")


def test_cheetah_init():
    print("\nTesting Cheetah's __init__ method")
    c = Cheetah((5, 3), 3)

    assert 'x' in c.__dict__ and 'y' in c.__dict__, \
        "x and y instance variables not set. Did you call the parent's constructor?"

    assert c.x == 5 and c.y == 3, \
        "x and y not set correctly. Did you call the parent's constructor?"

    print("\nTest of Cheetah.__init__ passed")

def test_cheetah_str():
    print("\nTesting Cheetah's __str__ method")

    print("\tTesting with newly created Cheetahs having hunger levels 0 to 9")
    for i in range(10):
        c = Cheetah((0, 0), i)
        actual_string = str(c)
        assert actual_string == str(i), \
            "Expected '%d' but got '%s'" % (i, actual_string)

    print("\nTest of Cheetah.__str__ passed")

def test_cheetah_get_color():
    print("\nTesting Cheetah's get_color method")

    # test with different hunger levels to make sure it doesn't vary
    for i in range(10):
        c = Cheetah((0, 0), i)
        actual_color = c.get_color()
        assert actual_color == "red", \
            "Expected: 'red'\nGot: " + actual_color

    print("\nTest of Cheetah.get_color passed")

def test_cheetah_eat():
    print("\nTesting Cheetah's eat method")

    print("\tTesting scenario with new Cheetah having hunger level 0")
    c = Cheetah((0, 0), 0)

    # test 3 times to make sure it doesn't vary
    for _ in range(3):
        assert c.eat() == False, \
            "Cheetah should not have eaten."

    print("\tTesting scenario with new Cheetah having hunger level 1 asked to eat 3 times")
    c = Cheetah((0, 0), 1)
    assert c.eat() == True, "Cheetah didn't eat when asked the first time."
    assert c.eat() == False, "Cheetah ate when asked the second time."
    assert c.eat() == False, "Cheetah ate when asked the third time."

    print("\tTesting scenario with new Cheetah having hunger level 3 asked to eat 5 times")
    c = Cheetah((0, 0), 3)

    for i, expected_eat in enumerate([True, True, True, False, False]):
        actual_eat = c.eat()
        assert actual_eat == expected_eat, \
            "Time %d: Expected %s, Got %s" % (i+1, expected_eat,
                                              actual_eat)

    print("\nTest of Cheetah.eat passed")

def test_cheetah_fight():
    print("\nTesting Cheetah's fight method")

    print("\tTesting attack with new cheetah having hunger level 0")
    c = Cheetah((0, 0), 0)
    actual_attack = c.fight("B")
    assert actual_attack == Attack.POUNCE, \
        "Cheetah did %s instead of Attack.POUNCE when NOT hungry." \
        % actual_attack

    actual_attack = c.fight("L")
    assert actual_attack == Attack.POUNCE, \
        "Cheetah did %s instead of Attack.POUNCE when NOT hungry." \
        % actual_attack

    print("\tTesting attack with new cheetah having hunger level 1")
    c = Cheetah((0, 0), 1)
    actual_attack = c.fight("B")
    assert actual_attack == Attack.SCRATCH, \
        "Cheetah did %s instead of Attack.SCRATCH when hungry." \
        % actual_attack

    actual_attack = c.fight("L")
    assert actual_attack == Attack.SCRATCH, \
        "Cheetah did %s instead of Attack.SCRATCH when hungry." \
        % actual_attack

    print("\tTesting scenario where hungry cheetah eats, is no longer hungry, and then fights.")
    c.eat()
    actual_attack = c.fight("B")
    assert actual_attack == Attack.POUNCE, \
        "Cheetah did %s instead of Attack.POUNCE when NOT hungry." \
        % actual_attack

    print("\nTest of Cheetah.fight passed")

def test_cheetah_get_move():
    print("\nTesting Cheetah's get_move method")
    c = Cheetah((0, 0), 0)

    neighbors = {Direction.NORTH: "B",
                 Direction.EAST: "L",
                 Direction.SOUTH: "0",
                 Direction.WEST: "3"}

    print("\tTesting movement of new Cheetah for 15 turns.")

    move_set = set()
    for i in range(15):
        curr_move = c.get_move(neighbors)
        if i % 3 == 0:
            print("\t\tNew direction found to be %s" % curr_move)
            lead_move = curr_move
            move_set.add(curr_move)
        else:
            assert curr_move == lead_move, \
                "Unexpected change to %s after %d moves." % (curr_move, i%3)

    assert len(move_set) > 1, \
        "Highly unlikely event occured: same random direction picked 5 straight times."

    print("\nTest of Cheetah.get_move passed")


if __name__ == "__main__":
    run_tests()
