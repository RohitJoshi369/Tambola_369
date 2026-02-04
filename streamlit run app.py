import streamlit as st
import pandas as pd

# -------------------------------
# App Configuration
# -------------------------------
st.set_page_config(
    page_title="Bhagat Search",
    layout="centered"
)

st.title("🔍 Bhagat Search Application")
st.write("Upload Excel file and search by Bhagat name")

# -------------------------------
# File Upload
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload Excel File (.xlsx)",
    type=["xlsx"]
)

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)

        # Required columns
        required_columns = [
            "House Name",
            "Room Number",
            "Bhagat Name 1",
            "Bhagat Name 2"
        ]

        if not all(col in df.columns for col in required_columns):
            st.error("Excel file does not contain required columns.")
            st.stop()

        st.success("Excel file loaded successfully")

        # -------------------------------
        # Search Section
        # -------------------------------
        bhagat_name = st.text_input("Enter Bhagat Name")

        if st.button("Search"):
            if bhagat_name.strip() == "":
                st.warning("Please enter a Bhagat name")
            else:
                # Case-insensitive search
                result = df[
                    (df["Bhagat Name 1"].str.lower() == bhagat_name.lower()) |
                    (df["Bhagat Name 2"].str.lower() == bhagat_name.lower())
                ]

                if result.empty:
                    st.error("Bhagat not found")
                else:
                    st.success("Bhagat found")
                    st.dataframe(result, use_container_width=True)

    except Exception as e:
        st.error(f"Error reading file: {e}")

else:
    st.info("Please upload an Excel file to begin")
