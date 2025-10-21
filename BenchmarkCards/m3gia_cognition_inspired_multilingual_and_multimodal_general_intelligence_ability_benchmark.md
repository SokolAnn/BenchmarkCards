# M3GIA (Cognition Inspired Multilingual and Multimodal General Intelligence Ability Benchmark)

## 📊 Benchmark Details

**Name**: M3GIA (Cognition Inspired Multilingual and Multimodal General Intelligence Ability Benchmark)

**Overview**: M3GIA is the first cognition-driven multilingual and multimodal benchmark to evaluate the general intelligence ability of multilingual large language models (MLLMs), identifying five cognitive factors based on the Cattell-Horn-Carroll (CHC) model of intelligence and proposing a novel evaluation metric.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing
- Cognitive Science

**Languages**:
- English
- Chinese
- French
- Spanish
- Portuguese
- Korean

**Similar Benchmarks**:
- MMBench
- AGIEval

**Resources**:
- [Resource](https://huggingface.co/datasets/Songweii/M3GIA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the cognitive abilities and general intelligence of multilingual large language models.

**Target Audience**:
- AI Researchers
- Psychologists
- Model Developers

**Tasks**:
- Cognitive Ability Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Human participants collected data relevant to cultural backgrounds from native context.

**Size**: 1,800 questions

**Format**: Parquet

**Annotation**: Human-annotated and sourced from the Internet.

## 🔬 Methodology

**Methods**:
- Confirmatory Factor Analysis
- Statistical Analysis

**Metrics**:
- General Intelligence Accuracy (GIA)
- Accuracy

**Calculation**: GIA scores calculated using the CFA model derived from human evaluation data.

**Interpretation**: Results are interpreted based on accuracy and correlation to human performance.

**Baseline Results**: Human average performance across tests is established for comparison.

**Validation**: Model validation against human performance data using statistical methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache 2.0

**Consent Procedures**: Voluntary participation and anonymity in data collection.

**Compliance With Regulations**: Not Applicable
