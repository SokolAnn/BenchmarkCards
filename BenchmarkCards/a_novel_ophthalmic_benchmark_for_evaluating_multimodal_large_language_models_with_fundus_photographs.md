# A NOVEL OPHTHALMIC BENCHMARK FOR EVALUATING MULTIMODAL LARGE LANGUAGE MODELS WITH FUNDUS PHOTOGRAPHS AND OCT IMAGES

## 📊 Benchmark Details

**Name**: A NOVEL OPHTHALMIC BENCHMARK FOR EVALUATING MULTIMODAL LARGE LANGUAGE MODELS WITH FUNDUS PHOTOGRAPHS AND OCT IMAGES

**Overview**: This benchmark introduces a novel multimodal dataset focused on ophthalmology, utilizing fundus photographs and optical coherence tomography (OCT) images to evaluate the diagnostic performance of multimodal large language models (MLLMs). The benchmark addresses limitations in existing MLLM benchmarks, which often do not capture real-world complexities, by providing a dataset curated through rigorous quality control and expert annotation.

**Data Type**: fundus photographs and OCT images

**Domains**:
- Healthcare

**Languages**:
- N/A

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://medbench.opencompass.org.cn/track)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively evaluate the diagnostic performance of multimodal large language models in interpreting fundus photographs and OCT images for ophthalmic disease diagnosis.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Fundus Photograph Diagnosis
- Optical Coherence Tomography Diagnosis

**Limitations**: N/A

## 💾 Data

**Source**: Fundus photographic images from the Multimodal Retinal Dataset (MuReD) and OCT images from Dataset C8 of the Retinal OCT Image Classification database.

**Size**: 439 fundus images and 75 OCT images

**Format**: N/A

**Annotation**: Curation through rigorous quality control and expert annotation involving a panel of ophthalmologists.

## 🔬 Methodology

**Methods**:
- API-based evaluation of MLLMs

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the proportion of correctly classified instances relative to the total test dataset.

**Interpretation**: Higher accuracy indicates better diagnostic performance in identifying various eye conditions from fundus photographs and OCT images.

**Baseline Results**: N/A

**Validation**: The benchmark was validated using performance assessments of various recognized MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
