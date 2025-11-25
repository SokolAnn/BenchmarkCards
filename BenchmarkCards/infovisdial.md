# InfoVisDial

## 📊 Benchmark Details

**Name**: InfoVisDial

**Overview**: InfoVisDial is a visual dialogue dataset that provides rich informative answers for each round, enabling long free-form responses while requiring external knowledge related to visual content.

**Data Type**: dialogue with scene text and external knowledge

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- VisDial

**Resources**:
- [Resource](https://arxiv.org/abs/2312.13503)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for informative visual dialogue tasks that require understanding of scene text and external knowledge.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Dialogue

**Limitations**: N/A

## 💾 Data

**Source**: Images from the TextVQA dataset with generated dialogues using a combination of GPT-3 and human annotators for quality filtering and fact-checking.

**Size**: 69,335 dialogues

**Format**: N/A

**Annotation**: Automatically generated dialogues with human filtering for quality.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- CIDEr
- B1
- B2
- B3
- B4
- METEOR
- ROUGE-L
- SPICE

**Calculation**: Metrics calculated based on generated dialogue responses compared to ground truth answers.

**Interpretation**: Higher scores indicate better performance in generating informative dialogues.

**Baseline Results**: Fine-tuned GIT model results showed significant improvements compared to GPT-3 alone.

**Validation**: Model evaluated through user studies and comparison with existing metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Exposing personal information
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
