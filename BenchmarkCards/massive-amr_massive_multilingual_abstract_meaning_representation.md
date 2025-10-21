# MASSIVE-AMR (Massive Multilingual Abstract Meaning Representation)

## 📊 Benchmark Details

**Name**: MASSIVE-AMR (Massive Multilingual Abstract Meaning Representation)

**Overview**: MASSIVE-AMR is a dataset containing more than 84,000 text-to-graph annotations, currently the largest and most diverse of its kind, providing AMR graphs for 1,685 information-seeking utterances mapped to 50+ typologically diverse languages.

**Data Type**: text-to-graph annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- French
- German
- Italian
- Lithuanian
- Vietnamese
- Japanese
- Korean
- Hungarian
- Urdu
- Amharic
- Azeri
- Finnish

**Similar Benchmarks**:
- QALD9-AMR

**Resources**:
- [GitHub Repository](https://github.com/amazon-science/MASSIVE-AMR)

## 🎯 Purpose and Intended Users

**Goal**: To create the largest-scale multilingual AMR question corpus to date and to improve structured parsing and SPARQL relation hallucination detection using large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Structured Parsing
- Hallucination Detection

**Limitations**: N/A

## 💾 Data

**Source**: MASSIVE dataset and manual annotations for AMR graphs.

**Size**: 84,000 annotations

**Format**: N/A

**Annotation**: Manual annotation by trained professionals for AMR graphs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on the accuracy of produced AMR outputs and SPARQL query executions.

**Interpretation**: A higher F1 Score indicates better performance of language models in parsing AMRs and SPARQL queries.

**Baseline Results**: N/A

**Validation**: Validation procedures were implemented to ensure the quality and consistency of AMR annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Informed consent was ensured for all annotators, detailing purpose and usage of their data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Annotations were conducted with informed individuals, ensuring fair compensation for their work.

**Compliance With Regulations**: Not Applicable
