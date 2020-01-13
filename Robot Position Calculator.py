import random

# Field Element Constants
bar_length = 114.25  # Distance From The Interior
middle_bar = (55.625, 58.625)  # Start and End Positions Of The Middle Handle
exact_middle = sum(middle_bar) / 2


# Takes Up To 3 bot Objects And Returns All Possible Position(s) For The GUI to Display
def balance_bots(bots):
    if len(bots) > 3:
        print("Too Many Bots, Only 3 Supported")
    else:
        # Case 1 - Only One Robot
        if len(bots) == 1:
            return bots, exact_middle

        # Case 2 - Two Robots
        elif len(bots) == 2:
            return static_equilibrium(bots)

        # Case 3 - Three Robots (Really Just Two With One In The Middle
        return static_equilibrium(bots)


# Generates All Working Static Equilibriums For the Bar
def static_equilibrium(bots):
    ranges = []
    for i in range(0, int(middle_bar[0])):
        if len(bots) == 2:
            unknown_distance = (i * bots[0].weight) / bots[1].weight
            if 0 < unknown_distance < bar_length and bar_length - unknown_distance > exact_middle:
                ranges.append((i, round(bar_length - unknown_distance)))

        # For 3 Robots, Balance The Two Lightest And Put The Heaviest in The Middle
        else:
            bots.sort(key=lambda x: x.weight, reverse=False)  # Sort By Weight

            unknown_distance = (i * bots[0].weight) / bots[1].weight
            if 0 < unknown_distance < bar_length and bar_length - unknown_distance > exact_middle:
                ranges.append((i, exact_middle, round(bar_length - unknown_distance)))

    return bots, ranges


# Weight : Weight of The Robot (In Lbs)
# Frame : Frame Perimeter For The Robot In Inches(L, W, H)
class RobotData:

    def __init__(self, weight, frame, team_number):
        self.weight = weight
        self.frame = frame
        self.number = team_number


def gen_bots(num) -> [RobotData]:
    bots = []
    for i in range(num):
        bots.append(RobotData(
            weight=random.randrange(100, 125),
            frame=(random.randrange(0, 12), random.randrange(0, 12), random.randrange(0, 12)),
            team_number=random.randrange(0, 9900)
        ))
    return bots


def test():
    x = balance_bots(gen_bots(2))

    for i in x[0]:
        print("Team {}, {} lbs".format(i.number, i.weight))

    print("Possible Equilibriums: ", "\n", *x[1])


test()
