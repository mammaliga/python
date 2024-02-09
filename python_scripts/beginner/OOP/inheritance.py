class Mother:
    def __init__(self, eye_color, hair_color, hair_type):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"


class Father:
    def __init__(self, eye_color, hair_color, hair_type):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"


class Child(Mother, Father):
    def __init__(self, eye_color, hair_color, hair_type):
        super().__init__(eye_color, hair_color, hair_type)
