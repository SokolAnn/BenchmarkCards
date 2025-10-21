# BannerRequest400

## 📊 Benchmark Details

**Name**: BannerRequest400

**Overview**: BannerRequest400 is a benchmark featuring 100 unique logos paired with 400 diverse banner requests, designed for evaluating advertising banner generation systems.

**Data Type**: text-image pairs

**Domains**:
- Marketing
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2503.11060)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and advance automatic advertising banner design generation capabilities through diverse design requests.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Banner Design Generation

**Limitations**: The benchmark primarily utilizes logo images as multimodal input and does not address product images or complex decorative elements.

## 💾 Data

**Source**: Curated logos and banner design requests synthesized for the benchmark.

**Size**: 5,200 multimodal specifications

**Format**: JSON

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Target Audience Alignment
- Logo Placement Score
- Call-to-Action Effectiveness
- Copywriting Quality
- Brand Identity Score
- Aesthetic Quality Score

**Calculation**: Metrics are based on assessments from human evaluators and GPT-4o ratings across multiple iterations.

**Interpretation**: Higher scores indicate better performance in generating banner designs that align with marketing objectives.

**Baseline Results**: Comparative evaluations against models including DALL-E3, FLUX.1-schnell, and OpenCOLE demonstrated the superior performance of the BannerAgency framework.

**Validation**: Continuous validation through human studies and automated metric evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
