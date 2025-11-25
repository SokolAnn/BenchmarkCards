# SLDS (Swiss Landmark Decisions Summarization)

## 📊 Benchmark Details

**Name**: SLDS (Swiss Landmark Decisions Summarization)

**Overview**: The Swiss Landmark Decisions Summarization (SLDS) dataset contains 20K rulings from the Swiss Federal Supreme Court, each with headnotes in German, French, and Italian, aimed at enhancing cross-lingual legal summarization research.

**Data Type**: decision-headnote pairs

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- German
- French
- Italian

**Similar Benchmarks**:
- EUR-Lex-Sum
- MILDSum

**Resources**:
- [Resource](https://huggingface.co/datasets/ipst/sldsverdicts)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, multilingual dataset for judicial summarization that addresses the unique challenges posed by the Swiss legal landscape.

**Target Audience**:
- Legal Researchers
- Natural Language Processing Practitioners
- Model Developers

**Tasks**:
- Text Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Swiss Federal Supreme Court repository

**Size**: 20,000 rulings, resulting in 60,000 data rows

**Format**: JSON

**Annotation**: Automatically generated headnotes by legal clerks

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-based evaluation

**Metrics**:
- BLEU
- ROUGE-1
- ROUGE-2
- ROUGE-L
- BERTScore
- JUDGE

**Calculation**: Metrics calculated based on generated headnotes in comparison to official headnotes.

**Interpretation**: Metrics provide insights into lexical similarity and legal accuracy, with high scores indicating better performance.

**Baseline Results**: Fine-tuned models generally achieved higher scores than un-tuned models, with notable improvements observed.

**Validation**: The dataset is partitioned by publication year to prevent data leakage.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset was anonymized according to guidelines before publication.

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
