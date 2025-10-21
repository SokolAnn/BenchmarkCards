# HowToDIV

## 📊 Benchmark Details

**Name**: HowToDIV

**Overview**: HowToDIV is a large-scale dataset comprising 507 conversations and 6,636 user-expert dialogue turns, involving task assistance across diverse domains such as cooking, mechanics, and planting. It enables the generation of interactive dialogues for procedural tasks without manual data collection.

**Data Type**: conversation pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- HoloAssist
- EgoPER
- NIV

**Resources**:
- [GitHub Repository](https://github.com/google/howtodiv)

## 🎯 Purpose and Intended Users

**Goal**: To present a scalable and cost-efficient dataset for generating dialogues in procedural task assistance, aiding in the training of AI agents.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Dialogue Generation
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Built upon two publicly available instructional video datasets: Narrated Instruction Videos (NIV) and Egocentric Procedural Error (EgoPER).

**Size**: 24 hours of video footage, 507 conversations, 6,636 dialogue turns

**Format**: N/A

**Annotation**: Automatic generation using large language models, no manual annotation.

## 🔬 Methodology

**Methods**:
- Dialogue generation using pre-trained language models
- Video localization

**Metrics**:
- BLEU Score
- ROUGE Score
- LLM-as-a-Judge Score

**Calculation**: Metrics are calculated based on the overlap between generated outputs and reference texts for dialogue turns.

**Interpretation**: BLEU scores range from 0 to 1; higher values indicate better match to reference dialogues. The LLM-as-a-Judge score is on a scale from 1 to 5, with higher scores indicating better quality.

**Baseline Results**: Gemma-3 model scores: BLEU = 0.32, ROUGE-L = 0.270, LLM-as-Judge = 2.87.

**Validation**: Dataset is split into training (70%), validation (10%), and testing (20%) sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
