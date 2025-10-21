# LifeTox

## 📊 Benchmark Details

**Name**: LifeTox

**Overview**: LifeTox is a dataset designed for identifying implicit toxicity within a broad range of advice-seeking scenarios, comprising diverse contexts derived from personal experiences through open-ended questions.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HarmfulQ
- BeaverTails
- HHH Alignments

**Resources**:
- [Resource](https://huggingface.co/datasets/mbkim/LifeTox)

## 🎯 Purpose and Intended Users

**Goal**: To contribute to the safer integration of large language models in everyday human interactions by understanding and detecting implicit toxicity.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Toxicity Detection
- Text Classification

**Limitations**: The operational style of the LifeProTips forum may introduce bias in the standards of advice and the participants’ opinions may not represent all demographic groups.

## 💾 Data

**Source**: Posts and comments crawled from the 'LifeProTips' and 'UnethicalLifeProTips' subreddits.

**Size**: 87,510 instances

**Format**: N/A

**Annotation**: Human evaluation confirmed the labeling of comments as safe or unsafe based on community guidelines.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Fine-tuning of RoBERTa on LifeTox dataset

**Metrics**:
- Macro-F1 Score

**Calculation**: Metrics were calculated based on the classification performance of models trained on the LifeTox dataset.

**Interpretation**: Higher Macro-F1 scores indicate better generalization ability in implicit toxicity detection.

**Baseline Results**: RoBERTa fine-tuned on LifeTox outperformed existing models on multiple out-of-domain benchmarks.

**Validation**: The effectiveness of LifeTox was validated through experiments comparing it against existing safety benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on education: plagiarism

**Demographic Analysis**: N/A

**Potential Harm**: ['Harmful advice leading to social risks']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
