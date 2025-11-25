# Image2Struct

## 📊 Benchmark Details

**Name**: Image2Struct

**Overview**: Image2Struct is a benchmark to evaluate vision-language models (VLMs) on extracting structure from images, such as webpages, LaTeX, and music sheets. It uses a round-trip evaluation process comparing the rendered structure against the input image to provide a similarity score.

**Data Type**: image and structure pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/stanford-crfm/image2struct-webpage-v1)
- [Resource](https://huggingface.co/datasets/stanford-crfm/image2struct-latex-v1)
- [Resource](https://huggingface.co/datasets/stanford-crfm/image2struct-musicsheet-v1)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of vision-language models in generating structured data (e.g., code) from images.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Structure Extraction
- Image-to-Code Translation

**Limitations**: The benchmark focuses on structure extraction and does not evaluate abstract reasoning.

## 💾 Data

**Source**: Data was collected from GitHub, arXiv, and IMSLP.

**Size**: 2400 instances total (900 webpages, 1200 LaTeX, 300 music scores)

**Format**: PNG images and associated structures.

**Annotation**: No manual annotation; uses automated metrics for evaluation.

## 🔬 Methodology

**Methods**:
- Round-trip evaluation
- Automated metrics

**Metrics**:
- Earth Mover Similarity
- Cosine Similarity
- Pixel Similarity

**Calculation**: Metrics are calculated based on the similarity between the rendered image and the original input image.

**Interpretation**: Scores range from 0 (no similarity) to 1 (identical images).

**Validation**: Data was filtered for relevance and diversity, and various automated metrics were employed to evaluate model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**

**Demographic Analysis**: N/A

**Potential Harm**: Potential negative impact on jobs due to automation in data extraction tasks.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: We apply automated filters to remove any potentially offensive content.

**Data Licensing**: The data is collected under Fair Use doctrine for non-commercial research purposes.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
