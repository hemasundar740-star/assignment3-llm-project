# Assignment 3 — Prompt Engineering with an LLM API

This project contains three beginner-friendly Python programs.

## Files
- `sentiment_few_shot.py` — classifies a customer message as Positive, Negative, or Neutral using few-shot examples.
- `math_word_problem.py` — asks the LLM to solve a math word problem and show clear calculation steps plus a final answer.
- `document_qa.py` — gives the LLM a Python Tutor persona and a document, and instructs it not to guess when the answer is missing.
- `requirements.txt` — Python dependency list.

## Requirements
- Python 3.10 or newer
- An API key for the OpenAI API

## Setup (Windows PowerShell)
1. Open this folder in VS Code.
2. Create and activate a virtual environment (optional but recommended):
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install the dependency:
   ```powershell
   pip install -r requirements.txt
   ```
4. Set your API key for the current PowerShell window:
   ```powershell
   $env:OPENAI_API_KEY="paste_your_api_key_here"
   ```
   Keep your API key private. Do not upload it to GitHub.
5. Run each task:
   ```powershell
   python sentiment_few_shot.py
   python math_word_problem.py
   python document_qa.py
   ```

## Notes
- API usage may incur charges depending on your account and provider settings.
- The document Q&A program includes two tests: one answerable from the document and one that should trigger the required fallback response.
- LLM output can vary. Always check the answer before submitting.
