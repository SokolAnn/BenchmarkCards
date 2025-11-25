# TurBLiMP (Turkish Benchmark of Linguistic Minimal Pairs)

## 📊 Benchmark Details

**Name**: TurBLiMP (Turkish Benchmark of Linguistic Minimal Pairs)

**Overview**: TurBLiMP is the first Turkish benchmark of linguistic minimal pairs, designed to evaluate the linguistic abilities of monolingual and multilingual language models, covering 16 linguistic phenomena with 1000 minimal pairs each.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Turkish

**Resources**:
- [GitHub Repository](https://github.com/ezgibasar/turblimp)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of language model's syntactic capabilities for Turkish.

**Target Audience**:
- Linguists
- NLP Researchers

**Tasks**:
- Syntax Evaluation
- Sentence Acceptability Judgment

**Limitations**: The benchmark currently includes only one paradigm per phenomenon and does not systematically test all model sizes.

## 💾 Data

**Source**: Manually crafted and semi-automatically generated minimal pairs focused on Turkish linguistic phenomena.

**Size**: 16,000 minimal pairs

**Format**: N/A

**Annotation**: Manual creation with semi-automated augmentations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Human Acceptability Judgment

**Calculation**: Calculating sequence log probabilities for acceptable and unacceptable sentences.

**Interpretation**: Human judgments were converted to z-scores to assess model performance relative to human acceptability ratings.

**Baseline Results**: N/A

**Validation**: 30 native Turkish speakers rated 216 sentences on a 7-point Likert scale.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collection was conducted anonymously with informed consent.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants provided informed consent prior to data collection.

**Compliance With Regulations**: Not Applicable
