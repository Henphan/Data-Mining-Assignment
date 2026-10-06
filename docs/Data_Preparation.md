## Data Preparation
Date: 2/10/2026
### Findings from manual examination of the data:
1. service is nullable
2. Large difference in scale between 'dur' and 'stcpb'
3. Mix of categorical, numerical data, and binary data
### Irrelevant Attributes
- The goal of this step is to find any irrelevant or redudntant attribute
- I am under the impression that building a correlation matrix will help us solve this
- Manual investigation of each attribute:
    - 'label' is the target label and not a predictor
    - 'dwin' and 'swin' seem duplicated.
    - 'tcprtt' is the sum of 'synack' and 'ackdat'
    - 'dur' and 'rate' are correlated, high 'rate' --> low 'dur'

    - 'ct_dst_src_ltm' is just 'ct_dst_ltm' and 'ct_src_ltm' combined.
    - 'is_ftp_login' is mostly zeros.
    - 'ct_ftp_command' is mostly zeros.
    - 'is_sm_ips_ports' is most zeros.
    - 'trans_depth' is most zeros.
    - 'service' is mostly empty
- I will now perform closer inspection on the mentioned attributes:
    - 'dwin' and 'swin' are highly correlated, but not identical.
    - 'is_ftp_login' is mostly zeros.
    - 'ct_ftp_command' is mostly zeros.
    - 'ct_ftp_command' seems to be correlated with 'is_ftp_login'.
    - 'trans_depth' is most zeros.
    - 'service' is mostly '-' and 'dns'.
- I will now perform a simple correlation matrix on these values
    - I will specifically find the Pearson (linear) correlation coefficient
    ![Correlation Matrix](../out/numeric_corr.png)
    - From this matrix, pairs that I should investigate include:
        - sbytes + spkts (0.98)
        - dbytes + dpkts (0.95)
        - sloss + spkts (0.99)
        - sloss + sbytes (1.00)
        - dloss + dpkts (0.96)
        - dloss + dbytes (0.99)
        - dwin + swin (0.96)
        - synack + tcprtt (0.95)
        - ct_src_dport_ltm + ct_dst_ltm (0.97)
        - ct_ftp_cmd + is_ftp_login (1.00) --> not identical
        - ct_src_ltm + ct_src_dport_ltm (0.95)
        - ct_srv_src + ct_srv_dst (0.98)
- Most of these correlations are not enough for me to remove attributes with certainty. 
- Attributes that can be removed from the training dataset with certainty are:
    - tcprrt --> sum of synack and ackdat
    - label --> target label
- While certain pairs present very-high correlation values, we cannot safely assume that one is relevant while the other isn't, these will be further investigated in the feature extraction.
### Missing Values
- The goal of this step is to identify all attributes/instsances with missing entries.
- I will need to produce a number which represents how many entries are missing.
- Decide on the actions to take to handle these missing entries.
- The two that stand out to me are 'service' and 'state', as these both can take on a value of '-' which I presume to be synonymous with a NULL value.
- Running df.isna().sum() tells us that there is no missing entry within the dataset.
- As there appears to be no missing entries within the Test-data-1.xlsx, we will skip this step for now.
### Duplicates
- The goal of this step is to identify duplicated attributes or instances within the dataset.
- This involves me checking whether any attribute is duplicated, i.e. two identical columns.
- I am also tasked with checking for any duplicated instances, i.e. two identical rows.
- Using df[df.duplicated()] returns us with a new DataFrame of 74 rows, i.e. there are 74 rows which are not unique.
- I have found that a certain row is duplicated 40 times, while other rows are only duplicated 8 times are less. 
- I have decided to investigate this specific row more indepth, to determine whether this duplication is valid or is it redundant.
- I have investigated the index of each of the duplicated row, to determine whether they are spread throughout the dataset or not.
- Having these duplicated rows clump together could indicate that these rows are duplicated data-entry or collection errors.
- As they spread throughout the dataset, they could very well be independent data records.
- Therefore, I have decided to keep every duplicated rows for now.
#### Training-data.xlsx
- Running it on this dataset, it is reported that 'is_ftp_login' and 'ct_ftp_cmd' are duplicated. This is could very well be concidence.
### Data Types
- Based on the feature description, the datasets are mixed-typed, meaning that it contains both numerical and categorical data.
- From the current dataset, we only have three categorical attributes, they are 'proto', 'service', and 'state'.
- proto:
    - Within Test-data-1.xlsx, proto has 131 unique values.
    - Feature description does not explicitly state the possible values.
- service:
    - Within Test-data-1.xlsx, service has 13 unique values.
    - Feature description indicates that 'service' can take on at least 8 values.
- state:
    - Within Test-data-1.xlsx, service has 7 unique values.
    - However, the feature description indicates that state has at least 16 different unique values.
- My initial instinct is to binarise these data into a vector, i.e. perform one-hot-encoding on them.
- However, I am unaware of how efficient it would be for attributes with a large number of unique values, e.g. proto.
- I have decided that I will still use one-hot-encoding, for now, and not worry too much about the size of proto's vectors.
- sklearn.preprocessing.OneHotEncoder()
    - "Encode categorical features as one-hot numeric array."
    - This transformer takes in an array-like of integers or strings.
    - It will then create a binary column for each category and returns a sparse matrix.
    - handle_unknown: tells the transformer how to handle unknown categories during 'transform'.
#### Note:
- From my understanding, this step will be performed onto the dataset once the data splitting to prevent data leakage, the event of validation data being used to train the model, which cause cause bias within the accuracy.