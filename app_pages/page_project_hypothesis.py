import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Hypothesis and Validation")

    st.success(
        f"* That cherry leaves will have clear visual signs of infection across the "
        f"surface of an infected leaf, that will differentiate them from healthy leaves. \n\n"
    

        f"* An Image Montage shows that typically a parasitised cell has purplish marks across it. "
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."

    )

    st.info(
        f"* Visually a healthy cherry leaf is a uniform rich green colour, it has a tapered, "
        f"eliptical shape, and evenly serated leaf edges. \n"
        f"* Whereas a leaf that is infected with powdery mildew have a lattice of white fibers covering "
        f"its surface, they will lose the healthy green and instead take on a sickly yellow colour, and as a "
        f"consequence of these factors will often be smaller and irregularly shaped. \n\n"
    )

    st.success(
        f"* An Image Montage will show a selection of images, the user can select which "
        f"image set to view."
    )

    st.info(
        f"* "
    )
