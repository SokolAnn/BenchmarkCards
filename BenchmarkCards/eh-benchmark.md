# EH-Benchmark

## 📊 Benchmark Details

**Name**: EH-Benchmark

**Overview**: EH-Benchmark is a novel ophthalmology benchmark designed to evaluate hallucinations in Medical Large Language Models (MLLMs), categorizing hallucinations based on specific tasks and error types into two primary classifications: Visual Understanding and Logical Composition, across three levels of clinical reasoning.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedHEval
- MedHallBench

**Resources**:
- [GitHub Repository](https://github.com/ppxy1/EH-Benchmark)
- [Resource](https://drive.google.com/file/d/1S4-RyfSjgZUodghn70c7TqXNI4WDeUJG/view?usp=sharing)
- [Resource](https://drive.google.com/file/d/1HNkkPoYmIRRrPRombB___SdMEH3Auzpr/view?usp=sharing)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate hallucinations in Medical Large Language Models (MLLMs) specific to ophthalmology and propose a framework for hallucination mitigation.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Ophthalmology Experts

**Tasks**:
- Visual Question Answering
- Diagnostic Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Includes data collected from 13 ophthalmic datasets that capture a variety of clinical scenarios and hallucination behaviors.

**Size**: 27,000 questions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Precision
- Recall
- Accuracy

**Calculation**: Metrics are calculated based on the performance of MLLMs over specified tasks within the benchmark.

**Interpretation**: Higher scores indicate better performance in mitigating hallucination while maintaining accuracy.

**Baseline Results**: State-of-the-art performance surpassing existing models.

**Validation**: The benchmark validation includes automatic assessment of tool outputs against ground truth using a multi-agent evaluation framework.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy
- Robustness

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
