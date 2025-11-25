# MIBench

## 📊 Benchmark Details

**Name**: MIBench

**Overview**: MIBench is designed to comprehensively evaluate fine-grained abilities of multimodal large language models (MLLMs) in multi-image scenarios across three scenarios: multi-image instruction, multimodal knowledge-seeking, and multimodal in-context learning, with a total of 13 tasks and 13,000 annotated samples.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MME
- MMBench
- SEED-Bench
- Sparkles-Eval
- Mantis-Eval

**Resources**:
- [Resource](https://huggingface.co/datasets/StarBottle/MIBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for assessing the multi-image abilities of MLLMs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multi-Image Instruction
- Multimodal Knowledge-Seeking
- Multimodal In-Context Learning

**Limitations**: Due to the input length limitation of current MLLMs, the benchmark includes 2 to 8 input images in each sample.

## 💾 Data

**Source**: Data constructed from various existing annotated datasets, including NLVR2, MagicBrush, VrR-VG, Something-Something V2, and others.

**Size**: 13,000 samples

**Format**: N/A

**Annotation**: Manual annotation and automated filtering, supplemented with GPT-4 generated distractors.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the predicted options from models against the correct options.

**Interpretation**: A model is considered to have correctly answered a sample only if it consistently provides the correct response across multiple tests.

**Validation**: Data quality ensured through automated filtering and manual verification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
