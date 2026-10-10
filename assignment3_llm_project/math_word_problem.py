"""
Task 2: Mathematical Word Problem — Step-by-Step Prompting
The model is asked for a short, clear explanation and a final answer.
Install: pip install -r requirements.txt
Set OPENAI_API_KEY in your environment before running.
"""
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def solve_word_problem(problem: str) -> str:
    prompt = f"""
Solve the following mathematical word problem.
Give a short, clear solution with numbered calculation steps.
Then write the final answer on a separate line beginning with "Final answer:".
Check the arithmetic before answering.

Problem: {problem}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a careful math tutor. Explain the key calculations clearly."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    problem = input(
        "Enter a math word problem (or press Enter for the sample): "
    ).strip()
    if not problem:
        problem = (
            "Ravi buys 3 notebooks for 40 rupees each and 2 pens for 15 rupees each. "
            "How much does he spend in total?"
        )
    try:
        print("\nSolution:\n")
        print(solve_word_problem(problem))
    except Exception as error:
        print("Error calling the LLM API:", error)
