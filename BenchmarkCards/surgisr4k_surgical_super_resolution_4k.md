# SurgiSR4K (Surgical Super Resolution 4K)

## 📊 Benchmark Details

**Name**: SurgiSR4K (Surgical Super Resolution 4K)

**Overview**: SurgiSR4K is the first publicly available surgical imaging and video dataset captured at a native 4K resolution, representing realistic conditions of robotic-assisted minimally invasive procedures. It comprises diverse visual scenarios and is designed to support tasks including super resolution (SR), surgical instrument detection, 3D tissue reconstruction, and more.

**Data Type**: image/video

**Domains**:
- Healthcare

**Languages**:
- N/A

**Similar Benchmarks**:
- EndoVis 2018
- HyperKvasir

**Resources**:
- [Resource](https://synapse.org/syn68756003)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of SurgiSR4K is to provide a high-resolution dataset for surgical imaging research, enabling the development of intelligent imaging technologies aimed at enhancing performance, safety, and usability in image-guided robotic surgeries.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Robotic Surgery Developers

**Tasks**:
- Super Resolution
- Surgical Instrument Detection
- 3D Tissue Reconstruction
- Instance Segmentation
- Monocular Depth Estimation

**Limitations**: The dataset's collection involved open surgical techniques which may limit the scope of traditional laparoscopic methods.

## 💾 Data

**Source**: Captured during in vivo surgeries on porcine models under realistic surgical conditions using a Da Vinci Xi surgical robot system.

**Size**: 800 images, 50 videos

**Format**: PNG for images, AVI for videos

**Annotation**: Clinical validation was performed by experienced medical professionals to ensure relevance and clarity.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- PSNR (Peak Signal-to-Noise Ratio)
- Mean Structural Similarity Index (MSSIM)

**Calculation**: Metrics are calculated based on pixel alignment and perceptual quality assessment against ground truth data.

**Interpretation**: Higher PSNR and MSSIM values indicate better performance and fidelity of generated images compared to real images.

**Baseline Results**: N/A

**Validation**: Dataset validation involved reviews by clinical experts to ensure accuracy and usability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Safety
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data was collected from animal models under strict ethical guidelines and approval from IACUC.

**Data Licensing**: Released under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license.

**Consent Procedures**: N/A - No human subjects were involved.

**Compliance With Regulations**: All procedures were conducted in accordance with the institution’s ethical standards.
