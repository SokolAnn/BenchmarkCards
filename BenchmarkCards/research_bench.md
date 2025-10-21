# RESEARCH BENCH

## 📊 Benchmark Details

**Name**: RESEARCH BENCH

**Overview**: RESEARCH BENCH is a benchmark that evaluates the quality of research community simulation in RESEARCH TOWN, utilizing a node-masking prediction task for scalable and objective assessment based on similarity. It includes 1,000 paper writing tasks and 200 review writing tasks requiring multi-agent collaboration.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Criminology
- Biology
- Astrophysics

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/ulab-ai/research-bench)
- [GitHub Repository](https://github.com/ulab-uiuc/research-town)

## 🎯 Purpose and Intended Users

**Goal**: To provide a framework for evaluating the simulation of human research communities by examining collaborative research activities.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Paper Writing
- Review Writing

**Limitations**: N/A

## 💾 Data

**Source**: Comprehensive dataset of 1,000 paper writing tasks and 200 review writing tasks sourced from recent top-tier machine learning conferences such as NeurIPS 2024 and ICLR 2024.

**Size**: 1,200 papers for initial collection, with 1,000 randomly sampled for benchmark

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Average Precision (MAP)
- Embedding-based similarity scores

**Calculation**: Metrics are calculated using the similarity between generated research outputs and ground truth using state-of-the-art embedding models.

**Interpretation**: Results are interpreted based on similarity scores, with higher scores indicating a better alignment with real-world data.

**Baseline Results**: Scores achieved included an average similarity score of 0.68 for paper writing and 0.49 for review writing.

**Validation**: The framework employs comparison with real-world research activities to validate the accuracy of the simulation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Impact on education: bypassing learning

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for facilitating research plagiarism and producing misleading or low-quality claims.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
