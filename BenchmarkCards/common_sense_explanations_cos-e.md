# Common Sense Explanations (CoS-E)

## 📊 Benchmark Details

**Name**: Common Sense Explanations (CoS-E)

**Overview**: We collect human explanations for commonsense reasoning in the form of natural language sequences and highlighted annotations in a new dataset called Common Sense Explanations (CoS-E).

**Data Type**: text (open-ended natural language explanations and highlighted span annotations)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- CommonsenseQA
- SWAG
- Story Cloze (ROC Stories)
- e-SNLI
- Winograd Schemas

**Resources**:
- [GitHub Repository](https://github.com/nazneenrajani/CoS-E)
- [Resource](https://www.tau-nlp.org/csqa-leaderboard)

## 🎯 Purpose and Intended Users

**Goal**: Introduce a new Common Sense Explanations (CoS-E) dataset to study neural commonsense reasoning and provide a new method, CAGE, for automatically generating explanations that can be used during training and inference.

**Tasks**:
- Question Answering
- Text Generation (Explanation Generation)

**Limitations**: CoS-E contains noisy explanations despite quality-control checks; explanations were collected from a single annotator per example; authors observed gender disparity in CQA with a higher proportion of feminine pronouns used in negative contexts which has propagated into CoS-E.

## 💾 Data

**Source**: Built on top of the CommonsenseQA dataset (CQA); explanations collected via Amazon Mechanical Turk for CQA train-random-split and dev-random-split.

**Size**: 7,610 examples (train) and 950 examples (dev) for v1.0; 9,741 examples (train) and 1,221 examples (dev) for v1.11.

**Format**: N/A

**Annotation**: Collected via Amazon Mechanical Turk: annotators highlighted relevant words in the question and provided brief open-ended explanations; one annotator per example; quality-control checks included in-browser checks (must highlight at least one word, minimum explanation length 4 words, explanation not a substring of question/answers) and post-collection filtering to remove templated explanations.

## 🔬 Methodology

**Methods**:
- Automated metrics (BLEU, Perplexity)
- Human evaluation (Mechanical Turk)
- Model-based evaluation (BERT classifier using human or auto-generated explanations; GPT fine-tuned to generate explanations)
- Transfer evaluation to out-of-domain datasets (SWAG, Story Cloze)

**Metrics**:
- Accuracy
- BLEU Score
- Perplexity

**Calculation**: Accuracy reported as percent correct on CQA splits. BLEU score computed as n-gram overlap between generated explanations and CoS-E-open-ended (paper reports peak BLEU of 4.1 between CAGE-reasoning and CoS-E-open-ended). Perplexity reported as token-level measure of language model prediction (paper reports perplexity of 32).

**Interpretation**: Higher Accuracy indicates better commonsense reasoning on CQA (authors report up to ~10% absolute improvement over previous state-of-the-art using CAGE). BLEU measures syntactic n-gram overlap (low BLEU can indicate different phrasing despite useful content). Lower Perplexity indicates better next-token prediction by the language model.

**Baseline Results**: Dev (dev-random-split): BERT baseline 63.8% accuracy; CoS-E-open-ended 65.5%; CAGE-reasoning 72.6%. Test (CQA v1.0): RC (Talmor et al., 2019) 47.7%; GPT (Talmor et al., 2019) 54.8%; CoS-E-open-ended 60.2%; CAGE-reasoning 64.7%; Human 95.3%. (Also reported CQA v1.11 test: CAGE-reasoning 55.7%; BERT baseline 56.7%; CoS-E-open-ended 58.2%.)

**Validation**: Best language model checkpoint selected based on validation BLEU and perplexity; ablation analyses conducted on CQA dev-random-split; human evaluation conducted on 400 examples via Mechanical Turk to judge explanations' sufficiency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness
- Misuse
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning
- **Misuse**: Spreading disinformation
- **Value Alignment**: Harmful output
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Observed gender disparity in CQA with a higher proportion of feminine pronouns used in negative contexts; this bias propagated into CoS-E.

**Potential Harm**: ['Reinforcing harmful or biased reasoning in downstream models', 'Gender bias manifesting in negative contexts']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
