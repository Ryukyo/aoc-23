from collections import Counter

hands_bets = open("day7.txt").read().rstrip()

def hand_type(hand):
    c = Counter(hand)
    counts = [0] if (jokers := c.pop("*", 0)) == 5 else sorted(c.values())
    # The most efficient use of a joker is always as the most common non-joker card
    counts[-1] += jokers
    match counts:
        case *_, 5:
            return 7
        case *_, 4:
            return 6
        case *_, 2, 3:
            return 5
        case *_, 3:
            return 4
        case *_, 2, 2:
            return 3
        case *_, 2:
            return 2
    return 1


def solve(data):
    ws = [l.split() for l in data.split("\n")]
    return sum(
        rank * bid
        for rank, (*_, bid) in enumerate(
            sorted(
                (hand_type(hand), *map("*23456789TJQKA".index, hand), int(bid))
                for hand, bid in ws
            ),
            1,
        )
    )

# Part 1
print(solve(hands_bets))

# Part 2
print(solve(hands_bets.replace("J", "*")))