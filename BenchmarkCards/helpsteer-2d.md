# HelpSteer-2D

## 📊 Benchmark Details

**Name**: HelpSteer-2D

**Overview**: HelpSteer-2D is a 2-dimensional preference dataset for improving alignment of Large Language Models with human preferences by evaluating responses across multiple aspects and segments.

**Data Type**: 2-dimensional scores for segment and aspect evaluation

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)

**Resources**:
- [Resource](https://anonymous.4open.science/r/2D-DPO-56E4/)

## 🎯 Purpose and Intended Users

**Goal**: To enable fine-grained alignment of Large Language Models through enhanced preference scoring across segments and aspects.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Preference Optimization

**Limitations**: Performance is only demonstrated on 7B models; it needs more extensive evaluation on larger foundational models.

## 💾 Data

**Source**: Constructed dataset composed of annotated responses with 2-dimensional scores based on segment and aspect breakdowns.

**Size**: N/A

**Format**: N/A

**Annotation**: Annotated using a combination of LLMs and human feedback for quality assurance.

## 🔬 Methodology

**Methods**:
- Preference Optimization

**Metrics**:
- Accuracy

**Calculation**: Utilizes a fine-grained scoring approach across segments and aspect levels in the alignment framework.

**Interpretation**: Higher scores reflect better performance in aligning model outputs with human preferences based on two-dimensional feedback.

**Baseline Results**: Compared against previous methods such as DPO and 1D-DPO, showing improvements across various benchmarks.

**Validation**: Extensive evaluation on three benchmarks: Arena-Hard, AlpacaEval 2.0, MT-Bench.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
