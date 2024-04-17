# Gearbox Fault Prediction Web Application

This project implements a web application for predicting gearbox faults based on temperature, pressure, vibration, oil quality, noise, and hours run. The prediction model is built using a Naive Bayes classifier trained on historical gearbox data.

## Getting Started

Follow these instructions to set up and run the Gearbox Fault Prediction Web Application.

### Prerequisites

Make sure you have Python installed on your system. You can download and install Python from the [official Python website](https://www.python.org/downloads/).

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Kedar-dave/EleconML.git
    ```

2. Navigate to the project directory:

    ```bash
    cd gearbox-fault-prediction
    ```

3. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. Access the application in your web browser. By default, it should be available at [http://localhost:8501](http://localhost:8501).

3. Use the sliders to input values for temperature, pressure, vibration, oil quality, noise, and hours run.

4. Click the "Predict" button to see the prediction result.

### File Structure

- `app.py`: Contains the main Streamlit application code.
- `gs_naive_bayes.joblib`: Pre-trained Naive Bayes model saved using joblib.
- `requirements.txt`: List of Python packages required for the project.

## Contributing

Contributions are not welcome!