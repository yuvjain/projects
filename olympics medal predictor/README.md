# Olympic Medal Predictor

This project involves predicting the number of Olympic medals a country is likely to win based on various features like GDP, population, and previous Olympic performance. The model is implemented using Python and machine learning algorithms to forecast the medal counts.

## Project Overview

The Olympic Medal Predictor aims to analyze various socio-economic factors, historical performance data, and country-specific details to predict the number of medals a country might win in the Olympics. This project leverages data analysis, feature engineering, and machine learning techniques to build an accurate prediction model.

### Key Features

- **Data Preprocessing:** Cleaned and transformed the dataset for better model accuracy.
- **Exploratory Data Analysis:** Performed detailed EDA to understand the relationship between features and medal counts.
- **Modeling:** Implemented regression and classification models to predict medal counts.
- **Evaluation:** Evaluated model performance using metrics like R-squared, Mean Squared Error (MSE), and accuracy.

## Project Structure

- `medals_predictor.ipynb`: Jupyter Notebook containing the code for data preprocessing, EDA, model training, and evaluation.
- `teams.csv`: The dataset containing information about countries, their GDP, population, and past Olympic performances.
- `models/`: Directory to store trained models (if applicable).
- `plots/`: Directory for saving visualizations and evaluation plots (if applicable).

## How to Run the Project

1. **Clone the repository:**
    ```bash
    git clone <https://github.com/yuvjain/projects/tree/main/olympics%20medal%20predictor>
    cd <olympics medal predictor>
    ```

2. **Install the required dependencies:**
    Ensure you have Python and the necessary libraries installed. You can install the required libraries using:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn
    ```

3. **Run the Jupyter Notebook:**
    Open the Jupyter notebook and run the cells sequentially to preprocess the data, train the model, and evaluate its performance:
    ```bash
    jupyter notebook medals_predictor.ipynb
    ```

## Dependencies

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Dataset
The dataset includes various features such as:

- GDP of the country
- Population
- Historical Olympic performance
- Number of athletes sent to the Olympics These features are used to predict the number of medals a country is likely to win.

## Model Architecture
- Linear Regression: A regression model used to predict the total number of medals.
- Decision Tree: A classification model used to predict the medal category (Gold, Silver, Bronze).
- Random Forest Regression: An ensemble method used to improve accuracy by combining multiple decision trees.

## Results
The project predicts medal counts with reasonable accuracy, considering both linear and non-linear relationships between features and the target variable. Evaluation metrics include R-squared and Mean Squared Error (MSE) for regression models.

## Visualization
- Heatmaps to show correlations between features.
- Bar plots for medal distribution across countries.
- Line plots to visualize the trend in medal wins over time.
- 
## Future Improvements
- Feature Engineering: Add more features like average age of athletes or training facilities data to improve predictions.
- Advanced Algorithms: Experiment with more complex algorithms like Gradient Boosting Machines (GBM) or XGBoost.
- Deployment: Deploy the model as a web application using Flask or Django to make predictions for upcoming Olympics.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Developed by Yuv Jain.  
For more projects, visit my [GitHub profile](https://github.com/yuvjain).
