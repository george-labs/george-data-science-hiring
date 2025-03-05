# Task 4: Production ready model

## Description

In this final iteration, you will create a robust function to wrap your model and refactor the code for better readability, maintainability, and consistent output, ensuring easier integration with downstream processes.

### What you need to do:

- **Create a model wrapper** - Create a robust function that wraps your machine learning model.
- **Ensure consistency** – Verify that all transformations align with previously defined requirements (input and output data structure).
- **Handle edge cases** – Ensure the model handles potential edge cases correctly.
- **Improve code structure** – Refactor the code to follow clean coding principles (modularity, clarity, and maintainability).
- **Persist work using git** – Use Git for version control, ensuring proper commits, clear messages, and structured repository organization.

This step ensures that you can write clean, maintainable, and robust code, which is crucial for real-world machine learning applications.

## Available resources

Below you find following components:

1. **Input data structure** - Description of the format and structure of input data.
2. **Output data structure** - Expected format of the model's output.

### 1. Input data structure
```
input
 |-- user_id: string (nullable = true)
 |-- category: string (nullable = true)
 |-- month: string (nullable = true)
```

### 2. Output data structure
```
output
 |-- user_id: string (nullable = true)
 |-- category: string (nullable = true)
 |-- month: string (nullable = true)
 |-- predicted_amount: double (nullable = true)
```