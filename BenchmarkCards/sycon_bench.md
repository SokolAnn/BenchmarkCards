# SYCON BENCH

## 📊 Benchmark Details

**Name**: SYCON BENCH

**Overview**: SYCON BENCH is a novel benchmark for evaluating sycophantic behavior in multi-turn, free-form conversational settings. It quantifies how quickly a model conforms to the user and how often it shifts its stance under sustained user pressure.

**Data Type**: multi-turn prompts

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/JiseungHong/SYCON-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and quantify sycophancy in real-world settings involving multi-turn, free-form interactions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multi-turn Conversation Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: User queries curated from debate, unethical stereotypes, and false presupposition scenarios.

**Size**: 500 prompts

**Format**: N/A

**Annotation**: Annotated through evaluation by models, specifically using GPT-4o.

## 🔬 Methodology

**Methods**:
- LLM-based evaluation
- Human evaluation

**Metrics**:
- Turn of Flip (ToF)
- Number of Flip (NoF)

**Calculation**: ToF measures the earliest turn where model response diverges from the expected stance. NoF counts the number of stance reversals throughout the conversation.

**Interpretation**: A lower NoF indicates better consistency and resistance to sycophantic behavior, while higher ToF indicates better support for the initial stance.

**Baseline Results**: N/A

**Validation**: Evaluated against both LLM and human-generated annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
