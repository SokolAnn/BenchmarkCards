# AMBER

## 📊 Benchmark Details

**Name**: AMBER

**Overview**: AMBER is an LLM-free multi-dimensional benchmark designed for evaluating hallucinations in Multi-modal Large Language Models (MLLMs). It addresses the challenges of evaluating hallucinations effectively across generative and discriminative tasks.

**Data Type**: Image and Text

**Domains**:
- Multi-modal
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/junyangwang0410/AMBER)

## 🎯 Purpose and Intended Users

**Goal**: To provide an efficient and comprehensive evaluation framework for hallucinations in MLLMs.

**Target Audience**:
- Researchers
- Developers of MLLMs
- AI practitioners

**Tasks**:
- Evaluate hallucinations in MLLMs
- Analyze performance across various tasks
- Mitigate hallucination issues

**Limitations**: None

## 💾 Data

**Source**: MS-COCO 2014 test set and UnSplash

**Size**: 1004 images

**Format**: Image

**Annotation**: Existence, attribute, relation, hallucinatory target objects

## 🔬 Methodology

**Methods**:
- Image collection
- Image annotation
- Prompt template design
- Evaluation pipeline

**Metrics**:
- CHAIR
- Cover
- Hal
- Cog
- Accuracy
- Precision
- Recall
- F1
- AMBER Score

**Calculation**: Various metrics calculated based on the responses obtained from MLLMs using specific prompts and annotations.

**Interpretation**: Evaluation of hallucination types across MLLMs using derived metrics.

**Validation**: Responses processed and validated based on established metrics for hallucination evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination evaluation
- Model performance assessment

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Transparency**: Lack of training data transparency
- **Privacy**: Exposing personal information
- **Fairness**: Output bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected from publicly available sources (UnSplash with CC0 license) ensures privacy compliance.

**Data Licensing**: Images from MS-COCO test set and UnSplash are used without licensing issues.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
