# ONTOURL (Ontology URL)

## 📊 Benchmark Details

**Name**: ONTOURL (Ontology URL)

**Overview**: ONTOURL is the first comprehensive benchmark designed to systematically evaluate LLMs’ capabilities in handling ontologies—formal and symbolic representations of domain knowledge. It assesses understanding, reasoning, and learning through 15 distinct tasks comprising 57,303 questions derived from 40 ontologies across 8 domains.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Science
- Finance
- Healthcare
- Legal
- Education
- Environmental Science
- Media and Entertainment

**Languages**:
- English

**Resources**:
- [Resource](https://anonymous.4open.science/r/OntoURL_anonymous-44FD)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of large language models in understanding, reasoning, and learning with structured symbolic knowledge through ontologies.

**Target Audience**:
- ML Researchers
- Ontology Practitioners

**Tasks**:
- Understanding
- Reasoning
- Learning

**Limitations**: N/A

## 💾 Data

**Source**: Extracted from 40 expert-created, open-source ontologies spanning various domains.

**Size**: 57,303 questions

**Format**: Multiple-choice questions and open-ended questions

**Annotation**: Generated using a systematic pipeline involving entity extraction and expert verification for quality assurance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BERTScore
- F1 Score

**Calculation**: Metrics are calculated based on model outputs compared to ground truth answers using standard evaluation practices.

**Interpretation**: Higher accuracy indicates better performance by the models in answering ontology-related questions.

**Validation**: Evaluated on 20 open-source LLMs using both zero-shot and few-shot settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International (CC BY 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
