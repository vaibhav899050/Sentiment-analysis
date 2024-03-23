import pickle
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Load the model from the .pkl file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

data = pd.read_csv('newtest.csv')
data = data.dropna(subset=['Content'])
data = data.dropna(subset=['Label'])
# Load your test data and labels
X_test = data['Content']
y_true = data['Label']
vec = CountVectorizer(stop_words = 'english')
xnew = vec.fit_transform(X_test)
xnew.toarray()

# Make predictions on the test data
y_pred = model.predict(xnew)

# Compute accuracy
accuracy = accuracy_score(y_true, y_pred)
print("Accuracy:", accuracy)
