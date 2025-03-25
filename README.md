# Mental Health Twitter Analysis

## HumanAI GSoC Test Submission - Task 1: Social Media Data Extraction & Preprocessing

### Skills & Tools

- **Python Libraries:**
  - Tweepy
  - Pandas
  - NumPy
  - Matplotlib
  - NLTK
  - TextBlob
  - Scikit-Learn
  - SNScrape
  - Jupyter Notebook

- **Techniques & Concepts:**
  - Data Preprocessing
  - Web Scraping / API Handling
  - Natural Language Processing (NLP)
  - Data Visualization
  - Exploratory Data Analysis (EDA)
  - Sentiment Analysis
  - K-Means Clustering

---

## Introduction

In today’s fast-paced world, people often prioritize external success while neglecting their mental well-being. With increasing awareness about mental health, discussions on platforms like Twitter have grown significantly. Social media is now a space where individuals share their struggles, seek support, and discuss self-care practices such as meditation, therapy, and exercise.

This project aims to analyze social media discussions related to mental health by answering two key questions:

1. **Which self-care practices contribute the most to mental well-being?** (Meditation, Yoga, Therapy, Exercise, etc.)
2. **Which influencers have the greatest impact on mental health awareness?** (Mental health advocates, spiritual teachers, psychologists, celebrities, etc.)

---

## Data Collection & Preprocessing

To gather relevant data, we used the **Twitter API** and **SNScrape**, which allowed us to extract a large number of tweets efficiently. SNScrape provided broader access to tweets compared to Tweepy, making it the preferred choice for data collection.

### Data Extraction:
- **Tweets were filtered** using keywords related to mental health distress, substance use, and suicidality (e.g., "depressed," "addiction help," "overwhelmed," "suicidal").
- **Extracted fields**: Post ID, Timestamp, Content, Engagement Metrics (likes, comments, shares).
- **Dataset Size**: 10,000+ tweets were retrieved.

### Data Cleaning:
- Removed **stopwords, emojis, special characters**, and redundant whitespace.
- Standardized text formatting for NLP preprocessing.
- Stored the cleaned dataset in **CSV/JSON format** for further analysis.

---

## Section 1: Self-Care Practices & Sentiment Analysis

We analyzed different mental health self-care methods by comparing sentiment scores of tweets discussing **meditation, therapy, and exercise**.

### Sentiment Analysis:
Using **NLTK** and **TextBlob**, we evaluated:
- **Polarity**: Measures whether the text is positive, neutral, or negative.
- **Subjectivity**: Determines whether the text is opinionated or factual.

### Key Findings:
1. **Meditation-related tweets** showed the highest positivity and subjectivity.
2. **Therapy-related tweets** were the most objective.
3. **Exercise-related tweets** had the lowest positivity scores.

---

## Section 2: Influence of Mental Health Advocates

To evaluate **who influences mental health discussions**, we collected data from two types of Twitter accounts:
- 40 **mental health advocates/spiritual teachers**
- 40 **celebrities (actors, influencers, etc.)**

We compared their engagement metrics and sentiment scores to determine **who has a greater impact** on mental health awareness.

### Key Findings:
- Mental health influencers received **higher engagement on positive tweets**.
- Celebrities had **wider reach but mixed sentiment polarity**.
- Tweets from psychologists and mental health advocates had the **most consistent positive sentiment**.

---

## Conclusion

This analysis provides insights into **effective self-care practices** and **the role of influencers** in mental health discussions on Twitter. By leveraging **NLP and sentiment analysis**, we identified patterns in online conversations that can help shape mental health awareness campaigns.

---

📌 **Deliverables:**
- ✅ Python script for **data extraction & preprocessing**
- ✅ Cleaned dataset in **CSV/JSON format**
- ✅ Exploratory Data Analysis & **Sentiment Analysis insights**
