# Skinlyze - Machine Learning Team (C242-PR613)
## Project Overview
This project aims to classify skin diseases to facilitate early detection and diagnosis, enabling timely treatment or medical examination. By leveraging Transfer Learning with MobileNet and TensorFlow, our model can identify and classify seven types of skin diseases: Actinic Keratoses and Intraepithelial Carcinoma/Bowen's Disease (AKIEC), Basal Cell Carcinoma (BCC), Benign Keratosis-like Lesions (BKL), Dermatofibroma (DF), Melanoma (MEL), Melanocytic Nevi (NV), and Vascular Lesions (VASC).

The system provides actionable insights, highlighting whether a detected condition requires immediate attention or further treatment. This approach aims to enhance diagnostic accuracy and support healthcare professionals in combating skin diseases, including malignant tumors and skin cancer, at earlier stages.

## Table of Contents
- [**Project Overview**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#table-of-contents)
- [**Data Set**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#data-set)
- [**Data Preprocessing**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#data-preprocessing)
- [**Model Architecture**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#model-architecture)
- [**Training**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#training)
- [**Model Conversion**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#model-conversion)
- [**Usage**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#usage)
- [**Authors**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#authors)
- [**Contributing**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#contributing)
- [**Acknowledgments**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#acknowledgments)


## Data Set


## Data Preprocessing


## Model Architecture


## Training
The model is trained using:

- Optimizer: Adam with a learning rate of 0.001.
- Loss Function: Categorical Crossentropy.
- Metrics: Accuracy (Categorical Accuracy).

The training process incorporates callbacks to:

- Save the model with the best performance.
- Halt training early if validation accuracy stops improving.
- Adjust the learning rate downward when validation loss levels off.

## Model Conversion
The trained model is saved in the .h5 format to facilitate continuous updates and allow fine-tuning with newer data. This decision ensures the flexibility and adaptability of the model as new skin disease patterns or datasets become available. The steps include:
1. Saving the Keras model in .h5 format, which stores both the architecture and weights.
2. Utilizing the .h5 format to reload the model easily for retraining or fine-tuning with additional or updated datasets.
3. Exporting the retrained model for deployment or conversion to other formats, ensuring compatibility with various systems.

By using the .h5 format, the model remains versatile for ongoing development and improvements, which is essential in medical applications where accuracy and relevance to current data are critical.

## Usage

#### 1. Clone the repository

```bash
git clone -b prod https://github.com/Skinlyze/Skinlyze-Backend.git
```

#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
#### 3. Start the server
```bash
python app.py
```


## Authors


## Contributing


## Acknowledgments


Data Set
https://drive.google.com/drive/u/3/folders/1VbOJbw3iNzIol4Tl4_LCHpZFLkvAno2b

Licence 
https://creativecommons.org/licenses/by-nc/4.0/ (CC-BY-NC)

Referensi 
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T
