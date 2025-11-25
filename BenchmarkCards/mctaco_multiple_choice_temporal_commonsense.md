# MCTACO (Multiple Choice Temporal Commonsense)

## 📊 Benchmark Details

**Name**: MCTACO (Multiple Choice Temporal Commonsense)

**Overview**: We define five classes of temporal commonsense, and use crowdsourcing to develop a new dataset, MCTACO, that serves as a test set for this task.

**Data Type**: text (question-answering pairs; sentence, question, candidate answer tuples)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- MultiRC
- SWAG
- ARC

**Resources**:
- [Resource](https://cogcomp.seas.upenn.edu/page/publication_view/882)
- [GitHub Repository](https://github.com/allenai/allennlp)
- [GitHub Repository](https://github.com/huggingface/pytorch-pretrained-BERT)
- [Resource](https://www.elastic.co)

## 🎯 Purpose and Intended Users

**Goal**: To define five classes of temporal commonsense and develop MCTACO as a test set to evaluate temporal commonsense understanding; to systematically study and quantify performance on a range of temporal commonsense phenomena.

**Target Audience**:
- Machine Learning Researchers
- Natural Language Processing Researchers

**Tasks**:
- Question Answering
- Commonsense Reasoning
- Temporal Reasoning

**Limitations**: The dataset cannot cover all possible events and their attributes; systems are expected to require external world knowledge beyond the dataset and training solely on this data is unlikely to succeed (performance plateaus after about 2.5k question-answer pairs).

## 💾 Data

**Source**: Sentences randomly selected from MultiRC (from each of its 9 domains). Questions and candidate answers collected via crowdsourcing on Amazon Mechanical Turk; candidate answer expansion used rule-based perturbations, BERT predictions, and an event phrase pool from PropBank/IR.

**Size**: 1,893 unique questions; 13,225 question-answer pairs; up to 20 candidate answers per question (expanded).

**Format**: Text tuples (sentence, question, candidate answer).

**Annotation**: Crowdsourced via Amazon Mechanical Turk with native-speaker restriction and qualification tryouts. Multi-step process: question generation, verification by two annotators, candidate answer expansion, and final labeling by 4 annotators (likely / unlikely / invalid). Tuples retained only if all 4 annotators agree on 'likely' or 'unlikely'.

## 🔬 Methodology

**Methods**:
- Automated metrics (Exact Match, F1)
- Model-based evaluation using ESIM and BERT (with variants)
- Human evaluation (expert annotator on sampled questions)

**Metrics**:
- Exact Match (EM)
- F1

**Calculation**: For a candidate answer a and question q, f(a;q) in {0,1} denotes correctness. EM is computed as the fraction of questions for which all candidate answers are correctly labeled: EM = (sum_q sum_{a in q} f(a;q)) / |{q in D}|. Per-question recall R(q)=#correctly labeled likely answers / #ground-truth likely answers; P(q) and F1(q) defined similarly. Aggregate F1 is the macro average of question-level F1's: F1 = (sum_q F1(q)) / |{q in D}|.

**Interpretation**: EM measures strict full-question correctness while F1 measures average overlap with ground truth. A small gap between EM and F1 (as in humans) indicates robust performance; large gaps indicate systems may be matching surface forms rather than modeling temporal commonsense.

**Baseline Results**: Random: F1=36.2%, EM=8.1%. Always Positive: F1=49.8%, EM=12.1%. Always Negative: F1=17.4%, EM=17.4%. ESIM + GloVe: F1=50.3%, EM=20.9%. ESIM + ELMo: F1=54.9%, EM=26.4%. BERT: F1=66.1%, EM=39.6%. BERT + unit normalization: F1=69.9%, EM=42.7%. Human (expert on sample): F1=87.1%, EM=75.8%.

**Validation**: Quality controls include annotator qualification tests and unanimity requirement of 4 annotators for final labels. Dataset split provided as a uniform 30%/70% dev/test; additional verification via an expert annotator and a performance-as-a-function-of-training-size analysis (performance plateaus after ~2.5k question-answer pairs) in Appendix A.2.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
