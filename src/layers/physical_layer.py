class PhysicalLayer:
    def __init__(self, name):
        self.name = name

    def send(self, data):
        return f"{self.name} converting to Bit Stream: {data}"

    def receive(self, data):
        return f"{self.name} received Bit Stream: {data}"