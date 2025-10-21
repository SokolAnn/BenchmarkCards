# contextually-situated judgments of appropriateness

## 📊 Benchmark Details

**Name**: contextually-situated judgments of appropriateness

**Overview**: We introduce a new dataset of contextually-situated judgments of appropriateness and show that large language models can readily incorporate relationship information to accurately identify appropriateness in a given context.

**Data Type**: text (conversational messages with relationship-context labels)

**Domains**:
- Natural Language Processing
- Sociolinguistics

**Languages**:
- English

**Similar Benchmarks**:
- Empathetic dialogs data
- Cornell movie dataset
- PRIDE dataset
- TalkDown
- Stanford Politeness Corpus
- Pushshift Reddit

**Resources**:
- [GitHub Repository](https://github.com/davidjurgens/contextual-appropriateness)
- [Resource](https://arxiv.org/abs/2307.02763)

## 🎯 Purpose and Intended Users

**Goal**: Detect contextually-inappropriate messages by explicitly modeling the social relationship between interlocutors and to provide a dataset for training/evaluating models on contextual appropriateness.

**Target Audience**:
- Natural Language Processing researchers
- Model developers
- Content moderation practitioners

**Tasks**:
- Text Classification
- Offensive Language Detection
- Politeness Detection

**Limitations**: The context modeled is limited to only the parties' relationship (other contextual factors like demographics, culture, setting, and history are not included); the dataset covers a finite set of 49 relationship types and may not generalize to less-common relationships; annotations were produced by a small pool of annotators (authors), so judgments may primarily reflect their values and may not generalize to other social or cultural contexts.

## 💾 Data

**Source**: Sampled conversational comments from English-language Reddit (Pushshift) and movie dialogues (Cornell movie dataset); PRIDE dataset used for counterfactual analysis; annotations produced by the paper's annotators (authors).

**Size**: 5,299 messages; 12,236 appropriateness ratings (12,236 judgments across 5,299 messages).

**Format**: N/A

**Annotation**: Manual annotation by the paper's authors (five annotators) in a two-phase process: Phase 1 ideation and adjudication producing 401 messages and 5,029 ratings; Phase 2 active-learning-guided annotation producing adjudicated and non-adjudicated ratings (2,159 adjudicated ratings; 5,408 Phase 2 ratings). Annotators judged plausibility first and then appropriateness; adjudication elevated inter-annotator agreement (plausibility α=0.72, appropriateness 0.92 after adjudication).

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation (Binary F1, Precision, Recall, Accuracy, macro-F1)
- Model-based evaluation using prompt-based LLMs (T5, GPT-2, FLAN-T5) and masked language model fine-tuning (DeBERTa-v3, MiniLM)
- Active learning for data selection (T5 prompt-based classifier)
- Baseline comparisons (random baseline, Perspective API)
- Ablation/held-out category experiments
- Downstream logistic regression for condescension and politeness using relationship-appropriateness feature vectors

**Metrics**:
- Binary F1
- Precision
- Recall
- F1 (macro-F1)
- Accuracy

**Calculation**: Primary task: Binary F1 where 'inappropriate' is the positive class. Data split at message level 70:10:20 (train:dev:test). Model performance reported as the average across five random runs; additional metrics (Precision, Recall) reported per model/run as shown in tables.

**Interpretation**: Higher Binary F1 (and corresponding Precision/Recall) indicates better recognition of contextual inappropriateness. The best-performing model (flan-t5-xl) attained approximately 0.70 Binary F1 on the test set. No explicit numeric thresholds for good vs. poor performance are provided beyond reported results.

**Baseline Results**: Random baseline Binary F1 ~0.399; Perspective API Binary F1 0.157; DeBERTa-v3 MLM fine-tuning F1 0.659; MiniLM MLM fine-tuning F1 0.656; t5-base prompt-based F1 0.669; gpt2-med prompt-based F1 0.665; flan-t5-large prompt-based F1 0.661; flan-t5-xl prompt-based F1 0.698 (test set averages).

**Validation**: Annotated data split 70:10:20 at message level (9,107 train; 1,100 dev; 2,029 test). Performance averaged across five random runs. Adjudicated subset (2,159 ratings) used for evaluation; Krippendorff's α reported for plausibility and appropriateness during annotation and adjudication.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Misuse
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Misuse**: Improper usage
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Annotators were the paper's authors (five annotators). The authors state they will release demographic information on annotators as part of the dataset to make potential biases explicit. The paper notes the annotations likely reflect annotators' values and may not generalize to other social or cultural contexts.

**Potential Harm**: ['Annotations and resulting models may reflect annotator values and could further marginalize communities whose norms are not represented.', "Adversarial actors could use the data and models to screen messages and evade detection, enabling harassment or abuse while 'abiding by the rules'."]

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Annotators were the authors and were compensated as part of their normal duties. The authors state they will release demographic information on annotators as part of the dataset to make biases explicit. Annotators were provided guidance on self-care due to exposure to potentially objectionable content. No explicit dataset anonymization procedure for released data is described.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
