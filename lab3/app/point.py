class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, point):
        if abs(self.x - point.x) < 3 and abs(self.y - point.y) < 3:
            return True
        else:
            return False
