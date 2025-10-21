# WebLists

## 📊 Benchmark Details

**Name**: WebLists

**Overview**: WebLists is a benchmark of 200 data-extraction tasks across four common business and enterprise use-cases, aimed at evaluating AI agents on interactive data extraction tasks from the web.

**Data Type**: structured data extraction tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WebVoyager
- WebArena
- Mind2Web

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To robustly measure whether an agent can extract structured data on a diverse set of websites.

**Target Audience**:
- ML Researchers
- Web Developers
- Data Scientists

**Tasks**:
- Data Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Manual tasks created from real-world data extraction use cases provided by customers of a commercial web automation provider.

**Size**: 200 tasks across 50 websites

**Format**: N/A

**Annotation**: Manually annotated reference solutions.

## 🔬 Methodology

**Methods**:
- Evaluation scripts for live websites
- Precision and recall metrics

**Metrics**:
- Recall
- Precision

**Calculation**: Recall is calculated as the percentage of gold set items extracted by the agent, precision as the percentage of agent-extracted items appearing in the gold set.

**Interpretation**: High recall ensures complete dataset extraction, while high precision identifies potential hallucinations.

**Baseline Results**: BardeenAgent achieves 66% recall overall, with a precision of 72%.

**Validation**: Evaluation was conducted by comparing agent outputs with manually extracted reference datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
