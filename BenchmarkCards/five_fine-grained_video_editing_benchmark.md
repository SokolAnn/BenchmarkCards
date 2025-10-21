# FiVE (Fine-grained Video Editing Benchmark)

## 📊 Benchmark Details

**Name**: FiVE (Fine-grained Video Editing Benchmark)

**Overview**: FiVE is a comprehensive benchmark designed to evaluate emerging diffusion and rectified flow models for fine-grained video editing, featuring 74 real-world videos, 26 generated videos, 6 fine-grained editing types, and 420 object-level editing prompt pairs with corresponding masks.

**Data Type**: video

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- TGVE
- TGVE+

**Resources**:
- [Resource](https://sites.google.com/view/five-benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To advance the field of fine-grained video editing by providing a standardized benchmark and metrics for evaluating video editing models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Fine-grained video editing

**Limitations**: N/A

## 💾 Data

**Source**: 74 real-world videos curated from the DA VIS dataset and 26 generated videos with 420 editing prompt pairs.

**Size**: 74 real-world videos and 26 generated videos

**Format**: video files

**Annotation**: Manual annotation with the aid of GPT-4o to generate captions and object masks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- VLM-based evaluation

**Metrics**:
- FiVE-YN (Yes/No Accuracy)
- FiVE-MC (Multi-choice Accuracy)
- FiVE-∪ (Union Accuracy)
- FiVE-∩ (Intersection Accuracy)
- CLIP Score
- PSNR
- SSIM

**Calculation**: Metrics are calculated based on the evaluation of object-level editing success using generated prompts and VLMs.

**Interpretation**: Higher scores indicate successful fine-grained video editing, with specific metrics assessing various aspects such as background preservation and text-video similarity.

**Baseline Results**: Wan-Edit and DMT achieved the highest FiVE-Acc scores among methods tested.

**Validation**: The benchmark was validated through comparisons with baseline models and human evaluations to ensure quality and reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
