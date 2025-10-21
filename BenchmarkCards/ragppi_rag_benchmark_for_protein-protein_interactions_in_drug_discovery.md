# RAGPPI (RAG Benchmark for Protein-Protein Interactions in Drug Discovery)

## 📊 Benchmark Details

**Name**: RAGPPI (RAG Benchmark for Protein-Protein Interactions in Drug Discovery)

**Overview**: RAGPPI is a factual question-answer benchmark of 4,420 question-answer pairs that focuses on the potential biological impacts of protein-protein interactions (PPIs).

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/Youngseung/RAGPPI)
- [GitHub Repository](https://github.com/youngseungjeon/RAGPPI)

## 🎯 Purpose and Intended Users

**Goal**: To support the research community in advancing RAG systems for drug discovery QA solutions.

**Target Audience**:
- ML Researchers
- Biomedical Researchers
- Drug Discovery Scientists

**Tasks**:
- Question Answering

**Limitations**: The number of samples may still be insufficient to cover the full range of biological impacts of PPIs.

## 💾 Data

**Source**: Constructed from expert-driven data annotation and generated with an ensemble auto-evaluation LLM.

**Size**: 4,420 question-answer pairs

**Format**: JSON

**Annotation**: Expert-driven data annotation combined with automated labeling.

## 🔬 Methodology

**Methods**:
- Expert evaluation
- Auto-evaluation with ensemble model

**Metrics**:
- Accuracy

**Calculation**: Predictions from three sub-models are aggregated through majority voting to assign labels.

**Interpretation**: Scores reflect the factual correctness of answers generated for protein-protein interaction questions.

**Baseline Results**: Achieved an accuracy of 93.71% in auto-evaluation.

**Validation**: Validated through user studies with domain experts.

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
