# MathBridge

## 📊 Benchmark Details

**Name**: MathBridge

**Overview**: MathBridge is the first extensive dataset for translating mathematical spoken sentences into LaTeX formulas, comprising approximately 23 million LaTeX formulas paired with their corresponding mathematical spoken sentences.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/MathBridge)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the conversion of mathematical spoken expressions into LaTeX format for improved accessibility and comprehension in educational contexts.

**Target Audience**:
- ML Researchers
- Education Technologists
- Content Creators

**Tasks**:
- Text-to-LaTeX Translation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from pre-prints and articles on arXiv in 2023 and open-source textbooks.

**Size**: 23 million examples

**Format**: N/A

**Annotation**: Automatically generated using language models and filtering steps.

## 🔬 Methodology

**Methods**:
- Fine-tuning of pretrained language models

**Metrics**:
- sacreBLEU
- ROUGE
- Character Error Rate (CER)
- Word Error Rate (WER)

**Calculation**: Metrics are calculated based on comparisons between the generated LaTeX and ground truth LaTeX outputs.

**Interpretation**: Increased scores indicate better translation accuracy for spoken mathematical expressions.

**Baseline Results**: For the T5-large model, the sacreBLEU score increased from 4.77 to 46.8 after fine-tuning with MathBridge.

**Validation**: Performance was evaluated through fine-tuning on the MathBridge dataset and subsequent testing on a held-out dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
