# SME Contract Risk Analyzer

This repository contains a lightweight prototype tool designed to help small and medium enterprises (SMEs) assess risk in service contracts using basic NLP and rule-based logic.

## 🧠 What It Does

The SME Contract Risk Analyzer:

- Accepts PDFs and TXT contract files
- Extracts key entities like parties, dates, amounts, and jurisdiction
- Segments text into clauses
- Assigns risk labels (Low, Medium, High) to each clause
- Displays clause explanations in plain business language
- Computes a composite contract-level risk score

This tool is designed for non-legal users to understand contract risks quickly and in a transparent way.

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
