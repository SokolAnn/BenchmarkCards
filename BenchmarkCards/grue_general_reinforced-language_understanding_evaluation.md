# GRUE (General Reinforced-language Understanding Evaluation)

## 📊 Benchmark Details

**Name**: GRUE (General Reinforced-language Understanding Evaluation)

**Overview**: GRUE (General Reinforced-language Understanding Evaluation) benchmark, a set of 6 language generation tasks which are supervised not by target strings, but by reward functions which capture automated measures of human preference. GRUE is the first leaderboard-style evaluation of RL algorithms for NLP tasks.

**Data Type**: text (generative text: continuations, summaries, translations, data-to-text, QA answers, dialogue responses)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/allenai/RL4LMs)
- [Resource](https://rl4lms.apps.allenai.org/)
- [Resource](https://arxiv.org/abs/2210.01241)

## 🎯 Purpose and Intended Users

**Goal**: Align pre-trained large language models (LMs) with human preferences by evaluating RL algorithms for LM-based generation using reward functions that capture automated measures of human preference.

**Target Audience**:
- ML Researchers
- Research Community

**Tasks**:
- Text Continuation
- Summarization
- Data-to-Text Generation
- Machine Translation
- Question Answering (abstractive)
- Dialogue Generation
- Generative Commonsense

**Limitations**: N/A

## 💾 Data

**Source**: IMDB (Maas et al., 2011); CommonGen (Lin et al., 2020); CNN/Daily Mail (Hermann et al., 2015); ToTTo (Parikh et al., 2020); WMT-16 (en-de) (Bojar et al., 2016); NarrativeQA (Kočiskỳ et al., 2018); DailyDialog (Li et al., 2017).

**Size**: IMDB: 25,000 training, 5,000 validation, 5,000 test; CNN/Daily Mail: 287,000 training, 13,000 validation, 11,000 test; other dataset sizes: N/A (not specified in paper).

**Format**: N/A

**Annotation**: Human judgments collected via Amazon Mechanical Turk for five tasks (3 unique human raters per sample); a DistilBERT classifier trained on sentiment labels for IMDB used as a reward model; pairwise human preference data collected for Commongen to train a T5-11B preference model (train/val/test splits described in Appendix).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation (crowdsourced Likert ratings and pairwise preference collection)
- Leaderboard-style evaluation

**Metrics**:
- Perplexity
- Learned Sentiment Classifier (sentiment score)
- CIDER
- ROUGE-1
- ROUGE-2
- ROUGE-L
- BLEU (n=3, n=4)
- METEOR
- Coverage
- SPICE
- SummaCZS
- SacreBLEU
- PARENT
- BLEURT
- TER
- chrF
- BertScore
- Mean Segmented Type Token Ratio (MSSTR)
- Shannon entropy (unigrams and bigrams)
- Distinct-1
- Distinct-2
- Krippendorf's alpha
- ROC AUC

**Calculation**: Each task is evaluated at test time using a task-specific mix of metrics (task preference metrics and naturalness metrics). During training models often optimize a single reward function; test-time scores are averaged across the task-specific metric mix. Results are averaged over multiple random seeds (exact counts in Appendix B).

**Interpretation**: Higher task-metric values indicate better task-specific performance; naturalness is assessed via perplexity and human Likert fluency judgments. The paper emphasizes balancing reward optimization with a KL-based naturalness penalty (removing KL penalty yields higher reward but worse perplexity / naturalness). NLPO is presented as better balancing reward and naturalness than prior policy-gradient methods.

**Baseline Results**: IMDB (sentiment / perplexity): Zero-shot 0.489 / 32.171; Supervised 0.539 / 35.472; PPO 0.602 / 33.816; NLPO 0.611 / 33.832; Supervised+PPO 0.626 / 35.049; Supervised+NLPO 0.620 / 34.816. Additionally: a 220 million parameter model trained with supervision+NLPO outperforms a 3 billion parameter supervised model (reported in paper).

**Validation**: Validation follows original dataset train/val/test splits. Human validation: crowd-sourced human judgments (3 annotators per sample), inter-annotator agreement measured via Krippendorf's alpha, statistical testing with one-way ANOVA and post-hoc Tukey HSD to assess significance; results averaged over multiple seeds; further experimental details and exact counts in Appendix B.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Governance

**Atlas Risks**:
- **Robustness**: Hallucination
- **Accuracy**: Unrepresentative data
- **Governance**: Lack of testing diversity

**Demographic Analysis**: Human evaluation annotators for qualification were recruited from Australia, Canada, New Zealand, Great Britain, and the United States (qualification round); further annotator qualification and per-task details are provided in Appendix B.

**Potential Harm**: ['Detecting and preventing reward hacking (nonsense outputs that exploit automated metrics)', 'Detecting and reducing factual inconsistency / hallucination in generated outputs (e.g., summarization)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
