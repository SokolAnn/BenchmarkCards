# PG-CE (Progressive Generation Dataset with Constraint Enhancement)

## 📊 Benchmark Details

**Name**: PG-CE (Progressive Generation Dataset with Constraint Enhancement)

**Overview**: This paper proposes the PG-CE approach, designed for Controllable Text Generation (CTG), which decomposes CTG tasks into three steps: type prediction, constraint construction, and guided generation. The paper presents a dataset containing 90,000 constraint-text pairs tailored to real-world applications.

**Data Type**: constraint-text pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To enhance controllability and practicality in text generation tasks through a structured approach using constraints.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Controllable Text Generation
- Text Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from various publicly available datasets including Alpaca-GPT4, ShareGPT, ChatCounselor, MedDialog, DISC-Law-SFT, and others.

**Size**: 90,000 constraint-text pairs

**Format**: N/A

**Annotation**: Data was screened for quality, removing duplicates and ensuring relevancy and clarity.

## 🔬 Methodology

**Methods**:
- Fine-tuning on LLaMA3-8B and GPT-2
- Multi-head attention
- Hierarchical design strategy for constraint generation

**Metrics**:
- Toxicity Probability
- Perplexity

**Calculation**: Metrics calculated based on the effectiveness of control strategies and overall generation output.

**Interpretation**: Lower toxicity scores indicate better performance in generating safe and relevant content.

**Validation**: Validated through experimental setups using toxic prompts and various comparison benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
