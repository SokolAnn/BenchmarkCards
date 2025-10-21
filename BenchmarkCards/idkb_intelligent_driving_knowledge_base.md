# IDKB (Intelligent Driving Knowledge Base)

## 📊 Benchmark Details

**Name**: IDKB (Intelligent Driving Knowledge Base)

**Overview**: IDKB is a large-scale vision-language dataset that includes over one million data items related to driving theory and practical knowledge, including traffic laws, rules, and driving techniques, aiming to enhance the capabilities of Large Vision-Language Models (LVLMs) in the context of autonomous driving.

**Data Type**: mixed (question-answering and multiple-choice questions)

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Chinese
- Italian
- German
- Spanish
- French
- Korean
- Japanese

**Resources**:
- [Resource](https://4dvlab.github.io/project_page/idkb.html)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating the performance of LVLMs in understanding driving knowledge, including theory and practical applications.

**Target Audience**:
- Research Scientists
- Model Developers
- Industry Practitioners

**Tasks**:
- Multiple Choice Question
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Driving handbooks, theory test data, and simulated road test data collected from multiple countries.

**Size**: 1,016,956 total data entries

**Format**: mixed (QA and MCQ formats)

**Annotation**: Data collected from various driving manuals and test questions, processed using layout detection and Optical Character Recognition (OCR), with manual reviews for quality control.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- SemScore
- ROUGE-1
- ROUGE-L

**Calculation**: The overall accuracy is calculated as a weighted average of single-choice and multiple-choice questions for Test Data and Road Data scores. The IDKB score is the average of these two.

**Interpretation**: Higher scores indicate better understanding and mastery of driving knowledge by the LVLMs.

**Baseline Results**: IDKB Score (Top Model): 0.64 (GPT-4o), 0.45 (XComposer2)

**Validation**: Extensive evaluation of 15 LVLMs using IDKB with rigorous cross-validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: The dataset incorporates driving knowledge from 15 different countries, encompassing diverse driving rules and languages.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
