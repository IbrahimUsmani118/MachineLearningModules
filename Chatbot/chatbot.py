from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample speech data
speech_data = [
    ("I love this product", "positive"),
    ("This is not good", "negative"),
    ("Great experience", "positive"),
    ("I'm disappointed", "negative"),
    ("The service was excellent", "positive"),
    ("The food was awful", "negative"),
    ("I highly recommend it", "positive"),
    ("I'm not impressed", "negative"),
    ("Outstanding performance", "positive"),
    ("I regret my decision", "negative"),
    ("This movie is amazing", "positive"),
    ("This book is boring", "negative"),
    ("I had a wonderful time", "positive"),
    ("I'm so frustrated", "negative"),
    ("Delicious and flavorful", "positive"),
    ("Poor quality product", "negative"),
    ("The staff was friendly", "positive"),
    ("Terrible customer service", "negative"),
    ("A great accomplishment", "positive"),
    ("I feel let down", "negative"),
    ("The music is fantastic", "positive"),
    ("This is a waste of money", "negative"),
    ("Impressive performance", "positive"),
    ("I'm completely dissatisfied", "negative"),
    ("Highly satisfied with the outcome", "positive"),
    ("This is a disaster", "negative"),
    ("The atmosphere is cozy", "positive"),
    ("I'm underwhelmed", "negative"),
    ("An enjoyable experience", "positive"),
    ("I'm fed up with it", "negative"),
    ("Incredible work", "positive"),
    ("I can't stand it", "negative"),
    ("The service was top-notch", "positive"),
    ("Extremely disappointing", "negative"),
    ("I'm thrilled with the results", "positive"),
    ("I'm not impressed at all", "negative"),
    ("A masterpiece", "positive"),
    ("I expected better", "negative"),
    ("Prompt and efficient service", "positive"),
    ("I'm deeply unsatisfied", "negative"),
    ("Very impressive", "positive"),
    ("This is a letdown", "negative"),
    ("The presentation was outstanding", "positive"),
    ("I'm not happy with it", "negative"),
    ("Exceptional quality", "positive"),
    ("I'm really annoyed", "negative"),
    ("Highly recommended", "positive"),
    ("This falls short of my expectations", "negative"),
    ("The staff was helpful and courteous", "positive"),
    ("Terrible performance", "negative"),
    ("Absolutely amazing", "positive"),
    ("This is terrible", "negative"),
    ("The product exceeded my expectations", "positive"),
    ("I'm extremely dissatisfied", "negative"),
    ("Fantastic service", "positive"),
    ("I'm so upset", "negative"),
    ("Impressive craftsmanship", "positive"),
    ("I'm not happy with the quality", "negative"),
    ("Outstanding value for money", "positive"),
    ("I'm really frustrated", "negative"),
    ("Great attention to detail", "positive"),
    ("This is a disaster", "negative"),
    ("Highly professional", "positive"),
    ("I'm thoroughly disappointed", "negative"),
    ("Very satisfying", "positive"),
    ("I can't tolerate it", "negative"),
    ("The service was exceptional", "positive"),
    ("Unacceptable behavior", "negative"),
    ("Truly remarkable", "positive"),
    ("I'm deeply unhappy", "negative"),
    ("Excellent customer support", "positive"),
    ("I'm really let down", "negative"),
    ("Incredible performance", "positive"),
    ("This is a huge disappointment", "negative"),
    ("Wonderful atmosphere", "positive"),
    ("I'm not impressed at all", "negative"),
    ("A delightful experience", "positive"),
    ("I'm fed up with it", "negative"),
    ("Exceptional talent", "positive"),
    ("I can't stand it", "negative"),
    ("The service was outstanding", "positive"),
    ("Extremely disappointing", "negative"),
    ("I'm thrilled with the outcome", "positive"),
    ("I'm not impressed at all", "negative"),
    ("Absolutely breathtaking", "positive"),
    ("I expected better", "negative"),
    ("Efficient and reliable service", "positive"),
    ("I'm deeply unsatisfied", "negative"),
    ("Very impressive work", "positive"),
    ("This is a letdown", "negative"),
    ("The presentation was excellent", "positive"),
    ("I'm not happy with it", "negative"),
    ("Exceptional performance", "positive"),
    ("I'm really annoyed", "negative"),
    ("Highly recommended", "positive"),
    ("This falls short of my expectations", "negative"),
    ("The staff was friendly and helpful", "positive"),
    ("Terrible quality", "negative"),
    ("Absolutely outstanding", "positive"),
    ("This is terrible", "negative"),
]

# Splitting data into training and testing sets
X = [speech for speech, label in speech_data]
y = [label for speech, label in speech_data]

# Transforming text data into feature vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Training a logistic regression model
classifier = LogisticRegression()
classifier.fit(X, y)

while True:
    # User input
    user_input = input("Enter your statement (or 'q' to quit): ")
    
    if user_input == "q":
        break
    
    # Transform user input into feature vector
    user_input_vector = vectorizer.transform([user_input])

    # Predicting sentiment
    sentiment = classifier.predict(user_input_vector)

    # Print sentiment indicator
    if sentiment[0] == "positive":
        print("The sentiment of your statement is positive.")
    else:
        print("The sentiment of your statement is negative.")
    
    # Ask user for the sentiment label
    sentiment_label = input("Enter the sentiment label for your statement (positive/negative): ")
    
    # Add user input and label to the speech data
    speech_data.append((user_input, sentiment_label))
    
    # Update X and y with new data
    X = vectorizer.transform([speech for speech, label in speech_data])
    y = [label for speech, label in speech_data]
    
    # Retrain the classifier
    classifier.fit(X, y)

print("Thank you for using the program!")