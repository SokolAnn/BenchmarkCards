# POLAR

## 📊 Benchmark Details

**Name**: POLAR

**Overview**: POLAR is a multilingual, multicultural, and multievent dataset for fine-grained polarization detection spanning seven languages from diverse online platforms and real-world events. It introduces a taxonomy of polarization types and manifestations, operationalized through a robust cross-lingual annotation protocol.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Social Science

**Languages**:
- Amharic
- Arabic
- English
- German
- Hausa
- Spanish
- Urdu

**Resources**:
- [Resource](https://arxiv.org/abs/2505.20624)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for multilingual, multicultural, and multievent online polarization detection.

**Target Audience**:
- ML Researchers
- Social Scientists
- Policy Makers

**Tasks**:
- Binary Polarization Detection
- Polarization Type Classification
- Manifestation Identification

**Limitations**: While POLAR is a significant step towards multilingual polarization analysis, potential issues with annotator understanding and variability might impact label quality.

## 💾 Data

**Source**: Data collected from various online platforms, including Twitter/X, Facebook, BlueSky, Reddit, and local news outlets.

**Size**: 23,000 instances

**Format**: N/A

**Annotation**: Cross-cultural annotation protocol tailored for each language's sociopolitical context, using both expert and crowdsourced annotators.

## 🔬 Methodology

**Methods**:
- Fine-tuning Multilingual Language Models (MLMs)
- Evaluating Large Language Models (LLMs) in Zero- and Few-shot Settings

**Metrics**:
- F1 Score
- Macro F1 Score
- Accuracy

**Calculation**: Metrics calculated based on the performance of models across three tasks in both monolingual and cross-lingual setups.

**Interpretation**: Higher F1 Score indicates better performance in detecting polarization, with different scores highlighting challenges in classifying types and manifestations.

**Baseline Results**: RemBERT achieved the highest F1 scores for many languages in binary polarization classification.

**Validation**: Performance was validated through testing on separate dataset splits designated for training, validation, and testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Analysis explores how polarization dynamics are shaped by linguistic, cultural, and contextual variables across different regions.

**Potential Harm**: Potential emotional distress for annotators due to the sensitive nature of the content.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: This research used publicly available, anonymized data, with measures to ensure ethical guidelines were followed during annotation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Annotators were informed of the project's goals and could opt out at any time.

**Compliance With Regulations**: Not Applicable
