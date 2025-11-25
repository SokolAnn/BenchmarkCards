# SEED-Data-Edit

## 📊 Benchmark Details

**Name**: SEED-Data-Edit

**Overview**: SEED-Data-Edit is a unique hybrid dataset for instruction-guided image editing, integrating high-quality editing data produced by automated pipelines, real-world scenario data capturing user intentions, and high-precision multi-turn editing data annotated by experts.

**Data Type**: image-editing pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- InstructPix2Pix
- MagicBrush
- HQ-Edit

**Resources**:
- [Resource](https://huggingface.co/datasets/AILab-CVC/SEED-Data-Edit)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate image manipulation using open-form language instructions and improve language-guided image editing models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Editing

**Limitations**: N/A

## 💾 Data

**Source**: Automated pipeline-generated data, real-world scenario data from websites, and multi-turn editing data from human annotators.

**Size**: 3,669,644 image editing pairs, 95K multi-turn editing data

**Format**: N/A

**Annotation**: Automated and human annotations

## 🔬 Methodology

**Methods**:
- Fine-tuning of a pre-trained Multimodal Large Language Model (MLLM)
- Evaluation against baseline models

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on the ability of the model to accurately follow editing instructions and improve upon baseline performance.

**Interpretation**: Promising results in adhering to editing instructions effectively.

**Baseline Results**: SEED-X-Edit model compared against MagicBrush, MGIE, and HQ-Edit with improved performance.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
