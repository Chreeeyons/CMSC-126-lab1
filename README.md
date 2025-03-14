# OSI Model Replica

This project is a simulation of the 7-layer OSI model, demonstrating how data is encapsulated and de-encapsulated as it passes through each layer of the model.

## Project Structure

```
osi-model-replica
├── src
│   ├── __init__.py
│   ├── main.py
│   └── layers
│       ├── __init__.py
│       ├── application_layer.py
│       ├── presentation_layer.py
│       ├── session_layer.py
│       ├── transport_layer.py
│       ├── network_layer.py
│       ├── data_link_layer.py
│       └── physical_layer.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd osi-model-replica
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the OSI model simulation, execute the following command:
```
python src/main.py
```

This will initialize the OSI model layers and simulate the process of data encapsulation and de-encapsulation, displaying the output for each layer.

## Contributing

Feel free to submit issues or pull requests if you would like to contribute to this project.