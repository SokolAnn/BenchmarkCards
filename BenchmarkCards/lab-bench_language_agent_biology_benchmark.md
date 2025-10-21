# LAB-Bench (Language Agent Biology Benchmark)

## 📊 Benchmark Details

**Name**: LAB-Bench (Language Agent Biology Benchmark)

**Overview**: LAB-Bench is a broad dataset of over 2,400 multiple choice questions designed to evaluate AI systems on practical biology research capabilities, including recall and reasoning over literature, interpretation of figures, access and navigation of databases, and comprehension and manipulation of DNA and protein sequences.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Biological Research

**Languages**:
- English

**Similar Benchmarks**:
- HELM
- BIG-Bench
- ChemBench

**Resources**:
- [Resource](https://huggingface.co/datasets/futurehouse/lab-bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide an evaluation dataset for the development of AI systems aimed at assisting with scientific research in biology.

**Target Audience**:
- ML Researchers
- Biology Researchers
- AI Developers

**Tasks**:
- Literature Search
- Protocol Planning
- Data Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from scientific literature and expert knowledge in biology, includes both programmatically and manually generated tasks.

**Size**: 2,400 questions

**Format**: JSON

**Annotation**: Manually annotated by biology experts and generated using algorithmic methods.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Coverage

**Calculation**: Metrics calculated based on correct answers out of total questions, with coverage as the ratio of questions answered to total questions.

**Interpretation**: Model performance is compared to expert human performance to gauge the utility of the AI systems.

**Baseline Results**: Baseline model performance reported against PhD-level biology researchers.

**Validation**: Ongoing assessment and improvement over time as new models and techniques emerge.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
