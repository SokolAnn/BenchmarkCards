# Compositional Freebase Questions (CFQ)

## 📊 Benchmark Details

**Name**: Compositional Freebase Questions (CFQ)

**Overview**: A large realistic natural language question answering dataset specifically designed to measure compositional generalization using the Distribution-Based Compositionality Assessment (DBCA) method. CFQ provides natural language questions, corresponding SPARQL queries against Freebase, and annotations tracking the rule application DAGs used to generate each example.

**Data Type**: question-answering pairs (text)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SCAN
- ComplexWebQuestions
- WebQuestionsSP
- WikiSQL
- CLEVR
- bAbI
- GQA

**Resources**:
- [GitHub Repository](https://github.com/google-research/google-research/tree/master/cfq)
- [Resource](https://arxiv.org/abs/1912.09713)

## 🎯 Purpose and Intended Users

**Goal**: Provide a dataset and a quantitative method (DBCA) to comprehensively measure compositional generalization by constructing train/test splits that maximize compound divergence while keeping atom divergence low, and to evaluate model performance on these splits.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Semantic Parsing Researchers

**Tasks**:
- Semantic Parsing
- Question Answering

**Limitations**: Current CFQ avoids ambiguous constructs and limits maximum example complexity; it is grounded in Freebase and therefore reflects Freebase modeling choices and data quality. The authors state extensions are desired for ambiguous constructs, negations, quantification, comparatives, additional languages, and other vertical domains.

## 💾 Data

**Source**: Automatically generated rule-based dataset grounded in Freebase; each example is a triple of natural language question, logical form, and SPARQL query, with tracked rule application DAGs.

**Size**: 239,357 question-answer pairs

**Format**: JSON (example provided in Appendix A)

**Annotation**: Automatically generated annotations including intermediate logical forms, SPARQL queries, and normalized rule application DAGs; semantic and structural filtering applied; entity placeholders replaced with Freebase MIDs when available.

## 🔬 Methodology

**Methods**:
- Model-based evaluation using baseline encoder-decoder architectures (LSTM+attention, Transformer, Universal Transformer)
- Automated metrics (accuracy)
- Controlled divergence-based data splits constructed via DBCA (including Maximum Compound Divergence splits)

**Metrics**:
- Accuracy
- Compound divergence (DC) defined as DC(V||W) = 1 - C_{0.1}(FC(V)||FC(W)) where C_beta is the Chernoff coefficient
- Atom divergence (DA) defined as DA(V||W) = 1 - C_{0.5}(FA(V)||FA(W)) corresponding to the Bhattacharyya coefficient
- Mean accuracy with 95% confidence intervals (reported across 5 replicates)

**Calculation**: Atom and compound divergences are computed using weighted frequency distributions of atoms and compounds and the Chernoff coefficient C_beta(P||Q)=sum p^beta q^{1-beta}; DA uses beta=0.5 and DC uses beta=0.1. Accuracy is exact-match accuracy of generated SPARQL against gold SPARQL; mean and 95% confidence intervals reported over 5 replicates.

**Interpretation**: Preferred compositionality benchmark: accuracy obtained on splits with maximum compound divergence and low atom divergence (authors use DA <= 0.02). The authors report a strong negative correlation between compound divergence and test accuracy for baseline models.

**Baseline Results**: CFQ: Random split - LSTM+attention 97.4 ± 0.3%, Transformer 98.5 ± 0.2%, Universal Transformer 98.0 ± 0.3%. CFQ: MCD split - LSTM+attention 14.9 ± 1.1%, Transformer 17.9 ± 0.9%, Universal Transformer 18.9 ± 1.4%. SCAN: Random split - LSTM+attention 99.9 ± 2.7%, Transformer 100.0 ± 0.0%, Universal Transformer 99.9 ± 0.2%. SCAN: MCD split - LSTM+attention 6.1 ± 2.2%, Transformer 1.1 ± 0.5%, Universal Transformer 1.2 ± 0.7%.

**Validation**: Hyperparameters tuned on a CFQ random split; experiments replicated 5 times and mean accuracy with 95% confidence intervals reported. For each target compound divergence, at least 3 different splits with different randomization parameters were produced. Train/validation/test sizes used for reported experiments: 40%/10%/10% of full set (approximately 96k train and 12k validation and test examples for CFQ).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Freebase names and MIDs in textual input and SPARQL output are anonymized by replacing them with placeholders (e.g., 'M0') for model training and evaluation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
