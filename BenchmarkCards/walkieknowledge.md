# WalkieKnowledge

## 📊 Benchmark Details

**Name**: WalkieKnowledge

**Overview**: WalkieKnowledge is a new evaluation benchmark with about 200 manually annotated questions across 8 diverse trajectories, enabling fair comparison between structured approaches and general-purpose VLMs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Robotics

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of visual scene understanding capabilities through diverse query types including scene description, spatial relations, object search, and action-place association.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Object Search
- Scene Description
- Action-Place Association
- Spatial Relations

**Limitations**: N/A

## 💾 Data

**Source**: Based on the EgoWalk dataset, spanning diverse indoor and outdoor environments with rich temporal annotations.

**Size**: 200 questions across 8 trajectories

**Format**: N/A

**Annotation**: Manually annotated questions linked to ground truth frame intervals.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Retrieval Accuracy
- Answer Accuracy
- Precision
- Recall
- Mean Reciprocal Rank (MRR)

**Calculation**: Metrics are calculated based on retrieval and answer correctness in assessing model performance.

**Interpretation**: Higher retrieval and answer accuracy indicates better performance in locating correct frames and answering correctly.

**Baseline Results**: N/A

**Validation**: Evaluated against state-of-the-art VLMs and methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
