# MMCircuitEval (MultiModal Circuit-focused Evaluation)

## 📊 Benchmark Details

**Name**: MMCircuitEval (MultiModal Circuit-focused Evaluation)

**Overview**: MMCircuitEval is the first multimodal benchmark specifically designed to assess multimodal large language model (MLLM) performance comprehensively across diverse Electrical Design Automation (EDA) tasks, comprising 3614 meticulously curated question-answer pairs spanning digital and analog circuits across critical EDA stages.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing
- Engineering

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/cure-lab/MMCircuitEval)

## 🎯 Purpose and Intended Users

**Goal**: To assess the professional capabilities of multimodal LLMs across all stages of the EDA circuit design workflow through closely-related QA samples.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collected from textbooks, technical question banks, datasheets, and real-world documentation.

**Size**: 3,614 question-answer pairs

**Format**: N/A

**Annotation**: Manually reviewed by EDA engineers and Ph.D. students for accuracy, relevance, and technical depth.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- ROUGE Score
- Embedding cosine similarity
- GPT preference

**Calculation**: Evaluation metrics compare the similarity between the provided solution and the model output.

**Interpretation**: Higher scores indicate better model performance in answering circuit-focused questions.

**Baseline Results**: Various existing MLLMs evaluated against MMCircuitEval benchmark with varying performance levels.

**Validation**: Extensive experiments conducted to evaluate the performance of existing LLMs using the proposed benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
