from turtle import Turtle
move_dist = 20


class Snake:

    def __init__(self):
        self.segments = [Turtle(shape="square") for _ in range(3)]
        self.head = self.segments[0]
        self._create_snake()

    def _create_snake(self):
        for seg in self.segments:
            self._add_segment(seg)

    def _add_segment(self, seg):
        x_cord = 0
        seg.color("white")
        seg.penup()
        seg.goto(x_cord, 0)
        x_cord -= 20

    def extend(self):
        new_segment = Turtle(shape="square")
        self.segments.append(new_segment)
        self._add_segment(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_dist)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.__init__()
