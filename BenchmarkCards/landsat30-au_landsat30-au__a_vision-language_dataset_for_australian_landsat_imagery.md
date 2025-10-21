# Landsat30-AU (Landsat30-AU: A Vision-Language Dataset for Australian Landsat Imagery)

## 📊 Benchmark Details

**Name**: Landsat30-AU (Landsat30-AU: A Vision-Language Dataset for Australian Landsat Imagery)

**Overview**: Landsat30-AU is a large-scale vision-language dataset constructed from 30-meter resolution imagery collected by four Landsat satellites (5, 7, 8, and 9) over Australia, spanning more than 36 years. It includes Landsat30-AU-Cap with 196,262 image-caption pairs and Landsat30-AU-VQA with 17,725 human-verified visual question answering samples aimed at enhancing vision-language model performance for remote sensing tasks.

**Data Type**: image-caption pairs, visual question answering pairs

**Domains**:
- Natural Language Processing
- Remote Sensing

**Languages**:
- English

**Similar Benchmarks**:
- EarthDial
- RSICD
- SKYSCRIPT
- GIT-10M
- GAIA

**Resources**:
- [GitHub Repository](https://github.com/papersubmit1/landsat30-au)

## 🎯 Purpose and Intended Users

**Goal**: To provide a vision-language dataset for understanding and interpreting Landsat satellite imagery through detailed captions and question-answering tasks.

**Target Audience**:
- ML Researchers
- Remote Sensing Specialists
- Model Developers

**Tasks**:
- Image Captioning
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Landsat imagery collected by Landsat satellites sourced from Digital Earth Australia Analysis Ready Data archives.

**Size**: 196,262 image-caption pairs, 17,725 VQA samples

**Format**: N/A

**Annotation**: Curated through a bootstrapped pipeline combining model-generated drafts with human verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- SPIDEr
- BLEU-4
- BERTScore-F1
- 1-CHAIR-s
- 1-CHAIR-i
- Accuracy

**Calculation**: Metric calculations are based on comparisons of model outputs against ground truth data including human-verified captions and answers.

**Interpretation**: Higher SPIDEr and BLEU scores indicate better performance in generating captions that accurately reflect image content.

**Baseline Results**: Open-source VLM EarthDial achieved a captioning score of 0.07 SPIDEr.

**Validation**: Validated through human review at multiple stages of data generation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Available under Creative Commons Attribution 4.0 Licence.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
