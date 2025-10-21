# SIFo (Sequential Instruction Following) Benchmark

## 📊 Benchmark Details

**Name**: SIFo (Sequential Instruction Following) Benchmark

**Overview**: The SIFo benchmark evaluates the ability of large language models (LLMs) to follow a sequence of instructions effectively by using four tasks: text modification, question answering, mathematics, and security rules. Each task assesses different aspects of instruction following in a coherent manner.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/shin-ee-chen/SIFo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the sequential instruction following ability of LLMs in a fair manner that addresses challenges such as coherence, positional bias, and verifiability of tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Modification
- Question Answering
- Mathematics
- Security Rules

**Limitations**: The SIFo benchmark currently comprises only four tasks designed to assess sequential instruction following in LLMs.

## 💾 Data

**Source**: Constructed using a mixture of datasets including SQuAD and GPT-4 prompts.

**Size**: 800 samples (200 samples for each task)

**Format**: JSON

**Annotation**: Quality checked by human reviewers to verify the correctness and diversity of instructions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Sample-level accuracy
- Instruction-level accuracy
- Instruction following depth
- Step-level accuracy

**Calculation**: Metrics calculated based on the percentage of correctly followed instructions and the depth of sequential instructions successfully completed.

**Interpretation**: Higher scores indicate better performance in following the sequence of instructions.

**Validation**: Cross-verified by experts in LLM evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
