# EndoVis Conversations

## 📊 Benchmark Details

**Name**: EndoVis Conversations

**Overview**: The EndoVis Conversations dataset consists of numerous question-answer pairs based on surgical contexts, designed to enhance the performance of large vision-language models in understanding and reasoning within surgical scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- EndoVis-17-VQLA
- EndoVis-18-VQLA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the development and evaluation of personalized large vision-language models for effective visual question answering in surgery.

**Target Audience**:
- Researchers in AI and healthcare
- Robotic surgery professionals

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated from EndoVis-18-VQLA and EndoVis-17-VQLA datasets, utilizing surgical images and corresponding questions.

**Size**: 19,020 training images, 2,151 test images

**Format**: N/A

**Annotation**: Questions synthesized using GPT-4 based on images and annotations from the EndoVis datasets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Mean Intersection over Union (mIoU)

**Calculation**: Metrics are calculated based on the comparison between model predictions and ground truth data in surgical contexts.

**Interpretation**: Accuracy reflects the model's correct answers, F1 Score balances precision and recall, while mIoU assesses the intersection of predicted and true regions in images.

**Validation**: Evaluated against established benchmarks in surgical VQA tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
