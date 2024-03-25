import pandas as pd
import os
from openai import OpenAI

client = OpenAI(
    api_key=""
)

# Function to get sentiment using OpenAI API
def get_sentiment(review_text):
    prompt = f'Given the following review for a restaurant: "{review_text}". What is the sentiment of this review? Answer with only POSITIVE or NEGATIVE'
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use GPT-3.5
        messages=[
            {"role": "system", "content": prompt}
        ],
        max_tokens=10,  # Set max tokens to 1 to get a concise sentiment label
        temperature=0,  # Set temperature to 0 for deterministic output
    )
    sentiment = response.choices[0].message.content
    return sentiment

current_directory = os.getcwd()

def getPath(filename):
    csv_path = os.path.join(current_directory, filename)
    return csv_path

numberOfRows = 1

oneStarReviews = pd.read_csv(getPath('one_star_reviews_sample.csv'),  nrows=numberOfRows)
fourStarReviews = pd.read_csv(getPath('four_star_reviews_sample.csv'), nrows=numberOfRows)

# Create lists to store the reviews and sentiments
one_star_data = []
four_star_data = []

# Iterate through one-star reviews and get sentiments
for index, row in oneStarReviews.iterrows():
    review_text = row['Reviews']
    sentiment = get_sentiment(review_text)
    one_star_data.append({'text': review_text, 'sentiment': sentiment})

# Iterate through four-star reviews and get sentiments
for index, row in fourStarReviews.iterrows():
    review_text = row['Reviews']
    sentiment = get_sentiment(review_text)
    four_star_data.append({'text': review_text, 'sentiment': sentiment})

# Print the data for one-star reviews
print('\n\nOne Star Reviews\n')
for index, data in enumerate(one_star_data):
    print(f"One-star Review {index + 1}\nText: {data['text']}\n\nSentiment: {data['sentiment']}")
    print('\n')

# Print the data for four-star reviews
print('\n\nFour Star Reviews\n')
for index, data in enumerate(four_star_data):
    print(f"Four-star Review {index + 1}\nText: {data['text']}\n\nSentiment: {data['sentiment']}")
    print('\n')