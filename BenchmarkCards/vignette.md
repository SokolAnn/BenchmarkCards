# VIGNETTE

## 📊 Benchmark Details

**Name**: VIGNETTE

**Overview**: VIGNETTE is a large-scale VQA benchmark with 30M+ images for evaluating bias in vision-language models (VLMs) across four directions: factuality, perception, stereotyping, and decision making.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- VISBIAS
- VLBiasBench
- VL-StereoSet

**Resources**:
- [GitHub Repository](https://github.com/chahatraj/Vignette)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate bias in vision-language models through a structured question-answering framework.

**Target Audience**:
- ML Researchers
- AI Ethicists
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic images generated based on a unified set of visually representative identities and diverse activities.

**Size**: 30,000,000 images

**Format**: N/A

**Annotation**: Manually annotated identities and activities; validation by human annotators.

## 🔬 Methodology

**Methods**:
- Visual Question Answering
- Pairwise Comparison

**Metrics**:
- Selection Frequency
- Log Odds
- PairComp
- Polarity Score

**Calculation**: Metrics are calculated based on voter selections and comparisons across pairs of identities.

**Interpretation**: Higher selection frequencies indicate model bias or favorability towards specific identities.

**Baseline Results**: Results observed from three evaluated models: LLAVA-1.6-7B, LLAMA-3.2-11B-VISION-INSTRUCT, and DEEPSEEK-VL2-4.5B.

**Validation**: Evaluated against established metrics and validated through statistical significance testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
