# Unmasking the Canvas (UTC Benchmark; UTCB)

## 📊 Benchmark Details

**Name**: Unmasking the Canvas (UTC Benchmark; UTCB)

**Overview**: Unmasking the Canvas (UTC Benchmark; UTCB) is a dynamic and scalable benchmark dataset to evaluate LLM vulnerability in image generation, combining structured prompt engineering and multilingual obfuscation.

**Data Type**: image generation prompts

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Zulu
- Gaelic

**Resources**:
- [Resource](https://huggingface.co/datasets/UTCB)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate image-based jailbreaks at scale and expose vulnerabilities in LLMs for responsible research.

**Target Audience**:
- Researchers
- Cybersecurity Experts

**Tasks**:
- Image Generation Security Evaluation

**Limitations**: The dataset may have incomplete annotative effects due to limited testing across a variety of models.

## 💾 Data

**Source**: Curated from various platforms and open-source datasets targeting image jailbreak vulnerabilities.

**Size**: 6,772 image-generation prompts

**Format**: CSV

**Annotation**: Mixed manual and automated tagging approaches, relying on LLM-aided verification and human verification.

## 🔬 Methodology

**Methods**:
- Automated metrics assessment
- Panel-based evaluation
- User testing

**Metrics**:
- Risk scoring

**Calculation**: Metrics are calculated based on the LLM's responses to the prompts, categorizing outputs based on success or failure in generating unsafe content.

**Interpretation**: High-risk prompts are flagged as potentially harmful based on the output generated.

**Validation**: Involves cross-verification of generated outputs against expected outcomes by experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Potential Harm**: ['Potential for unauthorized image generation leading to privacy violations.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All user interactions during dataset testing are anonymized for privacy protection.

**Data Licensing**: The dataset is available under special access conditions to ensure responsible use.

**Consent Procedures**: Users must acknowledge the risks and intended use of the dataset before access is granted.

**Compliance With Regulations**: Not Applicable
