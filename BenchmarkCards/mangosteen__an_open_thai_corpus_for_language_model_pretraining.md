# Mangosteen: An Open Thai Corpus for Language Model Pretraining

## 📊 Benchmark Details

**Name**: Mangosteen: An Open Thai Corpus for Language Model Pretraining

**Overview**: Mangosteen is a large-scale pre-training dataset for the Thai language, consisting of 47.4 billion tokens, developed to improve the quality and accessibility of Thai pre-training data for language models. The dataset is created using an adapted Dolma pipeline tailored to the Thai language, with sources including Common Crawl, Wikipedia, and government documents.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Thai

**Similar Benchmarks**:
- FineWeb2
- C4
- Dolma

**Resources**:
- [GitHub Repository](https://github.com/vistec-AI/Mangosteen)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality, reproducible Thai corpus for language model pretraining, addressing the linguistic and cultural specificities of the Thai language.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Language Model Pretraining

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from Common Crawl, Wikipedia, Creative Commons licensed content, legal documents, and other curated sources.

**Size**: 47.4 billion tokens

**Format**: Text files

**Annotation**: Automated filtering and cleaning processes using adapted pipelines.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Data ablation studies

**Metrics**:
- SEA-HELM
- Thai LLM Benchmark

**Calculation**: Metrics are calculated based on model performance evaluations on the SEA-HELM and Thai LLM benchmarks.

**Interpretation**: An increase in benchmark scores indicates improved dataset quality and model performance.

**Baseline Results**: A performance increase from 3 to approximately 11 points in the SEA-HELM benchmark.

**Validation**: Validated through systematic ablation studies demonstrating the contribution of each data cleaning step.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open-source license for dataset use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
