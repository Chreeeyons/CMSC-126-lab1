class ApplicationLayer:
    def __init__(self, name):
        self.name = name

    def send(self, data):
        return f"{self.name} processing: Application Data ({data})"

    def receive(self, data):
        return f"{self.name} received: {data}"