# Multilingual BERT has an accent: Evaluating English influences on fluency in multilingual models

## 📊 Benchmark Details

**Name**: Multilingual BERT has an accent: Evaluating English influences on fluency in multilingual models

**Overview**: We propose a novel method for comparing the fluency of multilingual models to monolingual models by testing preference for two carefully-chosen variable grammatical structures (optional pronoun-drop in Spanish and optional Subject-Verb ordering in Greek). We use this method to show that multilingual BERT is biased toward English-like sentence structure in Spanish and Greek compared to monolingual controls.

**Data Type**: text (natural sentences extracted from syntactic treebanks)

**Domains**:
- Natural Language Processing
- Linguistics

**Languages**:
- Spanish
- Greek
- English

**Similar Benchmarks**:
- XTREME
- XNLI
- XGLUE
- TyDi QA
- XL-WiC
- MTop
- CoLA

**Resources**:
- [Resource](https://arxiv.org/abs/2210.05619)

## 🎯 Purpose and Intended Users

**Goal**: To introduce a fluency evaluation method that detects English structural bias in multilingual models by comparing model preferences for Sparallel (English-like structure) versus Sdifferent (non-English-like structure) and to demonstrate this effect in Spanish (pro-drop) and Greek (subject-verb order).

**Target Audience**:
- Research community
- Multilingual NLP researchers

**Tasks**:
- Fluency Evaluation
- Language Modeling (Masked Language Modeling probability comparison)

**Limitations**: Does not focus on truly low-resource languages because the method requires an available monolingual model as a control; experiments focus on BERT-sized models and may not extrapolate to larger models; constructions tested are discourse-dependent but experiments use isolated sentences without discourse context.

## 💾 Data

**Source**: Spanish GSD treebank from the Universal Dependencies dataset (De Marneffe et al., 2021); Greek Dependency Treebank (Universal Dependencies) (Prokopidis and Papageorgiou, 2017).

**Size**: Spanish: C_parallel = 283 sentences, C_different = 2,656 sentences. Greek: C_parallel = 1,446 sentences, C_different = 425 sentences.

**Format**: N/A

**Annotation**: Sentences selected using syntactic dependency treebank annotations from Universal Dependencies.

## 🔬 Methodology

**Methods**:
- Automated model probability comparison using masked language model logits
- Statistical significance testing via bootstrap sampling
- Comparison against monolingual control models (BETO for Spanish, GreekBERT for Greek) and multilingual BERT (mBERT)

**Metrics**:
- Ratio of average model probability for Sparallel vs Sdifferent (r_model)
- Bootstrap sampling p-value (statistical significance)

**Calculation**: r_model = (average_{x in C_parallel} P_model(w(x) | x)) / (average_{x in C_different} P_model(w(x) | x)), where w(x) is a structurally-relevant word in sentence x and P_model(w(x) | x) is taken from the masked language model logits.

**Interpretation**: If r_multi is significantly larger than r_mono (assessed via bootstrap sampling, p < 0.05), the multilingual model is interpreted as exhibiting an English structural bias (preferring Sparallel more than the monolingual control).

**Baseline Results**: Multilingual BERT (mBERT) significantly prefers English-like structures compared to monolingual BETO (Spanish) and GreekBERT (Greek); reported significance: bootstrap sampling, p < 0.05.

**Validation**: Statistical validation via bootstrap sampling; comparison against monolingual control models (BETO and GreekBERT) to define the fluent distribution.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data
- **Governance**: Lack of testing diversity

**Demographic Analysis**: N/A

**Potential Harm**: ['Fluency discrepancies in multilingual models', 'Modeling flaws affecting lower-resource languages']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
