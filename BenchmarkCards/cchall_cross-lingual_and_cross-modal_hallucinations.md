# CCHall (Cross-lingual and Cross-modal Hallucinations)

## 📊 Benchmark Details

**Name**: CCHall (Cross-lingual and Cross-modal Hallucinations)

**Overview**: CCHall is a novel benchmark for detecting joint cross-lingual and cross-modal hallucinations in large language models, aimed at evaluating the capabilities of LLMs in handling complex hallucination scenarios.

**Data Type**: image-question-answer pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- French
- Spanish
- Portuguese
- Czech
- Dutch
- Swedish
- Croatian
- Welsh
- Swahili

**Similar Benchmarks**:
- mFACT
- MM-Eval
- HallusionBench

**Resources**:
- [GitHub Repository](https://github.com/BRZ911/CCHall)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for assessing the hallucination capabilities of large language models in joint cross-lingual and cross-modal contexts.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Hallucination Detection

**Limitations**: Current methods still struggle with effectively addressing cross-lingual and cross-modal hallucinations.

## 💾 Data

**Source**: Various multimodal tasks including Visual Question Answering and Image Captioning datasets such as GQA, XM3600, AMBER, and xFlickr&Co.

**Size**: 3,600 entries

**Format**: JSON

**Annotation**: Automatically generated with human verification for accuracy

## 🔬 Methodology

**Methods**:
- Direct evaluation
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Macro-F1 Score

**Calculation**: Computed based on the outputs of large language models evaluated on CCHall.

**Interpretation**: Higher scores indicate better performance at hallucination detection.

**Baseline Results**: InternVL2-8B: 34.0% Accuracy; GPT-4o (HalluciMAD): 77.5% Accuracy.

**Validation**: Experimentally validated through evaluation across multiple large language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: Analysis of language resource categories shows varying performance based on language availability.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
