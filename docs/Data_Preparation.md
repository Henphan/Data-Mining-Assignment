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
