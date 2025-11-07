# BS444 - Introduction to Machine Learning Final Project

## Overview

This project implements a machine learning pipeline to predict biological age from gut microbiome composition data. The system uses ensemble regression models to estimate age based on microbial DNA fragment counts from fecal samples.

## Features

- **Multiple Model Comparison**: Evaluates Random Forest, Gradient Boosting, and XGBoost regressors
- **Interactive GUI**: Displays model performance metrics in a Tkinter-based interface
- **Comprehensive Evaluation**: Reports Mean Absolute Error (MAE) and R² scores for each model

## Dataset

The project uses a dataset containing gut microbiome composition data from 4,274 individuals:

- **Ages.csv**: Contains sample identifiers and corresponding biological ages
- **data.csv**: Contains sample identifiers and DNA fragment counts for approximately 3,200 different microorganism species

## Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn
- xgboost
- lightgbm
- tkinter (usually included with Python)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd BS444-IntrotoML-FinalProject
```

2. Install required dependencies:
```bash
pip install pandas numpy scikit-learn xgboost lightgbm
```

## Usage

1. Ensure that `Ages.csv` and `data.csv` are in the project directory
2. Run the classifier:
```bash
python classifier.py
```

The script will:
- Load and merge the datasets
- Preprocess the data (handle missing values, convert to numeric)
- Split data into training (80%) and testing (20%) sets
- Train three regression models
- Evaluate performance metrics
- Display results in a GUI window

## Model Performance

The script evaluates three ensemble regression models:
- **Random Forest Regressor**
- **Gradient Boosting Regressor**
- **XGBoost Regressor**

Performance metrics (MAE and R²) are displayed in the GUI interface after training.

## Project Structure

```
BS444-IntrotoML-FinalProject/
├── classifier.py      # Main script with model training and evaluation
├── Ages.csv          # Age labels dataset
├── data.csv          # Microbiome composition dataset
├── README.md         # Project documentation
└── LICENSE           # License file
```

## License

See LICENSE file for details.
