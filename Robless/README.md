# Traffic Exercise Project

## Overview
This repository contains the implementation of a traffic simulation system with training and regulation processes. The project aims to model, analyze, and optimize traffic flow using machine learning techniques.

## Table of Contents
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Training Process](#training-process)
- [Regulation Process](#regulation-process)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

## Installation
```bash
# Clone the repository
git clone https://github.com/Robless08/Robless_Traffic_exercise.git

# Navigate to the project directory
cd Robless_Traffic_exercise

# Install dependencies
pip install -r requirements.txt
```

## Project Structure
```
├── data/                # Training and test datasets
├── models/              # Trained model files
├── src/                 # Source code
│   ├── training/        # Training implementation
│   ├── regulation/      # Traffic regulation algorithms
│   └── utils/           # Utility functions
├── configs/             # Configuration files
├── tests/               # Test cases
└── README.md            # This file
```

## Training Process

### Data Preparation
The training process begins with preparing traffic data that includes:
- Vehicle flow rates
- Traffic density metrics
- Signal timing information
- Environmental conditions

Data should be placed in the `data/` directory with the following format:
- CSV files with timestamps
- Each row representing a traffic state
- Features properly normalized

### Model Training
The training pipeline consists of the following steps:

1. **Data Loading and Preprocessing**
   ```python
   python src/training/preprocess.py --config configs/preprocess_config.yaml
   ```

2. **Feature Engineering**
   - Temporal features extraction
   - Spatial correlations
   - Traffic pattern identification

3. **Model Training**
   ```python
   python src/training/train.py --config configs/training_config.yaml
   ```
   
4. **Hyperparameter Optimization**
   ```python
   python src/training/optimize.py --config configs/hyperparams_config.yaml
   ```

5. **Model Evaluation**
   ```python
   python src/training/evaluate.py --model models/traffic_model.pkl
   ```

### Performance Metrics
The training process evaluates models based on:
- Mean Absolute Error (MAE)
- Root Mean Square Error (RMSE)
- Traffic flow improvement percentage
- Average waiting time reduction

## Regulation Process

### Traffic State Monitoring
The regulation system continuously monitors:
- Current traffic density
- Vehicle queue lengths
- Signal timing efficiency
- Special conditions (accidents, construction, events)

### Decision Making
The traffic regulation process follows these steps:

1. **State Assessment**
   ```python
   python src/regulation/assess.py --input live_data.json
   ```

2. **Optimization Calculation**
   - Determines optimal signal timing
   - Calculates lane allocation
   - Prioritizes emergency vehicles

3. **Regulation Implementation**
   ```python
   python src/regulation/implement.py --strategy adaptive
   ```

4. **Feedback Collection**
   - Records real-time performance metrics
   - Updates model if necessary

### Regulation Strategies
The system supports multiple regulation strategies:
- Fixed-time control
- Adaptive signal control
- Coordinated corridor management
- Incident response protocols

## Configuration
All aspects of training and regulation can be configured through YAML files in the `configs/` directory:

```yaml
# Example training_config.yaml
model:
  type: "lstm"
  layers: 3
  hidden_units: 128
  dropout: 0.2

training:
  batch_size: 64
  epochs: 100
  learning_rate: 0.001
  early_stopping: true
  patience: 10

data:
  train_split: 0.8
  validation_split: 0.1
  test_split: 0.1
  features:
    - "flow_rate"
    - "density"
    - "speed"
    - "time_of_day"
    - "day_of_week"
```

## Usage Examples

### Running a Complete Training Cycle
```bash
# Run the entire training pipeline
python src/main.py --mode training --config configs/full_training.yaml
```

### Implementing Traffic Regulation
```bash
# Start the regulation system
python src/main.py --mode regulation --config configs/regulation.yaml
```

### Visualizing Results
```bash
# Generate performance visualizations
python src/utils/visualize.py --data results/performance_metrics.csv --output visuals/
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.