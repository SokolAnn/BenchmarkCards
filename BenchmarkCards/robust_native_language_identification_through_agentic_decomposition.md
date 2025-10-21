# Robust Native Language Identification through Agentic Decomposition

## 📊 Benchmark Details

**Name**: Robust Native Language Identification through Agentic Decomposition

**Overview**: This work investigates the tendency of large language models (LLMs) to rely on superficial clues and take shortcuts in the native language identification (NLI) task. It introduces an agentic NLI pipeline to enhance robustness against misleading contextual clues. The approach enhances NLI robustness by using a structured methodology where specialized agents analyze distinct linguistic features, culminating in a final predictive assessment.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ETS Corpus of Non-Native Written English (TOEFL11)
- Write & Improve Corpus 2024

**Resources**:
- [GitHub Repository](https://github.com/projectauch/agents-nli)

## 🎯 Purpose and Intended Users

**Goal**: To develop a robust method for native language identification (NLI) that mitigates biases from superficial contextual clues in language models.

**Target Audience**:
- ML Researchers
- Forensic Linguists
- Language Identification Practitioners

**Tasks**:
- Native Language Identification

**Limitations**: N/A

## 💾 Data

**Source**: Two benchmark datasets: ETS Corpus of Non-Native Written English (TOEFL11) and Write & Improve Corpus 2024.

**Size**: 400 essays from Write & Improve corpus and 440 essays from the TOEFL4 subset.

**Format**: JSON

**Annotation**: The essays are labeled with native language (L1) metadata.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro-averaged F1 Score
- Accuracy

**Calculation**: Computed based on classifications across various experimental conditions.

**Interpretation**: Higher values indicate better performance consistency and robustness in NLI tasks.

**Baseline Results**: The agentic approach exhibited greater consistency but slightly lower peak accuracy than baseline direct prompting methods.

**Validation**: Evaluated using adversarial experiments with misleading contextual hints.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning, Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The datasets utilized contain no personally identifiable information.

**Data Licensing**: The use of L2 English learner corpora strictly adhered to their respective licensing terms.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
