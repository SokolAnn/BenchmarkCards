# Densely Captioned Images (DCI)

## 📊 Benchmark Details

**Name**: Densely Captioned Images (DCI)

**Overview**: We release the Densely Captioned Images (DCI) dataset, which contains dense and mask-aligned captions, alongside an LLM-summarized version (sDCI) containing captions under 77 tokens for use with current VLMs.

**Data Type**: image-caption pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Visual Genome
- COCO
- Localized Narratives
- ARO
- VL-Checklist

**Resources**:
- [GitHub Repository](https://github.com/facebookresearch/DCI)

## 🎯 Purpose and Intended Users

**Goal**: To collect a dataset of highly aligned text and image pairs primarily for evaluating how well existing models can make use of all of the data.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Subcrop-Caption Matching
- Image-Text Alignment

**Limitations**: N/A

## 💾 Data

**Source**: Images sampled from a random privacy-mitigated subset of SA-1B.

**Size**: 7,805 images

**Format**: N/A

**Annotation**: Manual annotation by crowdworkers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated based on the performance of vision-language models on tasks using DCI.

**Interpretation**: Performance evaluated by how well models perform on subtasks using the dense captions.

**Baseline Results**: N/A

**Validation**: Models validated against existing benchmarks such as VL-Checklist and ARO.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All known instances of people in the dataset have been face-blurred as per the SA-1B release.

**Data Licensing**: CC-BY-NC license.

**Consent Procedures**: Crowdworkers compensated and qualified.

**Compliance With Regulations**: Not Applicable
