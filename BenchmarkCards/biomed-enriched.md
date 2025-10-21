# Biomed-Enriched

## 📊 Benchmark Details

**Name**: Biomed-Enriched

**Overview**: Biomed-Enriched is a biomedical text dataset constructed from PubMed via a two-stage annotation process to enable refined extraction of high-quality clinical and educational content. It provides an openly available collection of clinical cases and demonstrates targeted performance improvements for biomedical NLP tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English
- French

**Similar Benchmarks**:
- MMLU
- MedQA
- MedMCQA

**Resources**:
- [Resource](https://www.ncbi.nlm.nih.gov/pmc/tools/textmining/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale biomedical dataset for pretraining language models, facilitating enhanced performance on specialized biomedical tasks.

**Target Audience**:
- ML Researchers
- Biomedical NLP Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Extracted text from PubMed Central (PMC) Open Access Subset.

**Size**: 2M paragraphs including 450K high-quality ones.

**Format**: Raw text files

**Annotation**: Two-stage annotation process involving large language model annotations followed by fine-tuning a smaller model for full corpus annotation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics were calculated based on performance benchmarks as stated in the methodology.

**Interpretation**: Higher scores on benchmarks indicate better model performance on biomedical NLP tasks.

**Baseline Results**: OLMo2-7B-stage1 demonstrated performance improvements reaching over 61.08% on medical benchmarks.

**Validation**: The validation procedure involved continual pre-training to evaluate the effects of data curation strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: All data derived from publicly available scientific literature in PMC, licensed for text and data mining.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
