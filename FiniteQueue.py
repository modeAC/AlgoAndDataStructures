class Queue:
    def __init__(self, volume):
        self.volume = volume
        self.items = list()

    def push(self, item):
        self.items.append(item)
        if self.volume < len(self.items):
            self.items.pop(0)

    def shift(self):
        if self.items != []:
            self.items.pop(0)

    def get_queue(self):
        for item in self.items:
            if item is not None:
                print(item, end=' ')
