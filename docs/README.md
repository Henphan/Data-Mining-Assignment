# COMP3009 - Data Mining
## Final Assignment
The two main programs within this ZIP file are:
1. run.ipynb
2. analysis.ipynb
## run.ipynb:
This is the Python Jupyter Notebook which contains the entire pipeline which loads the data, preprocesses the data, cross-validate training, classifier evaluation, and final model training and prediction.
### How to run it?:
- The note book can simply be run from top to bottom if you want to see the performance of each of the three classifiers.
- However, if you only want to see the performance of the final model:
    1. Run the two cells with the dependencies.
    1. Run the three cells that load the three datasets.
    2. Run all of the cells under Data Preparation
    3. Run the cell under Cross Validation Setup
    4. Run the cell with make_knn_pipeline()
    5. 
## analysis.ipynb:
This is also a Python Jupyter Notebook, but it contains the exploratory code. This Notebook was used to help me explore and examine the dataset, generating graphs, confusion matrices, statistics that would help justify choices that I have made throughout the assignment, mainly the preprocessing step.