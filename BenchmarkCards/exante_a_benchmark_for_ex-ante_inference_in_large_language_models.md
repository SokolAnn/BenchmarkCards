# ExAnte (A Benchmark for Ex-Ante Inference in Large Language Models)

## 📊 Benchmark Details

**Name**: ExAnte (A Benchmark for Ex-Ante Inference in Large Language Models)

**Overview**: ExAnte introduces a benchmark designed to evaluate the ability of large language models (LLMs) to reason while adhering to temporal constraints, specifically assessing their capabilities in making predictions or inferences without access to future events.

**Data Type**: question-answering pairs, event predictions, atomic facts generation

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- TRAM
- TimeBench

**Resources**:
- [Resource](https://huggingface.co/datasets/yachuanliu/ExAnte)
- [GitHub Repository](https://github.com/yachuan/ExAnte)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of ExAnte is to evaluate the temporal reasoning capabilities of large language models when responding to time-sensitive queries, enforcing strict temporal cutoffs for model outputs.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Question Answering
- Event Prediction
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Diverse datasets including stock market data, Wikipedia events, and scientific publications curated for ex-ante inference tasks.

**Size**: 1757 examples for Stock dataset, 304 for QA dataset, 630 for Wikipedia dataset, 98 for Publication dataset.

**Format**: CSV

**Annotation**: Annotated by human reviewers and automated checks for temporal adherence.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Model-based evaluation

**Metrics**:
- Leakage rate
- Mean Absolute Error (MAE)

**Calculation**: Leakage rate is calculated as the proportion of queries with temporal leakage across datasets, while MAE is computed comparing model predictions to actual values.

**Interpretation**: A lower leakage rate indicates better adherence to temporal constraints, while MAE provides insight into prediction accuracy.

**Baseline Results**: Baseline coverage across different models (GPT-4o, Gemini 1.5 Pro, Claude 3.5) shows significant variations in leakage rates under various prompting strategies.

**Validation**: The benchmark is validated using a mixture of quantitative leakage assessments and qualitative evaluations by domain experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Privacy**: Personal information in prompt

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misuse in time-sensitive decision-making or predictions without adequately addressing temporal adherence.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is anonymized and aggregated where applicable.

**Data Licensing**: N/A - Dataset licensing details are not specified in the paper.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
