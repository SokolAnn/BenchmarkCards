# LLMLingua-2 (Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression)

## 📊 Benchmark Details

**Name**: LLMLingua-2 (Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression)

**Overview**: This paper presents LLMLingua-2, a task-agnostic prompt compression method that utilizes a data distillation approach to derive knowledge from an LLM (GPT-4) for better performance in prompt compression. The method produces an extractive text compression dataset and evaluates the effectiveness of the approach across multiple benchmarks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LLMLingua

**Resources**:
- [Resource](https://aka.ms/LLMLingua-2)

## 🎯 Purpose and Intended Users

**Goal**: To improve generalizability and efficiency in task-agnostic prompt compression for LLMs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering
- Summarization

**Limitations**: The dataset was constructed using only training examples from MeetingBank, raising concerns about its generalization capability.

## 💾 Data

**Source**: Dataset constructed from MeetingBank and compressed using GPT-4.

**Size**: 5,169 examples

**Format**: CSV

**Annotation**: Tokens labeled as to be preserved or discarded based on compression.

## 🔬 Methodology

**Methods**:
- Token Classification
- Data Distillation

**Metrics**:
- Accuracy
- F1 Score
- ROUGE-L

**Calculation**: Metrics calculated from predictions of tokens being preserved or discarded.

**Interpretation**: Higher scores indicate better performance in retaining crucial information during compression.

**Baseline Results**: Compared against existing methods like Selective-Context and LLMLingua, with significant performance gains shown.

**Validation**: Evaluation against in-domain and out-of-domain tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Not analyzed.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
