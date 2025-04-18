# Bi’an

## 📊 Benchmark Details

**Name**: Bi’an

**Overview**: A bilingual (Chinese-English) benchmark for RAG hallucination detection, featuring a dataset and lightweight judge models.

**Data Type**: benchmark dataset

**Domains**:
- Multi-domain

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- HaluEval
- RAGTruth
- HaluBench

**Resources**:
- [GitHub Repository](https://github.com/OpenSPG/KAG)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of LLMs in detecting hallucinations in RAG outputs across multiple tasks.

**Target Audience**:
- Researchers
- Practitioners

**Tasks**:
- question answering
- summarization
- Data-to-Text
- machine translation

**Limitations**: The framework excludes creative writing tasks due to their subjective nature.

**Out of Scope Uses**:
- Creative writing

## 💾 Data

**Source**: Curated from open-source repositories and peer-reviewed datasets.

**Size**: 22,992 instances

**Format**: JSON

**Annotation**: Included hallucination perturbed samples and counterfactual cases.

## 🔬 Methodology

**Methods**:
- Hallucination Perturbation Pipeline
- Counterfactual QA Generation Pipeline
- Two-stage Training (Supervised Fine-Tuning and Preference Learning)

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated by matching predicted results with true labels.

**Interpretation**: Higher accuracy indicates better performance in hallucination detection.

**Validation**: Results validated against multiple models including GPT-4o.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data contamination
- Unrepresentative data

**Atlas Risks**:
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Accuracy**: Poor model accuracy

**Potential Harm**: Risks of generating incorrect outputs during model assessment.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data does not contain personally identifiable information.

**Data Licensing**: All datasets used are sourced from open repositories with proper licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
