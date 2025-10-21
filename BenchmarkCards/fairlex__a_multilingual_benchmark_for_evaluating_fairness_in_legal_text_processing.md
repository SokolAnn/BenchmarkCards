# FairLex: A Multilingual Benchmark for Evaluating Fairness in Legal Text Processing

## 📊 Benchmark Details

**Name**: FairLex: A Multilingual Benchmark for Evaluating Fairness in Legal Text Processing

**Overview**: We present a benchmark suite of four datasets for evaluating the fairness of pre-trained language models and the techniques used to fine-tune them for downstream tasks. Our benchmarks cover four jurisdictions (European Council, USA, Switzerland, and China), five languages (English, German, French, Italian and Chinese) and fairness across five attributes (gender, age, region, language, and legal area).

**Data Type**: text (legal case documents; document classification / multi-label and multi-class legal judgment and topic prediction)

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- English
- German
- French
- Italian
- Chinese

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- XTREME
- WILDS
- LexGLUE

**Resources**:
- [Resource](https://huggingface.co/datasets/coastalcph/fairlex)
- [GitHub Repository](https://github.com/coastalcph/fairlex)
- [Resource](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## 🎯 Purpose and Intended Users

**Goal**: Provide a multilingual benchmark suite to evaluate fairness (performance parity / equal risk) of pre-trained language models and group-robust fine-tuning techniques in legal NLP across jurisdictions, languages and sensitive attributes.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Legal Scholars/Domain Experts

**Tasks**:
- Document Classification
- Multi-label Classification
- Legal Judgment Prediction
- Legal Topic Classification
- Crime Severity Prediction

**Limitations**: Covers a very small fraction of legal applications, jurisdictions, and protected attributes; some protected attributes are extracted automatically (e.g., gender, age) and some are manually clustered; binarization of gender is a noted simplification and may be inappropriate in real-world applications; ground truth is relative to judges' interpretation within specific jurisdictions.

## 💾 Data

**Source**: Compiled from ECtHR (Chalkidis et al., 2021); SCOTUS (Spaeth et al., 2020); FSCS (Niklaus et al., 2021); CAIL (Xiao et al., 2018; Wang et al., 2021b). A unified version of the benchmark is released on Hugging Face Datasets.

**Size**: ECtHR: 11,000 cases (train 9,000; dev 1,000; test 1,000). SCOTUS: 9,262 cases (train ~7,416; dev 914; test 931). FSCS: >85,000 decisions (train 59,700; dev 8,200; test 17,400). CAIL: original dataset >1,000,000 cases; re-annotated subset used ~104,000 cases (train 80,000; dev 12,000; test 12,000).

**Format**: Hugging Face Datasets

**Annotation**: Attributes and labels come from original dataset metadata where available; some attributes are automatically extracted (e.g., applicant birth year and gender via regular expressions in ECtHR), some attributes manually clustered (e.g., defendant state grouping, SCOTUS respondent type), and CAIL subset re-annotated with demographic attributes (Wang et al., 2021b).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation
- Group-robust algorithm comparison
- Quantitative analysis
- Qualitative analysis

**Metrics**:
- Macro-F1 (per group)
- Group-wise standard deviation (Group Disparity, GD)
- Worst-group macro-F1 (mF1_W)
- Jensen-Shannon divergence (label distribution drift)

**Calculation**: Macro-F1 is computed per group (mF1_i), excluding the group of unidentifiable instances. Group disparity (GD) is computed as the standard deviation across groups: GD = sqrt( (1/G) * sum_i (mF1_i - mF1)^2 ). Worst-group mF1 (mF1_W) is the minimum mF1 across groups. Jensen-Shannon divergences reported between train/dev/test label distributions per group.

**Interpretation**: Higher macro-F1 (per group) indicates better group performance; lower GD indicates smaller performance disparity across groups; higher worst-group mF1 indicates improved fairness for the worst-off group. Lower Jensen-Shannon divergence indicates less temporal/label distribution drift.

**Baseline Results**: Transformer-based ERM baselines outperform linear Bag-of-Words in average and worst-case mF1. Example Transformer ERM results (Table 4): ECtHR mF1=53.2, mF1_W=44.9; SCOTUS mF1=75.1, mF1_W=70.8; FSCS mF1=67.8, mF1_W=65.0; CAIL mF1=60.2, mF1_W=60.1. Group-robust algorithms (Adversarial Removal, Group DRO, IRM, V-REx) do not consistently mitigate disparities across all datasets/attributes.

**Validation**: Chronological train/development/test splits per dataset (detailed per dataset). Models fine-tuned with early stopping on validation; training repeated five times with different random seeds and averaged scores reported; models trained up to 20 epochs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Legal Compliance
- Robustness

**Atlas Risks**:
- **Privacy**: Personal information in data, Exposing personal information
- **Data Laws**: Data usage restrictions
- **Legal Compliance**: Legal accountability
- **Fairness**: Data bias, Output bias
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Governance**: Lack of data transparency, Incomplete usage definition
- **Intellectual Property**: Data usage rights restrictions
- **Misuse**: Improper usage
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Per-group macro-F1 scores, group representation (#train-cases), Jensen-Shannon label-distribution drift, and Worst Class Influence (WCI) are reported per attribute and per group. Cross-attribute influence analyses are provided to study interactions between attributes.

**Potential Harm**: Detects and aims to measure performance disparities that may lead to discriminatory outcomes against protected groups (gender, age, region, language, legal area) in legal NLP applications.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is partially anonymized according to applicable national law; ECtHR cases are partially anonymized by the court; FSCS names redacted by court guidelines; CAIL cases partially anonymized. Data is considered public from a privacy perspective in the original sources.

**Data Licensing**: Compiled FairLex released under CC-BY-NC-SA-4.0. Original component datasets are publicly available under CC-BY-(NC-)SA-4.0 licenses as stated in the paper.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Data processed and made public in accordance with the respective national laws of the data sources; the paper references compliance with European data protection laws and discusses the proposed EU AI Act and its implications for high-risk AI systems used in the administration of justice.
