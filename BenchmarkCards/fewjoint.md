# FewJoint

## 📊 Benchmark Details

**Name**: FewJoint

**Overview**: FewJoint is a novel Few-Shot Learning benchmark for NLP that introduces few-shot joint dialogue language understanding, covering structure prediction and multi-task reliance problems, reflecting real-world NLP complexity beyond simple N-classification.

**Data Type**: utterance-label pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/AtmaHou/MetaDialog)

## 🎯 Purpose and Intended Users

**Goal**: To promote few-shot learning research in NLP by providing a unified benchmark for joint multi-task language understanding.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Intent Detection
- Slot Tagging

**Limitations**: N/A

## 💾 Data

**Source**: Real user utterances from the AIUI open dialogue platform of iFlytek and utterances written by workers.

**Size**: 6,694 utterances

**Format**: N/A

**Annotation**: Intent and slot labels annotated by workers with validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Intent Accuracy
- Slot F1 Score
- Sentence Accuracy

**Calculation**: Slot F1 Score is calculated on query samples using the conlleval script.

**Interpretation**: A sentence is correct only when all its slots and intent are correct.

**Baseline Results**: Intent Accuracy: 78.46, Slot F1 Score: 40.37, Sentence Accuracy: 23.65 for JointProto.

**Validation**: Models validated on different domains and scores averaged over 5 random seeds.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Sensitive information removed from user utterances.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
