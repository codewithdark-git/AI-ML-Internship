# Emotion Recognition with BERT

## Overview
This project demonstrates emotion recognition using a pre-trained BERT model fine-tuned on a multi-label emotion classification dataset. The script in `infer.py` loads the model and tokenizer, processes input text, and outputs the top 5 predicted emotions with their probabilities.

## Setup
- Install required packages:
  ```
  pip install transformers torch
  ```
- Download the pre-trained model `codewithdark/bert-Gomotions` from Hugging Face.
- Optional: For GPU usage, ensure CUDA is properly installed.

## Running Inference
Run the inference script using:
```
python infer.py
```
Expected output:
```
Top 5 Predicted Emotions:
Joy: 0.9478
Love: 0.7854
Optimism: 0.6342
Admiration: 0.5678
Excitement: 0.5231
```

## Troubleshooting
- Verify package installations and correct model access.
- For performance issues, try running on a machine with GPU support.
- Check error logs for model/tokenizer loading issues.

## Fine-Tuning Experiments
The notebook `fine-tuning-bert-on-goemotions.ipynb` contains detailed experiments on fine-tuning BERT for emotion recognition. It covers exploration of various hyperparameters, preprocessing techniques, and evaluation metrics.

## Project Structure
- `infer.py`: Contains the main inference code.
- `fine-tuning-bert-on-goemotions.ipynb`: Contains fine-tuning experiments (if applicable).
- `readme.md`: This file.
