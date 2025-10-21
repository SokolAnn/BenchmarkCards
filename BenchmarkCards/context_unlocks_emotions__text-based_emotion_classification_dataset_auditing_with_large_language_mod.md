# Context Unlocks Emotions: Text-based Emotion Classification Dataset Auditing with Large Language Models

## 📊 Benchmark Details

**Name**: Context Unlocks Emotions: Text-based Emotion Classification Dataset Auditing with Large Language Models

**Overview**: The paper introduces a method for auditing text-based emotion classification datasets by using Large Language Models (LLMs) to enhance the contextual information of emotional labels, improving alignment between inputs and human-annotated labels, demonstrated through human evaluations and empirical improvements in classification performance.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GoEmotions

**Resources**:
- [Resource](https://arxiv.org/abs/2311.03551)

## 🎯 Purpose and Intended Users

**Goal**: To improve the alignment of text-based emotion classification datasets with emotional labels using contextual information generated through LLMs.

**Target Audience**:
- ML Researchers
- Data Scientists
- Model Developers

**Tasks**:
- Emotion Classification

**Limitations**: The method's effectiveness can be undermined when original labels are already well suited for the text without further context.

## 💾 Data

**Source**: GoEmotions dataset and additional external datasets (ISEAR, SemEval 2019 Task 3, Tweet Eval, Daily Dialog)

**Size**: Modified dataset generated includes 1,000 samples from the GoEmotions dataset and various contexts added.

**Format**: N/A

**Annotation**: An initial dataset is annotated using human-provided emotion labels, followed by context generation using LLMs for refinement.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1-macro

**Calculation**: Evaluation is done through zero-shot performance and through human feedback on contextually generated inputs.

**Interpretation**: Higher F1-macro scores and positive human feedback indicate better alignment of text and emotion labels.

**Validation**: Empirical validation of the enhanced datasets is conducted through comparison with baseline datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: The impact of demographic factors on emotion interpretation is considered in the context evaluation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
