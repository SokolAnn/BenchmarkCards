# CS4 (Comparing the Skill of Creating Stories by Controlling the Synthesized Constraint Specificity)

## 📊 Benchmark Details

**Name**: CS4 (Comparing the Skill of Creating Stories by Controlling the Synthesized Constraint Specificity)

**Overview**: CS4 provides a novel benchmark dataset with varying levels of prompt specificity to measure the creativity of large language models (LLMs) in story writing without human annotations.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FollowBench
- IFEval
- Collie
- CIF-Bench
- InstructEval
- CFBench
- InfoBench

**Resources**:
- [GitHub Repository](https://github.com/anirudhlakkaraju/cs4_benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the creativity of large language models in story writing under varying levels of constraints.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Dataset consists of 50 user instructions and corresponding human-written reference stories.

**Size**: 500 unique prompts

**Format**: N/A

**Annotation**: Constraints are synthesized using GPT-4 and evaluated for satisfaction.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Constraint Satisfaction
- Story Coherence
- Output Diversity
- Creativity Scores

**Calculation**: Metrics are calculated based on the ratio of constraints satisfied and a combination of normalized coherence scores.

**Interpretation**: High scores indicate better adherence to constraints and higher creative output.

**Baseline Results**: N/A

**Validation**: Metrics validated against outputs from multiple LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
