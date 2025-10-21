# MMC OMPOSITION

## 📊 Benchmark Details

**Name**: MMC OMPOSITION

**Overview**: MMC OMPOSITION is a novel, human-annotated benchmark designed to evaluate the compositionality of pre-trained VLMs across three dimensions: compositional perception, reasoning, and probing, with a diverse set of 4,342 questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- GQA
- Winoground
- ARO

**Resources**:
- [Resource](https://hanghuacs.github.io/MMComposition)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and precise framework for evaluating the compositionality of VLMs, identifying key areas for improvement and suggesting potential directions for future advancements.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Visual Question Answering
- Compositional Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Various existing datasets including Visual Genome, VL-CheckList, Sugar-Crepe, and others.

**Size**: 4,342 questions

**Format**: N/A

**Annotation**: Human-annotated.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: The accuracy is calculated based on correct predictions across all annotations in various subtasks.

**Interpretation**: Higher accuracy indicates better compositional understanding by the VLMs.

**Baseline Results**: N/A

**Validation**: Empirically validated through evaluation of 54 VLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
