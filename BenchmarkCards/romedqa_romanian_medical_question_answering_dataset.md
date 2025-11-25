# RoMedQA (Romanian Medical Question Answering Dataset)

## 📊 Benchmark Details

**Name**: RoMedQA (Romanian Medical Question Answering Dataset)

**Overview**: RoMedQA is the first dataset comprising medical exam questions in the Romanian language, containing 4,127 single-choice questions used in entrance examinations for medical schools in Romania.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- Romanian

**Resources**:
- [Resource](https://huggingface.co/datasets/craciuncg/RoMedQA_v1)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that aids in training and testing large language models in medical knowledge and language comprehension for Romanian.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: The dataset may inherit biases present in the source texts from which it was derived.

## 💾 Data

**Source**: Data was collected from medical universities' websites, including HTML format, PDF documents, and OCR scans.

**Size**: 4,127 examples

**Format**: JSON

**Annotation**: Manual annotation and extraction, including verification of incorrect OCR outputs.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy and F1 Score are calculated based on the effective answers compared to the correct ones in the dataset.

**Interpretation**: Higher scores indicate better model performance in answering medical questions correctly.

**Validation**: The dataset was manually inspected to ensure quality and reduce noise.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset aims to ensure diversity by collecting data from varied sources.

**Potential Harm**: ['Potential perpetuation of biases present in the training data.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data was sourced and processed to maintain confidentiality.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
