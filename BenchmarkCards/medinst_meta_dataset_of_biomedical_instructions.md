# MEDINST (Meta Dataset of Biomedical Instructions)

## 📊 Benchmark Details

**Name**: MEDINST (Meta Dataset of Biomedical Instructions)

**Overview**: MEDINST is a novel multi-domain, multi-task instructional meta-dataset comprising 133 biomedical NLP tasks and over 7 million training samples. It aims to address the scarcity of diverse and well-annotated datasets in biomedical analysis by facilitating the training of large language models.

**Data Type**: instruction-following samples

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- BLUE (Biomedical Language Understanding Evaluation)
- BLURB (Biomedical Language Understanding and Reasoning Benchmark)
- SUPER-NATURAL INSTRUCTIONS

**Resources**:
- [GitHub Repository](https://github.com/aialt/MedINST)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of MEDINST is to provide a comprehensive instructional dataset to enhance the generalization abilities of large language models in biomedical tasks.

**Target Audience**:
- ML Researchers
- Model Developers
- Healthcare Practitioners

**Tasks**:
- Named Entity Recognition
- Question Answering
- Relation Extraction
- Text Classification
- Coreference Resolution
- Textual Entailment
- Event Extraction
- Summarization
- Translation

**Limitations**: Due to computational resource constraints, earlier experiments were conducted with limited data and model sizes.

## 💾 Data

**Source**: MEDINST collects data from 98 biomedical datasets formatted into 133 tasks.

**Size**: 7 million training samples

**Format**: N/A

**Annotation**: Instructions are human-annotated and tailored for each dataset/task.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Label F1
- Entity F1
- Exact Match
- Rouge-L

**Calculation**: Metrics are calculated based on model predictions against ground truth for each task assessed.

**Interpretation**: Higher scores on metrics like F1 and Exact Match indicate better model performance.

**Baseline Results**: The paper showcases results from multiple fine-tuned LLMs evaluated on tasks.

**Validation**: Validation was performed using a curated test set from the MEDINST dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
