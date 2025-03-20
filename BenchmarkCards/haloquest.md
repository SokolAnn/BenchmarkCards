# HaloQuest

## 📊 Benchmark Details

**Name**: HaloQuest

**Overview**: HaloQuest is a novel visual question answering dataset designed to capture various aspects of multimodal hallucination, including false premises, insufficient context, and visual challenges.

**Data Type**: visual question answering

**Domains**:
- multimodal reasoning

**Resources**:
- [GitHub Repository](https://github.com/google/haloquest)

## 🎯 Purpose and Intended Users

**Goal**: To advance multimodal reasoning and reduce hallucination in vision-language models (VLMs).

**Target Audience**:
- AI researchers
- Developers of vision-language models

**Tasks**:
- Evaluate multimodal hallucination
- Fine-tune models for better performance

**Limitations**: None

## 💾 Data

**Source**: Combination of real images from Open Images dataset and synthetic images from online galleries (Midjourney and Stable Diffusion).

**Size**: Over 7.7K examples

**Format**: Visual question-answer pairs

**Annotation**: Human and LLM-generated questions, answers, and filtering for quality.

## 🔬 Methodology

**Methods**:
- Data collection from real and synthetic images
- Crowdsourcing for question generation
- LLM-assisted question and answer generation

**Metrics**:
- Zero-shot accuracy
- Fine-tuning performance
- Auto-Eval correlation with human evaluators

**Calculation**: Correlation coefficients for evaluation metrics (e.g., r=0.97 for generated vs. real images, r=0.99 for Auto-Eval vs human ratings).

**Interpretation**: Evaluation based on the model's ability to answer questions related to visual hallucination.

**Validation**: Fine-tuning models on HaloQuest shows improved performance while maintaining other task performances.

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination in visual question answering
- Model performance inconsistency
- Overfitting on training data

**Atlas Risks**:
- **Robustness**: Hallucination
- **Value Alignment**: Improper data curation

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dataset collection from open sources ensures compliance with privacy standards.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
