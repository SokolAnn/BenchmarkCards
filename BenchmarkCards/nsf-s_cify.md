# NSF-S CIFY

## 📊 Benchmark Details

**Name**: NSF-S CIFY

**Overview**: NSF-S CIFY is a large-scale dataset for scientific claim extraction derived from the National Science Foundation awards database, comprising over 400K grant abstracts and establishing grant proposals as a novel source for scientific claim extraction.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Science
- Mathematics

**Languages**:
- English

**Similar Benchmarks**:
- SciFACT
- PubHEALTH
- CLIMATE-FEVER
- HealthVer
- COVID-Fact

**Resources**:
- [Resource](https://huggingface.co/darpa-scify)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate large-scale scientific claim verification, discovery tracking, and meta-scientific research.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Scientific Claim Extraction
- Investigation Proposal Extraction
- Abstract Generation

**Limitations**: N/A

## 💾 Data

**Source**: NSF awards database

**Size**: 412,155 abstracts with an estimated 2.8 million claims

**Format**: JSON

**Annotation**: Automatically generated through zero-shot prompting with large language models.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- BERTScore
- ROUGE
- Precision
- Recall
- F1

**Calculation**: Metrics such as precision and recall are calculated based on comparisons between extracted claims and a gold standard using boolean functions with LLMs.

**Interpretation**: High scores on metrics indicate successful extraction and generation quality.

**Baseline Results**: Performance metrics significantly improve with fine-tuning, showing over 100% relative improvement for tasks.

**Validation**: The dataset is processed and filtered to ensure quality and consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
