import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal infection of cherry trees caused by the fungus "
        f"Podosphaera clandestina.\n"
        f"* The fungus causes visual changes in the leaves that can be observed with "
        f"the naked eye. These visual changes can be used to detect powdery mildew.\n"
        f"* Within the cherry industry this fungus is extremely destructive, if not caught and treated "
        f"it can have a severe impact on the crop yield, and by extention income, as such a cheap "
        f"and easy way to check images is a much needed solution. "
        f"If the initial visual analysis returns a positive result, the farmers can then move forwards with "
        f"further DNA based testing, and treatment, minimisng losses.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset contains two folders of images each containing 2104 images, one folder has clean, "
        f"uninfected leaves, the other has leaves with visable powdery mildew present. ")

    st.write(
        f"* For more in depth information, you can check out the associated "
        f"[README](https://github.com/Swewi/milestone-project-mildew-detection-in-cherry-leaves/blob/main/README.md) file.")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy "
        f"from one that is infected with powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or infected. "
        )
