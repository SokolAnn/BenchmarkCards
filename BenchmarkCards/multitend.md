# MultiTEND

## 📊 Benchmark Details

**Name**: MultiTEND

**Overview**: MultiTEND is the first and largest multilingual benchmark for natural language to NoSQL query generation, covering six languages: English, German, French, Russian, Japanese, and Mandarin Chinese. It analyzes challenges in translating natural language to NoSQL queries across diverse linguistic structures.

**Data Type**: natural language queries to NoSQL queries

**Domains**:
- Natural Language Processing
- Database Management

**Languages**:
- English
- German
- French
- Russian
- Japanese
- Mandarin Chinese

**Similar Benchmarks**:
- TEND
- Spider
- nvBench

**Resources**:
- [Resource](https://arxiv.org/abs/2502.11022)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for assessing multilingual natural language to NoSQL query translation systems, facilitating research and development in this area.

**Target Audience**:
- ML Researchers
- Database Developers
- AI Practitioners

**Tasks**:
- Query Generation
- Machine Translation

**Limitations**: The dataset is limited to six languages, which only cover a portion of the mainstream languages within the Indo-European and Sino-Tibetan language families.

## 💾 Data

**Source**: MultiTEND dataset derived from a semi-automated construction process combining machine-generated data and manual verification.

**Size**: 101,789 NLQ to NoSQL query pairs

**Format**: N/A

**Annotation**: Combination of machine-generated and human-verified translations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- Execution Accuracy (EX)

**Calculation**: Metrics were calculated based on the percentage of generated queries that matched the ground truth queries exactly and those that executed correctly against the NoSQL database.

**Interpretation**: Higher values in EM and EX indicate better performance; a successful query generation results in queries that conform to the expected structure and produce accurate execution results.

**Baseline Results**: Comparison with other models like SMART and Zero-shot LLMs showed MultiLink's performance improvements of approximately 5% to 20%.

**Validation**: Extensive experiments demonstrated its challenging nature and the effectiveness of the proposed model.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes demographic factors, as it covers linguistic diversity across six languages.

**Potential Harm**: ['Inequity in access for speakers of underrepresented languages.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
