class SessionLayer:
    def __init__(self, name):
        self.name = name

    def send(self, data):
        return f"{self.name} processing: Session Established ({data})"

    def receive(self, data):
        return f"{self.name} received: {data}"