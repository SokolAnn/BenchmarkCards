# Breaking Language Barriers: Equitable Performance in Multilingual Language Models

## 📊 Benchmark Details

**Name**: Breaking Language Barriers: Equitable Performance in Multilingual Language Models

**Overview**: This paper presents a new dataset of synthetic code-switched text derived from the CommonSenseQA dataset, aiming to improve performance in low-resource languages (LRLs) while maintaining high-resource language (HRL) performance.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Hindi
- English

**Similar Benchmarks**:
- CommonSenseQA
- LinCE

**Resources**:
- [GitHub Repository](https://github.com/tnagar72/Breaking-Language-Barriers-Equitable-Performance-in-Multilingual-Language-Models)

## 🎯 Purpose and Intended Users

**Goal**: To mitigate the performance gap in commonsense reasoning tasks between high-resource languages and low-resource languages through the development of synthetic code-switched datasets.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Commonsense Reasoning

**Limitations**: Current evaluation is on a single language pair, Hindi-English.

## 💾 Data

**Source**: Synthetic code-switched text derived from the CommonSenseQA dataset.

**Size**: 1,200 examples

**Format**: N/A

**Annotation**: The data was generated using controlled language-mixing methods based on prompts applied to existing datasets.

## 🔬 Methodology

**Methods**:
- Fine-tuning LLMs
- Synthetic code-switched text generation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the proportion of correctly answered questions out of the total number of questions in the test set.

**Interpretation**: Higher accuracy indicates better performance of the LLM on the test dataset.

**Baseline Results**: Baseline model accuracy results shown in Table 1.

**Validation**: Cross-validation methodology employed in experimental setup.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
