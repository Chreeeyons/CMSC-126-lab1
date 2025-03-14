class OSILayer:
    def __init__(self, name):
        self.name = name

    def send(self, data):
        return f"{self.name} processing: {data}"

    def receive(self, data):
        return f"{self.name} received: {data}"


def osi_simulation(data):
    from layers.application_layer import ApplicationLayer
    from layers.presentation_layer import PresentationLayer
    from layers.session_layer import SessionLayer
    from layers.transport_layer import TransportLayer
    from layers.network_layer import NetworkLayer
    from layers.data_link_layer import DataLinkLayer
    from layers.physical_layer import PhysicalLayer

    layers = [
        ApplicationLayer("Application Layer"),
        PresentationLayer("Presentation Layer"),
        SessionLayer("Session Layer"),
        TransportLayer("Transport Layer"),
        NetworkLayer("Network Layer"),
        DataLinkLayer("Data Link Layer"),
        PhysicalLayer("Physical Layer")
    ]
    
    print("\nEncapsulation:")
    for layer in layers:
        data = layer.send(data)
        print(data)
        print()  
    
    print("\nDe-encapsulation:")
    for layer in reversed(layers):
        data = layer.receive(data)
        print(data)
        print()  


if __name__ == "__main__":
    osi_simulation("Python is awesome!")