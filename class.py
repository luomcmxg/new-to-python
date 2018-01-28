import scipy


class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.population += 1

    def die(self):
        print("{} is being detroyed".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} robots working".format(
                Robot.population))

    def say_hi(self):
        print("Greetings, my masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        print("We have {:d} robots.".format(cls.population))


class SuperRobot(Robot):
	# pass
    def __init__(self, Robot):
        self.name = Robot.name
        print("\nUpgrading to Super {}".format(self.name))


droid1 = Robot("R2-D2")
droid1.say_hi()
droid1.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
droid2.how_many()

droid1 = SuperRobot(droid1)
droid2 = SuperRobot(droid2)
print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.\n")


droid1.die()
droid2.die()

SuperRobot.how_many()
print(type(droid1), type(droid2), type(Robot), type(int))

