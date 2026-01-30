# SME Contract Risk Analyzer

This project is a prototype tool for small and medium enterprises (SMEs) to analyze service contracts and detect risky clauses.

## Features
- Upload PDF or TXT contracts
- Extract parties, dates, amounts, and jurisdiction
- Identify key clauses: termination, payment, indemnity, auto-renewal, etc.
- Assign Low / Medium / High risk
- Simple clause explanations for SMEs
- Rule-based, fully explainable logic

## Tech Stack
- Python
- spaCy (NLP)
- Streamlit (UI)
- pdfplumber (PDF extraction)

## How to Run
1. Clone this repository
2. Install dependencies: 

       pip install -r requirements.txt
   
       python -m spacy download en_core_web_sm
   
4. Run the app:
   
       streamlit run app.py
   
6. Upload a sample contract and view analysis.

## Note
This is a prototype for demonstration purposes only. It is not legal advice.
