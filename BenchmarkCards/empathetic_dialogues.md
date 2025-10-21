# EMPATHETIC DIALOGUES

## 📊 Benchmark Details

**Name**: EMPATHETIC DIALOGUES

**Overview**: We introduce a new task for dialogue systems to respond to people discussing situations that cover a wide range of emotions, and EMPATHETIC DIALOGUES (ED), a novel dataset with about 25k personal dialogues grounded in emotional situations, intended as a benchmark for empathetic dialogue generation.

**Data Type**: text (one-on-one conversational dialogues)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- DailyDialog
- SEMEVAL 2019 EmoContext challenge
- ConvAI2 (second conversational intelligence challenge) 

**Resources**:
- [Resource](https://parl.ai/)
- [GitHub Repository](https://github.com/facebookresearch/EmpatheticDialogues)
- [Resource](https://arxiv.org/abs/1811.00207)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate evaluating models' ability to produce empathetic responses and to provide a training resource to improve empathetic response generation.

**Target Audience**:
- Researchers
- Practitioners
- Model Developers

**Tasks**:
- Dialogue Generation
- Response Generation
- Emotion Classification

**Limitations**: Some emotion labels are very closely related and researchers could merge similar emotions to obtain coarser labels.

## 💾 Data

**Source**: Crowdsourced one-on-one conversations collected via the ParlAI platform interacting with Amazon Mechanical Turk; 810 US workers; each conversation grounded in a speaker-written situation associated with an emotion label (32 emotion labels).

**Size**: 24,850 conversations (train/validation/test split: 19,533 / 2,770 / 2,547 conversations)

**Format**: Distributed via the ParlAI framework dataset format and accompanying code on GitHub (downloadable through ParlAI / GitHub repository).

**Annotation**: Emotion labels chosen by crowdworkers from a set of 32 labels; each speaker wrote a 1-3 sentence situation description associated with the selected emotion; two workers then conducted a short 4-8 utterance conversation (speaker and listener roles).

## 🔬 Methodology

**Methods**:
- Retrieval-based evaluation
- Generative evaluation
- Automated metrics
- Human evaluation (crowdsourced ratings on Amazon Mechanical Turk)

**Metrics**:
- Precision at 1 out of 100 (P@1,100)
- BLEU (BLEU-1 through BLEU-4; reported as average BLEU)
- Perplexity
- Human Likert ratings: Empathy/Sympathy, Relevance, Fluency (1-5 scale)

**Calculation**: BLEU computed comparing model response to the gold (target) response; P@1,100 computed as precision of selecting the correct response out of 100 candidates (the actual response included among candidates for this metric); Perplexity computed on the gold response for generative models; human ratings collected on a 1-5 Likert scale for Empathy, Relevance, and Fluency with at least 100 ratings per model.

**Interpretation**: Human evaluation is emphasized as automated metrics do not always correlate with human judgments; higher human Empathy scores indicate more empathetic responses. Fine-tuning on ED or using ED candidates tends to increase human-rated empathy.

**Baseline Results**: Human-rated baseline (Table 2): Retrieval Pretrained (Reddit candidates) Empathy 2.82 ±0.12, Relevance 3.03 ±0.13, Fluency 4.14 ±0.10. Fine-Tuned on ED (Retrieval) Empathy 3.76 ±0.11, Relevance 3.76 ±0.12, Fluency 4.37 ±0.09. Generative Fine-Tuned Empathy 3.25 ±0.12. Automated example: Pretrained generative AVG BLEU ~4.26 and Perplexity 27.96 (Table 1).

**Validation**: Data split into ~80% train / 10% validation / 10% test (19,533 / 2,770 / 2,547). Models selected based on lowest validation loss. Human evaluation collected via MTurk with at least 100 ratings per model; some manual quality checks of worker submissions were performed.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Value Alignment

**Atlas Risks**:
- **Fairness**: Data bias
- **Value Alignment**: Toxic output

**Demographic Analysis**: N/A

**Potential Harm**: ['Aggressive or callous responses / toxic output from models trained on spontaneous internet conversation data']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
