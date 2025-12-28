


class Demo:
    count = 0

    @staticmethod
    def inc():
        Demo.count += 1
        print(f"Class count is now {Demo.count}")
    @staticmethod
    def add(a, b):
        print(f"Sum is {a + b}")
Demo.inc()
Demo.inc()

Demo.add(2, 2)