# GenCodeSearchNet (GeCS)

## 📊 Benchmark Details

**Name**: GenCodeSearchNet (GeCS)

**Overview**: GenCodeSearchNet is a benchmark that tests the generalization capabilities of language models for programming language understanding, particularly focusing on code search tasks using natural language queries across different programming languages and domains.

**Data Type**: text-code pairs

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English
- R

**Similar Benchmarks**:
- CodeSearchNet
- CoSQA
- CodeXGLUE

**Resources**:
- [GitHub Repository](https://github.com/drndr/gencodesearchnet)
- [Resource](https://doi.org/10.5281/zenodo.8310891)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation protocol for language models' generalization capabilities in programming language understanding.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Search
- Text-Code Matching

**Limitations**: The StatCodeSearch dataset consists only of a single programming language, R.

## 💾 Data

**Source**: Open Science Framework (OSF) and existing datasets like CodeSearchNet.

**Size**: 1,070 pairs of code and comments

**Format**: JSONL

**Annotation**: Manually curated and semi-automated filtering using GPT-3.5 Turbo.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Mean Reciprocal Rank (MRR)

**Calculation**: Accuracy is calculated on balanced test sets with positives and negatives. MRR is calculated by averaging the reciprocal ranks of the correct answer across all queries.

**Interpretation**: High accuracy indicates good text-code matching, while MRR measures the ranking performance of correct code snippets.

**Validation**: Validation is done using test sets designed to evaluate different types of generalization.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset focuses on underrepresented programming languages (e.g., R).

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: All data sources include publicly available content with permissive licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
