"""
Task 3: Persona + Hallucination Control + Document Question Answering
The tutor must answer only from the supplied document.
Install: pip install -r requirements.txt
Set OPENAI_API_KEY in your environment before running.
"""
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DOCUMENT = """
Solar energy is energy obtained from sunlight. Solar panels convert sunlight
into electricity. Solar energy is renewable and can reduce electricity bills.
The amount of electricity generated depends on sunlight, panel efficiency,
and the installation size. Solar panels may generate less electricity on
cloudy days and generally do not generate electricity at night without a
storage system.
"""

def answer_from_document(question: str) -> str:
    prompt = f"""
You are a patient Python Tutor who answers questions using only the document below.
Do not use outside knowledge or guess.
If the document does not contain the answer, reply exactly:
I don't know based on the provided document.

DOCUMENT:
{DOCUMENT}

QUESTION:
{question}

Answer:
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Use only the provided document. Do not invent facts."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    # Test 1: The answer is in the document.
    question_in_document = "What do solar panels convert sunlight into?"
    # Test 2: The answer is not in the document.
    question_not_in_document = "In which year was the first solar panel invented?"

    try:
        print("DOCUMENT QUESTION ANSWERING TESTS\n")
        print("Q1:", question_in_document)
        print("A1:", answer_from_document(question_in_document))
        print()
        print("Q2:", question_not_in_document)
        print("A2:", answer_from_document(question_not_in_document))
    except Exception as error:
        print("Error calling the LLM API:", error)

    # Optional interactive question:
    # question = input("\nAsk another question about the document: ")
    # print(answer_from_document(question))
