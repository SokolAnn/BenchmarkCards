# Danoliterate Benchmark

## 📊 Benchmark Details

**Name**: Danoliterate Benchmark

**Overview**: The Danoliterate Benchmark evaluates Danish language and cultural competency across diverse scenarios such as citizenship tests and social media question answering.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Danish

**Similar Benchmarks**:
- ScandEval

**Resources**:
- [GitHub Repository](https://github.com/sorenmulli/danoliterate)
- [Resource](https://danoliterate.compute.dtu.dk/Leaderboard)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of Generative Large Language Models in Danish across multiple tasks.

**Target Audience**:
- ML Researchers
- Language Technologists
- Industry Practitioners

**Tasks**:
- Natural Language Understanding
- Natural Language Generation

**Limitations**: N/A

## 💾 Data

**Source**: Eight scenario datasets created specifically for the benchmark, including the Citizenship Test and others derived from existing resources.

**Size**: 605 multiple-choice questions, 125 questions from HellaSwag, and various other datasets with several hundred examples each.

**Format**: N/A

**Annotation**: Manual translations and extractions conducted by the research team.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy calculated based on the frequency of correct model responses across multiple-choice questions.

**Interpretation**: Higher accuracy indicates better Danoliteracy of the model in handling Danish language tasks.

**Baseline Results**: GPT-4 and Claude Opus ranked highest in the evaluation.

**Validation**: Used bootstrapping techniques to validate the robustness of the benchmark results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Misuse**: Spreading disinformation

**Demographic Analysis**: The benchmark results include analysis based on user feedback from Danish speakers.

**Potential Harm**: The benchmark aims to minimize the risk of bias and maximize fairness in model evaluations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is anonymized to remove personally identifiable information particularly in social media scenarios.

**Data Licensing**: Datasets have different licensing agreements, both open and restricted.

**Consent Procedures**: Written permissions were obtained for using certain datasets.

**Compliance With Regulations**: Not Applicable
