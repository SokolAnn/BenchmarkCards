# Pick-Double Caption dataset

## 📊 Benchmark Details

**Name**: Pick-Double Caption dataset

**Overview**: The Pick-Double Caption dataset provides distinct captions for preferred and less preferred images to mitigate issues of conflict distribution and irrelevant prompts in image synthesis models.

**Data Type**: image-caption pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Pick-a-Pic v2

**Resources**:
- [GitHub Repository](https://github.com/username/repo)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for optimizing preference alignment in diffusion models with distinct captions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image Generation

**Limitations**: The dataset may contain out-of-distribution captions, which could affect model performance.

## 💾 Data

**Source**: Derived from the Pick-a-Pic v2 dataset, modified to include distinct captions for images.

**Size**: 20,000 instances

**Format**: N/A

**Annotation**: Captions generated using state-of-the-art captioning models.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Pickscore
- HPSv2.1
- CLIPscore
- ImageReward
- GenEval

**Calculation**: Metrics are calculated based on performance evaluations against benchmark datasets.

**Interpretation**: Higher scores indicate better image quality and alignment with human preferences.

**Validation**: The dataset and methods were validated through comparative evaluation with existing models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Hallucination

**Demographic Analysis**: The dataset includes various prompts, but demographic factors of images are not explicitly analyzed.

**Potential Harm**: ['Potential generation of biased content due to training data.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
