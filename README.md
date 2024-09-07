# Self-Organizing Maps for Credit Card Applications

## Overview

This project aims to analyze a dataset of credit card applications using Self-Organizing Maps (SOM), a type of unsupervised neural network. The goal is to visualize and cluster the data to identify patterns and anomalies in credit card applications, which can provide valuable insights for credit risk assessment and decision-making processes.

## Dataset

The dataset used in this project is named `Credit_Card_Applications.csv`. It contains various features related to credit card applications, including customer demographics and application details. The dataset is structured as follows:

- **CustomerID**: Unique identifier for each customer
- **A1 to A14**: 14 attributes related to the customer and their application, such as age, income, debt, and credit history
- **Class**: Target variable indicating the status of the application (e.g., approved or rejected)

The dataset provides a comprehensive view of credit card applications, allowing for in-depth analysis and pattern discovery.

## Requirements

To run the notebook and reproduce the results, you will need the following software and libraries:

- Python 3.x
- NumPy: A fundamental library for scientific computing in Python
- Pandas: A powerful data manipulation and analysis library
- Matplotlib: A plotting library for creating static, animated, and interactive visualizations in Python
- Scikit-learn: A machine learning library that provides simple and efficient tools for data mining and data analysis
- MiniSom: A minimalistic and efficient implementation of the Self-Organizing Maps (SOM) algorithm

You can install the required libraries using pip:

```bash
pip install numpy pandas matplotlib scikit-learn minisom
```

## Usage

1. **Clone the repository or download the Jupyter Notebook and the dataset.**
2. **Open the `SOM.ipynb` notebook in Jupyter.**
3. **Run the cells sequentially to execute the SOM analysis.**

The notebook provides a step-by-step guide on how to preprocess the data, train the SOM model, and visualize the results. It includes explanations of the code and the underlying concepts of Self-Organizing Maps.

## Results

The notebook generates various visualizations of the clustered data, allowing for in-depth analysis of patterns in credit card applications. Key insights can be drawn from the clustering results, such as:

- **Identifying groups of customers with similar characteristics**
- **Detecting anomalies or outliers in the data**
- **Analyzing the distribution of approved and rejected applications across clusters**
- **Gaining a better understanding of the factors influencing credit card application decisions**

These insights can inform decision-making processes in credit risk assessment and help financial institutions make more informed decisions when evaluating credit card applications.

## Contributing

Contributions to this project are welcome! If you have suggestions for improvements, additional features, or bug fixes, feel free to open an issue or submit a pull request. When contributing, please adhere to the project's coding style and guidelines.
