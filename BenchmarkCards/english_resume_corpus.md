# English Resume Corpus

## 📊 Benchmark Details

**Name**: English Resume Corpus

**Overview**: Transforms resume information extraction into a sentence classification task; improves classification rules to create a larger and more fine-grained English resume classification dataset and uses it to test mainstream pre-trained language models and study the relationship between training sample size and accuracy.

**Data Type**: text (sentence-level resume segments)

**Domains**:
- Natural Language Processing
- Human Resources

**Languages**:
- English

**Similar Benchmarks**:
- The resume corpus (Su et al., 2019)
- resume-text-batch (Kaggle)
- resume-text-classification-dataset (Kaggle)

**Resources**:
- [Resource](https://www.kaggle.com/datasets/oo7kartik/resume-text-batch)
- [Resource](https://www.kaggle.com/datasets/chingkuangkam/resume-text-classification-dataset)
- [Resource](https://docs.python.org/ja/3/library/tkinter.html)

## 🎯 Purpose and Intended Users

**Goal**: Create a larger, more fine-grained English resume classification dataset by improving annotation rules; evaluate mainstream pre-trained language models on this dataset; and examine how training sample size affects model correctness.

**Tasks**:
- Text Classification
- Information Extraction

**Limitations**: The constructed resume corpus is highly sample-imbalanced across categories (e.g., Experience accounts for ~50% while Qualifications, Object, and Skill are 1%–7%); sample imbalance remains a limitation to be addressed in future work.

## 💾 Data

**Source**: Original CVs from Kaggle (referenced Kaggle datasets: https://www.kaggle.com/datasets/oo7kartik/resume-text-batch and https://www.kaggle.com/datasets/chingkuangkam/resume-text-classification-dataset) and prior English resume dataset (Gan and Takahashi, 2021).

**Size**: 1,000 resumes; 78,000 sentences total (split into 58,000 training, 10,000 validation, 10,000 test).

**Format**: TXT (segmented sentence-level records; each annotated resume exported as a separate txt file).

**Annotation**: Manual sentence-level annotation using a custom Tkinter annotation tool with rule-based sentence segmentation and manual label selection. Seven labels: Experience, Personal Information, Summary, Education, Qualifications, Skill, Object.

## 🔬 Methodology

**Methods**:
- Model-based evaluation: fine-tuning pre-trained language models (BERT large, ALBERT xxlarge, RoBERTa large, T5 large)
- Automated metrics evaluation (F1-micro)
- Training-sample-size ablation (varying training samples and measuring performance)
- Repeated runs (each experiment performed 3 times and averaged)

**Metrics**:
- F1 Score (micro)

**Calculation**: Datasets randomly split in ratio 7:1.5:1.5 (training:validation:test). For each experimental setting, runs were repeated three times and F1-micro scores averaged.

**Interpretation**: Increasing the number of training samples increases model correctness; models reach maximum performance around 40,000 training samples. The newly constructed corpus yields higher F1 compared to the original dataset (e.g., +0.70% for BERT).

**Baseline Results**: BERT* large (baseline): 85.97; BERT large: 86.67; ALBERT large: 86.40; RoBERTa large: 87.00; T5 large: 87.35.

**Validation**: Random 7:1.5:1.5 split with experiments repeated three times and averaged. Confusion matrix analysis was used to analyze per-category learning (e.g., RoBERTa and T5 confusion matrices).

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
