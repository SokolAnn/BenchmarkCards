# EMScore (Embedding Matching-based score)

## 📊 Benchmark Details

**Name**: EMScore (Embedding Matching-based score)

**Overview**: EMScore is a novel reference-free metric for video captioning, which directly measures similarity between video and candidate captions. It combines matching scores of both coarse-grained (video and caption) and fine-grained (frames and words) levels.

**Data Type**: text

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/shiyaya/emscore)

## 🎯 Purpose and Intended Users

**Goal**: To develop a reference-free metric for evaluating video captions that better aligns with human judgment.

**Target Audience**:
- ML Researchers
- Video Captioning Practitioners

**Tasks**:
- Video Captioning

**Limitations**: N/A

## 💾 Data

**Source**: Datasets collected include VATEX-EVAL and ActivityNet-FOIL.

**Size**: 54,000 human ratings

**Format**: N/A

**Annotation**: Human ratings by annotators on a scale of 1 to 5.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Human correlation
- Kendall's tau
- Spearman's rank correlation

**Calculation**: EMScore is calculated as the average of coarse-grained and fine-grained embedding matches.

**Interpretation**: Higher EMScore indicates a better quality caption, reflecting its consistency with the video.

**Baseline Results**: EMScore shows higher human correlation than existing metrics like BLEU, ROUGE, and CIDEr.

**Validation**: V ATEX-EVAL and ActivityNet-FOIL datasets were used for validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
