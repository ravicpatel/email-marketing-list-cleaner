import pandas as pd
import numpy as np
import  re
import streamlit as st

# Define Streamlit app
st.title("Merging all email")

st.write("This app merges all email from all author and output a csv file with one single column of unique merged email ids")

st.write("create one consolidated list of emails till date")

st.write("Criteria for any email to be eligible to get in this list is as follows:")

st.write("1. They have to be from all author")

st.write("2. Duplicate should be removed")



# Create input fields for the user and upload file


uploaded_file = st.file_uploader("Upload only CSV file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # cleaning email

    # Step 1: Clean email

    def clean_email_address(email):
        # Define a regex for a valid email pattern
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        # Check if the email matches the pattern
        if re.match(email_pattern, str(email)):
            return email
        else:
            return np.nan
    
    # List of the email columns to clean
    email_columns_to_clean = ['column_email_1', 'column_email_2', 'column_email_3', 'column_email_4', 'column_email_5', 'column_email_6', 'column_email_7', 'column_email_8', 'column_email_9', 'column_email_10']

    # Loop to clean email
    for col in email_columns_to_clean:
        cleaned_col_name = col + '_cleaned'
        df[cleaned_col_name] = df[col].apply(clean_email_address)
    
    # Step 2 filtering 

    df_filtered_email = df[(df['column_filter_1'] == 'required_value_1') & (~df['column_filter_2'].isin(['required_value_2','required_value_3']))]

    # Step 3 Melting and merging in one columns

    df_melted_emails = df_filtered_email[[col + '_cleaned' for col in email_columns_to_clean]].melt(value_name = 'merged_email_cleaned').dropna(subset = ['merged_email_cleaned'])

    # Step 4 drop duplicates

    df_melted_emails = df_melted_emails[['merged_email_cleaned']].drop_duplicates().reset_index(drop=True)

    # Create a CSV buffer for download
    csv = df_melted_emails.to_csv(index=False)

    # Create download button
    st.download_button(
        label = "Download all merged emails as csv",
        data = csv,
        file_name = "Merge_emails_2024_09_26.csv",
        mime = "text/csv"
    )

else:
    st.write("file not uploaded")

