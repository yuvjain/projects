# Gold Price Predictor

This project involves building a machine learning model to predict the price of gold based on various economic factors. The model is implemented using Python and utilizes algorithms like Linear Regression to forecast future gold prices.

## Project Overview

Gold price prediction is a crucial aspect for investors, traders, and analysts who are involved in the precious metals market. This project uses historical data and other economic indicators to train a model that predicts gold prices accurately. The dataset includes features such as the price of gold, oil prices, stock market indices, and more.

### Key Features

- **Data Preprocessing:** Cleaned and transformed the dataset for optimal model performance.
- **Exploratory Data Analysis:** Conducted visualizations and analysis to understand correlations between variables.
- **Modeling:** Implemented and compared multiple regression models to identify the most accurate prediction model.
- **Evaluation:** Assessed model performance using metrics like R-squared and Mean Squared Error (MSE).

## Project Structure

- `gld_price_predictor.ipynb`: Jupyter Notebook containing the full code, including data preprocessing, EDA, model training, and evaluation.
- `gld_price_data.csv`: The dataset used for training and testing the model, including economic indicators and historical gold prices.
- `models/`: Directory to store trained models (if applicable).
- `plots/`: Directory for saving visualizations and evaluation plots (if applicable).

## How to Run the Project

1. **Clone the repository:**
    ```bash
    git clone <https://github.com/yuvjain/projects/tree/main/gold%20price%20predictor>
    cd <gold price predictor>
    ```

2. **Install the required dependencies:**
    Ensure you have Python and the necessary libraries installed. You can install the required libraries using:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn
    ```

3. **Run the Jupyter Notebook:**
    Open the Jupyter notebook and run the cells sequentially to preprocess the data, train the model, and evaluate its performance:
    ```bash
    jupyter notebook gld_price_predictor.ipynb
    ```

## Dependencies

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Dataset
The dataset contains historical data on gold prices along with other features such as oil prices, stock market indices, exchange rates, and more. These features are used to train the machine learning model for accurate predictions.

## Model Architecture
- Linear Regression: A basic regression model used to establish a relationship between gold prices and other variables.
- Random Forest Regression: A more advanced model used for capturing non-linear relationships in the data.
- Evaluation: The models were evaluated using R-squared, Mean Squared Error (MSE), and other relevant metrics.

## Results
The project successfully predicts gold prices with a high degree of accuracy. The performance of the models is compared, and the best model is chosen based on evaluation metrics.

## Visualization
- Heatmaps and pair plots to show correlations between features.
- Time-series plots to visualize trends in gold prices over time.
- Residual plots to assess the performance of regression models.

## Future Improvements
- Hyperparameter Tuning: Further optimize model performance through hyperparameter tuning.
- Feature Engineering: Explore additional economic indicators or transform existing features for better predictions.
- Deployment: Deploy the model as a web application using Flask or Django for real-time gold price prediction.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Developed by Yuv Jain.  
For more projects, visit my [GitHub profile](https://github.com/yuvjain).
