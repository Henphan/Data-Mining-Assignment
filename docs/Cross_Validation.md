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
    - hyperparameters:
        - k = 7
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