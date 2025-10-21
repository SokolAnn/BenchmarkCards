# YAIR (Youth AI Risk)

## 📊 Benchmark Details

**Name**: YAIR (Youth AI Risk)

**Overview**: YAIR is the first benchmark dataset designed to evaluate and improve the safety of youth–LLM (Large Language Model) interactions, consisting of 12,449 annotated conversation snippets spanning 78 fine-grained risk types relevant to youth-specific harms.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WildGuard
- SafetyBench
- SALAD-Bench

**Resources**:
- [Resource](https://arxiv.org/abs/2509.08997)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to assess and enhance the safety of youth interactions with generative AI systems, improving risk detection frameworks in this domain.

**Target Audience**:
- ML Researchers
- AI Safety Developers
- Youth-support Organizations

**Tasks**:
- Risk Detection
- Risk Classification

**Limitations**: N/A

## 💾 Data

**Source**: The data comes from real-world chat logs collected from teenagers and synthetic data generated to reflect realistic youth-GenAI interaction scenarios.

**Size**: 12,449 snippets

**Format**: JSON

**Annotation**: Annotation was done through manual coding and machine-assisted methods involving experts in youth digital safety and AI ethics.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- F1 Score
- Area Under the Precision-Recall Curve (AUPRC)
- Precision
- Recall

**Calculation**: Metrics are calculated using standard classification metrics evaluating model performance on detection and classification tasks.

**Interpretation**: Higher metrics indicate better performance in risk detection and classification tasks tailored for youth-specific interactions.

**Baseline Results**: YouthSafe achieved an AUPRC of 0.9432, an F1 score of 0.8832, precision of 0.8799, and recall of 0.8865.

**Validation**: A combination of real-world data and carefully generated synthetic examples was used to ensure robust validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data was anonymized to protect participant identities, using natural language processing techniques to ensure compliance.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from parents and teens participating in the study.

**Compliance With Regulations**: The study adhered to IRB guidelines and ethical standards for research involving minors.
