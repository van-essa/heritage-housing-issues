import streamlit as st

def page_4_hypothesis_and_validation_body():

    st.write("### Project Hypothesis and Validation")
	
    st.info(
    f"**1.** We suspect houses with vast `square footing` may have had "
    f"a higher `sales price`: **Correct**. \n "
    f"- The correlation study on the **House Sale Price Study** supports that; "
    f"there is a strong correlation between the two. \n\n"

    f"**2.** We suspect that between houses with similar `square footing`, "
    f"those with a more recent `Year Built` date may have had a higher "
    f"`sales price`: **Correct**.\n "
    f"- The correlation study on the **House Sale Price Study** supports that; "
    f"there is a moderate correlation between the two. "
    f"Also noteworthy: houses with a more recent `Year Built` date are "
    f"usually higher in `Overall Quality` which has stronger correlation "
    f"to `Sale Price`.\n\n"

    f"**3.** We suspect that between houses with similar `square footing` and "
    f"`year built` to date, those with a more recent `Remodel` date may "
    f"have had a higher `sale price`: **Correct**.\n"
    f"- The correlation study on the **House Sale Price Study** supports that; "
    f"there is a weak to moderate correlation between the two. "
    f"Also noteworthy: there is a relationship between houses with a more "
    f"recent `Remodel` date being higher in `Overall Quality`\n\n"

    f"**4.** We suspect that between houses with similar `square footing`, "
    f"those with higher `quality and condition` scores may have had a  "
    f"higher `sales price`: **Correct**.\n "
    f"- The correlation study on the **House Sale Price Study** supports "
    f"that; there is a strong correlation between the two variables."
    )

# The code above was copied from the Churnometer Project from Code Institute with some adjustments