# DABench

## 📊 Benchmark Details

**Name**: DABench

**Overview**: DABench is a comprehensive dataset encompassing an extensive range of T2I APIs from the community, specifically designed for text-to-image generation API calling.

**Data Type**: Instruction-API pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/OpenGVLab/DiffAgent)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large instruction-following dataset for text-to-image API calling that enhances the alignment of T2I API outputs with user prompts.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Text-to-Image Generation

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from the Civitai community, a platform for T2I innovation.

**Size**: 50,482 pieces of instruction data

**Format**: JSON

**Annotation**: Data was filtered and reconstructed to ensure high quality and relevancy.

## 🔬 Methodology

**Methods**:
- Evaluation metrics
- Supervised fine-tuning
- Human preference-based reinforcement learning

**Metrics**:
- Unified Metric
- CLIP Score
- ImageReward
- Human Preference Score v2

**Calculation**: Metrics are calculated using various scoring models that evaluate the correlation between user prompts and generated images.

**Interpretation**: Higher scores indicate better alignment with human preferences and relevancy to the prompts.

**Baseline Results**: DiffAgent significantly outperformed baseline models in multiple settings, achieving improvements up to 40%.

**Validation**: Performance evaluated through comprehensive experiments on various datasets and user studies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
