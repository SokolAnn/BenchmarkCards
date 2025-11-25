# FunBench

## 📊 Benchmark Details

**Name**: FunBench

**Overview**: FunBench is a novel visual question answering (VQA) benchmark designed to comprehensively evaluate MLLMs' fundus reading skills, featuring hierarchical task organization across four levels: modality perception, anatomy perception, lesion analysis, and disease diagnosis.

**Data Type**: visual question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- OmniMedVQA
- GMAI-MMBench
- LMOD

**Resources**:
- [Resource](https://huggingface.co/datasets/AIMClab-RUC/FunBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the efficacy of open-source MLLMs for fundus reading tasks of varied difficulties.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners

**Tasks**:
- Visual Question Answering
- Image Recognition
- Disease Classification

**Limitations**: N/A

## 💾 Data

**Source**: 14 public datasets including CFP, OCT, UWF datasets and multimodal datasets.

**Size**: 16,348 fundus images and 91,810 visual questions

**Format**: N/A

**Annotation**: Multi-choice VQA quadruples generated from given images and their associated labels.

## 🔬 Methodology

**Methods**:
- Holistic evaluation
- Knowledge-prompted LLM evaluation
- Linear-probe based VE evaluation

**Metrics**:
- F1 Score
- Sensitivity
- Specificity

**Calculation**: F1 Score calculated as the harmonic mean of Sensitivity and Specificity.

**Interpretation**: A higher F1 Score indicates better performance in fundus reading tasks.

**Validation**: Evaluated performance on nine open-source MLLMs and proprietary baseline models.

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
