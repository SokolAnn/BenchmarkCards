# RS-GPT4V (Unified Multimodal Instruction-Following Dataset for Remote Sensing Image Understanding)

## 📊 Benchmark Details

**Name**: RS-GPT4V (Unified Multimodal Instruction-Following Dataset for Remote Sensing Image Understanding)

**Overview**: RS-GPT4V is a high-quality, diversified, and unified multimodal instruction-following dataset for remote sensing image understanding, designed to support tasks such as image description, visual question answering, and reasoning capabilities using a unified (Question, Answer) format.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RS5M
- SkyScrip
- LHRS-Align
- MMRS-1M

**Resources**:
- [GitHub Repository](https://github.com/GeoX-Lab/RS-GPT4V)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for enhancing the capabilities of multimodal instruction-following models in remote sensing.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Image Captioning
- Visual Question Answering
- Visual Grounding
- Multi-turn Conversation

**Limitations**: The overall scale remains limited, particularly in specific application scenarios involving infrared and SAR modalities, where data support is insufficient.

## 💾 Data

**Source**: Various remote sensing visual language datasets including NWPU-Captions, RSICD, RSITMD, Sydney-Captions, and RSVQA.

**Size**: 91,937 training images, 991,206 question-answer pairs, 15,999 test images, 258,419 question-answer pairs

**Format**: N/A

**Annotation**: The dataset includes images with diverse annotations through manual correction and automatic generation by GPT-4V.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- METEOR
- ROUGE-L
- CIDEr
- SPICE

**Calculation**: Metrics are calculated based on the quality of generated responses from multimodal models fine-tuned with RS-GPT4V.

**Interpretation**: Higher scores indicate better performance in accurately describing images and understanding complex tasks.

**Validation**: The dataset was evaluated through experiments with benchmark models such as Full-FT, LoRA, and MoE-LoRA.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
