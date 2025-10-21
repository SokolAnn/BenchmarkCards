# Behance video transcripts corpus

## 📊 Benchmark Details

**Name**: Behance video transcripts corpus

**Overview**: A novel corpus and method for keyphrase extraction from the transcripts of videos streamed on the Behance platform; includes a data augmentation technique to leverage general-domain keyphrase resources and information-filtering components to handle noisy, informal transcripts.

**Data Type**: text (video transcripts with keyphrase annotations)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- OpenKP

**Resources**:
- [Resource](https://www.behance.net)
- [Resource](https://arxiv.org/abs/2209.04951)

## 🎯 Purpose and Intended Users

**Goal**: To provide annotated data of Behance live-stream video transcripts for keyphrase extraction and to propose methods (data augmentation, domain discriminator, information filtering, reinforcement learning rewards) to improve keyphrase extraction on noisy transcript data.

**Tasks**:
- Keyphrase Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Transcripts of videos streamed on the Behance platform.

**Size**: 361 recordings; more than 500 hours of audio; average transcript contains 7,219 words.

**Format**: N/A

**Annotation**: Manual annotation by 10 annotators recruited via Upwork (5 annotators for section-level labels and 5 annotators for chapter-level labels). Annotators were trained; annotators select paragraph boundaries and keyphrases. Silver labels for domain-specific phrase detection are automatically constructed using a pre-trained domain discriminator.

## 🔬 Methodology

**Methods**:
- Human annotation
- Automated metrics

**Metrics**:
- F1 Score (F1@1, F1@3, F1@5)

**Calculation**: F1 computed on top-k predicted keyphrases where k = 1, 3, 5. Keyphrases are sorted based on the likelihood of their first word (P(B | D, w_i, θ)).

**Interpretation**: Higher F1@k indicates better keyphrase extraction performance. Authors compare F1@1, F1@3, and F1@5 against baselines to demonstrate improvements.

**Baseline Results**: JointKPE (BERT): F1@1 14.44, F1@3 18.91, F1@5 24.19; JointKPE (RoBERTa): F1@1 16.00, F1@3 22.07, F1@5 25.08; JointKPE (SpanBERT): F1@1 16.08, F1@3 24.96, F1@5 27.63; Ours: F1@1 28.50, F1@3 36.43, F1@5 33.83.

**Validation**: Development set used to select thresholds (e.g., k for attention pruning and trade-off parameters). The pre-trained domain discriminator achieves 93% accuracy on the test set of the combined domain dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
