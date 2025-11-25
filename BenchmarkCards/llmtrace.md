# LLMTrace

## 📊 Benchmark Details

**Name**: LLMTrace

**Overview**: LLMTrace is a large-scale, bilingual corpus designed to support two key tasks: traditional full-text binary classification (human vs. AI) and AI-generated interval detection, facilitated by character-level annotations.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Russian

**Similar Benchmarks**:
- MAGE
- MGTBench
- BUST

**Resources**:
- [Resource](https://huggingface.co/iitolstykh/LLMTrace)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate a new wave of research into more nuanced, practical, and robust AI detection models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Binary Classification
- Interval Detection

**Limitations**: N/A

## 💾 Data

**Source**: Constructed using a diverse range of modern proprietary and open-source LLMs.

**Size**: 589,086 examples

**Format**: N/A

**Annotation**: Character-level annotations marking all AI-generated spans within mixed texts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Mean Accuracy
- Mean Average Precision (mAP)

**Calculation**: Metrics are calculated based on the evaluation of models against train, validation, and test subsets.

**Interpretation**: Metrics indicate the model's performance in classifying text as human or AI-generated, as well as correctly identifying intervals of AI-generated content.

**Baseline Results**: F1 scores for the classification tasks are reported as follows: English-only model F1: 98.64%, Russian-only model F1: 98.62%. Detection task mAP@0.5 for English-only is 0.8749 and for Russian-only is 0.8928.

**Validation**: Validated through domain and length balanced sampling strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
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
