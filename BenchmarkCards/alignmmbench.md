# AlignMMBench

## 📊 Benchmark Details

**Name**: AlignMMBench

**Overview**: AlignMMBench is a comprehensive evaluation benchmark specifically designed to assess the Chinese alignment capabilities of Vision-Language Models. It includes 1,054 images and 4,978 question-answer pairs, covering thirteen specific tasks across three categories, incorporating both single-turn and multi-turn dialogue scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/THUDM/AlignMMBench)

## 🎯 Purpose and Intended Users

**Goal**: To assess the alignment capabilities of large Vision-Language Models in Chinese contexts and provide a robust evaluation framework for future improvements in multimodal models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image Captioning
- Visual Question Answering
- Dialogue Generation

**Limitations**: None

## 💾 Data

**Source**: Collected from real-world scenarios and internet sources; image queries generated based on user requests.

**Size**: 4,978 question-answer pairs

**Format**: N/A

**Annotation**: Manual annotation by experts, including a detailed two-phase review process.

## 🔬 Methodology

**Methods**:
- Automated evaluation using CritiqueVLM
- Human evaluation

**Metrics**:
- Alignment score
- Mean Absolute Error

**Calculation**: Scores are generated based on the responses from the AI models compared to human annotations.

**Interpretation**: Higher scores indicate better alignment and understanding capabilities of models in the corresponding tasks.

**Baseline Results**: CritiqueVLM exceeds GPT-4 in evaluation accuracy for task completion across benchmarks

**Validation**: Internal testing dataset to assess reliability and performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: Potential for bias in evaluation based on the limited representation of the Chinese visual context.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
