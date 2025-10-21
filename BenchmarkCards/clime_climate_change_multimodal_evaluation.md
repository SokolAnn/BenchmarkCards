# CliME (Climate Change Multimodal Evaluation)

## 📊 Benchmark Details

**Name**: CliME (Climate Change Multimodal Evaluation)

**Overview**: CliME is a first-of-its-kind multimodal dataset comprising 2579 Twitter and Reddit posts, rich in humorous memes and skeptical content, intended for evaluating the performance of large language models (LLMs) in understanding and generating credible climate discourse.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MultiClimate
- GreenScreen

**Resources**:
- [Resource](https://huggingface.co/datasets/climedataset/)

## 🎯 Purpose and Intended Users

**Goal**: To assess the ability of large language models to comprehend and generate credible climate-related communications.

**Target Audience**:
- ML Researchers
- Climate Scientists
- Policy Makers

**Tasks**:
- Text Generation
- Text Classification

**Limitations**: The dataset relies on existing pre-trained models for assessment, which may not capture the latest social media trends effectively.

## 💾 Data

**Source**: Scraped posts from Twitter (now X) and Reddit focusing on climate-related discourse.

**Size**: 2,579 examples

**Format**: JSON

**Annotation**: Manual review and human annotation for generated descriptions to ensure alignment with intended meanings.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Climate Alignment Quotient (CAQ)

**Calculation**: CAQ is calculated as a weighted sum of five core metrics: Articulation, Evidence, Resonance, Transition, and Specificity.

**Interpretation**: Higher CAQ scores indicate stronger alignment with effective climate communication, characterized by coherent articulation, strong evidence, and actionable specifics.

**Validation**: Evaluation based on five state-of-the-art LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset captures a range of climate discourse but does not explicitly analyze demographic factors.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected from publicly accessible posts without retaining personally identifiable information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
