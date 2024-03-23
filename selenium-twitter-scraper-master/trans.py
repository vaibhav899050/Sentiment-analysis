import pandas as pd
import csv
from googletrans import Translator

file_path = 'tweets/Extracted_1.csv'
df = pd.read_csv(file_path)
translator = Translator()


def translate_to_english(text):
    translation = translator.translate(text, dest='en')
    return translation.text


df['content_english'] = df['Content'].apply(translate_to_english)
df.to_csv('tweets/translated_file.csv', index=False)