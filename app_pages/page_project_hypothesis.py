import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Hypothesis and Validation")

    st.success(
        f"* That infected cherry leaves will have clear visual signs of infection across the "
        f"surface of an leaf, that will differentiate them from healthy leaves. \n\n"
    

        f"* An Image Montage shows that typically an infected leaf is covered in a web of white fibers. "
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."

    )

    st.info(
        f"* Visually a healthy cherry leaf is a uniform rich green colour, it has a tapered, "
        f"eliptical shape, and evenly serated leaf edges. \n"
        f"* Whereas a leaf that is infected with powdery mildew will have a lattice of white fibers "
        f"covering its surface. They will lose the healthy green and instead take on a sickly yellow "
        f"colour, and as a consequence of these factors will often be smaller and irregularly shaped. \n\n"
    )
