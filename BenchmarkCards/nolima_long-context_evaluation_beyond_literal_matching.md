# NOLIMA (Long-Context Evaluation Beyond Literal Matching)

## 📊 Benchmark Details

**Name**: NOLIMA (Long-Context Evaluation Beyond Literal Matching)

**Overview**: NOLIMA introduces a benchmark extending the Needle-in-a-Haystack test by designing a needle set with minimal lexical overlap, requiring models to infer latent associations to locate answers in long irrelevant contexts.

**Data Type**: question-needle pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- NIAH (Needle-in-a-Haystack)

**Resources**:
- [GitHub Repository](https://github.com/adobe-research/NoLiMa)

## 🎯 Purpose and Intended Users

**Goal**: To design a high-challenge benchmark for evaluating large language models' reasoning capabilities in long context scenarios.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Long-context Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Open-license books prepared through application of filtering mechanisms.

**Size**: 5 needle sets totaling 58 question-needle pairs

**Format**: N/A

**Annotation**: Manually designed by authors to ensure minimal literal overlap.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- ROUGE

**Calculation**: Calculated based on the proportion of correct answers from multiple tests conducted under varying context lengths.

**Interpretation**: Interpret results based on how well models generalize across increasing context lengths and the ability to reason through associative tasks.

**Baseline Results**: The base scores achieved at shorter context lengths (1K, 2K) were used to evaluate performance declines at longer lengths.

**Validation**: Results analyzed under controlled experiments with 7,540 tests per context length.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
