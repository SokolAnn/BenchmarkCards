# Knowledge Hierarchy Guided Biological-Medical Dataset Distillation

## 📊 Benchmark Details

**Name**: Knowledge Hierarchy Guided Biological-Medical Dataset Distillation

**Overview**: The KAILIN framework automates the distillation of high-quality textual training data from extensive scientific literature for biomedical applications, generated through a knowledge hierarchy guided approach using Medical Subject Headings (MeSH).

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- PubMedQA

**Resources**:
- [Resource](https://arxiv.org/abs/2501.15108)

## 🎯 Purpose and Intended Users

**Goal**: Develop a high-quality, automatically generated dataset for training language models in biomedical Q&A tasks.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 23 million abstracts collected from PubMed and open-source annotated datasets.

**Size**: N/A

**Format**: N/A

**Annotation**: Automatically generated through the KAILIN framework

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the evaluation of the model's performance on the PubMedQA benchmark.

**Interpretation**: Higher accuracy indicates better understanding and alignment with biomedical knowledge hierarchy.

**Baseline Results**: KAILIN framework enables LLaMA-3-70B to outperform GPT-4 on PubMedQA.

**Validation**: Deep evaluations made using ablation studies and case analyses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
