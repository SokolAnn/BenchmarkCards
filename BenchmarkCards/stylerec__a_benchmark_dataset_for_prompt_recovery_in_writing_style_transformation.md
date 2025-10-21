# StyleRec: A Benchmark Dataset for Prompt Recovery in Writing Style Transformation

## 📊 Benchmark Details

**Name**: StyleRec: A Benchmark Dataset for Prompt Recovery in Writing Style Transformation

**Overview**: This paper explores a unique prompt recovery task focused on reconstructing prompts for style transfer and rephrasing, introducing a benchmark dataset designed to address this specialized challenge while ensuring quality and comprehensive coverage.

**Data Type**: prompt-recovery pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/promptrecovery501/StyleRec)

## 🎯 Purpose and Intended Users

**Goal**: To introduce a dataset for prompt recovery in writing style transformation, facilitating further research in this domain.

**Target Audience**:
- ML Researchers
- Language Model Developers

**Tasks**:
- Prompt Recovery

**Limitations**: The metrics used may not adequately reflect the performance of the models in all cases.

## 💾 Data

**Source**: YouTube video transcripts covering a variety of topics.

**Size**: 10,193 instances

**Format**: JSON

**Annotation**: Created with LLM assistance, ensuring quality through rigorous construction techniques.

## 🔬 Methodology

**Methods**:
- Direct Inference with LLM
- Fine-Tuning
- Zero-shot Learning

**Metrics**:
- BLEU Score
- F1 Score
- Rouge-L
- Sharpened Cosine Similarity (SCS)

**Calculation**: Metrics are calculated based on comparing the generated outputs to the ground truth using various statistical measures.

**Interpretation**: Metrics indicate the quality of prompt recovery, with higher scores representing better reconstruction of prompts.

**Baseline Results**: Fine-tuned models achieved the best performance across various metrics.

**Validation**: The dataset was validated through cosine similarity measures to ensure accurate prompt recovery.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
