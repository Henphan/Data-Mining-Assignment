## Cross-Validation
- Select between:
    - ShuffleSplit
    - KFold
    - StratifiedKFold
- Decide on the number of splits for each

6/10/2026:
- I ran the k-NN with the following context:
    - preprocessing:
        - dropped: tcprtt, is_ftp_login, dwin
        - one-hot-encoded: state, service, proto
        - scaling: z-score norm
    - hyperparameter search:
        - k = [1,3,7,11,17,21]
- CV accuracy:
```
    Cross-validation accuracy by k (training set):
    k  mean_cv_acc  std_cv_acc
    7     0.994145    0.000310O
    11     0.994131    0.000326
    17     0.993987    0.000350
    21     0.993850    0.000460
    3     0.993514    0.000323
    1     0.991731    0.000541
    Best k: 7
```
- ran the Decision Tree with the following context:
    - preprocessing:
        - dropped: tcprtt, is_ftp_login, dwin
        - one-hot-encoded: state, service, proto
        - scaling: z-score norm
    - hyperparameter search:
        - criterion = gini, entropy
        - minimum split = 1 to 10
- CV accuracy:
```
({'dt__criterion': 'gini', 'dt__min_samples_split': 4},
 np.float64(0.9940557047931666))
```
- I ran the Naive Bayes classifier with the following context:
    - preprocessing:
        - dropped: tcprtt, is_ftp_login, dwin
        - one-hot-encoded: state, service, proto
        - scaling: z-score norm
    - hyperparameter search:
        - var_smoothing = [1e-12, 1e-11, 1e-10, 1e-9, 1e-8, 1e-7, 1e-6]
- CV accuracy:
```
{'nb__var_smoothing': 1e-06}
0.4430046487958525
```