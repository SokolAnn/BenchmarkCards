# NYK-MS (NewYorKer for Metaphor and Sarcasm)

## 📊 Benchmark Details

**Name**: NYK-MS (NewYorKer for Metaphor and Sarcasm)

**Overview**: A new benchmark for multi-modal metaphor and sarcasm understanding, containing 1,583 samples for metaphor tasks and 1,578 samples for sarcasm tasks, with 7 well-annotated tasks.

**Data Type**: cartoon-caption pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MVSA
- HFM
- MultiMET
- MetaCLUE

**Resources**:
- [GitHub Repository](https://github.com/jmhessel/caption_contest_corpus)

## 🎯 Purpose and Intended Users

**Goal**: To provide a well-annotated dataset for training and evaluating models on metaphor and sarcasm understanding tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Metaphor Classification
- Metaphor Word Detection
- Metaphor Explanation
- Sarcasm Classification
- Sarcasm Word Detection
- Sarcasm Explanation
- Sarcasm Target Detection

**Limitations**: The dataset only contains image and text modalities; it is not very large and may have some annotation inconsistencies.

## 💾 Data

**Source**: newyorker_caption_contest dataset

**Size**: 3,161 samples

**Format**: JSON

**Annotation**: Multi-round manual annotation by human annotators and post-processing with GPT-4V.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Exact Match (EM)
- BLEU-4

**Calculation**: Calculated using standard evaluation metrics for classification tasks.

**Interpretation**: Higher F1 and accuracy indicate better model performance on metaphor and sarcasm tasks.

**Baseline Results**: Baseline model using BERT and ViT with performance metrics shown in the paper.

**Validation**: Validated through human evaluations and experiments comparing various model performance on the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Demographic data of annotators included gender distribution.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Informed consent was obtained from annotators.

**Data Licensing**: Not Applicable

**Consent Procedures**: Annotators were paid and informed about the study.

**Compliance With Regulations**: Not Applicable
