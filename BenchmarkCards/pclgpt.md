# PclGPT

## 📊 Benchmark Details

**Name**: PclGPT

**Overview**: PclGPT is a comprehensive LLM benchmark designed specifically for detecting patronizing and condescending language (PCL) targeting vulnerable groups. It integrates a dataset collection and annotation process to enhance the performance of language models in identifying implicit toxic language.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/dut-laowang/emnlp24-PclGPT)

## 🎯 Purpose and Intended Users

**Goal**: Enhance detection of patronizing and condescending language directed at vulnerable communities using a specialized benchmark and model.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Text Classification

**Limitations**: The study lacks examination of false positive cases and requires further linguistic foundation to refine the definition of PCL.

## 💾 Data

**Source**: Community data collected from mainstream internet platforms like Reddit and Sina Weibo, structured into specific datasets for training and testing.

**Size**: 1,409,945 entries (Pre-training), 31,969 entries (Fine-tuning)

**Format**: N/A

**Annotation**: Data was manually annotated by a team of experts, leveraging hierarchical structured annotations to ensure quality.

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning
- Pre-training

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: The metrics are calculated using macro-average methods based on the performance of the model across the test datasets.

**Interpretation**: Higher scores in precision, recall, and F1 indicate better detection capabilities of the model.

**Baseline Results**: PclGPT-EN achieved an F1 score of 81.1 on DPM dataset and 88.9 on TD dataset, demonstrating significant improvements over baseline models.

**Validation**: The benchmark was validated using a series of tests on English and Chinese datasets comparing it with traditional PLMs and advanced LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes analysis across various demographic groups, highlighting the varying biases in PCL detection.

**Potential Harm**: The benchmark aims to minimize the harm caused by implicit toxicity against vulnerable groups through improved detection methods.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collection procedures followed community privacy agreements, and user-sensitive information was replaced to comply with ethical standards.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
