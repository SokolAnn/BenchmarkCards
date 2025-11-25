# PRISM (Prompt Template Stealing Benchmark)

## 📊 Benchmark Details

**Name**: PRISM (Prompt Template Stealing Benchmark)

**Overview**: PRISM is a benchmark for prompt template stealing consisting of 50 templates and 450 images, organized into Easy and Hard difficulty levels.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://whitepagewu.github.io/evostealer-site)

## 🎯 Purpose and Intended Users

**Goal**: To systematically study the prompt template stealing attack and evaluate the vulnerability of visual language models.

**Target Audience**:
- Security Researchers
- AI Developers
- ML Researchers

**Limitations**: The benchmark's single-subject design limits its applicability to multi-subject templates in real-world applications.

## 💾 Data

**Source**: Templates sourced from PromptBase and LaPrompt, with images generated using DALL·E 3.

**Size**: 450 images

**Format**: N/A

**Annotation**: Templates were manually curated for subject-prompt alignment and stylistic consistency.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Subject Similarity
- Style Similarity
- Semantic Similarity
- Human Evaluation

**Calculation**: Fitness function based on semantic and style similarity.

**Interpretation**: Higher similarity scores indicate better template reproduction and generalization capabilities.

**Validation**: Extensive experiments were conducted across both open-source and closed-source models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Security

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The capability to extract templates may pose risks to creators' intellectual property even without fine-tuning.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
