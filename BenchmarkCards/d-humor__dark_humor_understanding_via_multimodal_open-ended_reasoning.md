# D-HUMOR: Dark Humor Understanding via Multimodal Open-ended Reasoning

## 📊 Benchmark Details

**Name**: D-HUMOR: Dark Humor Understanding via Multimodal Open-ended Reasoning

**Overview**: We introduce a novel dataset of 4,379 Reddit memes annotated for dark humor, target category (gender, mental health, violence, race, disability, and other), and a three-level intensity rating (mild, moderate, severe).

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Sai-Kartheek-Reddy/D-Humor-Dark-Humor-Understanding-via-Multimodal-Open-ended-Reasoning)

## 🎯 Purpose and Intended Users

**Goal**: To provide a resource for studying dark humor in memes and develop models for accurate detection, target identification, and intensity prediction.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Dark Humor Detection
- Target Identification
- Intensity Prediction

**Limitations**: Skewed toward the Gender/Sex-Related Topics label, reflecting the greater availability of such content online.

## 💾 Data

**Source**: Memes collected from Reddit using the Reddit API, combined with OCR for text extraction.

**Size**: 4,379 memes

**Format**: JSON

**Annotation**: Annotated for dark humor presence, target categories, and intensity levels.

## 🔬 Methodology

**Methods**:
- Multimodal training with reasoning-augmented framework
- Feature extraction from text and images using BERT and ViT
- Tri-stream Cross-Reasoning Network (TCRNet)

**Metrics**:
- Accuracy
- Macro-F1
- Weighted-F1
- Pearson correlation

**Calculation**: Metrics calculated based on classification results of the proposed model and various baselines.

**Interpretation**: Higher accuracy indicates better detection and classification of dark humor, target identification, and intensity prediction.

**Baseline Results**: TCRNet achieved 75.00% accuracy on dark humor detection and 62.72% accuracy on intensity prediction.

**Validation**: Ablation studies confirmed the importance of structured explanations for model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Dataset annotated to identify if humor targets sensitive topics affecting various demographic groups.

**Potential Harm**: ['Potential offense due to dark humor content']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Respect user privacy as per Reddit's policies; no personally identifiable information was collected.

**Data Licensing**: Not Applicable

**Consent Procedures**: Data collection adhered to ethical guidelines.

**Compliance With Regulations**: Not Applicable
