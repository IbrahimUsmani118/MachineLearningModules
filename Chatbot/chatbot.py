import random
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def load_data_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def save_data_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def add_new_data(speech_data):
    while True:
        user_input = input("Enter a new statement (or 'q' to quit adding data): ")
        if user_input.lower() == "q":
            break

        sentiment_label = input("Enter the sentiment label for your statement (positive/negative): ")
        while sentiment_label.lower() not in ['positive', 'negative']:
            sentiment_label = input("Invalid input. Enter 'positive' or 'negative': ")

        speech_data.append((user_input, sentiment_label))
        print("Statement added.")

    return speech_data

def guessing_game(classifier, vectorizer, speech_data):
    statement, label = random.choice(speech_data)
    user_guess = input(f"Guess if this statement is positive or negative:\n'{statement}'\nEnter your guess: ")

    user_input_vector = vectorizer.transform([statement])
    prediction = classifier.predict(user_input_vector)

    if user_guess.lower() == prediction[0]:
        print("Correct guess!")
    else:
        print(f"Sorry, it was a {label} statement.")

def main():
    filename = 'speech_data.json'
    speech_data = load_data_from_json(filename)

    X = [speech for speech, label in speech_data]
    y = [label for speech, label in speech_data]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(X)

    classifier = LogisticRegression()
    classifier.fit(X, y)

    while True:
        print("\nMenu:")
        print("1. Add new data")
        print("2. Guess sentiment")
        print("3. Quit")
        choice = input("Select an option (1/2/3): ")

        if choice == "1":
            speech_data = add_new_data(speech_data)
            X = vectorizer.transform([speech for speech, label in speech_data])
            y = [label for speech, label in speech_data]
            classifier.fit(X, y)
        elif choice == "2":
            guessing_game(classifier, vectorizer, speech_data)
        elif choice == "3":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
