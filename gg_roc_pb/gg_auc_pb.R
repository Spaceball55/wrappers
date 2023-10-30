# David Rauch
# Baylor College of Medicine MHG
# 7/14/2023

##

# gg_auc_pb
# uses ggplot to generate a figure of the AUC and the ratio of PLP/BLB for each model tested

#Usage:
# gg_auc_pb(data)
#NOTE: the function returns a ggplot object, to display the plot, use the print function! E.g. print(plot)

#Arguments:
# data (dataframe): the dataframe only with the model, AUC, and PLP/BLB - each model recorded only once
# fig_title (string): the title of the figure
#Returns:
# a box plot that records the AUC value as the y-value


library("ggpubr")
library('tidyverse')
library('readxl')

gg_auc_pb <- function(data, fig_title="AUCs and PLP/BLB"){
  auc_pb_plot <- ggplot(data, aes(x=reorder(model, -AUC), y=AUC, label = paste0(round(AUC, 3), " (", `PLP/BLB`, ")"))) + 
    geom_col(aes(fill = reorder(model, -AUC))) + 
    geom_text(size = 4, vjust = -1) + 
    coord_cartesian(ylim = c(0.80, 1.00)) + 
    labs(title = fig_title, x = "Model") +
    guides(fill = "none") +
    theme_bw() + 
    theme(axis.text.x = element_text(angle = 60, hjust = 1),
          plot.title = element_text(hjust = 0.5))
  
  return(auc_pb_plot)
}
