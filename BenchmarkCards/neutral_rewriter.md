# NeuTral Rewriter

## 📊 Benchmark Details

**Name**: NeuTral Rewriter

**Overview**: A rule-based and neural approach to gender-neutral rewriting, providing alternatives for gendered English sentences.

**Data Type**: Synthetic and natural language data

**Domains**:
- Natural Language Processing
- Gender-Neutral Language

**Languages**:
- English

**Similar Benchmarks**:
- WinoBias
- Sun et al. (2021)

**Resources**:
- [GitHub Repository](https://github.com/anonymous-until-publication/NeuTralRewriter)
- [Resource](https://creativecommons.org/licenses/by-sa/4.0/)

## 🎯 Purpose and Intended Users

**Goal**: Provide gender-neutral alternatives and increase inclusiveness in NLP applications.

**Target Audience**:
- Researchers in NLP
- Developers of language technology

**Tasks**:
- Gender-neutral rewriting
- Debiasing training data

**Limitations**: Currently limited to English; potential to extend to other languages in future work.

**Out of Scope Uses**:
- Targeting specific referents for pronoun changes

## 💾 Data

**Source**: WinoBias+, OpenSubtitles, Reddit

**Size**: Over 4 million sentences (including synthetic and natural)

**Format**: Text

**Annotation**: Manual curation and correction of gender-neutral alternatives

## 🔬 Methodology

**Methods**:
- Rule-based rewriting
- Neural machine translation

**Metrics**:
- Word Error Rate

**Calculation**: WER calculated by comparing generated outputs to correct neutral forms.

**Interpretation**: Lower WER indicates better performance in generating gender-neutral alternatives.

**Baseline Results**: WER below 0.18%

**Validation**: Errors evaluated on both synthetic and natural benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data bias
- Output quality
- Legal compliance

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Misuse**: Improper usage

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Various datasets distributed under open-source or Creative Commons licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Followed the guidelines of the European Parliament for gender-neutral language.
