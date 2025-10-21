# ZHUANG RULES

## 📊 Benchmark Details

**Name**: ZHUANG RULES

**Overview**: ZHUANG RULES is a modularized dataset of grammar rules and their corresponding test sentences, aiming to investigate the role of grammar books in translating extremely low-resource languages by deconstructing the translation process into grammar rule retrieval and application.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Zhuang
- Chinese

**Similar Benchmarks**:
- MTOB

**Resources**:
- [GitHub Repository](https://github.com/Infinite-set/ZhuangRules)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide controlled and interpretable evaluation of grammar understanding in large language models for low-resource language translation.

**Target Audience**:
- ML Researchers
- Language Technologists
- Linguists

**Tasks**:
- Grammar Rule Application
- Translation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from two grammar books on Zhuang written in Chinese: 《壮语通论》和《壮语基础教程》。

**Size**: 109 grammar rules paired with an average of 608 Zhuang-Chinese parallel sentences.

**Format**: CSV

**Annotation**: Each grammar rule is annotated with attributes that include action, difficulty, and domain.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU
- chrF++

**Calculation**: Metrics are calculated based on the translation performance of models using the grammar rules provided in the dataset.

**Interpretation**: Higher BLEU and chrF++ scores indicate better translation performance and comprehension of grammar rules.

**Baseline Results**: Previous translation models using only grammar books without the modularized approach.

**Validation**: Cross-validation with different language models to assess reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Analysis of effectiveness across different Zhuang demographics will be explored in potential future work.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
