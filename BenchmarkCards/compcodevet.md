# CompCodeVet

## 📊 Benchmark Details

**Name**: CompCodeVet

**Overview**: CompCodeVet is a compiler-guided approach that enhances the quality of code datasets for training Large Language Models (LLMs) by rectifying non-compilable C and C++ code, improving their training dataset for better performance in code-related tasks.

**Data Type**: code snippets

**Domains**:
- Computer Science

**Languages**:
- C
- C++

**Resources**:
- [Resource](https://arxiv.org/abs/2311.06505)

## 🎯 Purpose and Intended Users

**Goal**: To improve the quality of code datasets used for training LLMs and enhance the model's ability to generate compilable code.

**Target Audience**:
- ML Researchers
- Software Developers

**Tasks**:
- Code Generation
- Code Completion

**Limitations**: N/A

## 💾 Data

**Source**: Datasets used include Stack and HPCorpus, which contain source code from open-source repositories.

**Size**: 6.4 TB

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Fine-tuning of LLMs using a compiler-guided approach
- Error rectification using a chain-of-thought strategy

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated by comparing the model's output against ground truth labels.

**Interpretation**: Higher values in precision, recall, and F1 scores indicate better model performance in code generation and classification tasks.

**Baseline Results**: CompCodeVet's Llama2-7b model achieved an F1 Score of 0.95 in programming language classification.

**Validation**: Models were validated through performance tests against other established LLMs like GPT-4.

## ⚠️ Targeted Risks

**Risk Categories**:
- Quality
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
