# HR-MultiWOZ: A Task Oriented Dialogue (TOD) Dataset for HR LLM Agent

## 📊 Benchmark Details

**Name**: HR-MultiWOZ: A Task Oriented Dialogue (TOD) Dataset for HR LLM Agent

**Overview**: HR-MultiWOZ is the first labeled open-sourced conversation dataset in the HR domain for NLP research, comprising 550 fully-labeled conversations across 10 HR domains, aimed at evaluating/training LLM agents for HR applications.

**Data Type**: conversation transcripts

**Domains**:
- Natural Language Processing
- Human Resources

**Languages**:
- English

**Similar Benchmarks**:
- MultiWOZ

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate/train HR LLM agents using a dataset tailored for HR-specific task-oriented dialogue.

**Target Audience**:
- ML Researchers
- HR Professionals
- AI Developers

**Tasks**:
- Task Oriented Dialogue
- Dialogue State Tracking

**Limitations**: The dataset does not contain task parts of the conversation.

## 💾 Data

**Source**: Generated using a pipeline from expert-validated HR schemas and LLMs with minimal human involvement for annotation.

**Size**: 550 dialogues

**Format**: N/A

**Annotation**: Mostly LLM-generated with some human labeling and verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Naturalness rating
- Clarity rating
- Politeness rating

**Calculation**: Metrics calculated based on human evaluations on a scale of 1 to 5.

**Interpretation**: Higher scores indicate better naturalness, clarity, and politeness.

**Baseline Results**: N/A

**Validation**: Human evaluations confirmed the quality and characteristics of the generated dialogues.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: The synthetic data may reflect biases inherent in LLMs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Generated dialogues are based on synthetic user profiles to ensure privacy.

**Data Licensing**: CC BY 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The dataset's generation follows rigorous internal security policies.
