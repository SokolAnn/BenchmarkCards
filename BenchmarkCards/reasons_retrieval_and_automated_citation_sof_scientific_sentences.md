# REASONS (REtrieval and Automated citation SOf scieNtific Sentences)

## 📊 Benchmark Details

**Name**: REASONS (REtrieval and Automated citation SOf scieNtific Sentences)

**Overview**: REASONS is a novel dataset designed to address the limitations of citation ambiguity and overgeneralization in citation generation by large language models (LLMs). It features sentence-level annotations across 12 scientific domains from arXiv, facilitating evaluation of citation capabilities in scientific contexts.

**Data Type**: sentence-level annotations

**Domains**:
- Natural Language Processing
- Computer Science
- Biology

**Languages**:
- English

**Similar Benchmarks**:
- UnarXive
- S2ORC

**Resources**:
- [GitHub Repository](https://github.com/YashSaxena21/REASONS)

## 🎯 Purpose and Intended Users

**Goal**: To serve as a challenging benchmark for evaluating the source attribution capabilities of large language models in scientific literature.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Citation Generation
- Source Attribution

**Limitations**: The dataset does not cover mathematics, statistics, and physics papers due to equation prevalence that complicates citation processing.

## 💾 Data

**Source**: Sentences extracted from related work sections of IEEE-formatted papers in Computer Science and Biology published on arXiv between 2017-2024.

**Size**: Varies by domain, detailed breakdown available in the paper.

**Format**: JSON

**Annotation**: Sentence-level annotations created through a multi-stage process involving semantic parsing and citation verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Pass Percentage (PP)
- Hallucination Rate (HR)
- BLEU Score
- F1 Score

**Calculation**: Metrics such as PP and HR are calculated based on model responses to prompts during evaluation.

**Interpretation**: Higher F1 Scores and lower Hallucination Rates indicate better performance in citation accuracy and reliability.

**Validation**: The dataset established a standard for evaluating LLMs' citation capabilities with a focus on scientific contexts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**

**Demographic Analysis**: The dataset includes cross-domain citation mapping and categorical classification tags, allowing analysis of disciplinary research propagation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No author contact information was utilized, and all processing received formal IRB approval.

**Data Licensing**: The dataset is designed specifically for attribution capability assessment, adhering to ethical safeguards.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
