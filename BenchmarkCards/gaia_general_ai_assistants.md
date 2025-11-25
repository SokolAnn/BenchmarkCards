# GAIA (General AI Assistants)

## 📊 Benchmark Details

**Name**: GAIA (General AI Assistants)

**Overview**: GAIA proposes real-world questions that require fundamental abilities such as reasoning, multi-modality handling, web browsing, and tool-use proficiency. It consists of 466 questions designed to challenge AI systems and provide a leaderboard for evaluation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- GSM8k

**Resources**:
- [Resource](https://huggingface.co/gaia-benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate AI assistants in solving real-world questions requiring complex reasoning and tool use.

**Target Audience**:
- ML Researchers
- AI Developers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Designed and curated questions based on reliable sources such as Wikipedia and other trusted documents.

**Size**: 466 questions

**Format**: JSON

**Annotation**: Questions were annotated by human experts to ensure clarity and correctness.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Evaluation is based on a quasi exacter match between model responses and ground truths.

**Interpretation**: Scores reflect the proportion of correct responses against a unique correct answer.

**Baseline Results**: Human annotators scored approximately 92% accuracy.

**Validation**: Each question was validated by independent annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Privacy**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
