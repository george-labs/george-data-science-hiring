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
            Feature data (not used in this model, only the count of instances is considered).
        
        Returns:
        pd.Series
            A pandas Series of predicted rent values, each set to 500 EUR.
        """
        return pd.Series([self.estimated_rent] * len(X), index=X.index)


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
        X_train (pd.DataFrame), y_train (pd.Series), X_test (pd.DataFrame), y_test (pd.Series)
    """
    X_train = X.iloc[:6,:]
    y_train = y.iloc[:6]
    X_test = X.iloc[-3:,:]
    y_test = y.iloc[-3:]
    
    return X_train, y_train, X_test, y_test


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

df_prod = pd.DataFrame(
    columns=["user_id", "category", "date"],
    data=[
        ["user_1", "RENT", "2024-04-01",],
    ],
)  