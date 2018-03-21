from collections import defaultdict
from bs4 import BeautifulSoup

def parse_reviews(file_name):
    with open(file_name, encoding = "utf-8") as f:
        soup = BeautifulSoup(f, "lxml")
    
    reviews = defaultdict()
    for review in soup.find_all("review"):
        text = review.find("text").text
        avg_rating = (review.find("food").text + 
                      review.find("interior").text + 
                      review.find("service").text)/3
        
        reviews[review["id"]] = { "text" :  text, 
                                  "avg_rating" : avg_rating }
        
        print(reviews)

def preprocess_text(text):
    pass

    
parse_reviews("SentiRuEval_rest_train.xml")