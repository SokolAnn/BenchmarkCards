# LHRS-Bot-Nova

## 📊 Benchmark Details

**Name**: LHRS-Bot-Nova

**Overview**: LHRS-Bot-Nova is a multimodal large language model (MLLM) specialized in understanding remote sensing (RS) imagery, designed to perform a wide range of RS understanding tasks aligned with human instructions. It features an enhanced vision encoder and a novel bridge layer and introduces a large-scale RS image-caption dataset, LHRS-Align-Recap, and an instruction dataset to improve spatial recognition abilities.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LHRS-Bench

**Resources**:
- [GitHub Repository](https://github.com/NJU-LHRS/LHRS-Bot)

## 🎯 Purpose and Intended Users

**Goal**: To provide improved capabilities in interpreting remote sensing images through a multimodal model that enhances visual understanding and human interaction capabilities.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Domain Experts

**Tasks**:
- Image Captioning
- Visual Question Answering
- Visual Grounding
- Scene Classification

**Limitations**: N/A

## 💾 Data

**Source**: Generated through feature-guided image recaptioning and instruction tuning.

**Size**: 76,600 images

**Format**: N/A

**Annotation**: Automatically generated captions using multimodal captioners.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on standard evaluation benchmarks for remote sensing image understanding tasks.

**Interpretation**: Good performance is indicated by higher accuracy scores across various tasks and benchmarks.

**Baseline Results**: LHRS-Bot-Nova achieved an average accuracy of 34.93% on the LHRS-Bench, outperforming previous models.

**Validation**: Validation procedures involve thorough testing across multiple RS image understanding tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
