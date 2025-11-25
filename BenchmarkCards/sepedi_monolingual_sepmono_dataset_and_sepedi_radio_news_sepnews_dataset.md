# Sepedi monolingual (SepMono) dataset and Sepedi radio news (SepNews) dataset

## 📊 Benchmark Details

**Name**: Sepedi monolingual (SepMono) dataset and Sepedi radio news (SepNews) dataset

**Overview**: This study curates two new datasets, the Sepedi monolingual dataset (SepMono) and the Sepedi radio news dataset (SepNews), to train transformer-based language models for the Sepedi language, focusing on the impact of occlusion-based training techniques.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Sepedi

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To analyze the implications of pre-training a Sepedi generative pre-trained model when only a relatively small dataset is available, specifically for text generation.

**Target Audience**:
- ML Researchers
- Linguistic Researchers

**Tasks**:
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: The SepMono dataset consists of various South African resources and the SepNews dataset is derived from radio news broadcasts.

**Size**: 432,970 sentences with 11,360,000 tokens

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Hyperparameter tuning
- Occlusion-based training
- Non-occlusion training

**Metrics**:
- Validation Loss
- Perplexity
- BLEU Score

**Calculation**: Metrics of validation loss and perplexity are calculated as per standard definitions; BLEU score compares generated text to reference text.

**Interpretation**: Lower validation loss and perplexity indicate better performance, while higher BLEU scores indicate higher quality of generated text.

**Baseline Results**: N/A

**Validation**: The datasets were partitioned into training, validation, and testing sets, with performance tracked during training.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Ethics
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
