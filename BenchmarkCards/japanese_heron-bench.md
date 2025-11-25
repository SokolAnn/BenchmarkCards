# Japanese Heron-Bench

## 📊 Benchmark Details

**Name**: Japanese Heron-Bench

**Overview**: Japanese Heron-Bench is introduced to evaluate the Japanese capabilities of Vision Language Models (VLMs). It consists of a variety of image-question-answer pairs tailored to the Japanese context, helping to reveal the strengths and limitations of VLMs.

**Data Type**: image-question-answer pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Japanese

**Similar Benchmarks**:
- JA-VG-VQA-500
- JA-VLM-Bench-In-the-Wild

**Resources**:
- [GitHub Repository](https://github.com/turingmotors/heron)
- [Resource](https://huggingface.co/turing-motors)

## 🎯 Purpose and Intended Users

**Goal**: To create a benchmark that allows for assessing the performance of Vision Language Models in understanding Japanese visual and linguistic contexts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering
- Image Captioning

**Limitations**: The benchmark's effectiveness is still dependent on the scoring quality provided by external models like GPT-4, which may have limitations in performance with Japanese compared to English.

## 💾 Data

**Source**: A collection of public domain and CC BY 2.0 licensed images relevant to Japanese contexts.

**Size**: 102 questions

**Format**: N/A

**Annotation**: Manually annotated with context provided to a language model to generate expected answers.

## 🔬 Methodology

**Methods**:
- Evaluation against baseline GPT-4 generated answers

**Metrics**:
- Scoring out of 10 for quality of answers
- Accuracy of visual question answering

**Calculation**: Average score of VLM answers compared to GPT-4 answers, normalized to scale out of 10.

**Interpretation**: Higher scores indicate better understanding and response generation in Japanese visual contexts.

**Baseline Results**: Heron GIT serves as a baseline and shows competitive performance compared to other Japanese VLMs.

**Validation**: The evaluation dataset was constructed using established frameworks akin to LLaVA-Bench methodologies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: Analysis of performance across different questions and visuals relevant to various Japanese cultural contexts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data is collected from public domain or CC BY 2.0 licensed sources.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
