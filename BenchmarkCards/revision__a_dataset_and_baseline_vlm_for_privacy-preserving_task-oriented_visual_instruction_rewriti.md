# ReVision: A Dataset and Baseline VLM for Privacy-Preserving Task-Oriented Visual Instruction Rewriting

## 📊 Benchmark Details

**Name**: ReVision: A Dataset and Baseline VLM for Privacy-Preserving Task-Oriented Visual Instruction Rewriting

**Overview**: This paper introduces a dataset for Visual Instruction Rewriting, encompassing over 39,000 examples across 14 diverse domains, aimed at enabling privacy-preserving interactions in multimodal environments.

**Data Type**: image-original instruction-rewritten instruction triplets

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/abhijitmishra/visual_instruction_rewriting)
- [Resource](https://huggingface.co/datasets/hsiangfu/multimodal_query_rewrites)
- [Resource](https://huggingface.co/hsiangfu/ReVision-250M-256-16-baseline)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to develop a lightweight and privacy-preserving multimodal interaction framework by rewriting visual instructions into text commands.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Text Classification
- Semantic Parsing

**Limitations**: The dataset is monolingual, limiting its applicability to multilingual and culturally varied settings.

## 💾 Data

**Source**: Dataset consists of image-original instruction-rewritten instruction triplets, derived from real-world scenarios including images sourced from publicly available datasets.

**Size**: 39,023 examples

**Format**: N/A

**Annotation**: Generated and validated using OpenAI's GPT-4 model and human annotators via Amazon Mechanical Turk.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU
- METEOR
- ROUGE

**Calculation**: Metrics are calculated to assess the linguistic similarity and effectiveness of instruction rewriting.

**Interpretation**: Higher scores in BLEU, ROUGE, and METEOR indicate better alignment with original intents and improved instruction clarity.

**Validation**: Human evaluations through Amazon Mechanical Turk to validate the accuracy of rewritten instructions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Safety

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The framework eliminates the need to transmit personal visual data, ensuring a privacy-centric model.

**Data Licensing**: Dataset is sourced from publicly available datasets ensuring compliance with fair use policies.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
