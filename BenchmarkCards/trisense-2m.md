# TriSense-2M

## 📊 Benchmark Details

**Name**: TriSense-2M

**Overview**: TriSense-2M is a large-scale multimodal dataset containing over 2 million annotations designed to support video temporal understanding tasks through the integration of visual, audio, and speech modalities, facilitating robust multimodal learning.

**Data Type**: video and audio samples with event-based annotations

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- DiDeMo
- Charades-STA
- ActivityNet Captions
- VALOR

**Resources**:
- [GitHub Repository](https://github.com/zinuoli/TriSense)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for multimodal video understanding, enabling models to effectively integrate visual, audio, and speech information for tasks like moment retrieval and segment captioning.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Moment Retrieval
- Segment Captioning

**Limitations**: N/A

## 💾 Data

**Source**: Curated from long-form videos, enriched with annotated events across various modalities using an automated pipeline.

**Size**: 2 million annotations from approximately 38,000 long videos

**Format**: N/A

**Annotation**: Automated annotation using fine-tuned large language models with manual quality checks

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- BLEU Score
- ROUGE-L
- CIDEr
- Recall@IoU

**Calculation**: Metrics are calculated based on generated captions and retrieved moments against ground truth annotations for segment captioning and moment retrieval tasks.

**Interpretation**: Higher scores indicate a better alignment of the generated content with human-generated captions or the ability to correctly retrieve moments based on textual queries.

**Baseline Results**: TriSense significantly outperforms other models like LongVALE and Qwen2.5-Omni on both TriSense-2M and existing benchmarks.

**Validation**: Extensive experimental evaluations across multiple benchmarks and tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
