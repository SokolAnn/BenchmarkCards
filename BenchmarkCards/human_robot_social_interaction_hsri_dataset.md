# Human Robot Social Interaction (HSRI) Dataset

## 📊 Benchmark Details

**Name**: Human Robot Social Interaction (HSRI) Dataset

**Overview**: The HSRI Dataset aims to benchmark the capabilities of language models and foundational models to reason about social interactions, with annotations of robot social errors, competencies, rationale, and corrective actions in real-world human-robot interactions, consisting of ∼400 real-world interaction videos and over 10K annotations.

**Data Type**: video with annotations

**Domains**:
- Robotics
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SocialIQA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset and benchmark for measuring the social reasoning capabilities of AI agents in real-world human-robot interactions.

**Target Audience**:
- ML Researchers
- Robotics Developers

**Tasks**:
- Error Detection
- Competency Detection
- Social Attribute Identification
- Rationale and Correction Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Collected from natural conversational interactions between humans and physical social robots.

**Size**: 440 interaction videos, 10,214 annotations

**Format**: Video and annotation files

**Annotation**: Manual annotation by multiple annotators based on defined categories of social errors and competencies.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the predictions of models against ground truth annotations.

**Interpretation**: Higher scores indicate better performance in detecting social errors and competencies.

**Baseline Results**: Performance gaps were observed between AI models and human evaluators.

**Validation**: Metrics are validated through multiple experimental trials with varying model inputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset has been collected under a newly accepted IRB protocol and anonymization processes are in place.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
