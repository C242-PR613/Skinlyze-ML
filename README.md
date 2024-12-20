# Skinlyze - Machine Learning Team (C242-PR613)
## Project Overview
This project aims to classify skin diseases to facilitate early detection and diagnosis, enabling timely treatment or medical examination. By leveraging Transfer Learning with MobileNet and TensorFlow, our model can identify and classify seven types of skin diseases: Actinic Keratoses and Intraepithelial Carcinoma/Bowen's Disease (AKIEC), Basal Cell Carcinoma (BCC), Benign Keratosis-like Lesions (BKL), Dermatofibroma (DF), Melanoma (MEL), Melanocytic Nevi (NV), and Vascular Lesions (VASC).

The system provides actionable insights, highlighting whether a detected condition requires immediate attention or further treatment. This approach aims to enhance diagnostic accuracy and support healthcare professionals in combating skin diseases, including malignant tumors and skin cancer, at earlier stages.

## Table of Contents
- [**Project Overview**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#project-overview)
- [**Data Set**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#data-set)
- [**Data Preprocessing**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#data-preprocessing)
- [**Model Architecture**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#model-architecture)
- [**Training**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#training)
- [**Model Conversion**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#model-conversion)
- [**Usage**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#usage)
- [**Authors**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#authors)
- [**Contributing**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#contributing)
- [**License**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#license)
- [**Acknowledgments**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#acknowledgments)
- [**Reference**](https://github.com/Skinlyze/Skinlyze-ML?tab=readme-ov-file#reference)


## Data Set
We use datasets sourced from [Harvard Dataverse (The HAM10000 dataset)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T) and [ISIC](https://challenge.isic-archive.com/data/#2018), which provide extensive collections of images for skin lesion analysis and classification. It contains various Skin image categorized into 7 disease, that are Actinic Keratoses and Intraepithelial Carcinoma/Bowen's Disease (AKIEC), Basal Cell Carcinoma (BCC), Benign Keratosis-like Lesions (BKL), Dermatofibroma (DF), Melanoma (MEL), Melanocytic Nevi (NV), and Vascular Lesions (VASC).

## Data Preprocessing
The dataset used for the Skin Lesion Classification model consists of images categorized into seven classes of skin conditions: Actinic Keratoses and Intraepithelial Carcinoma/Bowen's Disease (AKIEC), Basal Cell Carcinoma (BCC), Benign Keratosis-like Lesions (BKL), Dermatofibroma (DF), Melanoma (MEL), Melanocytic Nevi (NV), and Vascular Lesions (VASC). This diverse dataset includes images of various skin lesion types to support accurate analysis and classification.

Data augmentation techniques are applied to enhance the diversity and size of the skin lesion dataset. The ImageDataGenerator class from TensorFlow and [tf.keras.applications.mobilenet.preprocess_input](https://www.tensorflow.org/api_docs/python/tf/keras/applications/mobilenet/preprocess_input) used to preprocess the data. These transformations help improve the model's ability to generalize and make more accurate predictions across the different skin lesion categories.

 These preprocessing steps include:
 - Resizing Image to 224 x 224
 - Normalize the pixel values
 - Applying augmentation

## Model Architecture
The model is built using the MobileNetV2 architecture with pre-trained weights from ImageNet. The architecture includes:

- A base model from MobileNetV2, with the last six layers removed.
- A flatten layer to reshape the output.
- A dense layer with 7 units and a softmax activation function for classification.
- The layers before the last 23 layers are frozen to prevent them from being trained.

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

To deploy ML model, follow these steps:
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
- [Rafid Ahmad Arfianto](https://github.com/rafid0004)
- [M. Fauzan Naufal Ridho](https://github.com/ozannaufal15)

## Contributing
Feel free to contribute to this project by submitting your ideas, suggestions, or improvements through a pull request. Please ensure that your contributions relevant for this project.

## License
Shield: [![CC BY-NC 4.0][cc-by-nc-shield]][cc-by-nc]

This work is licensed under a
[Creative Commons Attribution-NonCommercial 4.0 International License][cc-by-nc].

[![CC BY-NC 4.0][cc-by-nc-image]][cc-by-nc]

[cc-by-nc]: https://creativecommons.org/licenses/by-nc/4.0/
[cc-by-nc-image]: https://licensebuttons.net/l/by-nc/4.0/88x31.png
[cc-by-nc-shield]: https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg

## Acknowledgments
This project is a part of the Bangkit Academy 2024 capstone initiative by Team C242-PR613. We extend our heartfelt gratitude to our advisors, Mr. Firdhaus R. Azis and Mrs. Monifa Arini, for their guidance and support.

## Reference
Data Set: <https://drive.google.com/drive/u/3/folders/1VbOJbw3iNzIol4Tl4_LCHpZFLkvAno2b>

Referensi: <https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T>
