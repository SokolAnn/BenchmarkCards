# StructFlowBench

## 📊 Benchmark Details

**Name**: StructFlowBench

**Overview**: StructFlowBench is a multi-turn instruction following benchmark with structural flow modeling, designed to capture the structural intricacies of complex dialogue scenarios.

**Data Type**: multi-turn dialogues

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MT-Bench
- Multi-IF
- MT-Eval

**Resources**:
- [GitHub Repository](https://github.com/MLGroupJLU/StructFlowBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models' capabilities in multi-turn instruction following by incorporating structural dependencies between dialogue turns.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multi-turn Instruction Following

**Limitations**: The current StructFlowBench is more of an exploration of new directions in evaluating multi-turn dialogue instruction following rather than targeting an increase in difficulty of the evaluation set.

## 💾 Data

**Source**: Data generated from user prompts across various topics and structured dialogue relationships.

**Size**: 155 dialogues

**Format**: JSON

**Annotation**: Annotated using GPT-4o with manual review

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Constraint Satisfaction Rate (CSR)
- Instruction Satisfaction Rate (ISR)
- Decomposed Requirements Following Ratio (DRFR)
- Weighted Constraint Satisfaction Rate (WCSR)

**Calculation**: Metrics are calculated based on satisfied constraints ratios and defined formulas for each metric.

**Interpretation**: Higher scores on metrics indicate better model performance in following complex multi-turn instructions.

**Baseline Results**: Evaluation conducted on 13 state-of-the-art LLMs including GPT-4o and DeepSeek-v3.

**Validation**: The evaluation framework utilizes a 'Golden Context' approach for reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Utilizes GPT-4o for data generation with manual review to filter inappropriate content.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
