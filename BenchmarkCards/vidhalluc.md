# VIDHALLUC

## 📊 Benchmark Details

**Name**: VIDHALLUC

**Overview**: The largest benchmark designed to examine hallucinations in multimodal large language models (MLLMs) for video understanding tasks. It evaluates hallucinations across three dimensions: action, temporal sequence, and scene transition.

**Data Type**: Videos

**Domains**:
- Video Understanding

**Languages**:
- English

**Similar Benchmarks**:
- HallusionBench
- VideoHallucer
- Vript-HAL
- EventHallusion

**Resources**:
- [Resource](https://vid-halluc.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and understand hallucinations in multimodal large language models for video understanding tasks.

**Target Audience**:
- Researchers in AI
- Developers of MLLMs
- Academics in Computer Vision

**Tasks**:
- Assessing action hallucination
- Assessing temporal sequence hallucination
- Assessing scene transition hallucination

**Limitations**: N/A

**Out of Scope Uses**:
- Applications outside of video understanding
- Static content analysis

## 💾 Data

**Source**: Curated from existing video description datasets including ActivityNet, YouCook2, and VALOR32K.

**Size**: 5,002 videos and 9,295 QA pairs

**Format**: Videos in digital formats

**Annotation**: Dynamic video pairs with automated question generation targeting hallucination types.

## 🔬 Methodology

**Methods**:
- Semantic and Visual Similarity Filtering
- Automatic Question Generation
- Quality Filtering
- Human Validation

**Metrics**:
- Accuracy of hallucination identification
- Matthews correlation coefficient (MCC)
- Cosine similarity for scene description

**Calculation**: Accuracy is calculated using Ncorrect/Ntotal where Ncorrect is the number of correctly answered questions and Ntotal is the total questions asked.

**Interpretation**: Higher accuracy indicates better performance against hallucinations for MLLMs across the tasks defined.

**Baseline Results**: N/A

**Validation**: Extensive experiments conducted with ten state-of-the-art models including performance comparisons.

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination in generated content
- Misinterpretation of video content
- Inability to differentiate between visually similar video pairs

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Explainability**: Unexplainable output
- **Accuracy**: Poor model accuracy
- **Societal Impact**: Impact on Jobs

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
