# CEBench

## 📊 Benchmark Details

**Name**: CEBench

**Overview**: CEBench is an open-source toolkit specifically designed for multi-objective benchmarking that focuses on the critical trade-offs between expenditure and effectiveness required for LLM deployments.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/amademicnoboday12/CEBench)

## 🎯 Purpose and Intended Users

**Goal**: To address the shortcomings of existing benchmarking toolkits by providing a way to evaluate the cost-effectiveness of LLM deployments.

**Target Audience**:
- Industry Practitioners
- Model Developers
- Research Communities

**Tasks**:
- Benchmarking
- Model Evaluation

**Limitations**: Latency estimation based on GPU performance is not sufficiently accurate.

## 💾 Data

**Source**: Open-source and public datasets, including DAIC-WOZ and ContractNLI.

**Size**: 187 dialogues (DAIC-WOZ dataset) and unspecified for others.

**Format**: Various formats including text.

**Annotation**: Data from existing datasets is typically obtained (e.g., interviews, contracts).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Mean Absolute Error (MAE)
- F1 Score
- Latency

**Calculation**: Metrics calculated based on model performance during the benchmarks.

**Interpretation**: Lower MAE and higher F1 scores indicate better performance.

**Validation**: The toolkit supports zero-code execution, facilitating easy benchmarking.

## ⚠️ Targeted Risks

**Risk Categories**:
- Cost-Effectiveness
- Efficiency

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymization procedures are followed by dataset providers.

**Data Licensing**: All resources used in this work are open-source resources.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
