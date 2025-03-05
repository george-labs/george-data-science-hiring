# Task 1: Evaluating an expert machine learning model

## Description

You are given an expert-based machine learning model that predicts rent values.

### What you need to do:

 - **Understand the target feature** – Identify what the model is predicting.
 - **Select an appropriate error metric** – Choose a suitable performance metric for evaluation.
 - **Implement evaluation logic** – Write code to calculate the selected error metric.
 - **Assess model performance** – Analyze and interpret the model’s results.

This exercise tests your ability to critically evaluate a machine learning model before making modifications.

## Available resources

Below you find following components:

1. **The Expert Model** – A predefined model that outputs a fixed rent estimate.
2. **The `train_test_split` function** – A function that splits data into training and test sets.
3. **Data available during development** – The dataset used to train and validate the model.
4. **Data available during production** – The dataset the model will encounter in a real-world setting

### 1. The Expert Model
```python
import pandas as pd

class Expert:
    """
    A simple expert-based model that provides rent value for a house.
    
    This expert assumes that the rent should be 500 EUR regardless of input features.
    """
    
    def __init__(self):
        """
        Initializes the Expert model. No parameters are needed.
        """
        self.estimated_rent = 500  # Expert's rent estimate in EUR
    
    def fit(self, X: pd.DataFrame, y: pd.Series):
        """
        This model does not require training. The method is included for compatibility.
        
        If an updated average estimate is needed, please contact the housing market analyst.
        
        Parameters:
        X : pd.DataFrame
            Feature data (not used in this model).
        y : pd.Series
            Target values (not used in this model).
        """
        pass  # No fitting required

    def predict(self, X: pd.DataFrame):
        """
        Predicts the rent based on the expert's estimation.
        
        Parameters:
        X : pd.DataFrame
            Feature data (not used in this model).
        
        Returns:
        pd.Series
            A pandas Series of predicted rent values, each set to 500 EUR.
        """
        return pd.Series([self.estimated_rent] * len(X), index=X.index)
```

### 2. The `train_test_split` function.

```python
def train_test_split(X: pd.DataFrame, y: pd.Series):
    """
    Splits data into training and test sets.
    
    The first 6 observations go to the training set, the last 3 to the test set.
    
    Parameters:
    X : pd.DataFrame
        The input dataframe containing features.
    y : pd.Series
        The target variable.
    
    Returns:
    tuple:
        X_train (pd.DataFrame), 
        y_train (pd.Series), 
        X_test (pd.DataFrame), 
        y_test (pd.Series)
    """
    X_train = X.iloc[:6,:]
    y_train = y.iloc[:6]
    X_test = X.iloc[-3:,:]
    y_test = y.iloc[-3:]
    
    return X_train, y_train, X_test, y_test
```


### 3. Data available during development.
```python
df_dev = pd.DataFrame(
    columns=["user_id", "category", "date", "amount"],
    data=[
        ["user_1", "RENT", "2024-01-01", 700.0],
        ["user_1", "RENT", "2024-02-01", 900.0],
        ["user_1", "RENT", "2024-03-01", 700.0],

        ["user_2", "RENT", "2024-01-01", 900.0],
        ["user_2", "RENT", "2024-02-01", 1100.0],
        ["user_2", "RENT", "2024-03-01", 900.0],

        #...

        ["user_n", "RENT", "2024-01-01", 800.0],
        ["user_n", "RENT", "2024-02-01", 1000.0],
        ["user_n", "RENT", "2024-03-01", 800.0],
    ],
)   
```

### 4. Data available during production.
```python
df_prod = pd.DataFrame(
    columns=["user_id", "category", "month"],
    data=[
        ["user_1", "RENT", "2024-04-01",],
    ],
)  
```