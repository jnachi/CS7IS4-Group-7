import nltk
nltk.download('punkt')
nltk.download('stopwords')
import os
import json
import string
import re
import nltk
import enchant
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
enchant_dict = enchant.Dict("en_US")  # American English dictionary
enchant_dict.add("en_GB")  # British English dictionary

input_directory = './data/raw-txt'
output_directory = './data/tokenized-txt'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = "".join(re.findall("[a-z\s]*", text))  # Remove special characters
    tokens = word_tokenize(text)
    filtered_text = []
    for word in tokens:
        if word not in stop_words:
            try:
                if enchant_dict.check(word): 
                    filtered_text.append(word)
            except:
                pass
    
    tokens = [lemmatizer.lemmatize(l) for l in filtered_text]
    return tokens

def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        preprocessed_text = preprocess_text(text)
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(preprocessed_text, file)

for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)
        process_file(input_path, output_path)
