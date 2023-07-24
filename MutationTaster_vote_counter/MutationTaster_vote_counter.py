#David Rauch
#Baylor College of Medicine MHG
#07/21/2023

import pandas as pd
import numpy as np

def MutationTaster_vote_counter(df):
    """
    Takes MutationTaster Output and finds all of the model classification, and turns them into votes for either the 
    "pathogenic" or "benign" class

    arguments:
        df (pandas dataframe): the dataframe containing the MutationTaster data
    returns:
        pivot_df (pandas dataframe): a dataframe containing the rows "#CHROM, Position, REF, ALT, and the aggregated MutationTaster vote"
    """
    #add values to REF and ALT so we don't get weird NA value errors

    columns_to_replace = ['REF', 'ALT']
    df[columns_to_replace] = df[columns_to_replace].fillna('.')
    
    #group the input df by the columns "#CHROM", "Position", "REF", "ALT", and "Mutation_Taster_Prediction", counting the 
    #instances of "Mutation_Taster_Prediction" in each group
    grouped_df = df.groupby(["#CHROM", "Position", "REF", "ALT","Mutation_Taster_Prediction"]).size().reset_index(name='Count_Predictions')

    # Pivot the DataFrame to create separate columns for counts of C values (0 and 1) for each group
    pivot_df = grouped_df.pivot(index=["#CHROM", "Position", "REF", "ALT"], columns='Mutation_Taster_Prediction', values='Count_Predictions').reset_index()

    # Rename the columns for better readability
    ##I'm not sure why we need to have deleterious there, but we do or else the code won't work
    pivot_df.rename(columns={"Benign": 'Count_Benign','Deleterious': 'Count_Deleterious', 'Pathogenic': 'Count_Pathogenic'}, inplace=True)

    #Replace NAN values with 0
    pivot_df["Count_Benign"] = pivot_df["Count_Benign"].replace(np.NAN, 0)
    pivot_df["Count_Pathogenic"] = pivot_df["Count_Pathogenic"].replace(np.NAN, 0)

    #loop through the rows in pivot_df to get the votes
    for idx, row in pivot_df.iterrows():
        #more false negatives than false positives for MutationTaster, so we account for this
        if pivot_df.iloc[idx,4] > pivot_df.iloc[idx,6]:
            pivot_df.loc[idx, "MutationTaster_vote"] = "benign"
        
        #if pathogenic vote is greater, choose pathogenic to account for higher false negative rate (this will increase false positives)
        elif pivot_df.iloc[idx,4] <= pivot_df.iloc[idx,6]:
            #print('patho')
            pivot_df.loc[idx, "MutationTaster_vote"] = "pathogenic"
    
    # Drop unnecesary rows
    pivot_df.drop(columns=["Count_Benign", "Count_Deleterious", "Count_Pathogenic"], inplace=True)

    #drop the . values added to REF and ALT to align it with the other dfs
    pivot_columns_to_replace = ['REF', 'ALT']
    pivot_df[pivot_columns_to_replace] = pivot_df[pivot_columns_to_replace].replace('.', np.nan)
    
    return pivot_df