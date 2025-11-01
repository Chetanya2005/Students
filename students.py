class Students:
    def __init__(self, name, roll, mark):
        self.name = name
        self.roll = roll
        self.mark = mark

    def display(self):
        print(f"name: {self.name}, roll: {self.roll}, mark: {self.mark}")


if __name__ == "__main__":
    student = Students("chetanya", 22, 300)
    student.display()
