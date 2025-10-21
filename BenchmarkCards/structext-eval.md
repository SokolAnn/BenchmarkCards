# StrucText-Eval

## 📊 Benchmark Details

**Name**: StrucText-Eval

**Overview**: StrucText-Eval is a benchmark containing 5,800 pre-generated and annotated samples designed to evaluate how well LLMs understand and reason through structured text. It aims to assess LLMs’ ability to interpret structured data presented in unstructured formats across 29 tasks and 8 structured languages.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- JSON
- YAML
- XML
- Markdown
- LaTeX
- ORG
- CSV
- Tree

**Similar Benchmarks**:
- GraphQA
- Struc-Bench
- TEMPTABQA
- TableLLM

**Resources**:
- [GitHub Repository](https://github.com/MikeGu721/StrucText-Eval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the reasoning capabilities of large language models (LLMs) on structure-rich text.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Structured Data Reasoning
- Text Retrieval
- Data Extraction
- Statistical Queries
- Data Combining
- Tree Structure Analysis

**Limitations**: StrucText-Eval includes only eight types of structured languages and encompasses a total of 29 different tasks.

## 💾 Data

**Source**: Pre-generated data based on structured languages designed for evaluating LLMs.

**Size**: 5,800 samples

**Format**: JSON

**Annotation**: Automated generation with manual validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- RougeL
- BLEU Score

**Calculation**: Metrics such as RougeL are calculated based on the degree of character-level similarity between model outputs.

**Interpretation**: Higher scores indicate better reasoning abilities by LLMs on structure-rich text.

**Baseline Results**: Open-source LLMs achieved a maximum accuracy of 74.9% on the standard dataset.

**Validation**: Tested performance using both prompt-based and finetuning methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
