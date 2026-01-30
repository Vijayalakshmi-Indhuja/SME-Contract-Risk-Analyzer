import streamlit as st
import pdfplumber

from utils import get_entities, split_clauses
from risk_logic import check_risk, overall_risk, explain_clause

st.title("SME Contract Risk Analyzer")
st.write("Upload a service contract to understand potential risks.")

uploaded_file = st.file_uploader("Upload contract file", type=["pdf", "txt"])

def read_contract(file):
    if file.type == "application/pdf":
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text()
        return text
    else:
        return file.read().decode("utf-8")

if uploaded_file is not None:
    contract_text = read_contract(uploaded_file)

    st.subheader("Extracted Contract Details")
    entities = get_entities(contract_text)
    st.json(entities)

    clauses = split_clauses(contract_text)

    st.subheader("Risk Analysis")
    total_score = 0

    for clause in clauses:
        risk, score = check_risk(clause)
        total_score += score

        with st.expander(f"Clause Risk: {risk}"):
            st.write(clause)
            st.write("Explanation:", explain_clause(clause))

    final_risk = overall_risk(total_score)

    st.subheader("Overall Contract Risk")
    st.write(final_risk)
    st.write("Risk Score:", total_score)
