# HalluLens: LLM Hallucination Benchmark

## 📊 Benchmark Details

**Name**: HalluLens: LLM Hallucination Benchmark

**Overview**: HalluLens is a comprehensive hallucination benchmark that includes both new extrinsic and existing intrinsic evaluation tasks, distinguishing between extrinsic and intrinsic hallucinations to promote consistency and facilitate research.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/facebookresearch/HalluLens)

## 🎯 Purpose and Intended Users

**Goal**: To establish a clear taxonomy of hallucinations, introduce new extrinsic hallucination evaluation tasks, and provide a comprehensive analysis of existing benchmarks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Extrinsic Hallucination Evaluation
- Intrinsic Hallucination Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Dynamic test set generation based on Wikipedia content and automatically generated entities.

**Size**: 5,000 questions

**Format**: JSON

**Annotation**: Automatically generated responses with human verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the proportion of correct responses and hallucinations detected.

**Interpretation**: A good performance indicates lower hallucination rates and higher accuracy in extrinsic tasks.

**Baseline Results**: N/A

**Validation**: Validation involves ensuring dynamically generated sets maintain low variance over different trials.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
