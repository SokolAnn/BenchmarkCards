# JRDB-Social

## 📊 Benchmark Details

**Name**: JRDB-Social

**Overview**: JRDB-Social is a dataset designed to address limitations in understanding human social behavior across diverse contexts, providing annotations at the individual, intra-group, and social group levels.

**Data Type**: video

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://jrdb.erc.monash.edu/dataset/social)

## 🎯 Purpose and Intended Users

**Goal**: To investigate human social behavior within varied contexts through a comprehensive robotic dataset.

**Target Audience**:
- Researchers
- Developers in Robotics and Computer Vision
- Social Behavior Analysts

**Tasks**:
- Human Interaction Recognition
- Social Context Understanding

**Limitations**: N/A

## 💾 Data

**Source**: JRDB dataset, originally containing over 1.8 million annotations from various real-life social interactions recorded by a robot.

**Size**: 64 minutes of sensory data

**Format**: N/A

**Annotation**: Annotated by experts following strict protocols for quality and consistency.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics calculated from model performance on tasks involving gender, age, race, interactions, and social context understanding.

**Interpretation**: Higher scores indicate better understanding of human social dynamics in crowded environments.

**Baseline Results**: Previous JRDB benchmarks provide a comparative baseline, but specific model performances are noted within the experiments.

**Validation**: Each annotation underwent quality assessment by multiple reviewers to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: The dataset includes demographic breakdowns including gender, age, and race to facilitate fairness analysis.

**Potential Harm**: ['Misrepresentation of demographic categories', 'Reinforcement of societal biases']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymized and aggregated data to protect individual identities in the dataset.

**Data Licensing**: N/A - Specific licensing details not provided in the paper.

**Consent Procedures**: N/A - Consent procedures are not discussed in the paper.

**Compliance With Regulations**: N/A - Compliance with regulations is not mentioned.
