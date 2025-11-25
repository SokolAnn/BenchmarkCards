# SAKURA (Speech and Audio-based Question-answering Benchmark for Multi-hop Reasoning of Large Audio-Language Models)

## 📊 Benchmark Details

**Name**: SAKURA (Speech and Audio-based Question-answering Benchmark for Multi-hop Reasoning of Large Audio-Language Models)

**Overview**: SAKURA is a benchmark assessing Large Audio-Language Models' (LALMs) multi-hop reasoning based on speech and audio information, comprising 4000 human-verified multiple-choice questions across various attributes.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ckyang1124/SAKURA)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate LALMs' multi-hop reasoning capabilities using speech and audio information.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Multi-hop Reasoning

**Limitations**: SAKURA currently covers only four speech/audio attributes and does not account for acoustic variations affecting model performance.

## 💾 Data

**Source**: Speech and audio sources from Common Voice, CREMA-D, MELD, and ESC-50 datasets.

**Size**: 4000 questions

**Format**: multiple-choice

**Annotation**: Questions generated using GPT-4o and verified by human annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on alignment between model responses and golden answers evaluated by GPT-4o.

**Interpretation**: Higher accuracy indicates better multi-hop reasoning capability in LALMs.

**Validation**: Human verification of evaluator judgments showed 99.5% agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
