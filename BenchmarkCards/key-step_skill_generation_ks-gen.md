# Key-step Skill Generation (KS-Gen)

## 📊 Benchmark Details

**Name**: Key-step Skill Generation (KS-Gen)

**Overview**: The Key-step Skill Generation (KS-Gen) task aims to generate video clips of key steps needed to complete a human skill from an initial state and skill description. It tackles the complexities of generating human skills through a novel framework and a curated dataset for evaluation.

**Data Type**: video clips

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- COIN
- CrossTask
- HT-Step
- Kinetics-400

**Resources**:
- [GitHub Repository](https://github.com/MCG-NJU/KS-Gen)

## 🎯 Purpose and Intended Users

**Goal**: To learn and generate human skills at key-step levels, facilitating human skill learning and providing experience for embodied intelligence.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Video Generation

**Limitations**: N/A

## 💾 Data

**Source**: The raw data for the dataset comes from COIN, CrossTask, HT-Step, and Kinetics-400 instructional video datasets, with a data curation pipeline developed to enhance clip quality.

**Size**: 110,000 subclips

**Format**: various video formats

**Annotation**: Annotations include step categories and corresponding segments.

## 🔬 Methodology

**Methods**:
- Automated metrics
- User study

**Metrics**:
- Action score
- CLIP
- DINO
- Motion distance
- Fréchet Inception Distance (FID)
- Fréchet Video Distance (FVD)

**Calculation**: Metrics are calculated based on cosine similarities and feature distributions compared between generated and real video clips.

**Interpretation**: Higher scores in automatic metrics indicate better alignment with human evaluations.

**Baseline Results**: Various baseline methods including GenHowTo and CogVideoX were evaluated, with detailed results presented in tabular form.

**Validation**: Results validated through comparison with real videos and user studies to ensure human-like video generation effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Unintended propagation of biases present in training data that could lead to inadequate or skewed video outputs.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
