# Twitter Sentiment Analysis - Task 2 Submission (humaAi GSoC)

This repository contains the submission for **Task 2: Sentiment & Crisis Risk Classification (NLP & Text Processing)** as part of the humaAi Google Summer of Code (GSoC). The project focuses on classifying the sentiment of tweets as positive or negative, providing insights into public perception on various topics.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Objectives](#objectives)
- [Methodology](#methodology)
  - [TF-IDF Vectorization (Unigram)](#tf-idf-vectorization-unigram)
  - [TF-IDF Vectorization (N-grams)](#tf-idf-vectorization-n-grams)
  - [Custom Trained Word2Vec](#custom-trained-word2vec)
  - [Custom Trained Doc2Vec](#custom-trained-doc2vec)
  - [Pre-trained Google News Word2Vec](#pre-trained-google-news-word2vec)
  - [GloVe Embeddings](#glove-embeddings)
  - [FastText (Trained from Scratch)](#fasttext-trained-from-scratch)
  - [BERT](#bert)
  - [RoBERTa](#roberta)
  - [Latent Dirichlet Allocation (LDA)](#latent-dirichlet-allocation-lda)
  - [Universal Sentence Encoder](#universal-sentence-encoder)
  - [Sentence Transformers](#sentence-transformers)
  - [ELMo](#elmo)
  - [CLIP](#clip)
- [Results](#results)
- [Future Scope](#future-scope)
- [Installation](#installation)

## Introduction

Sentiment analysis is a natural language processing (NLP) task that determines whether a given text expresses a positive or negative sentiment. This project involves analyzing a large collection of tweets to classify public sentiment effectively.

## Dataset

The dataset used for this task is the [Sentiment140 dataset](https://www.kaggle.com/datasets/kazanova/sentiment140). It consists of **1.6 million tweets**, each labeled with either **0 (negative)** or **4 (positive)** sentiment. The dataset includes the following fields:
- **`target`**: Sentiment label (0 = negative, 4 = positive)
- **`ids`**: Unique Tweet ID
- **`date`**: Timestamp of the tweet
- **`flag`**: Query flag
- **`user`**: Twitter username
- **`text`**: Actual tweet content

## Objectives

The key goals of this project are:
1. Cleaning and preprocessing tweets for effective sentiment classification.
2. Exploring the dataset through visualizations and statistical analysis.
3. Developing machine learning and deep learning models to classify tweet sentiment.

## Methodology

We experimented with a variety of text representation techniques and models for feature extraction and classification. Below are the approaches used:

### TF-IDF Vectorization (Unigram)
TF-IDF (Term Frequency-Inverse Document Frequency) assigns importance to words based on their occurrence in a document relative to the entire corpus. This method effectively transforms text into numerical features suitable for machine learning algorithms.

### TF-IDF Vectorization (N-grams)
This extends TF-IDF by considering sequences of words (bigrams, trigrams) to capture contextual information and phrase-level dependencies, enhancing sentiment classification accuracy.

### Custom Trained Word2Vec
Word2Vec generates dense vector representations of words by training on a corpus. We used both **Continuous Bag of Words (CBOW)** and **Skip-gram** architectures to train word embeddings from scratch.

### Custom Trained Doc2Vec
Doc2Vec extends Word2Vec by generating vector representations for entire sentences or documents, capturing deeper contextual meaning beyond individual words.

### Pre-trained Google News Word2Vec
This model, trained on a large corpus of news articles, provides high-quality embeddings that capture word relationships and contextual semantics effectively.

### GloVe Embeddings
GloVe (Global Vectors for Word Representation) constructs word embeddings by analyzing global word co-occurrence statistics, offering robust semantic relationships between words.

### FastText (Trained from Scratch)
FastText improves upon Word2Vec by representing words as subword character n-grams. This helps in handling out-of-vocabulary (OOV) words and improves accuracy.

### BERT
BERT (Bidirectional Encoder Representations from Transformers) captures word meaning by considering both left and right context, significantly improving NLP tasks like sentiment classification.

### RoBERTa
RoBERTa (Robustly Optimized BERT Pretraining Approach) is an optimized version of BERT with longer training, dynamic masking, and removal of Next Sentence Prediction (NSP), leading to improved performance.

### Latent Dirichlet Allocation (LDA)
LDA is a topic modeling algorithm that uncovers hidden topics in a collection of texts, helping to identify key themes and topics in tweets.

### Universal Sentence Encoder
This model encodes text into fixed-length embeddings, leveraging transformer-based architecture to generate meaningful sentence representations.

### Sentence Transformers
Sentence Transformers generate sentence-level vector representations that capture semantic similarity, making them useful for sentiment classification tasks.

### ELMo
ELMo (Embeddings from Language Models) provides deep contextualized word representations by considering entire sentences, improving text classification performance.

### CLIP
CLIP (Contrastive Language-Image Pretraining) is primarily designed for vision-language tasks but has been explored for text classification by leveraging its robust multimodal embeddings.

## Results

We evaluated various models based on accuracy, precision, recall, and F1-score to determine the best-performing approach. The results indicate that deep learning models, particularly **BERT** and **RoBERTa**, achieve the highest accuracy in sentiment classification.


## Installation

To set up the project locally, follow these steps:

```bash
# Clone the repository
# Install dependencies
pip install -r requirements.txt
```

## Usage

To train a model and classify tweet sentiment, run:

```bash
jupyter nbconvert --to notebook --execute main.ipynb
```
