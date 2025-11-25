# SciMMIR (Scientific Multi-Modal Information Retrieval)

## 📊 Benchmark Details

**Name**: SciMMIR (Scientific Multi-Modal Information Retrieval)

**Overview**: SciMMIR is a benchmark designed to evaluate multi-modal information retrieval (MMIR) models specifically in the scientific domain, featuring a dataset of 530K meticulously curated image-text pairs extracted from scientific documents.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Wusiwei0410/SciMMIR)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for MMIR models in the scientific domain.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Multi-modal Information Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Open-access research papers retrieved from arXiv.

**Size**: 530,000 image-text pairs

**Format**: N/A

**Annotation**: Annotated with a two-level subset-subcategory hierarchy based on the content.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Fine-tuned evaluations

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Hits@K

**Calculation**: Metrics are calculated based on the ranking of the golden answer within the set of candidates provided by the models.

**Interpretation**: Higher MRR and Hits@K indicate better retrieval performance.

**Baseline Results**: Performance results vary across multiple models tested.

**Validation**: Evaluated on training, validation, and test splits of 498,279, 16,433, and 16,263 samples respectively.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
