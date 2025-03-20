# REVERIE

## 📊 Benchmark Details

**Name**: REVERIE

**Overview**: REVERIE is the first large-scale visual instruction tuning dataset with reflective rationale annotations, encompassing 115k machine-generated reasoning instructions. Each instruction is paired with correct and confusing responses alongside comprehensive rationales elucidating the justification behind their correctness or erroneousness.

**Data Type**: Visual Instruction Tuning Dataset

**Domains**:
- Vision-Language Tasks

**Languages**:
- English

**Similar Benchmarks**:
- LLaVA-Instruct-158k
- ScienceQA
- A-OK-VQA

**Resources**:
- [Resource](Project page: https://zjr2000.github.io/projects/reverie)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the reasoning capabilities of large vision-language models and mitigate hallucinations through reflective instruction tuning.

**Target Audience**:
- Researchers
- Data Scientists
- AI Developers

**Tasks**:
- Visual Instruction Tuning
- Reasoning Tasks in AI
- Mitigating Hallucinations in AI Models

**Limitations**: Focused on visual instruction tuning tasks; other AI model training tasks are outside scope.

**Out of Scope Uses**:
- General AI applications outside visual instruction tasks

## 💾 Data

**Source**: Visual Genome, COCO, ScienceQA, A-OK-VQA

**Size**: 254,177 training instances

**Format**: Instruction-Response-Rationale tuples

**Annotation**: Contains both positive and negative rationales for responses.

## 🔬 Methodology

**Methods**:
- Reflective Instruction Tuning
- Multi-turn Conversation format for rationale generation

**Metrics**:
- Accuracy
- Precision
- F1 Score

**Calculation**: Performance improvement measured against baseline models across multiple benchmarks.

**Interpretation**: Interprets the effectiveness of rationale inclusion in training models.

**Baseline Results**: Substantial performance gains observed over baseline models in all evaluated benchmarks.

**Validation**: Validated through experiments on six different evaluation benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data bias
- Output bias
- Privacy concerns

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Exposing personal information

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is anonymized where applicable.

**Data Licensing**: Dataset details regarding licensing are not specified.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The dataset complies with standard research regulations.
