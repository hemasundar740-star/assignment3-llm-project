
"""
Assignment 3 - Task 1
Few-Shot Prompting: Customer Sentiment Classification
"""

import os
import openai
from openai import OpenAI

# Read your API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY is not set.")
    print("Please set your OpenAI API key before running this program.")
    exit()

client = OpenAI(api_key=api_key)


def classify_sentiment(message: str) -> str:
    prompt = f"""
You are a customer sentiment classifier.

Classify the customer message into exactly one category:
Positive, Negative, or Neutral.

Examples:

Customer message: "The product is excellent!"
Sentiment: Positive

Customer message: "The product arrived broken."
Sentiment: Negative

Customer message: "My order number is 12345."
Sentiment: Neutral

Customer message: "I love the quality and service."
Sentiment: Positive

Customer message: "The delivery was very late."
Sentiment: Negative

Now classify this message:

Customer message: "{message}"
Sentiment:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You classify customer sentiment. "
                    "Return only Positive, Negative, or Neutral."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    customer_message = input("Enter a customer message: ")

    try:
        sentiment = classify_sentiment(customer_message)
        print("Sentiment:", sentiment)

    except openai.APIConnectionError as error:
        print("Connection failed.")
        print("Detailed error:", repr(error.__cause__))
        print("Check your internet, firewall, proxy, or SSL connection.")

    except openai.AuthenticationError:
        print("Authentication failed. Check whether your API key is valid.")

    except openai.RateLimitError as error:
        print("Rate limit or API quota issue:", error)

    except openai.APIStatusError as error:
        print("API error status:", error.status_code)
        print("Details:", error.message)

    except Exception as error:
        print("Error type:", type(error).__name__)
        print("Error details:", error)
