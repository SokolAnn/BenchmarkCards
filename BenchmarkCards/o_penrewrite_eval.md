# O PENREWRITE EVAL

## 📊 Benchmark Details

**Name**: O PENREWRITE EVAL

**Overview**: A novel benchmark that covers a wide variety of rewriting types expressed through natural language instructions, specifically designed for research on cross-sentence text rewriting.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/google-research/google-research/tree/master/rewritelm)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the evaluation of open-ended rewriting, focusing on natural language instructions for cross-sentence text transformations.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Rewriting

**Limitations**: N/A

## 💾 Data

**Source**: Collected human-generated text rewrites with natural language instructions, covering tasks like formality, paraphrasing, and expansion.

**Size**: 1,629 examples

**Format**: JSON

**Annotation**: Human annotators attached appropriate instructions to each source text and rewrote them accordingly.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- NLI
- SARI
- GLEU
- Update-ROUGE

**Calculation**: Metrics are calculated based on the differences and similarities between model predictions and reference texts.

**Interpretation**: A higher value of NLI, SARI, GLEU, and Update-ROUGE indicates better performance.

**Baseline Results**: Previous models evaluated include PaLM, LLaMA, Alpaca, and others, with RewriteLM models outperforming them.

**Validation**: Empirical studies were conducted to evaluate model performance on the O PENREWRITE EVAL benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
