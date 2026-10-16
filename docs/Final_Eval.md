# Final Evaluation
Scores:
```
Test 1: 0.7800926312973397
Test 2: 0.8908153944261561
```
Classifier: kNN
Hyperparameters: k = 7
Random seed: 67
Preprocessing:
- Columns that were dropped: ```['tcprtt', 'service', 'proto', 'is_ftp_login', 'dwin', 'smean', 'dmean']```
- Columns that were log transformed: ```['trans_depth', 'response_body_len', 'sbytes', 'sloss', 'spkts', 'dinpkt']```
- The rest of the numerical columns were standardised
- One-hot-encoding done on: ```state```


## Final freeze on classifiers
### k-NN:
```
              precision    recall  f1-score   support

           0       1.00      0.98      0.99     38777
           1       0.99      1.00      1.00    107077

    accuracy                           0.99    145854
   macro avg       0.99      0.99      0.99    145854
weighted avg       0.99      0.99      0.99    145854

Cross-validation accuracy by k (training set):
 k  mean_cv_acc  std_cv_acc
 7     0.993055    0.000389
11     0.992828    0.000489
 3     0.992801    0.000513
17     0.992431    0.000537
21     0.992184    0.000568
 1     0.991032    0.000363
Best k: 7
```

### DT:
```
              precision    recall  f1-score   support

           0       0.99      0.99      0.99     38777
           1       1.00      1.00      1.00    107077

    accuracy                           0.99    145854
   macro avg       0.99      0.99      0.99    145854
weighted avg       0.99      0.99      0.99    145854

{'dt__criterion': 'entropy', 'dt__min_samples_split': 2}
0.9943025210352641
```

### NB:
```
 precision    recall  f1-score   support

           0       0.97      0.96      0.97     38777
           1       0.98      0.99      0.99    107077

    accuracy                           0.98    145854
   macro avg       0.98      0.97      0.98    145854
weighted avg       0.98      0.98      0.98    145854
{'nb__var_smoothing': 0.01}
0.9821053982148177
```