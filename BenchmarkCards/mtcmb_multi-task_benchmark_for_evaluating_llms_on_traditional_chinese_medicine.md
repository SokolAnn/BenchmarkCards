# MTCMB (Multi-Task Benchmark for Evaluating LLMs on Traditional Chinese Medicine)

## 📊 Benchmark Details

**Name**: MTCMB (Multi-Task Benchmark for Evaluating LLMs on Traditional Chinese Medicine)

**Overview**: MTCMB is a multi-task benchmark for evaluating large language models on Traditional Chinese Medicine (TCM) knowledge, reasoning, and safety, designed to fill gaps in existing benchmarks by providing a more comprehensive evaluation framework.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/Wayyuanyuan/MTCMB)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous evaluation framework for assessing and guiding the development of TCM-capable AI systems.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Knowledge Question Answering
- Language Understanding
- Diagnosis
- Prescription Recommendation
- Safety Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Curated datasets from authoritative sources including national licensing exams, clinical case records, and classical TCM texts.

**Size**: N/A

**Format**: N/A

**Annotation**: Expert-verified and curated in collaboration with certified TCM practitioners.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- BERT Score
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are calculated based on the match of predicted outputs to ground truth reference answers.

**Interpretation**: Higher scores indicate better performance of LLMs in accurately handling TCM-specific tasks.

**Baseline Results**: N/A

**Validation**: Comprehensive validation through expert review and performance analysis across various LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
