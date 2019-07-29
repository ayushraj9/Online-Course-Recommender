
from collections import Counter
import csv
import re


with open("train.csv", 'r') as file:
  reviews = list(csv.reader(file))

def get_text(reviews, score):
  
  
  return " ".join([r[0].lower() for r in reviews if r[1] == str(score)])

def count_text(text):
  
  words = re.split("\s+", text)
  
  return Counter(words)

negative_text = get_text(reviews, -1)
positive_text = get_text(reviews, 1)

negative_counts = count_text(negative_text)

positive_counts = count_text(positive_text)

print("Negative text sample: {0}".format(negative_text[:100]))
print("Positive text sample: {0}".format(positive_text[:100]))






def get_y_count(score):
  
  return len([r for r in reviews if r[1] == str(score)])


positive_review_count = get_y_count(1)
negative_review_count = get_y_count(-1)


prob_positive = positive_review_count / len(reviews)
prob_negative = negative_review_count / len(reviews)

def make_class_prediction(text, counts, class_prob, class_count):
  prediction = 1
  text_counts = Counter(re.split("\s+", text))
  for word in text_counts:
      
      
      
      prediction *=  text_counts.get(word) * ((counts.get(word, 0) + 1) / (sum(counts.values()) + class_count))
  
  return prediction * class_prob



print("Review: {0}".format(reviews[0][0]))
print("Negative prediction: {0}".format(make_class_prediction(reviews[0][0], negative_counts, prob_negative, negative_review_count)))
print("Positive prediction: {0}".format(make_class_prediction(reviews[0][0], positive_counts, prob_positive, positive_review_count)))





def make_decision(text, make_class_prediction):
    
    negative_prediction = make_class_prediction(text, negative_counts, prob_negative, negative_review_count)
    positive_prediction = make_class_prediction(text, positive_counts, prob_positive, positive_review_count)

    
    if negative_prediction > positive_prediction:
      return -1
    return 1

with open("test.csv", 'r') as file:
    test = list(csv.reader(file))

predictions = [make_decision(r[0], make_class_prediction) for r in test]
print(predictions)
