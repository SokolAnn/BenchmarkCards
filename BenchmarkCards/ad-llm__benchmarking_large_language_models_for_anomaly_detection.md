# AD-LLM: Benchmarking Large Language Models for Anomaly Detection

## 📊 Benchmark Details

**Name**: AD-LLM: Benchmarking Large Language Models for Anomaly Detection

**Overview**: AD-LLM is the first benchmark that evaluates how large language models (LLMs) can assist in natural language processing anomaly detection through three key tasks: zero-shot detection, data augmentation, and model selection.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/USC-FORTIS/AD-LLM)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance the effectiveness of large language models in anomaly detection tasks within natural language processing.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Domain Experts

**Tasks**:
- Zero-Shot Anomaly Detection
- Data Augmentation
- Model Selection

**Limitations**: The evaluation is constrained to a narrow set of datasets with clear normal-anomaly distinctions.

## 💾 Data

**Source**: Five NLP AD datasets sourced from literature, including AG News, BBC News, IMDB Reviews, N24 News, SMS Spam.

**Size**: 5 datasets

**Format**: Text

**Annotation**: Normal categories with one designated anomaly category; training data includes only normal samples.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Area Under the Receiver Operating Characteristic Curve (AUROC)
- Area Under the Precision-Recall Curve (AUPRC)

**Calculation**: Metrics are calculated as the area under specified curves, which are comparative evaluations across different anomaly detection methods.

**Interpretation**: Higher AUROC and AUPRC values indicate better performance in distinguishing between normal and anomalous samples.

**Baseline Results**: Compared LLM-based AD with 18 traditional unsupervised methods.

**Validation**: Results validated through tests on multiple datasets, demonstrating LLM's performance across the benchmark tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: Analysis of anomaly detection performance may vary across different demographic groups based on LLM outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
