# StreamBench

## 📊 Benchmark Details

**Name**: StreamBench

**Overview**: StreamBench is a pioneering benchmark designed to evaluate the continuous improvement of LLM agents over input-feedback sequences, simulating an online learning environment where LLMs receive and act on a continuous flow of feedback.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- GSM8K
- BIG-Bench-Hard

**Resources**:
- [GitHub Repository](https://github.com/stream-bench/stream-bench)
- [Resource](https://stream-bench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLM agents' ability to improve themselves over input-feedback sequences in an online setting and develop effective streaming strategies for LLMs.

**Target Audience**:
- ML Researchers
- AI Developers

**Tasks**:
- Text-to-SQL
- Python Programming
- Tool Use
- Medical Diagnosis
- Question Answering

**Limitations**: StreamBench does not encompass all possible types of tasks or domains where LLMs can be applied and is limited to text without other modalities.

## 💾 Data

**Source**: Diverse datasets including Spider, CoSQL, BIRD, DS-1000, ToolBench, DDXPlus, HotpotQA.

**Size**: 1,780 unique instances across various tasks.

**Format**: N/A

**Annotation**: Data is obtained from existing datasets with specific structures for each task.

## 🔬 Methodology

**Methods**:
- Self-StreamICL
- MAM-StreamICL
- GrowPrompt
- MemPrompt

**Metrics**:
- Execution accuracy
- Pass@1
- Exact Match
- F1 Score

**Calculation**: Metrics are calculated based on the defined outputs of LLM agents, comparing generated outputs against expected outputs.

**Interpretation**: Higher accuracy metrics indicate better agent performance in continuous learning setups.

**Baseline Results**: MAM-StreamICL outperformed other methods across all evaluated tasks.

**Validation**: Results validated through average performance comparison across multiple datasets and random seeds.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
