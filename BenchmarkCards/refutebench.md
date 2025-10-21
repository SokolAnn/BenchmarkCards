# RefuteBench

## 📊 Benchmark Details

**Name**: RefuteBench

**Overview**: This paper proposes a comprehensive benchmark, RefuteBench, covering tasks such as question answering, machine translation, and email writing. The evaluation aims to assess whether models can positively accept feedback in the form of refuting instructions and whether they can consistently adhere to user demands throughout the conversation. The benchmark includes single-feedback and multi-feedback interaction settings and evaluates models' feedback acceptance and ability to apply feedback to memorization and generalization queries.

**Data Type**: question-answering pairs; source-target sentence pairs for machine translation; instruction-email pairs (dialogue turns)

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Hebrew

**Similar Benchmarks**:
- RIPPLEEDITS
- WMT2023 GeneralMT
- MTBench
- alpaca-eval

**Resources**:
- [GitHub Repository](https://github.com/ElliottYan/RefuteBench)
- [Resource](https://spacy.io/)
- [Resource](https://openai.com/)
- [Resource](https://claude.ai/)

## 🎯 Purpose and Intended Users

**Goal**: To test LLMs' resistance to modifying their original responses upon receiving contradictory (refuting) instructions, measuring whether models accept feedback and consistently apply it across subsequent conversational turns and generalization queries.

**Tasks**:
- Question Answering
- Machine Translation
- Email Writing

**Limitations**: We currently consider only three tasks (QA, MT and Email Writing). Other application tasks related to refuting instructions such as Code or Reasoning are not considered. We do not consider fine-tuning techniques to enhance the model's ability to follow refuting instructions to avoid issues such as forgetting.

## 💾 Data

**Source**: Question Answering: RIPPLEEDITS (Cohen et al., 2023). Machine Translation: WMT2023 GeneralMT tasks (English->Chinese, English->Hebrew). Email Writing: collected from MTBench, alpaca-cleaned, LIMA, and alpaca-eval (filtered and manually checked).

**Size**: Question Answering: 1,227 single-feedback dialogues and 200 multi-feedback dialogues; Machine Translation: Single-feedback En->Zh 250 dialogues, En->He 250 dialogues; Multi-feedback En->Zh 283 dialogues, En->He 194 dialogues; Email Writing: 100 single-feedback dialogues and 100 multi-feedback dialogues.

**Format**: N/A

**Annotation**: Automated evaluation annotations via GPT-4 for the Feedback Acceptance (FA) metric (using a designed prompt). Manual human annotation on a subset: two PhD annotators labeled 100 QA samples (annotator agreement reported as 94%). The authors report Cohen's Kappa between GPT-4 and human annotation as 0.59 and GPT-4 accuracy of 0.80 against human labels.

## 🔬 Methodology

**Methods**:
- Automated model-based evaluation (GPT-4 used as a judge for Feedback Acceptance)
- Human annotation (manual labeling on a subset for validation)
- Retrieval-based selection (classifier to recall relevant prior feedback) combined with prompting (recall-and-repeat) for intervention experiments

**Metrics**:
- Feedback Acceptance (FA)
- Response Rate (RR)
- Cohen's Kappa
- Pearson correlation coefficient

**Calculation**: FA: percent of immediate model responses judged by GPT-4 to positively accept the feedback (range 0 to 1). RR: defined as the average over dialogues of R(fi, rj)*V(fi, qj) where V(fi, qj) is a viability indicator (0/1) if the i-th feedback applies to the j-th query and R(fi, rj) is a function (0/1 or [0,1]) indicating whether response rj meets the feedback fi; RR is computed by averaging these products across dialogues and queries as described in the paper.

**Interpretation**: Higher FA indicates the model immediately accepts user refuting feedback; higher RR indicates the feedback is correctly applied in subsequent queries. FA ranges 0-1. The authors report that higher FA correlates with higher RR (positive Pearson correlations reported), and that generalization queries and longer dialogue contexts reduce RR and FA (worse performance).

**Baseline Results**: Representative results (from Table 2): QA Single-Feedback (Memory, Context=0) FA: GPT-4 83.00, Claude-2 98.50, ChatGPT 6.50. Overall Multi-Feedback RR: GPT-4 roughly ~70% in many settings and Claude-2 roughly ~60% in many settings. Full per-model per-task results are reported in Table 2 of the paper.

**Validation**: Validation of GPT-4 as an automatic judge: Cohen's Kappa between GPT-4 and human annotation on 100 QA samples is 0.59, and GPT-4 achieves accuracy 0.80 when human labels are considered gold. Human annotation agreement reported as 94% over 100 samples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Value Alignment

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Value Alignment**: Over- or under-reliance

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No private data or non-public information was used in this work (explicitly stated).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
