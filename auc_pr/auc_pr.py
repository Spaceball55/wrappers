#David Rauch
#Baylor College of Medicine MHG
#7/27/2023

import pandas as pd
from sklearn.metrics import auc, precision_recall_curve

def auc_pr(df, model, filt=None):
    """
    Gets a model's precision-recall values for graphing and the corresponding precision-recall curve AUC values

    Inputs:
     df (pandas dataframe): the dataframe containing the model's scores and a column labeled "truth" containing the values 1 for 
     a positive classification and 0 for a negative classification

     model (string): the name of the column containing the model's scores

     filt (string): the name of the model by which you are filter out NA values in the dataset. If none is passed, then the filter
     is the model (so we only use the model's values)

    Outputs:
     precision (list): a list of the precision values for the model
     recall (list): a list of the recall values for the model
     thresholds (list): a list of the threshold values for the model
     pr_auc (float): a float representing the AUC of the precision-recall curve
    """
    
    # check if a filter is specified; if not, the default filter is the model being analyzed
    if filt == None:
        filt = model

    #filter our NA values and get AUC-PR score
    df_filt = df[~df[filt].isna()]

    #get precision and recall to plot pr curve
    precision, recall, thresholds  = precision_recall_curve(df_filt["truth"], df_filt[model])

    #get the AUC of precision recall curve
    pr_auc = auc(recall, precision)

    return precision, recall, thresholds, pr_auc
