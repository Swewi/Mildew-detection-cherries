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
    st.success(
        f" The following series of images displays how the model utilized the training "
        f"and validation datasets to improve its ability to predict whether an uploaded "
        f"image shows a healthy leaf or one infected with powdery mildew."
    )
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.warning(
        f" As you can see from these images the model is a good fit for both "
        f"the training and validation sets. Both the accuracy and the loss curves "
        f"are tracking in a similar pattern."
    )
    st.write("") 
    model_loss_acc = plt.imread(f"outputs/{version}/model_loss_acc.png")
    st.image(model_loss_acc, caption='Model Loss and Accuracy')
    st.write("---")

    st.write("### Confusion Matrix")
    st.info(
        f" A confusion matrix is a great way of to see how well the model has worked "
        f"with the test data, it is a good gauge as to whether the model will work "
        f"with real world data."
    )
    confusion_matrix = plt.imread(f"outputs/{version}/confusion_matrix.png")
    st.image(confusion_matrix, caption='Confusion Matrix')
    st.warning(
        f" As you can see this confusion matrix shows that the model correctly classified "
        f"all the images within the test set."
    )
    st.write("---")

    st.write("### Classification Report")
    st.info(
        f" The classification report shown here is focused on Precision, Recall, "
        f"and the f1 score, these are usefull measures of how well the model fits "
        f"the data.  In many ways the f1 value is the most important because it is "
        f"a combination of both the precision and the recall, as such it reflects "
        f"the model fit exceptionally well."
    )
    classification_report_heatmap = plt.imread(f"outputs/{version}/classification_report_heatmap.png")
    st.image(classification_report_heatmap, caption='Classification Report')
    st.warning(
        f" As you can see from this classification report the models f1 score is "
        f"extremely high. Indicating that the model worked exceptionally well with the "
        f"test data."
    )
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.info(
        f" The client requires the model to achieve at least 97% accuracy to meet "
        f"their needs.  The generalised performance of the test data has achieved "
        f"an accuracy of 1.0000, this equates to 100%, and as such suggests a "
        f"perfect fit."
    )
    st.warning(
        f"There is no such thing as a perfect fit, therefore this model will need further "
        f"data to truely test the model."
    )
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))
