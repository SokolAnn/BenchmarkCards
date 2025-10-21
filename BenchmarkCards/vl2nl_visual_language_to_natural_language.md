# VL2NL (Visual Language to Natural Language)

## 📊 Benchmark Details

**Name**: VL2NL (Visual Language to Natural Language)

**Overview**: VL2NL is a Large Language Model framework that generates rich and diverse natural language datasets using Vega-Lite specifications, aimed at streamlining the development of Natural Language Interfaces (NLIs) for data visualization.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Data Visualization

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/hyungkwonko/chart-llm)
- [Resource](https://hyungkwonko.info/chart-llm-data)

## 🎯 Purpose and Intended Users

**Goal**: To generate diverse NL datasets for enhancing Natural Language Interfaces (NLIs) for data visualization.

**Target Audience**:
- ML Researchers
- Visualization Researchers

**Tasks**:
- Caption Generation
- Utterance Generation
- Question Generation

**Limitations**: N/A

## 💾 Data

**Source**: Vega-Lite specifications from GitHub.

**Size**: 1,981 specifications

**Format**: JSON

**Annotation**: Manually inspected for validity.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is evaluated based on strict and lenient criteria for the correctness of chart semantics and generated captions.

**Interpretation**: Achieved an accuracy of 89.4% for chart semantics and 76.0% for L1 captions under strict criteria.

**Baseline Results**: N/A

**Validation**: Validated through quantitative and qualitative analyses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: ['N/A']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
