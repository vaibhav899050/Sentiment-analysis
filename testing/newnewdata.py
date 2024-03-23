import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load the CSV file
df = pd.read_csv("newdata.csv")
df['CONTENT'] = df['CONTENT'].fillna('')
# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

def compound_score1(text):
    scores = sid.polarity_scores(text)
    compound_score = scores['compound']
    return compound_score


# Function to determine sentiment label
def get_sentiment_label(text):
    scores = sid.polarity_scores(text)
    compound_score = scores['compound']
    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Add 'label' column
df['LABEL'] = df['CONTENT'].apply(get_sentiment_label)
df['score'] = df['CONTENT'].apply(compound_score1)

# Save the modified CSV file
df.to_csv("modified_file.csv", index=False)

print("Modified CSV file created successfully.")
