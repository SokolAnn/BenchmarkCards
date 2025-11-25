# Kvasir-VQA-x1

## 📊 Benchmark Details

**Name**: Kvasir-VQA-x1

**Overview**: Kvasir-VQA-x1 is a new, large-scale dataset for gastrointestinal (GI) endoscopy designed to benchmark reasoning-intensive visual question answering in medical contexts, incorporating 159,549 new question-answer pairs and a variety of visual augmentations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- Kvasir-VQA

**Resources**:
- [GitHub Repository](https://github.com/simula/Kvasir-VQA-x1)
- [Resource](https://huggingface.co/datasets/SimulaMet/Kvasir-VQA-x1)

## 🎯 Purpose and Intended Users

**Goal**: To develop a clinically relevant benchmark for visual question answering in medical imaging to improve AI application in gastroenterology.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- AI Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset builds upon the original Kvasir-VQA dataset, derived from HyperKvasir and Kvasir-Instrument, containing images from GI endoscopy procedures.

**Size**: 159,549 question-answer pairs

**Format**: JSON

**Annotation**: Generated and validated by medical experts to ensure clinical relevance.

## 🔬 Methodology

**Methods**:
- Automated metrics
- LLM-based adjudication

**Metrics**:
- ROUGE-L
- METEOR
- BLEU
- BERT-F1

**Calculation**: Metrics are calculated using established formulas providing insight into performance concerning ground truth.

**Interpretation**: Quantifying correct responses against set criteria, focusing on clinical reasoning capabilities.

**Baseline Results**: Performance evaluated against MedGemma and Qwen2.5-VL models.

**Validation**: Robustness tested through standard and transformed evaluation settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution Non Commercial 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
