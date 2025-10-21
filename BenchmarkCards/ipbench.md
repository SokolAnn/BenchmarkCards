# IPBench

## 📊 Benchmark Details

**Name**: IPBench

**Overview**: IPBench provides a comprehensive IP task taxonomy and a large-scale bilingual benchmark with 10,374 data points across 20 distinct tasks designed to evaluate large language models in real-world intellectual property scenarios.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- PatentEval
- MoZIP
- IPEval

**Resources**:
- [Resource](https://ipbench.wangqiyao.me/)
- [GitHub Repository](https://github.com/IPBench/IPBench)
- [Resource](https://huggingface.co/datasets/IPBench/IPBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust evaluation framework for large language models in the complex and nuanced field of intellectual property, facilitating advancements in NLP applications.

**Target Audience**:
- ML Researchers
- Model Developers
- Legal Practitioners

**Tasks**:
- Legal Concept Memory
- Legal Clause Memory
- Legal Evolution
- Typical Case Memory
- Patent IPC Classification
- Patent CPC Classification
- IP Element Identification
- Process Guidance
- Patent Technology Forecasting
- Infringement Behavior Determination
- Compensation Calculation
- Patent Valuation
- Trade Secret Requirements
- Patent Document Proofreading
- Patent Validity Identification
- Patent Match
- Rights Attribution Analysis
- Patent Application Examination
- Abstract Generation
- Dependent Claim Generation
- Design-Around Solution Generation

**Limitations**: N/A

## 💾 Data

**Source**: Data constructed from expert-curated annotations, databases from national IP offices, and publicly available datasets.

**Size**: 10,374 examples

**Format**: JSON

**Annotation**: Annotated by a team of trained experts under supervised protocols.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L
- BERTScore

**Calculation**: Metrics were calculated based on performance across various tasks, including precision in classification and generation tasks.

**Interpretation**: High scores generally indicate superior performance in handling IP-related tasks, according to established benchmarks.

**Validation**: IPBench was validated through comprehensive evaluations of 17 leading language models across IP tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack, Data poisoning

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data used in the development of IPBench was sourced from publicly available, non-commercial datasets.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
