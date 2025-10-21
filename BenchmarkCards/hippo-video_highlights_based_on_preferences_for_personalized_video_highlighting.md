# HIPPO-VIDEO (Highlights Based on Preferences for Personalized Video Highlighting)

## 📊 Benchmark Details

**Name**: HIPPO-VIDEO (Highlights Based on Preferences for Personalized Video Highlighting)

**Overview**: HIPPO-VIDEO is a novel dataset for personalized video highlighting created using an LLM-based user simulator to generate realistic watch histories reflecting diverse user preferences. The dataset includes 2,040 (watch history, saliency score) pairs covering 20,400 videos across 170 semantic categories.

**Data Type**: watch history and saliency score pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- QVHighlights
- SumMe
- TVSum

**Resources**:
- [Resource](https://huggingface.co/datasets/jeongeunnn/HIPPO-video)
- [GitHub Repository](https://github.com/jeongeunnn-e/HIPPO-Video)

## 🎯 Purpose and Intended Users

**Goal**: To introduce personalized video highlighting as a novel task leveraging user watch history to tailor video highlights to individual preferences.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Highlight Detection
- Moment Retrieval
- Video Summarization
- Personalized Video Highlighting

**Limitations**: N/A

## 💾 Data

**Source**: Generated using LLM-based user simulator by simulating user interactions with video platforms.

**Size**: 2,040 (watch history, saliency score) pairs, totaling 20,400 videos.

**Format**: N/A

**Annotation**: Saliency scores were assigned based on long-term user preferences generated during simulation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Average Precision (mAP)
- Hit@1
- Recall@1
- Root Mean Square Error (RMSE)

**Calculation**: Metrics are calculated based on the performance of the HiPHer system against segmented videos according to user preferences.

**Interpretation**: Higher values indicate better alignment of predicted highlights with user preferences.

**Baseline Results**: Various existing methods including SL-Module, Moment-DETR, UMT, QD-DETR, and UVCOM were compared, with HiPHer demonstrating superior performance in capturing user-specific preferences.

**Validation**: The dataset was validated through human assessments of the reliability of simulated watch histories and saliency annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Utilized LLM-based user simulator to generate realistic watch histories without collecting actual user data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
