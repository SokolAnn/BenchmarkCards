# EGOILLUSION

## 📊 Benchmark Details

**Name**: EGOILLUSION

**Overview**: EGOILLUSION is a first benchmark to evaluate MLLM hallucinations in egocentric videos, comprising 1,400 videos paired with 8,000 human-annotated open and closed-ended questions designed to trigger hallucinations in both visual and auditory cues.

**Data Type**: video-question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- POPE
- HallusionBench
- MMHal-Bench
- VideoHallucer

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate hallucination in MLLMs across a diverse set of egocentric video-language tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Episodic Information Reasoning
- Temporal Reasoning
- Hand-Object Interaction
- Visual Object Identification
- Object State Change Detection
- Audio Event Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Curated primarily from the VideoRecap and Ego4D datasets.

**Size**: 1,400 videos and 8,000 question-answer pairs

**Format**: N/A

**Annotation**: Human annotation with expert oversight was employed.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is computed as the primary metric where lower accuracy indicates a higher degree of hallucinations.

**Interpretation**: Lower accuracy reveals a greater susceptibility to hallucinations.

**Baseline Results**: The best performance achieved by models on EGOILLUSION was 59% accuracy.

**Validation**: Extensive analysis of the models’ responses to uncover insights about hallucination tendencies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
