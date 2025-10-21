# ZNO-Eval

## 📊 Benchmark Details

**Name**: ZNO-Eval

**Overview**: ZNO-Eval is a comprehensive benchmark designed to assess the reasoning capabilities of large language models in the Ukrainian language, based on real exam tasks from Ukraine's standardized educational testing system.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Ukrainian

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- GSM8K (Grade School Math 8K)
- BIG-Bench (Beyond the Imitation Game Benchmark)

**Resources**:
- [GitHub Repository](https://github.com/NLPForUA/ZNO)

## 🎯 Purpose and Intended Users

**Goal**: To establish a robust tool in the form of a benchmark dataset designed to assess the reasoning capabilities of large language models in the Ukrainian language.

**Target Audience**:
- ML Researchers
- Education Researchers
- Model Developers

**Tasks**:
- Reasoning Assessment
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Real exam tasks from Ukraine's External Independent Evaluation and National Multi-subject Test.

**Size**: 2,746 questions in total

**Format**: N/A

**Annotation**: Manually extracted from existing examination documents.

## 🔬 Methodology

**Methods**:
- Model evaluation
- Zero-shot prompting

**Metrics**:
- Accuracy

**Calculation**: Models were evaluated in a zero-shot prompting manner with specific instructions.

**Interpretation**: Performance scores provide insights into reasoning capabilities of different language models.

**Baseline Results**: GPT-4o achieved the highest overall performance.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0 license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
