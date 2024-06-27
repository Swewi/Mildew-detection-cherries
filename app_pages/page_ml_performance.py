import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    version = 'v1'

    st.write("### Dataset breakdown")
    st.info(
        f" In order to use this dataset within the machine learning environment we break the data "
        f"into three sets named: Train, Validation, and Test, across both the healthy and infected images. "
        f"These sets are divided in a 70, 10, 20 split, as visualualised in the pie charts below."
    )
    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Cherry leaf dataset breakdown')
    st.write("---")

    st.write("### Model History")
    st.info(
        f" As we fit the model to the data we need a way to track the results in order to further optimise "
        f"and refine the model. The goal is to create a model that is accurate and generalises well to "
        f"unseen data, ensuring that it performs reliably on new, real-world inputs."
    )
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    
    st.write("") 
    model_loss_acc = plt.imread(f"outputs/{version}/model_loss_acc.png")
    st.image(model_loss_acc, caption='Model Loss and Accuracy')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))