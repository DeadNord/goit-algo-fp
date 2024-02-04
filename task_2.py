import turtle


class PythagorasTree:
    def __init__(self, recursion_level):
        self.recursion_level = recursion_level
        self.turtle = turtle.Turtle()
        self.setup_turtle()

    def setup_turtle(self):
        self.turtle.screen.bgcolor("lightblue")
        self.turtle.left(90)
        self.turtle.color("brown")
        self.turtle.speed(0)
        self.turtle.up()
        self.turtle.goto(0, -200)
        self.turtle.down()

    def draw_tree(self, branch_length, level):
        if level == 0:
            self.turtle.color("green")
            self.turtle.begin_fill()
            self.turtle.forward(branch_length)
            self.turtle.right(90)
            self.turtle.forward(branch_length)
            self.turtle.right(90)
            self.turtle.forward(branch_length)
            self.turtle.right(90)
            self.turtle.forward(branch_length)
            self.turtle.right(90)
            self.turtle.end_fill()
            self.turtle.color("brown")
        else:
            self.turtle.forward(branch_length)
            self.turtle.left(45)
            self.draw_tree(branch_length / (2**0.5), level - 1)
            self.turtle.right(90)
            self.draw_tree(branch_length / (2**0.5), level - 1)
            self.turtle.left(45)
        self.turtle.backward(branch_length)

    def start_drawing(self):
        self.draw_tree(100, self.recursion_level)
        turtle.done()


def main():
    recursion_level = int(
        input("Please, enter the recursion level for the Pythagoras tree: ")
    )
    pythagoras_tree = PythagorasTree(recursion_level)
    pythagoras_tree.start_drawing()


if __name__ == "__main__":
    main()
