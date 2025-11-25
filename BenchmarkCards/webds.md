# WebDS

## 📊 Benchmark Details

**Name**: WebDS

**Overview**: WebDS is the first end-to-end web-based data science benchmark comprising 870 tasks across 29 diverse websites, challenging agents to perform complex, multi-step operations that reflect realistic data science workflows.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Data Science
- Web Navigation

**Languages**:
- English

**Similar Benchmarks**:
- WebVoyager
- GAIA
- InfiAgent-DABench

**Resources**:
- [Resource](https://arxiv.org/abs/2508.01222)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate AI agents on complex, web-based data science tasks.

**Target Audience**:
- AI Researchers
- Data Scientists
- Machine Learning Engineers

**Tasks**:
- Web Navigation
- Data Analysis
- Multi-Modal Reasoning

**Limitations**: Despite covering 870 tasks across 29 websites and 10 domains, it lacks full representation of some real-world applications.

## 💾 Data

**Source**: Data sourced from 29 diverse websites featuring structured and unstructured data.

**Size**: 870 tasks

**Format**: N/A

**Annotation**: Tasks were authored manually based on data science principles and requirements.

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Subjective evaluation via LLM judges

**Metrics**:
- Success Rate
- Quality scoring (1–5 scale)

**Calculation**: Success determined by comparing agent outputs to ground truth and using LLMs for qualitative scoring.

**Interpretation**: Scores between 1 and 5 where 5 fully satisfies the task requirements, and lower scores indicate lesser quality.

**Baseline Results**: Previous benchmarks on simpler tasks such as WebVoyager were used as comparisons.

**Validation**: Validation was achieved through a consistent Docker environment, ensuring reproducibility of evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
