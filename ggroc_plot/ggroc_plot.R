#David Rauch
#Baylor College of Medicine MHG
#07/11/2023

### 

#create_roc_plot(data)
# creates an ROC plot from some data, formatted with the model, AUC, fpr, tpr, thresholds,
# and model_AUC (a combined column of model and AUC score)

# Inputs:
# data (dataframe): the dataframe with the ROC data to be plotted (read from either csv, excel, etc)

# Returns:
# an ROC plot of the models (a list of 9 values)

library("ggpubr")
library('tidyverse')
library('readxl')

ggroc_plot <- function(data, fig_title="ROC Curve(s)", legend_x=10, legend_y=10) {
  
  roc_plot <- roc_plot_better <- ggplot(data = data, mapping=aes(x = fpr, y = tpr, color = reorder(model_AUC, -AUC))) +
    geom_line() +
    labs(title = fig_title, x = "False Positive Rate", y = "True Positive Rate", color = "Model") + 
    theme_bw() + 
    theme(plot.title = element_text(hjust = 0.5),
          legend.position = c(legend_x, legend_y), 
          legend.background = element_rect(color = "black"),
          legend.box.margin = margin(10, 10, 10, 10))
  
  return(roc_plot)
}