#David Rauch
#Baylor College of Medicine
#07/14/2023

import pandas as pd
from sklearn.metrics import roc_curve, auc, roc_auc_score

def auc_roc(df, model, filt=None):
    """
    Gets all the data needed for ROC plotting and AUC analysis, alongside a proportion of PLP/BLB CLINVAR labels
    
    arguments:
     df (Pandas dataframe): the dataframe which has the raw scores and the truth label
     model (string):  the model which we are analyzing
     filt (string): the model to filter out NA values in the dataset. If none is passed, then the filter is the model (so we
     only use the model's values). If any NA values exist for the filter model, they will be dropped
    Outputs:
     fpr: false positive rate
     tpr: true positive rate
     thresholds: the model thresholds calculated by scikitlearn
     auc: the model AUC
     PB_prop: a string representng a fraction of #PLP / #BLB labels 

     sample use:
     auc_roc(example_df, model1, filter_model)
    """

    #check if a special filter is called. Otherwise, just use the model filter
    if filt==None:
        filt=model

    #filter our NA values and get AUC score
    df_filt = df[~df[filt].isna()]
    #df_filt = df[~df["MetaRNN-Indel"].isna()]
    auc = roc_auc_score(df_filt["truth"], df_filt[model])

    # get ROC curve values
    fpr, tpr, threshold = roc_curve(df_filt["truth"], df_filt[model])

    #Give the number of PLP compared to BLB
    nPLP = str(df_filt["truth"].value_counts()[1])
    nBLB = str(df_filt["truth"].value_counts()[0])
    PB_prop = nPLP + "/" + nBLB

    return fpr, tpr, threshold, auc, PB_prop