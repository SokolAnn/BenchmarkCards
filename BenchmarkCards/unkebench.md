# UnKEBench

## 📊 Benchmark Details

**Name**: UnKEBench

**Overview**: UnKEBench is a newly proposed dataset specifically designed for unstructured knowledge editing tasks, aimed at accurately handling information-rich and free-format unstructured knowledge.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- KEBench
- KnowEdit

**Resources**:
- [GitHub Repository](https://github.com/TrustedLLM/UnKE)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating unstructured knowledge editing methods, facilitating advancements in this area of research.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Knowledge Editing

**Limitations**: N/A

## 💾 Data

**Source**: Generated through ChatGPT prompts based on real-world unstructured texts.

**Size**: 1,000 examples

**Format**: JSON

**Annotation**: Annotated through automated processes and manual checks to ensure accuracy.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- BERT Score
- BLEU
- ROUGE-1
- ROUGE-2
- ROUGE-L
- Fact Score

**Calculation**: Metrics are calculated based on lexical overlap and semantic similarity between edited outputs and target answers.

**Interpretation**: Higher scores indicate better performance in editing unstructured knowledge.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
