# 6GPlan

## 📊 Benchmark Details

**Name**: 6GPlan

**Overview**: 6GPlan is a novel dataset designed for hierarchical debate-based task planning related to network management in 6G networks, consisting of 110 complex tasks and 5000 keyword solutions.

**Data Type**: complex task planning

**Domains**:
- Network Management
- Telecommunications

**Languages**:
- English

**Similar Benchmarks**:
- TeleQnA
- NetEval
- ORAN-bench-13

**Resources**:
- [GitHub Repository](https://github.com/haozhou1995/6GPlan_Dataset.git)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve complex task planning and management capabilities of large language models in the context of 6G networks.

**Target Audience**:
- ML Researchers
- Telecommunications Engineers
- Network Planners

**Tasks**:
- Task Planning
- Network Management Optimization

**Limitations**: N/A

## 💾 Data

**Source**: Generated from expert prompts and verified through human corrections.

**Size**: 110 tasks and around 5,000 keywords

**Format**: N/A

**Annotation**: Human verification and correction for quality assurance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro Coverage Rate (MCR)
- Keyword Hit Count (KHC)
- Global Recall Rate (GRR)

**Calculation**: Metrics are calculated based on the comparison of generated solutions against a set of gold-standard keywords for each task.

**Interpretation**: Higher values in MCR, KHC, and GRR indicate better performance in retrieving and generating relevant solutions.

**Baseline Results**: MCR for Baseline: 36.99%, for Regular Debate: 49.75%, and for Hierarchical Debate: 81.19%.

**Validation**: Performance comparison with baseline techniques through experimental evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
