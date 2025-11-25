# CoMT (Chain of Multi-modal Thought)

## 📊 Benchmark Details

**Name**: CoMT (Chain of Multi-modal Thought)

**Overview**: CoMT is a novel benchmark for evaluating Chain of Multi-modal Thought (CoMT) reasoning which requires both multi-modal input and output, incorporating visual operations for enhanced reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MCoT (Multimodal Chain-of-Thought)
- ScienceQA

**Resources**:
- [GitHub Repository](https://github.com/czhhzc/CoMT)

## 🎯 Purpose and Intended Users

**Goal**: To assess the multi-modal reasoning capabilities of Large Vision-Language Models through the Chain of Multi-modal Thought tasks.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Multi-modal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Developed from GeoQA+, JHU-CROWD++, KILOGRAM datasets, and online data sources.

**Size**: 3,853 samples, 14,801 images

**Format**: N/A

**Annotation**: Annotated by multiple experts, following a template-based approach.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Macro-F1

**Calculation**: Metrics calculated based on the standard question-answering performance metrics.

**Interpretation**: Higher accuracy and Macro-F1 indicate better performance.

**Baseline Results**: Models often perform at random chance levels in zero-shot configurations.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack, Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected from publicly available datasets with permission for academic use.

**Data Licensing**: Not Applicable

**Consent Procedures**: All annotators signed informed consent documents.

**Compliance With Regulations**: Not Applicable
