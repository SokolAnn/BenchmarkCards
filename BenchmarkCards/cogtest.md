# CogTest

## 📊 Benchmark Details

**Name**: CogTest

**Overview**: CogTest is a principled benchmark designed to evaluate Large Reasoning Models' (LRMs) cognitive habits using 16 cognitive habits, each instantiated with 25 diverse tasks.

**Data Type**: task-based evaluations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/jianshuod/CogTest)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and understand the cognitive habits exhibited by Large Reasoning Models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Cognitive Habit Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: 16 widely used LLMs

**Size**: 400 tasks (16 habits * 25 tasks each)

**Format**: N/A

**Annotation**: Manual verification for task quality and automated extraction of cognitive habits via LLMs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Evidence-first habit extraction

**Metrics**:
- Cognitive habit identification

**Calculation**: Cognitive habits are identified through the reasoning Chains of Thought (CoTs) produced by LRM responses to tasks.

**Interpretation**: LRMs showing a higher frequency of certain cognitive habits indicate stronger reasoning capabilities.

**Validation**: Compared performance across 16 models and their cognitive habit profiles.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Societal Impact**: Impact on affected communities
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
