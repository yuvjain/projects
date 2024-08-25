
# Breast Cancer Prediction using Neural Networks

This project focuses on building a deep learning model to predict whether a tumor is benign or malignant based on various features extracted from breast cancer data. The model is implemented using Python and TensorFlow, utilizing a neural network for classification.

## Project Overview

Breast cancer is a significant health concern worldwide. Early detection is crucial for improving survival rates. This project aims to classify breast tumors as benign or malignant using machine learning techniques. The dataset used contains various features that help in distinguishing between the two categories.

### Key Features

- **Data Preprocessing:** Cleaned and normalized data for better model performance.
- **Modeling:** Implemented a neural network using TensorFlow and Keras for binary classification.
- **Evaluation:** Evaluated the model's performance using metrics like accuracy, precision, recall, and F1-score.
- **Visualization:** Included visualizations such as loss and accuracy curves to monitor model training.

## Project Structure

- `DL_Project_1_Breast_Cancer_Classification_with_NN.ipynb`: The Jupyter notebook containing the code for data processing, model training, and evaluation.
- `data.csv`: The dataset used for training and testing the model, containing various features related to breast cancer.
- `models/`: Directory to store trained models (if applicable).
- `plots/`: Directory for saving visualizations and evaluation plots (if applicable).

## How to Run the Project

1. **Clone the repository:**
    ```bash
    git clone <https://github.com/yuvjain/projects/tree/main/breast%20cancer%20detection>
    cd <breast cancer detection>
    ```

2. **Install dependencies:**
    Ensure you have Python and the necessary libraries installed. You can install the required libraries using:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Jupyter Notebook:**
    Open the Jupyter notebook and run the cells sequentially to preprocess the data, train the model, and evaluate its performance:
    ```bash
    jupyter notebook DL_Project_1_Breast_Cancer_Classification_with_NN.ipynb
    ```

## Dependencies

- Python 3.x
- TensorFlow
- Keras
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

You can install these dependencies using:
```bash
pip install tensorflow keras pandas numpy matplotlib seaborn scikit-learn
