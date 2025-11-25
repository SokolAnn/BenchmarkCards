# LTLBench

## 📊 Benchmark Details

**Name**: LTLBench

**Overview**: LTLBench is a benchmark for evaluating the temporal reasoning ability of large language models (LLMs), constructed using a novel pipeline that generates controllable and scalable temporal reasoning problems based on random directed graph generation and linear temporal logic (LTL).

**Data Type**: text

**Domains**:
- Artificial Intelligence

**Languages**:
- English

**Similar Benchmarks**:
- TRAM
- TimeBench

**Resources**:
- [Resource](https://huggingface.co/datasets/RutaTang/LTLBench)
- [GitHub Repository](https://github.com/RutaTang/LTLBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the temporal reasoning ability of large language models and provide insights into their performance and robustness in handling temporal reasoning challenges.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Temporal Reasoning

**Limitations**: The evaluation includes a limited subset of LTL operators, omitting several complex operators that could enhance future assessments.

## 💾 Data

**Source**: Generated using a random graph generation process, linear temporal logic (LTL) formulas, and NuSMV model checking.

**Size**: 2,000 problems

**Format**: N/A

**Annotation**: Problems are labeled as True or False based on their ground truth obtained through model checking.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- AUC

**Calculation**: Accuracy, F1 Score, and AUC are calculated based on the model's performance on LTLBench problems.

**Interpretation**: Higher metrics indicate a better ability of models to handle complex temporal reasoning challenges.

**Baseline Results**: The model qwen:72b-chat shows the highest Accuracy at 0.60, F1 at 0.59, and AUC at 0.60.

**Validation**: The benchmark is validated through comprehensive evaluations on six large language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
