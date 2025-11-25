# SciPostLayout

## 📊 Benchmark Details

**Name**: SciPostLayout

**Overview**: SciPostLayout is the first scientific poster layout dataset for layout analysis and generation, containing 7,855 scientific posters with manual layout annotations and 100 scientific papers paired with the posters.

**Data Type**: image-layout pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/omron-sinicx/scipostlayout_v2)
- [GitHub Repository](https://github.com/omron-sinicx/scipostlayout)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for evaluating layout analysis and generation systems in the context of scientific posters.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Layout Analysis
- Layout Generation

**Limitations**: N/A

## 💾 Data

**Source**: Poster images downloaded from F1000Research and manually annotated by professional annotators.

**Size**: 7,855 posters

**Format**: PNG

**Annotation**: Manually annotated with categories of layout elements.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- mean Average Precision (mAP)
- maximum IoU (mIoU)
- Alignment
- Overlap
- Fréchet Inception Distance (FID)

**Calculation**: Metrics were calculated as described in the methodology section of the paper.

**Interpretation**: Higher mAP and mIoU indicate better performance for layout analysis; lower values of FID indicate better similarity in layout generation.

**Validation**: Evaluated using existing models on the defined tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
