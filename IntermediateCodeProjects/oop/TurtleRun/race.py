from turtle_runner import TurtleRunner


class Race:

    COLORS = ["red", "blue", "green", "yellow", "black"]

    POSITION = [(0, 0, 0), (90, 60, 90), (90, 60, 90),
                (90, 120, 90), (90, 120, 90)]

    def __init__(self):
        self.runners = [TurtleRunner(self.COLORS[0]), TurtleRunner(self.COLORS[1]),
                        TurtleRunner(self.COLORS[2]), TurtleRunner(self.COLORS[3]), TurtleRunner(self.COLORS[4])]
        self.down_or_up = 0

    def set_runners_position(self):
        i = 0
        for position in self.POSITION:
            self.runners[i].get_runner().backward(350)
            if self.down_or_up == 0:
                self.down_or_up = 1
                self.runners[i].get_runner().left(position[0])
                self.runners[i].get_runner().forward(position[1])
                self.runners[i].get_runner().right(position[2])
            else:
                self.down_or_up = 0
                self.runners[i].get_runner().right(position[0])
                self.runners[i].get_runner().forward(position[1])
                self.runners[i].get_runner().left(position[2])
            i += 1

    def start_race(self):
        winner = ""
        end = False
        while not end:
            for i in range(5):
                self.runners[i].get_runner().forward(self.runners[i].get_velocity())
            for i in range(5):
                if self.runners[i].get_runner().pos()[0] >= 325:
                    winner = self.runners[i].get_color()
                    end = True
                    break
        return winner
