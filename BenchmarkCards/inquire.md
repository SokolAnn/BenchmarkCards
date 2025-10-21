# INQUIRE

## 📊 Benchmark Details

**Name**: INQUIRE

**Overview**: INQUIRE is a text-to-image retrieval benchmark designed to challenge multimodal vision-language models on expert-level queries, consisting of 250 expert-level retrieval queries paired with images labeled within the iNaturalist 2024 dataset (iNat24), which includes five million natural world images.

**Data Type**: text-image pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Flickr30k
- COCO

**Resources**:
- [Resource](https://inquire-benchmark.github.io/)
- [GitHub Repository](https://github.com/inquire-benchmark/INQUIRE)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate image retrieval capabilities of multimodal models using expert-level scientific queries regarding the natural world.

**Target Audience**:
- ML Researchers
- Ecologists
- Biodiversity Researchers

**Tasks**:
- Image Retrieval
- Reranking

**Limitations**: N/A

## 💾 Data

**Source**: iNaturalist data

**Size**: 5,000,000 images

**Format**: JSON, CSV

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Retrieval evaluation
- Reranking evaluation

**Metrics**:
- Mean Average Precision (mAP)
- Normalized Discounted Cumulative Gain (nDCG)
- Mean Reciprocal Rank (MRR)

**Calculation**: Mean Average Precision is computed by taking the weighted mean of precision scores at k thresholds.

**Interpretation**: Higher values of mAP, nDCG, and MRR indicate better retrieval performance of the models.

**Baseline Results**: Baseline results show that the best models have mAP@50 scores less than 50% on INQUIRE.

**Validation**: The benchmark was validated on expert-level queries across a large dataset of natural world images.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: ['Potentially biased scientific assessments if results from AI models are used falsely.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All images were filtered to remove personally identifiable information.

**Data Licensing**: The dataset includes images licensed under various Creative Commons licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
