# MMDU (Multi-Turn Multi-Image Dialog Understanding)

## 📊 Benchmark Details

**Name**: MMDU (Multi-Turn Multi-Image Dialog Understanding)

**Overview**: MMDU is a comprehensive benchmark designed to evaluate and improve Large Vision-Language Models (LVLMs) abilities in multi-turn and multi-image conversations, addressing the limitations of existing benchmarks which primarily focus on single-choice questions or short-form responses.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMStar
- MathVista
- ChartQA

**Resources**:
- [GitHub Repository](https://github.com/Liuziyu77/MMDU)
- [Resource](https://huggingface.co/datasets/laolao77/MMDU)

## 🎯 Purpose and Intended Users

**Goal**: To assess the multi-turn, multi-image dialog understanding capabilities of LVLMs, specifically designed for human-AI interaction.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Data is sourced from Wikipedia entries, including images and textual information, which are clustered and annotated for creating multi-turn dialogues.

**Size**: 45,000 dialogues

**Format**: N/A

**Annotation**: Human annotators reviewed and verified the dialogues generated with the assistance of the GPT-4o model.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the output quality in response to questions generated using the benchmark.

**Interpretation**: Higher scores indicate better understanding and reasoning abilities of the models evaluated.

**Baseline Results**: The best open-source model scores 42.8%, whereas closed-source models like GPT-4o reach 70.2%.

**Validation**: Benchmark validated using multiple rounds of human and model evaluations to ensure reliability and performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
