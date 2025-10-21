# WILDVISION -BENCH

## 📊 Benchmark Details

**Name**: WILDVISION -BENCH

**Overview**: WILDVISION -BENCH is a challenging and natural benchmark for evaluating vision-language models (VLMs) that reflects real-world human use cases, closely aligned with user preferences collected from WILDVISION -ARENA.

**Data Type**: multimodal chat interactions

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMVet
- MMMU
- MMStar

**Resources**:
- [Resource](https://huggingface.co/spaces/WildVision/vision-arena)
- [Resource](https://huggingface.co/datasets/WildVision/wildvision-arena-data)
- [Resource](https://huggingface.co/WildVision)
- [GitHub Repository](https://github.com/WildVision-AI)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate vision-language models in accordance with real-world human preferences and provide a benchmark that reflects actual usage scenarios.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Visual Question Answering
- Human Preference Ranking

**Limitations**: N/A

## 💾 Data

**Source**: WILDVISION -ARENA user submissions

**Size**: 500 samples

**Format**: N/A

**Annotation**: Manually annotated by experts

## 🔬 Methodology

**Methods**:
- User voting
- Crowdsourced interaction evaluations

**Metrics**:
- Spearman correlation

**Calculation**: Statistical analysis correlating model scores with user preferences.

**Interpretation**: Higher scores indicate better alignment with human preferences.

**Baseline Results**: GPT-4o outperforms other models with high Elo ratings.

**Validation**: User feedback and pairwise voting results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User data is logged for research purposes with appropriate consent.

**Data Licensing**: Not Applicable

**Consent Procedures**: User agreements obtained during interaction.

**Compliance With Regulations**: Not Applicable
