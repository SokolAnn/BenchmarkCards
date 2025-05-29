# MedHallu

## 📊 Benchmark Details

**Name**: MedHallu

**Overview**: A comprehensive benchmark designed for detecting medical hallucinations in Large Language Models (LLMs). The dataset comprises 10,000 high-quality question-answer pairs derived from PubMedQA, systematically categorized into easy, medium, and hard detection tiers based on the subtlety of hallucinations.

**Data Type**: Medical

**Domains**:
- Healthcare
- Medicine

**Languages**:
- English

**Similar Benchmarks**:
- HaluEval
- HaluBench

**Resources**:
- [Resource](https://medhallu.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured evaluation resource for the detection of medical hallucinations in LLMs.

**Target Audience**:
- Researchers
- Healthcare professionals
- AI developers

**Tasks**:
- Hallucination detection in medical contexts
- Model benchmarking for AI safety in healthcare

**Limitations**: None

## 💾 Data

**Source**: PubMedQA

**Size**: 10,000 samples

**Format**: Question-answer pairs

**Annotation**: Annotated to distinguish accurate responses from hallucinated content.

## 🔬 Methodology

**Methods**:
- LLM-based quality filtering
- Bidirectional entailment
- TextGrad optimization

**Metrics**:
- F1 score
- Precision

**Calculation**: F1 score calculated based on true positive, false positive, and false negative values.

**Interpretation**: Higher F1 scores indicate better hallucination detection performance.

**Baseline Results**: Best model achieved F1 score of 0.625 for 'hard' hallucination detection.

**Validation**: Validation performed using a multi-model ensemble approach.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Transparency
- Privacy
- Fairness

**Atlas Risks**:
- **Accuracy**: The dataset allows evaluation of model accuracy; poor performance on MedHallu indicates hallucination issues in tested models, not in the dataset itself.
- **Transparency**: No training process is involved in this benchmark; however, models evaluated on MedHallu may lack transparency regarding their own training data.
- **Privacy**: No personal information exists in MedHallu or its PubMedQA source; all data are de-identified biomedical literature.
- **Fairness**: The risk of data bias is minimal, as PubMedQA is a well-curated dataset and no modifications introduce bias; any bias observed reflects the models, not the dataset.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data uses de-identified biomedical literature.

**Data Licensing**: Utilizes publicly available PubMedQA data under MIT licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
