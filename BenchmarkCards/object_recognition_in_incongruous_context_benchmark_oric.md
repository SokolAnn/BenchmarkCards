# Object Recognition in Incongruous Context Benchmark (ORIC)

## 📊 Benchmark Details

**Name**: Object Recognition in Incongruous Context Benchmark (ORIC)

**Overview**: ORIC evaluates Large Vision-Language Models (LVLMs) on their performance in recognizing objects under contextual incongruity, where deviations from expected object-context relationships lead to misidentification and hallucinations.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- POPE
- Hallu-PI
- HallusionBench

**Resources**:
- [GitHub Repository](https://github.com/ZhaoyangLi-1/ORIC)

## 🎯 Purpose and Intended Users

**Goal**: To systematically analyze the impact of contextual incongruity on the performance of Large Vision-Language Models (LVLMs) in recognizing objects.

**Target Audience**:
- ML Researchers
- Model Developers
- AI Practitioners

**Tasks**:
- Object Recognition

**Limitations**: N/A

## 💾 Data

**Source**: MSCOCO validation set

**Size**: 1,000 images

**Format**: N/A

**Annotation**: Human annotation with a low error rate of 2%

## 🔬 Methodology

**Methods**:
- LLM-guided sampling
- CLIP-guided sampling

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated as standard binary classification performance metrics.

**Interpretation**: Higher values of precision, recall, and F1 Score indicate better performance in recognizing objects under contextual incongruity.

**Validation**: Evaluation of LVLMs across a range of prompts and testing conditions to ensure robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
