# CURIE (Scientific Long-Context Understanding, Reasoning and Information Extraction)

## 📊 Benchmark Details

**Name**: CURIE (Scientific Long-Context Understanding, Reasoning and Information Extraction)

**Overview**: CURIE is a benchmark designed to measure the potential of Large Language Models (LLMs) in scientific problem-solving through ten challenging tasks across six disciplines, featuring 580 problems and solution pairs curated by experts.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- GPQA

**Resources**:
- [GitHub Repository](https://github.com/google/curie)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs on scientific reasoning and understanding long-context information across diverse scientific fields.

**Target Audience**:
- ML Researchers
- Domain Experts
- Industry Practitioners

**Tasks**:
- Information Extraction
- Concept Tracking
- Aggregation
- Algebraic Manipulation
- Coding

**Limitations**: N/A

## 💾 Data

**Source**: Curated from scientific literature across six disciplines with annotations by domain experts.

**Size**: 580 examples

**Format**: JSON

**Annotation**: Manual annotation by experts in scientific domains.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated scoring metrics
- Prompt-based evaluation

**Metrics**:
- F1 Score
- Accuracy
- ROUGE-L
- BERTScore

**Calculation**: Metrics calculated based on the comparison of model outputs to curated ground truth by experts.

**Interpretation**: Scores are normalized to [0, 1] representing performance from poor to good.

**Baseline Results**: N/A

**Validation**: Evaluation frameworks established through expert collaboration and iterative testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
