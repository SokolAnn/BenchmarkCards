# SCI-Reason

## 📊 Benchmark Details

**Name**: SCI-Reason

**Overview**: SCI-Reason is a dataset for complex multimodal reasoning in academic areas, aiming to test and improve the reasoning ability of large multimodal models using real complex images in academic domains.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To bridge the gap in systematic investigation of complex multimodal reasoning in academic domains and assess the reasoning abilities of large multimodal models.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Visual Question Answering
- Multimodal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Academic image-text pairs extracted from PubMed Central's open-access repository.

**Size**: 12,626 question-answer pairs and 12,066 images

**Format**: N/A

**Annotation**: Expert-validated image descriptions and evidence-based scientific claims.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Average Normalized Levenshtein Similarity (ANLS)
- Wu-Palmer Similarity (WUPS)

**Calculation**: Accuracy is computed as the ratio of correct answers to total questions. ANLS measures answer similarity based on Levenshtein distance. WUPS assesses semantic similarity using WordNet hierarchy.

**Interpretation**: Higher scores indicate better reasoning performance in academic contexts.

**Baseline Results**: Claude-3.7-Sonnet with an accuracy of 55.19%.

**Validation**: Rigorous evaluation of multiple models on the test set to assess complex academic image reasoning.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
