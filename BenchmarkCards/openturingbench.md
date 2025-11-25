# OpenTuringBench

## 📊 Benchmark Details

**Name**: OpenTuringBench

**Overview**: OpenTuringBench is a large-scale benchmark designed to train and evaluate machine-generated text detectors on the Turing Test and Authorship Attribution problems, focusing on a representative set of Open Large Language Models (OLLMs) and featuring challenging evaluation tasks including various types of human/machine texts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/OpenTuringBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for assessing the effectiveness of detectors for machine-generated text, particularly in the context of open large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification
- Authorship Attribution

**Limitations**: Focuses primarily on news articles and currently only includes English texts. Future expansions are planned to include additional discourse domains and multilingual models.

## 💾 Data

**Source**: News Category dataset from HuffPost spanning between 2012 and 2022, with additional generated text from various OLLMs.

**Size**: 543,091 texts

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Contrastive learning
- Evaluation on defined tasks

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics computed using confusion matrices based on predicted versus actual labels.

**Interpretation**: Higher scores in precision, recall, and F1 indicate better performance of the detection systems.

**Baseline Results**: OTBDetector achieved F1 Score results exceeding 0.9 across multiple tasks.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential misuse of generated texts, impacting individual and societal levels.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
