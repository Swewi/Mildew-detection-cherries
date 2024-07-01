import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Hypothesis and Validation")

    st.success(
        f"* **Hypothesis 1** - That infected cherry leaves will have clear visual signs "
        f"of infection across the surface of a leaf, that will differentiate them from "
        f"healthy leaves. \n\n"
    )
    
    st.info(
        f"* Visually a healthy cherry leaf is a uniform rich green colour, it has a tapered, "
        f"eliptical shape, and evenly serated leaf edges. \n"
        f"* Whereas a leaf that is infected with powdery mildew will have a lattice of white fibers "
        f"covering its surface. They will lose the healthy green and instead take on a sickly yellow "
        f"colour, and as a consequence of these factors will often be smaller and irregularly shaped. \n\n"
    )

    st.warning(
        f"* The model successfully detected the differences between infected and healthy leaves, "
        f"learning to differentiate and generalise to make accurate predictions. \n"
        f"* A good model trains its ability to predict classes on a batch of data without adhering "
        f"too closely to that specific set. This way, the model generalises and reliably predicts "
        f"future observations because it didn't merely 'memorise' the relationships between features "
        f"and labels seen in the training dataset but learned the general patterns from features to labels. \n\n"
    )

    st.success(
        f"* **Hypothesis 2** - An Image Montage shows that typically an infected leaf is covered in "
        f"a web of white fibers. Average Image, Variability Image and Difference between Averages "
        f"studies did not reveal any clear pattern to differentiate one from another. \n\n"
    )

    st.warning(
        f"* The analysis of the Image Montage confirmed that the visual differences between "
        f"infected and healthy leaves were subtle and not easily distinguishable using average "
        f"and variability images alone. \n"
        f"* Despite this, the model demonstrated a perfect F1 score of 1.0, indicating that it "
        f"successfully learned to identify the specific features distinguishing infected from "
        f"healthy leaves, even when these features were not apparent in simple image comparisons. \n"
        f"* This indicates that the model was not misled by the visual complexity of the infected "
        f"leaves but instead captured the underlying patterns necessary for accurate classification. \n\n"
    )

    st.write(
        f"* For more in depth information, you can check out the associated "
        f"[README](https://github.com/Swewi/milestone-project-mildew-detection-in-cherry-leaves/blob/main/README.md) file.")
