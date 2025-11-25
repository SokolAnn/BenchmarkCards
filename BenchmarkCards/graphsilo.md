# GraphSilo

## 📊 Benchmark Details

**Name**: GraphSilo

**Overview**: GraphSilo is the largest dataset for graph reasoning problems with fine-grained step-wise labels, built using automated Task-oriented Trajectories and Monte Carlo Tree Search to generate detailed reasoning steps with step-wise labels.

**Data Type**: graph tasks with step-wise reasoning

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GraphWiz

**Resources**:
- [GitHub Repository](https://github.com/GKNL/GraphPRM)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the reasoning capabilities of large language models using process reward models for graph computational problems.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Graph Reasoning
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: GraphSilo dataset built using automated methods for generating graph reasoning tasks.

**Size**: 118,189 examples

**Format**: N/A

**Annotation**: Automated labeling with Task-oriented Trajectories and Monte Carlo Tree Search.

## 🔬 Methodology

**Methods**:
- Inference-Time Scaling
- Reinforcement Learning
- Direct Preference Optimization

**Metrics**:
- Accuracy

**Calculation**: Incremental scoring based on step-wise labels during reinforcement learning and inference.

**Interpretation**: Higher scores correspond to more correct reasoning in each step.

**Baseline Results**: N/A

**Validation**: Evaluation against multiple known graph reasoning tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
