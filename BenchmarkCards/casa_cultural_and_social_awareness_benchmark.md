# CASA (Cultural and Social Awareness Benchmark)

## 📊 Benchmark Details

**Name**: CASA (Cultural and Social Awareness Benchmark)

**Overview**: CASA is a benchmark designed to assess LLM agents’ sensitivity to cultural and social norms across two web-based tasks: online shopping and social discussion forums. It evaluates the agents' ability to detect and appropriately respond to norm-violating queries and observations.

**Data Type**: user queries and observations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AGENT BENCH

**Resources**:
- [GitHub Repository](https://github.com/SalesforceAIResearch/CASA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLM agents' cultural and social awareness in web-based environments.

**Target Audience**:
- Researchers
- Developers

**Tasks**:
- Cultural Sensitivity Assessment
- Task Orientation

**Limitations**: N/A

## 💾 Data

**Source**: Generated user queries and observations based on cultural and social taxonomies across 17 countries.

**Size**: 1,225 user queries and 622 observations

**Format**: N/A

**Annotation**: Validated by expert annotators from their respective cultures.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Awareness Coverage Rate (AC-R)
- Educational Rate (Edu-R)
- Helpfulness Rate (Help-R)
- Violation Rate (Vio-R)

**Calculation**: Metrics are calculated based on agent responses to cultural and social norm violations.

**Interpretation**: A higher score in AC-R, Edu-R, and Help-R indicates better cultural sensitivity, while a higher Vio-R indicates the agent's failure to recognize misleading content.

**Baseline Results**: Current LLM agents show less than 10% awareness coverage and over 40% violation rates.

**Validation**: Evaluated through a comprehensive multi-step validation process.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Analysis across different cultural contexts.

**Potential Harm**: Potential for cultural insensitivity in agent responses.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
