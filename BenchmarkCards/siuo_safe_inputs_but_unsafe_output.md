# SIUO (Safe Inputs but Unsafe Output)

## 📊 Benchmark Details

**Name**: SIUO (Safe Inputs but Unsafe Output)

**Overview**: SIUO introduces a cross-modality benchmark that evaluates the safety alignment of Large Vision-Language Models by considering cases where single modalities may be safe on their own but can lead to unsafe outputs when combined.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Similar Benchmarks**:
- VLSafe
- GOAT-Bench
- MM-Safetybench

**Resources**:
- [Resource](https://sinwang20.github.io/SIUO/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the cross-modality safety alignment of Large Vision-Language Models by identifying safety vulnerabilities when combining safe inputs.

**Target Audience**:
- AI Researchers
- Developers of Large Vision-Language Models
- Safety Analysts

**Tasks**:
- Safety Evaluation
- Effectiveness Evaluation

**Limitations**: The current dataset size is not large but covers 9 safety aspects and 33 subcategories.

## 💾 Data

**Source**: Human curation and AI-assisted curation methods were utilized to construct the SIUO dataset.

**Size**: 1,079 test cases

**Format**: JSONL

**Annotation**: Data annotated through manual reviews and consensus by team members, ensuring quality.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics using GPT-4V

**Metrics**:
- Safe Rate
- Effective Rate

**Calculation**: Safe Rate is the ratio of safe responses to total responses, and Effective Rate is the ratio of effective responses to total responses.

**Interpretation**: Safe responses are those that do not lead to unsafe behavior, while effective responses are those that adequately address user inquiries.

**Validation**: Dual validation through automated model safety reviews and human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data derived from publicly available sources, ensuring compliance with privacy regulations and anonymizing identifiable information.

**Data Licensing**: Dataset sourced from public and openly licensed datasets, adhering to relevant copyright policies.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
