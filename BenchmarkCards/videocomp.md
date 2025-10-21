# VideoComp

## 📊 Benchmark Details

**Name**: VideoComp

**Overview**: VideoComp is a benchmark and learning framework for advancing video-text compositionality understanding, focusing on improving vision-language models in fine-grained temporal alignment. It introduces two compositional benchmarks, ActivityNet-Comp and YouCook2-Comp, which assess models’ abilities to capture fine-grained, temporally coherent alignment in continuous multi-event video sequences.

**Data Type**: video-text pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ActivityNet-Captions
- YouCook2

**Resources**:
- [GitHub Repository](https://github.com/google-deepmind/video_comp)

## 🎯 Purpose and Intended Users

**Goal**: To enhance video-text compositionality and improve models' understanding of fine-grained temporal alignment in video sequences.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Video-Text Alignment
- Compositional Learning

**Limitations**: N/A

## 💾 Data

**Source**: ActivityNet-Captions and YouCook2 datasets.

**Size**: Approximately 17,000 annotated triplets for ActivityNet-Comp and 4,500 annotated triplets for YouCook2-Comp.

**Format**: N/A

**Annotation**: Manual annotation based on video-captioning datasets.

## 🔬 Methodology

**Methods**:
- Hierarchical pairwise preference loss
- Contrastive learning

**Metrics**:
- Recall@1
- Binary classification accuracy

**Calculation**: The metrics are calculated based on the video-text alignment and compositional coherence evaluated through provided positive and negative samples.

**Interpretation**: Higher accuracy indicates better compositional understanding and alignment of video and text.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
