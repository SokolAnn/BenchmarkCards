# MCA-Bench: A Multimodal Benchmark for Evaluating CAPTCHA Robustness Against VLM-based Attacks

## 📊 Benchmark Details

**Name**: MCA-Bench: A Multimodal Benchmark for Evaluating CAPTCHA Robustness Against VLM-based Attacks

**Overview**: MCA-Bench is the first end-to-end CAPTCHA security benchmark spanning four modalities—static visual recognition, point-and-click localization, interactive manipulation, and textual logic Q&A—across twenty real-world tasks. It provides over 180,000 training samples and a 4,000-item test set.

**Data Type**: image-caption pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/noheadwuzonglin/MCA-Bench)
- [Resource](https://www.kaggle.com/datasets/luffy798/mca-benchmultimodal-captchas)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and reproducible benchmarking suite that integrates heterogeneous CAPTCHA types into a single evaluation protocol.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Security Analysts

**Tasks**:
- Static Visual Recognition
- Point-and-Click Localization
- Interactive Manipulation
- Textual Logic Q&A

**Limitations**: N/A

## 💾 Data

**Source**: Mixed directly created and publicly sourced datasets adhering to licensing agreements and privacy regulations.

**Size**: 180,000 training samples and 4,000 test samples

**Format**: JSON

**Annotation**: Manual filtering and automated generation for structured, semantically relevant QA pairs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Pass rate

**Calculation**: Pass rates indicate the success of models in correctly solving CAPTCHA tasks.

**Interpretation**: A higher pass rate indicates better performance; models exceed 96% accuracy on simple tasks but drop to as low as 2.5% on complex ones.

**Baseline Results**: N/A

**Validation**: Evaluation reveals relations between challenge complexity, interaction depth, and model solvability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Artificial Intelligence Security

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Ensured compliance through preprocessing steps like anonymization.

**Data Licensing**: Datasets will be made publicly available with licenses that allow free usage for research purposes.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
