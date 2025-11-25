# Thai-H6 and Thai Cultural and Linguistic Intelligence Benchmark (ThaiCLI)

## 📊 Benchmark Details

**Name**: Thai-H6 and Thai Cultural and Linguistic Intelligence Benchmark (ThaiCLI)

**Overview**: Two comprehensive benchmarks aimed at advancing LLM research in Thai: Thai-H6 evaluates reasoning, knowledge, and commonsense capabilities, while ThaiCLI assesses understanding of Thai cultural norms and values.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Thai

**Similar Benchmarks**:
- MMLU
- TruthfulQA
- HellaSwag
- AI2 Reasoning Challenge (ARC)
- Winograd Schema Challenge (Winogrande)
- Grade School Math (GSM8k)

**Resources**:
- [GitHub Repository](https://github.com/UpstageAI/ThaiCLI_H6)

## 🎯 Purpose and Intended Users

**Goal**: To create evaluation frameworks that rigorously assess core capabilities and cultural alignment of Thai LLMs.

**Target Audience**:
- ML Researchers
- NLP Developers
- Cultural Analysts

**Tasks**:
- Question Answering
- Cultural Understanding Assessment

**Limitations**: The benchmark may not fully capture the rich diversity of perspectives within Thai society, affecting consistency of evaluation outcomes.

## 💾 Data

**Source**: Constructed from various existing datasets adapted for Thai context

**Size**: Total of over 26,000 samples across all datasets

**Format**: JSON

**Annotation**: Human annotation by native Thai speakers with multi-round review for cultural alignment and accuracy

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Log-probability evaluation
- Exact match score

**Calculation**: Metrics are calculated based on log-probability and exact match protocols as detailed in the methodology section.

**Interpretation**: Scores reflect models' capacities to handle reasoning, knowledge, and cultural alignment tasks appropriate for Thai contexts.

**Baseline Results**: Performance on Thai-H6 and ThaiCLI benchmarks, as evaluated across various LLMs.

**Validation**: Validated through expert reviews and multi-step annotation processes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis of cultural sensitivity and appropriateness based on demographic contexts.

**Potential Harm**: ['Reinforcement of cultural stereotypes', 'Misrepresentation of cultural norms']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data collected ensures participants' anonymity and respects cultural sensitivities.

**Data Licensing**: Open access under appropriate licensing agreements ensuring compliance with ethical standards.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: All data practices adhere to local and international data protection regulations.
