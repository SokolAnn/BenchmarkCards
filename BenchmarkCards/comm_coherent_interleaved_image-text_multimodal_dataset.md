# CoMM (Coherent interleaved image-text MultiModal dataset)

## 📊 Benchmark Details

**Name**: CoMM (Coherent interleaved image-text MultiModal dataset)

**Overview**: CoMM is a high-quality coherent interleaved image-text dataset designed to enhance the coherence, consistency, and alignment of generated multimodal content.

**Data Type**: interleaved image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMC4
- OBELICS

**Resources**:
- [GitHub Repository](https://github.com/HKUST-LongGroup/CoMM)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality dataset for training and evaluating multimodal language models on interleaved image-text generation tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image-to-Text Sequence Generation
- Text-to-Image Sequence Generation
- Interleaved Image-Text Content Continuation
- Question-based Interleaved Image-Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Various sources of instructional content and visual storytelling including WikiHow and eHow.

**Size**: 227,000 documents with 2.28 million images

**Format**: N/A

**Annotation**: Filtered and refined using advanced models for coherence and relevance.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Development
- Completeness
- Image-Text Alignment
- METEOR
- ROUGE

**Calculation**: Metrics are calculated based on evaluations conducted by LLMs such as GPT-4o and Llama3.

**Interpretation**: Higher scores indicate better coherence, completeness, and alignment in interleaved image-text sequences.

**Baseline Results**: N/A

**Validation**: Dataset validated against previous datasets like MMC4 and OBELICS.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
