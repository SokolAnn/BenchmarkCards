# VoxRole

## 📊 Benchmark Details

**Name**: VoxRole

**Overview**: VoxRole is the first comprehensive benchmark specifically designed for the evaluation of speech-based Role-Playing Conversational Agents (RPCAs), comprising 13,335 multi-turn dialogues, totaling 65.6 hours of speech from 1,228 unique characters across 261 movies.

**Data Type**: multi-turn dialogues

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Aveek-Saha/Movie-Script-Database)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation framework for speech-based Role-Playing Conversational Agents.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Role-Playing Dialogue Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Spoken dialogues extracted from movies using a two-stage automated pipeline.

**Size**: 13,335 dialogues

**Format**: N/A

**Annotation**: Automatic extraction and annotation without manual labeling.

## 🔬 Methodology

**Methods**:
- Automated metrics
- LLM-based evaluation

**Metrics**:
- Rouge-L
- Meteor
- BertScore-F1
- UTMOS

**Calculation**: Metrics calculated based on generated responses compared to ground truth references.

**Interpretation**: High scores indicate strong fidelity and contextual coherence in role-playing.

**Baseline Results**: N/A

**Validation**: Human evaluation study correlating automated evaluations with human judgments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
