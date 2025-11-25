# Cross-platform Short-Video (XS-Video)

## 📊 Benchmark Details

**Name**: Cross-platform Short-Video (XS-Video)

**Overview**: We propose the Cross-platform Short-Video (XS-Video) dataset with 381,926 samples from 5 biggest Chinese platforms, including short-video content, post information, interactive information, comment content, and elaborately annotated propagation levels, for short-video propagation analysis.

**Data Type**: text

**Domains**:
- Computer Vision

**Languages**:
- Chinese

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The goal is to promote the research of Short-video Propagation Influence Rating (SPIR) from both the data and model perspectives.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Prediction
- Influence Rating

**Limitations**: N/A

## 💾 Data

**Source**: Collected from the 5 biggest Chinese platforms (Douyin, Kuaishou, Xigua, Toutiao, Bilibili).

**Size**: 117,720 videos, 381,926 samples

**Format**: N/A

**Annotation**: Annotated with the propagation influence from level 0 to 9, based on multi-dimensional interactive indicators.

## 🔬 Methodology

**Methods**:
- Graph Neural Networks (GNNs)
- Large Language Models (LLMs)

**Metrics**:
- Accuracy
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)

**Calculation**: Metrics calculated from predicted results and ground truth based on classification and regression tasks.

**Interpretation**: Higher Accuracy indicates better prediction; lower MSE and MAE indicate better regression performance.

**Baseline Results**: Compared to the best small GNN (RGCN), our NetGPT model performs best with improved accuracy and reduced error rates.

**Validation**: Comprehensive experimental results evaluated by both classification and regression metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User names replaced with anonymous IDs to avoid privacy issues.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
