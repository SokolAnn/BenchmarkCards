# GLOBE SUMM

## 📊 Benchmark Details

**Name**: GLOBE SUMM

**Overview**: GLOBE SUMM is a benchmark dataset constructed for Multi-lingual, Cross-lingual, and Multi-document news summarization, addressing the challenges of redundancies, omissions, and conflicts in news reports.

**Data Type**: news articles and summaries

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- Chinese
- Russian
- Arabic
- French
- German
- Italian
- Japanese
- Hindi
- Korean
- Turkish
- Dutch
- Polish
- Ukrainian
- Romanian
- Swedish
- Finnish
- Danish
- Hungarian
- Greek
- Bulgarian
- Macedonian
- Vietnamese
- Thai
- Czech

**Similar Benchmarks**:
- MLSUM
- XL-Sum
- WikiLingua

**Resources**:
- [GitHub Repository](https://github.com/YYF-Tommy/GlobeSumm)

## 🎯 Purpose and Intended Users

**Goal**: To unify Multi-lingual, Cross-lingual and Multi-document Summarization into a single, coherent task, enabling better evaluation and handling of these complex challenges.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Model Developers

**Tasks**:
- Multi-lingual Summarization
- Cross-lingual Summarization
- Multi-document Summarization

**Limitations**: While omissions and conflicts can be alleviated, redundancies have not shown significant improvement.

## 💾 Data

**Source**: News reports collected from the GDELT database and curated for the GLOBE SUMM dataset.

**Size**: 4687 documents with a total of 4317 summaries

**Format**: N/A

**Annotation**: Summaries are generated using protocol-guided prompting and automatic processes.

## 🔬 Methodology

**Methods**:
- Chronological Recurrent Summarization
- KIS-then-CLP

**Metrics**:
- ROUGE
- Red
- Normalized Inverse of Coverage (NIC)
- Conflict Resolution Effectiveness (CRE)

**Calculation**: Metrics are calculated using established definitions for evaluating summarization quality and addressing specific conflicts.

**Interpretation**: Higher ROUGE and lower NIC indicate better summarization quality.

**Baseline Results**: Performance comparisons against existing multilingual datasets like MLSUM and XL-Sum.

**Validation**: Extensive manual verification and comparisons against human annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes various languages and news sources, addressing potential biases across demographics.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Publicly available news data has been used for the dataset; privacy measures are not explicitly stated.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
