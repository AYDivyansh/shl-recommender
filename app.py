import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("shl_assessments.csv")

def get_recommendations(query):
    query = query.lower()
    # Match the first skill word and filter by duration if specified
    results = df[
        df["Description"].str.lower().str.contains(query.split()[0], na=False) & 
        (df["Duration"] <= int(query.split()[-2]) if "mins" in query else True)
    ].head(10)
    return results

# Streamlit app
st.title("SHL Assessment Recommender")
query = st.text_area("Enter your query (e.g., 'Java developers, 40 mins')")
if st.button("Recommend"):
    if query:
        results = get_recommendations(query)
        st.table(results[["Name", "URL", "RemoteTesting", "AdaptiveIRT", "Duration", "TestType"]])
    else:
        st.write("Please enter a query!")

# API endpoint simulation
if "api" in st.query_params:
    query = st.query_params["query"]
    results = get_recommendations(query)
    st.json(results.to_dict(orient="records"))