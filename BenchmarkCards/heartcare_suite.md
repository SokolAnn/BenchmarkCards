# Heartcare Suite

## 📊 Benchmark Details

**Name**: Heartcare Suite

**Overview**: Heartcare Suite is a multimodal comprehensive framework for fine-grained electrocardiogram (ECG) understanding, comprising the Heartcare-220K dataset and Heartcare-Bench evaluation framework to optimize and evaluate Medical Multimodal Large Language Models (Med-MLLMs) in ECG scenarios.

**Data Type**: multimodal

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- PTB-XL

**Resources**:
- [GitHub Repository](https://github.com/DCDmllm/Heartcare-Suite)

## 🎯 Purpose and Intended Users

**Goal**: To establish a unified and scalable framework for evaluating and improving ECG understanding in medical applications using multimodal instruction datasets and benchmarks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Medical Professionals

**Tasks**:
- Closed Question Answering
- Open Question Answering
- Report Generation
- Signal Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Heartcare-220K dataset, including ECG signals and clinical report images collected from public hospitals and existing ECG datasets.

**Size**: 220,000 ECG examples

**Format**: JSON

**Annotation**: Automated annotation using a multi-agent data engine and expert review for clinical relevance.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- ROUGE-L

**Calculation**: Metrics are calculated based on performance against predefined clinical tasks like diagnosis classification and waveform analysis.

**Interpretation**: Higher accuracy and F1 scores indicate better model performance across ECG related tasks, with clinical correctness as a primary concern.

**Baseline Results**: HeartcareGPT shows superior performance compared to existing models like MedVLM and Claude-3.5 on various ECG tasks.

**Validation**: Evaluation is conducted using a multi-dimensional framework tailored for specific ECG tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Analysis of patient demographics in the dataset shows diverse representation across age and sex.

**Potential Harm**: ['Potential biases in diagnosis due to underrepresentation of rare conditions.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Patient data is anonymized, and all personal identifiers are removed during data collection and annotation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
