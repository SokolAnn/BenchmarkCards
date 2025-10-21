# MetaVQA

## 📊 Benchmark Details

**Name**: MetaVQA

**Overview**: MetaVQA is a comprehensive benchmark designed to assess and enhance vision language models’ understanding of spatial relationships and scene dynamics through Visual Question Answering (VQA) and closed-loop simulations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://metadriverse.github.io/metavqa)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve embodied scene understanding of vision language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering
- Embodied Scene Understanding

**Limitations**: N/A

## 💾 Data

**Source**: nuScenes and Waymo Open Motion datasets

**Size**: 4,305,450 questions

**Format**: N/A

**Annotation**: Generated via automated methods using Set-of-Mark prompting.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Closed-loop simulation

**Metrics**:
- Accuracy
- Route Completion Ratio
- Collision Rate
- Average Displacement Error (ADE)
- Final Displacement Error (FDE)

**Calculation**: Metrics are calculated based on the model's responses to the questions and their effectiveness in a simulated environment.

**Interpretation**: Higher accuracy indicates better embodied scene understanding.

**Validation**: The benchmark is validated through experiments showing improved performance of VLMs when fine-tuned with the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
