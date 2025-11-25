# Doc-750K

## 📊 Benchmark Details

**Name**: Doc-750K

**Overview**: Doc-750K is a high-quality document-level dataset designed to support in-depth understanding of multimodal documents, featuring diverse document structures and extensive cross-page dependencies with real question-answer pairs derived from the original documents.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- DocVQA
- MP-DocVQA
- MMLongbench-Doc
- DocGenome

**Resources**:
- [GitHub Repository](https://github.com/OpenGVLab/Docopilot)

## 🎯 Purpose and Intended Users

**Goal**: To develop a large-scale dataset and model for document-level multimodal understanding, enhancing the ability to integrate and comprehend information across multi-page documents.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multi-Page Question Answering
- Single-Page Question Answering
- Abstract Writing
- Caption Writing
- Paper Titling

**Limitations**: The dataset currently has a domain restriction to academic documents and intends to expand to a broader range of document types.

## 💾 Data

**Source**: Data collected from Sci-Hub, Arxiv, and OpenReview.

**Size**: 758,000 question-answer samples

**Format**: Interleaved Text-Image Format and Multi-Image Format

**Annotation**: Real, in-depth question-answer pairs collected and constructed based on document structure.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Evaluation on several document-level benchmarks

**Metrics**:
- Accuracy
- F1 Score
- ANLS
- Relaxed Exact Match

**Calculation**: Metrics are calculated based on the similarity between model responses and ground truth answers.

**Interpretation**: Higher scores indicate better model performance in retrieving accurate and relevant information from the documents.

**Baseline Results**: Docopilot-8B achieved a score of 61.8 on MM-NIAH, outperforming baseline models.

**Validation**: Evaluated against multiple existing benchmarks for robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data processed publicly available documents ensuring no sensitive personal information is included.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
