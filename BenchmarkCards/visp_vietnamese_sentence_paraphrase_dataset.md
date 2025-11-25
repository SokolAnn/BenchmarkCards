# ViSP (Vietnamese Sentence Paraphrase Dataset)

## 📊 Benchmark Details

**Name**: ViSP (Vietnamese Sentence Paraphrase Dataset)

**Overview**: This paper presents ViSP, a high-quality Vietnamese dataset for sentence paraphrasing, consisting of 1.2M original–paraphrase pairs collected from various domains. The dataset was constructed using a hybrid approach that combines automatic paraphrase generation with manual evaluation to ensure high quality.

**Data Type**: sentence-paraphrase pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Vietnamese

**Resources**:
- [GitHub Repository](https://github.com/ngwgsang/ViSP)

## 🎯 Purpose and Intended Users

**Goal**: To provide a valuable foundation for future research and applications in Vietnamese paraphrase tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Paraphrase Generation

**Limitations**: While our models were fine-tuned on the ViSP dataset, they were trained under low-resource conditions, which means the overall performance may not be fully optimized. Additionally, the current dataset lacks representation from certain specialized domains such as metaphor, mathematics, and programming.

## 💾 Data

**Source**: The dataset is compiled from several publicly available sources, including UIT-ViQuAD, UIT-ViNewsQA, ALQAC, and ViNLI.

**Size**: 1,200,000 pairs

**Format**: JSON

**Annotation**: Manually verified by a team of annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU-4
- ROUGE-2
- BERTScore

**Calculation**: Metrics are calculated to measure the quality of paraphrase generation.

**Interpretation**: Higher scores indicate better paraphrase quality in terms of similarity and fluency.

**Baseline Results**: The best models achieved BLEU-4 scores of 72.06 on the validation set.

**Validation**: A review process involving several annotators to ensure the quality of the paraphrased sentences.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
