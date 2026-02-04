# SME Contract Risk Analyzer

A GenAI-powered prototype that helps Small and Medium Enterprises (SMEs) understand service contracts, identify risky clauses, and receive simple explanations using basic NLP and rule-based logic.

## 🔹 Problem Statement
SMEs often sign legal contracts without clearly understanding complex legal clauses such as termination rights, indemnity, auto-renewals, or jurisdiction terms. This system analyzes contracts and highlights potential risks in a simple and explainable manner.

## 🔹 Solution Overview
The application extracts text from contracts, identifies important clauses, extracts entities like parties and dates, and applies rule-based risk scoring. Each clause is labeled as Low, Medium, or High risk and displayed through a Streamlit web interface.

## 🔹 Features
- Upload PDF or TXT contract
- Clause extraction
- Named Entity Recognition (Parties, Dates, Amounts, Locations)
- Rule-based risk detection
- Overall contract risk score
- Simple clause explanations

## 🚀 Live Demo

Try the live deployed app here:  

👉  https://vijayalakshmi-sme-contract-risk-analyzer.streamlit.app

## 📦 Project Structure
<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/8c8bab8a-4dc8-41bb-b343-6b9df7835116" />


## 🛠 Tech Stack

- Python
- spaCy (NLP)
- pdfplumber (PDF text extraction)
- Streamlit (Web UI)

## 🧪 How to Run Locally

1. Clone this repository
2. Install dependencies:

       pip install -r requirements.txt
   
       python -m spacy download en_core_web_sm
   
4. Run the app:
   
       streamlit run app.py
   
6. Upload a sample contract and view analysis.


## ⚠️ Notes

This is a prototype. It does not provide legal advice and does not use external legal databases or AI for legal judgment. Its purpose is to provide explainable high-level risk insights.
