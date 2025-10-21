# VSMRC (Vietnamese Text Segmentation and Multiple-Choice Reading Comprehension Dataset)

## 📊 Benchmark Details

**Name**: VSMRC (Vietnamese Text Segmentation and Multiple-Choice Reading Comprehension Dataset)

**Overview**: VSMRC is a comprehensive dataset that includes 15,942 documents for text segmentation and 16,347 synthetic multiple-choice question-answer pairs, specifically designed for Vietnamese natural language processing tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Vietnamese

**Similar Benchmarks**:
- ViMMRC 2.0
- UIT-ViQuAD

**Resources**:
- [Resource](https://huggingface.co/VSMRC)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified resource for Vietnamese text segmentation and multiple-choice reading comprehension tasks.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Segmentation
- Multiple-Choice Reading Comprehension

**Limitations**: N/A

## 💾 Data

**Source**: Vietnamese Wikipedia

**Size**: 15,942 documents and 16,347 questions

**Format**: N/A

**Annotation**: Generated with human quality assurance

## 🔬 Methodology

**Methods**:
- Automated metrics
- Expert evaluation

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics calculated based on precision and recall for text segmentation and correct choices for multiple-choice comprehension.

**Interpretation**: Higher scores indicate better performance in segmenting texts and accurately answering comprehension questions.

**Baseline Results**: mBERT achieved an accuracy of 88.01% on the MRC test set and an F1 score of 63.15% on the text segmentation test set.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
