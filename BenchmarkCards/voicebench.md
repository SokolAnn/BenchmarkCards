# VoiceBench

## 📊 Benchmark Details

**Name**: VoiceBench

**Overview**: VoiceBench is the first benchmark designed to provide a multi-faceted evaluation of LLM-based voice assistants, assessing their performance in various real-world scenarios including speaker characteristics, environmental factors, and content variations.

**Data Type**: spoken instructions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AIR-Bench

**Resources**:
- [GitHub Repository](https://github.com/MatthewCYM/VoiceBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the multi-faceted capabilities of LLM-based voice assistants and identify areas for improvement.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- General Knowledge Evaluation
- Instruction Following
- Safety Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Real and synthetic spoken instructions with various attributes and complexities.

**Size**: 3,894 samples

**Format**: N/A

**Annotation**: Data annotated based on response accuracy and safety evaluations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Refusal Rate

**Calculation**: Metrics are calculated based on the performance of models against ground-truth instructions and safety criteria.

**Interpretation**: Higher scores indicate better performance in understanding and responding to the spoken instructions.

**Baseline Results**: Comparison of various LLM-based and pipeline voice assistants.

**Validation**: The evaluation framework is tested across various speaker and environmental conditions to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack, Prompt injection attack
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in prompt

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
