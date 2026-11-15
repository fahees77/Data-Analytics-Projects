# Survey Feedback Analyzer

# Step 1: given data
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


# Step 2: add more feedbacks
count = input("How many more feedbacks do you want to add? ")
while not count.isdigit():
    count = input("Please enter a number: ")
count = int(count)

for i in range(count):
    print("\nFeedback", i + 1)
    name = input("Name: ")
    feedback = input("Feedback: ")
    rating = input("Rating (1-5): ")
    while not (rating.isdigit() and 1 <= int(rating) <= 5):
        rating = input("Rating must be between 1 and 5, try again: ")

    # S_No continues from the last number (so it starts at 11)
    feedback_data['S_No'].append(feedback_data['S_No'][-1] + 1)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(int(rating))


# Step 3: clean the feedback text
punctuations = ['.', ',', '!', '?']

for i in range(len(feedback_data['Feedback'])):
    text = feedback_data['Feedback'][i]

    # replace punctuation with a space
    for p in punctuations:
        text = text.replace(p, ' ')

    # split() drops extra spaces, join() puts the words back with one space
    text = ' '.join(text.split())

    feedback_data['Feedback'][i] = text.lower()


# Step 4: word count function
def count_word_in_feedbacks(word):
    word = word.lower()
    total = 0
    for text in feedback_data['Feedback']:
        if word in text.lower().split():
            total += 1
    return total


print("\n--- Word Count ---")
print("Feedbacks containing 'good':", count_word_in_feedbacks("good"))
print("Feedbacks containing 'poor':", count_word_in_feedbacks("poor"))
print("Feedbacks containing 'excellent':", count_word_in_feedbacks("excellent"))


# Step 5: final summary
print("\n--- Cleaned Feedback Data ---")
for key in feedback_data:
    print(key, ":", feedback_data[key])

# average rating
average = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print("\nAverage rating:", round(average, 2))

# longest feedback (by number of words)
longest_text = ""
longest_name = ""
max_words = 0
for i in range(len(feedback_data['Feedback'])):
    words = len(feedback_data['Feedback'][i].split())
    if words > max_words:
        max_words = words
        longest_text = feedback_data['Feedback'][i]
        longest_name = feedback_data['Name'][i]

print("\nLongest feedback:", longest_text)
print("By:", longest_name, "| Words:", max_words)

# unique words (set removes duplicates)
unique_words = set()
for text in feedback_data['Feedback']:
    for w in text.split():
        unique_words.add(w)

print("\nUnique words used:")
print(sorted(unique_words))


# Optional: sort by rating, highest to lowest
all_entries = zip(feedback_data['S_No'], feedback_data['Name'],
                  feedback_data['Feedback'], feedback_data['Rating'])

# x[3] is the rating
sorted_entries = sorted(all_entries, key=lambda x: x[3], reverse=True)

print("\n--- Feedbacks sorted by rating (high to low) ---")
for entry in sorted_entries:
    print(entry)
