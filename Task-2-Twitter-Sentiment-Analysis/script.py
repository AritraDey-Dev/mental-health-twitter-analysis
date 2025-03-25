import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Download necessary NLTK resources
nltk.download('vader_lexicon')
nltk.download('punkt')

# Initialize VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

def classify_sentiment(text):
    """Classifies sentiment using VADER and TextBlob."""
    vader_score = sia.polarity_scores(text)['compound']
    blob_score = TextBlob(text).sentiment.polarity
    avg_score = (vader_score + blob_score) / 2
    
    if avg_score > 0.05:
        return "Positive"
    elif avg_score < -0.05:
        return "Negative"
    else:
        return "Neutral"

def classify_risk(text, tfidf_model, kmeans_model):
    """Classifies risk level based on TF-IDF and clustering."""
    text_vector = tfidf_model.transform([text])
    cluster = kmeans_model.predict(text_vector)[0]
    
    if cluster == 0:
        return "High-Risk"
    elif cluster == 1:
        return "Moderate Concern"
    else:
        return "Low Concern"

# Load dataset (Assumes a CSV file with a 'text' column)
df = pd.read_csv("tweets.csv")

df['sentiment'] = df['text'].apply(classify_sentiment)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(df['text'])

# K-Means Clustering for Risk Classification
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

df['risk_level'] = df['text'].apply(lambda text: classify_risk(text, vectorizer, kmeans))

# Plot Sentiment and Risk Distribution
plt.figure(figsize=(10, 5))
sns.countplot(x='sentiment', data=df, palette='coolwarm')
plt.title("Sentiment Distribution")
plt.show()

plt.figure(figsize=(10, 5))
sns.countplot(x='risk_level', data=df, palette='viridis')
plt.title("Risk Level Distribution")
plt.show()

# Save classified data
df.to_csv("classified_tweets.csv", index=False)

print("Classification complete. Results saved in 'classified_tweets.csv'.")