### **Task 3: Satellite Image Analysis for Deforestation Monitoring**

- **Objective**:  
  Detect deforestation trends and monitor environmental changes in the Amazon using satellite imagery.

- **Dataset**:  
  [Planet: Understanding the Amazon from Space](https://www.kaggle.com/competitions/planet-understanding-the-amazon-from-space)

- **Approach**:
  1. **Data Acquisition**:  
     - Downloaded the dataset from Kaggle.  
     - Unzipped the dataset to access image files and associated labels.
  
  2. **Data Exploration**:  
     - Loaded `train_classes.csv` using pandas to inspect image labels.  
     - Analyzed the number of images in both the training and testing sets.  
     - Visualized tag distributions to understand prevalence and potential imbalances.  
     - Identified missing data and verified the consistency of image-label mappings.
  
  3. **Data Preprocessing**:  
     - Mapped textual tags to a one-hot encoded format for model compatibility.  
     - Applied the one-hot encoding transformation to the 'tags' column in the training DataFrame.  
     - Combined data into a single DataFrame to streamline further processing.
  
  4. **Dataset Preparation**:  
     - Defined image transformations using `torchvision.transforms`, including:  
       - **Resizing**: Standardizing image dimensions.  
       - **Normalization**: Scaling pixel values for neural network input.  
       - *(Optional: Considered augmentations like random flipping or rotations for improved model generalization.)*
     - Developed a custom `PlanetDataset` class (subclassing `torch.utils.data.Dataset`):  
       - Implemented methods to locate and load images.  
       - Integrated the transformation pipeline to preprocess images on the fly.
  
  5. **Model Training & Evaluation**:  
     - Split the prepared dataset into training and validation sets.  
     - Employed `torch.utils.data.DataLoader` for efficient mini-batch processing.  
     - Constructed a custom CNN model for multi-label classification.  
     - Planned evaluation routines include calculating loss and accuracy on the validation data.
  
- **Outcome**:  
  Established an initial pipeline for deforestation monitoring. This framework encompasses data acquisition, exploration, preprocessing, and the creation of a custom dataset class, paving the way for model training and detailed evaluation in subsequent steps.