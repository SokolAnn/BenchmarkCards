# Taskmaster-1

## 📊 Benchmark Details

**Name**: Taskmaster-1

**Overview**: Introduces the Taskmaster-1 dataset: 13,215 task-based dialogs across six domains, collected via two procedures (two-person Wizard of Oz spoken dialogs and self-dialog written dialogs). Dialogs are labeled with API calls and arguments (API-oriented annotation). The dataset aims to provide realistic and diverse goal-oriented conversational data and includes baseline model evaluations and human judgments.

**Data Type**: text (dialog transcripts, API call & argument annotations); audio (spoken recordings)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MultiWOZ

**Resources**:
- [Resource](https://g.co/dataset/taskmaster-1)
- [GitHub Repository](https://github.com/pytorch/fairseq)
- [Resource](https://arxiv.org/abs/1909.05358)

## 🎯 Purpose and Intended Users

**Goal**: Provide a high-quality, diverse corpus of goal-oriented conversational data to support data-driven dialog system research, development and design.

**Target Audience**:
- Dialog system researchers
- Machine learning researchers
- Model developers

**Tasks**:
- Response Generation
- Argument Prediction

**Limitations**: Self-dialogs cannot fully recreate disfluencies and other complex error patterns seen in two-person spoken dialogs; two-person (WOz) collection is time-consuming, complex and expensive compared to self-dialog collection.

## 💾 Data

**Source**: Collected via two methods: two-person Wizard of Oz (WOz) spoken dialogs pairing trained agents (assistant role) with crowdsourced workers (user role), and self-dialogs where crowdsourced workers wrote entire dialogs. Covers six domains: ordering pizza, creating auto repair appointments, setting up ride service, ordering movie tickets, ordering coffee drinks, making restaurant reservations.

**Size**: 13,215 dialogs (5,507 spoken dialogs, 7,708 written dialogs)

**Format**: N/A

**Annotation**: Dialogs annotated with API calls and API arguments (arguments annotated as spans in utterances) and transaction status markers ('.accept' or '.reject'); complete list of labels included with corpus release.

## 🔬 Methodology

**Methods**:
- Automated evaluation metrics (Perplexity, BLEU Score)
- Human evaluation (ranking and 1-5 Likert ratings)

**Metrics**:
- Perplexity
- BLEU Score
- Micro F1
- Likert-scale human ratings
- Human ranking

**Calculation**: Perplexity and BLEU computed on model outputs evaluated on test sets. Human evaluation: ranking and 1-5 Likert ratings performed on 500 partial dialogs with 3 crowdsourced workers per item (averaged). Micro F1 computed for API argument prediction (arguments annotated as spans).

**Interpretation**: Lower Perplexity and higher BLEU indicate better response generation performance. BLEU correlates with human ranking judgments. Higher human Likert ratings indicate better perceived appropriateness (1-5 scale, higher is better).

**Baseline Results**: Response generation baselines (self-dialog corpus): Transformer PPL 18.19, BLEU 6.11, human rating (Likert) 3.22, rank 1; LSTM-attention PPL 20.05, BLEU 5.12, human rating 3.51, rank 2; Convolution PPL 21.25, BLEU 5.09, human rating 2.89, rank 3. API argument prediction: Transformer Micro F1 48.73%; Transformer + copy Micro F1 51.79%.

**Validation**: Dataset validated via quantitative comparisons with MultiWOZ (vocabulary, utterance statistics, perplexity/BLEU) and via human evaluations (500 dialogs × 3 annotations). Reported inter-annotator reliability (Krippendorff's Alpha): Rating 0.21, Ranking 0.29.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
