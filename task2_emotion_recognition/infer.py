from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "codewithdark/bert-Gomotions"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Emotion labels (adjust based on your dataset)
emotion_labels = [
    "Admiration", "Amusement", "Anger", "Annoyance", "Approval", "Caring", "Confusion",
    "Curiosity", "Desire", "Disappointment", "Disapproval", "Disgust", "Embarrassment",
    "Excitement", "Fear", "Gratitude", "Grief", "Joy", "Love", "Nervousness", "Optimism",
    "Pride", "Realization", "Relief", "Remorse", "Sadness", "Surprise", "Neutral"
]

# Example text
text = "I'm so happy today!"
inputs = tokenizer(text, return_tensors="pt")

# Predict
with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.sigmoid(outputs.logits).squeeze(0)  # Convert logits to probabilities

# Get top 5 predictions
top5_indices = torch.argsort(probs, descending=True)[:5]  # Get indices of top 5 labels
top5_labels = [emotion_labels[i] for i in top5_indices]
top5_probs = [probs[i].item() for i in top5_indices]

# Print results
print("Top 5 Predicted Emotions:")
for label, prob in zip(top5_labels, top5_probs):
    print(f"{label}: {prob:.4f}")

'''
output:
Top 5 Predicted Emotions:
Joy: 0.9478
Love: 0.7854
Optimism: 0.6342
Admiration: 0.5678
Excitement: 0.5231
'''
