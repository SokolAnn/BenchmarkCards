# SlangDIT (Interpretative Slang Translation)

## 📊 Benchmark Details

**Name**: SlangDIT (Interpretative Slang Translation)

**Overview**: SlangDIT introduces a new task that consists of three subtasks: slang detection, cross-lingual slang explanation, and slang translation, leveraging context to produce more accurate translations of slang terms.

**Data Type**: English-Chinese sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- Urban Dictionary
- OSD
- GDoS
- OpenSubtitles-Slang
- CLIX

**Resources**:
- [GitHub Repository](https://github.com/XL2248/SlangDIT)

## 🎯 Purpose and Intended Users

**Goal**: To produce more accurate translations by taking detected slang and corresponding cross-lingual explanations into account.

**Target Audience**:
- ML Researchers
- Language Translators
- AI Developers

**Tasks**:
- Slang Detection
- Cross-lingual Slang Explanation
- Slang Translation

**Limitations**: N/A

## 💾 Data

**Source**: Large-scale movie subtitles

**Size**: 25,000 examples

**Format**: CSV

**Annotation**: Automatically generated using advanced LLMs for slang detection, explanation, and polysemy annotation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU
- ROUGE-1
- ROUGE-2
- ROUGE-L
- Comet
- F1 Score

**Calculation**: Standard metrics for evaluating slang detection, explanation, and translation accuracy as described in the paper.

**Interpretation**: Higher scores indicate better alignment with correct slang understanding.

**Baseline Results**: Compared to various LLM models and fine-tuned baselines, SlangOWL shows superior performance in all tasks.

**Validation**: Cross-validation across training and testing datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset includes a diverse set of slang terms from various cultural contexts.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset is sourced from publicly available movie subtitles and does not involve sensitive data.

**Data Licensing**: Permitted under the Creative Commons Attribution-ShareAlike 3.0 Unported License and Creative Commons CC0 License for slang explanations.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
