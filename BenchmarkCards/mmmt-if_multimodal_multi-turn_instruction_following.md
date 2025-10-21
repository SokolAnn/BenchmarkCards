# MMMT-IF (Multimodal Multi-Turn Instruction Following)

## 📊 Benchmark Details

**Name**: MMMT-IF (Multimodal Multi-Turn Instruction Following)

**Overview**: MMMT-IF is an evaluation benchmark for instruction following capabilities in multimodal, multi-turn dialogue contexts. It includes image-based Q&A tasks with global instructions across turns, designed to assess how well models retrieve and follow instructions throughout an extended conversation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMDU (Multi-Turn Multi-Image Dialog Understanding)

**Resources**:
- [GitHub Repository](https://github.com/username/repo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the instruction following capabilities of large language models (LLMs) in the context of multimodal, multi-turn conversations.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Instruction Following
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated dataset through image-based dialogues with multiple instructions and turns.

**Size**: 990 turns across 71 chats

**Format**: JSON

**Annotation**: Human annotations for reference answers and ratings on instruction following and accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Programmatic Instruction Following (PIF)
- PIF-N-K

**Calculation**: PIF is calculated as the fraction of given instructions followed in responses using the original input context and model outputs.

**Interpretation**: Higher PIF scores indicate better adherence to instructions across multiple turns.

**Validation**: Based on correlation with human evaluations and automated metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
