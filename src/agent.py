class Agent:
    def __init__(self, start, path):
        self.position = start
        self.path = path

    def move(self):
        for step in self.path:
            self.position = step
            print(f"Agent moved to {self.position}")