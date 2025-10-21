# ChemRxivQuest

## 📊 Benchmark Details

**Name**: ChemRxivQuest

**Overview**: ChemRxivQuest is a curated dataset of 970 high-quality question–answer (QA) pairs derived from 155 ChemRxiv preprints across 17 subfields of chemistry. Each QA pair is explicitly linked to its source text segment to ensure traceability and contextual accuracy.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing
- Chemistry

**Languages**:
- English

**Similar Benchmarks**:
- PubMedQA
- BioASQ
- SciQ
- S2ORC

**Resources**:
- [Resource](https://chemrxiv.org/)

## 🎯 Purpose and Intended Users

**Goal**: To support advancements in chemistry-focused natural language processing (NLP) by providing a reliable, structured, and versatile dataset tailored to the unique demands of chemical language.

**Target Audience**:
- ML Researchers
- Domain Experts
- Educators

**Tasks**:
- Question Answering

**Limitations**: The reliance on large language models (LLMs) to generate questions and answers may result in hallucinations and inaccuracies not supported by source materials.

## 💾 Data

**Source**: ChemRxiv preprints

**Size**: 970 QA pairs

**Format**: N/A

**Annotation**: Automated generation of QA pairs followed by rigorous validation.

## 🔬 Methodology

**Methods**:
- Automated QA generation
- Fuzzy matching for answer verification

**Metrics**:
- Exact Match (EM)
- ROUGE-L
- BLEU

**Calculation**: Metrics are calculated based on standard evaluation procedures with dataset splits into training, validation, and test sets.

**Interpretation**: High performance indicates effective model understanding of chemistry-specific tasks.

**Validation**: The dataset was validated through a meticulous process involving both automated checks and manual reviews.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential misinformation from generated QA pairs if source content is inaccurate.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons CC BY license allows for unrestricted reuse and adaptation.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
