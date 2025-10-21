# MEDCALC-BENCH

## 📊 Benchmark Details

**Name**: MEDCALC-BENCH

**Overview**: MEDCALC-BENCH is a first-of-its-kind dataset focused on evaluating the medical calculation capability of LLMs. It contains an evaluation set of over 1000 manually reviewed instances from 55 different medical calculation tasks. Each instance consists of a patient note, a question requesting to compute a specific medical value, a ground truth answer, and a step-by-step explanation showing how the answer is obtained.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedQA
- PubMedQA
- MedMCQA

**Resources**:
- [GitHub Repository](https://github.com/ncbi-nlp/MedCalc-Bench)
- [Resource](https://huggingface.co/datasets/ncbi/MedCalc-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark assessing the medical calculation capabilities of large language models.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Medical Calculation

**Limitations**: Limited dataset size of 1,047 instances may restrict comprehensive evaluation.

## 💾 Data

**Source**: The dataset was curated from publicly available patient notes and templates generated for various medical calculators.

**Size**: 1,047 instances

**Format**: JSON

**Annotation**: Manually reviewed by medical professionals.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: The evaluation scores are computed as the percentage of correct answers out of total questions.

**Interpretation**: Higher accuracy indicates better capability of the model in performing medical calculations.

**Baseline Results**: GPT-4 achieved the highest baseline performance of 50.9% accuracy using one-shot chain-of-thought prompting.

**Validation**: The dataset was meticulously curated with instances manually verified by medical professionals.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Only publicly available patient notes were used, with no identifiable personal health information.

**Data Licensing**: Released under the CC-BY-SA 4.0 license for non-commercial use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
