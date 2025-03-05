# Task 2: Replacing the expert model with an average model

## Description

In this iteration, you will replace the previous expert-based model with a simple average model (most preferably using linear regression). This model will not use any features. It will only learn the average rent from the training data and predict this value for all inputs.

### What you need to do:

- **Implement linear regression** – Set up a linear regression model that predicts rent based solely on the average value in the training data.
- **Train the model** – Fit the model without using any features. Only the target variable (rent).
- **Make predictions** – The model should always output the average rent from the training set.
- **Evaluate performance** – Compare the new model’s performance against the expert model using appropriate metrics.

This step ensures a data-driven approach while maintaining a simple baseline for comparison before incorporating additional features.