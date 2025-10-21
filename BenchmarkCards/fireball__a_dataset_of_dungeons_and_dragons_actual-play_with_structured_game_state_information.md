# FIREBALL: A Dataset of Dungeons and Dragons Actual-Play with Structured Game State Information

## 📊 Benchmark Details

**Name**: FIREBALL: A Dataset of Dungeons and Dragons Actual-Play with Structured Game State Information

**Overview**: We present FIREBALL, a large dataset containing nearly 25,000 unique sessions from real Dungeons & Dragons gameplay on Discord with true game state information recorded from the Avrae bot, capturing language, game commands, and underlying game state information. FIREBALL is intended to enable tasks such as predicting executable Avrae commands from natural language and generating grounded narrations from state changes, and the paper demonstrates that models using Avrae state information improve automated metrics and human judgments of generation quality.

**Data Type**: text (dialogue utterances and Avrae commands) and structured game state records (event logs / JSON-like combat state records)

**Domains**:
- Natural Language Processing
- Game AI

**Languages**:
- English

**Similar Benchmarks**:
- Louis and Sutton (2018)
- Rameshkumar and Bailey (2020)
- Si et al. (2021)
- Callison-Burch et al. (2022)
- Papazov et al. (2022)

**Resources**:
- [GitHub Repository](https://github.com/zhudotexe/FIREBALL)
- [Resource](https://arxiv.org/abs/2305.01528)
- [GitHub Repository](https://github.com/avrae/avrae/blob/v4.2.2/cogs5e/initiative/upenn_nlp.py)
- [Resource](https://avrae.readthedocs.io/en/latest/automation_ref.html)
- [GitHub Repository](https://github.com/avrae/avrae/blob/v4.2.2/cogs5e/models/automation/results.py)
- [GitHub Repository](https://github.com/zhudotexe/FIREBALL/blob/main/Filgo_Bitterfoot.pdf)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large, state-augmented dataset of real Dungeons & Dragons actual-play with ground-truth game state information to enable and evaluate tasks such as predicting executable Avrae commands from natural language (Utterance to Command) and generating grounded narrations from state changes (State to Narration), with the aim of improving grounded natural language generation and command generation.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Game AI Researchers

**Tasks**:
- Semantic Parsing (Natural Language to Structured Game Command / Utterance to Command)
- Text Generation (State-conditioned Narration / State to Narration)
- Dialogue Understanding

**Limitations**: FIREBALL does not record overarching narrative context, does not record players' inventory, does not account for movement or placement on a map, and was filtered post-hoc to remove profanity and sensitive topics. Models trained on the dataset are not able to autonomously play D&D and GPT-3 fine-tuning was limited by budget.

**Out of Scope Uses**:
- Autonomous play of Dungeons & Dragons without human oversight

## 💾 Data

**Source**: Recorded gameplay sessions from English-speaking play-by-post Dungeons & Dragons Discord servers instrumented via the Avrae Discord bot with cooperation from the Avrae developer; data collection was approved by Wizards of the Coast, the institution's IRB, and Discord's Bot Safety team; players provided informed consent and could opt out and request deletion.

**Size**: 25,000 unique combat scenarios; 8,012,706 messages; 2,109,603 command invocations; 1,297,254 combat_state_update events; over 8M gameplay utterances; 2.1M commands; 1.2M gameplay states (authors report); 160,000 unique actors; after distillation: 120,000 aligned utterance-command pairs (Utterance to Command) and 43,000 aligned state-utterance pairs (State to Narration).

**Format**: JSON-like Avrae event logs (event schemas available on GitHub) with example character sheets as PDF; event schemas and action attribute definitions available at the linked GitHub and ReadTheDocs URLs.

**Annotation**: Utterance-action alignment performed by matching each utterance to its chronologically nearest state change; utterances with fewer than five words discarded; authorship filtering removed triples not authored by the issuing command user or the DM and triples with multiple command-origin actors; in-character vs out-of-character classification performed using GPT-3 Ada fine-tuned on 750 hand-labeled utterances (94% accuracy on a 125-example validation set); additional manual filtering (removing parenthetical OOC text) and hand-written unit tests used for evaluation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Execution testing via Avrae (pass rate)
- Hand-written unit tests on state updates
- Human evaluation (crowd of experienced Avrae users)
- Model-based evaluation using GPT-3 variants (few-shot and fine-tuning)

**Metrics**:
- Pass Rate (proportion of generated commands that successfully execute in Avrae)
- Unit Tests (proportion of generated commands that result in desired state update via hand-written assertions)
- ROUGE-L
- Average Sentence GLEU (SGleu)
- Perplexity (GPT-2 baseline)
- BERTScore
- ROUGE-1
- Human evaluation: Sense (yes/no), Specific (yes/no), Interestingness (10-point scale)

**Calculation**: Pass rate: models generate commands for 1,000 held-out utterances and proportion that Avrae executes successfully is measured. Unit tests: 10 common scenarios used, 10 commands per scenario-model pair generated, unique commands taken and run through hand-written assertions to validate state updates. ROUGE, SGleu, BERTScore, and Perplexity computed against human references where applicable. Human evaluation: 45 evaluators rated outputs with 3- to 7-scenario assignments and at least 3-way redundancy per scenario.

**Interpretation**: Higher pass rate and unit test pass proportions indicate more correct/executable command generation; higher ROUGE/BERTScore indicates greater similarity to human narrations though authors note automated metrics are imperfect for creative generation; human Sense/Specific/Interestingness ratings measure practical quality and grounding of generated narrations.

**Baseline Results**: Utterance to Command (Table 2): FT+S - Pass Rate 0.726, Unit Tests 0.65, SGleu 0.355, ROUGE-L 0.75; FT - Pass Rate 0.235, Unit Tests 0.234, SGleu 0.189, ROUGE-L 0.551; FS+S - Pass Rate 0.432, Unit Tests 0.429, SGleu 0.325, ROUGE-L 0.771; FS - Pass Rate 0.319, Unit Tests 0.25, SGleu 0.246, ROUGE-L 0.598. State to Narration (Table 3): DIALOG Perplexity 208.97, BERTScore 0.8458, ROUGE-1 0.1077; COMMAND Perplexity 156.98, BERTScore 0.8421, ROUGE-1 0.0919; FIREBALL-SHORT Perplexity 202.39, BERTScore 0.8478, ROUGE-1 0.1087; FIREBALL-FULL Perplexity 208.98, BERTScore 0.8476, ROUGE-1 0.1156; Human Perplexity 452.653 (BERT/ROUGE N/A). Human evaluation (Table 4): DIALOG Sense 0.36, Specific 0.27, Interest 4.27; COMMAND Sense 0.41, Specific 0.37, Interest 4.72; FIREBALL-SHORT Sense 0.52, Specific 0.48, Interest 4.98; FIREBALL-FULL Sense 0.55, Specific 0.47, Interest 4.6; Human Sense 0.54, Specific 0.48, Interest 4.91.

**Validation**: Classifier validation: in-character/out-of-character classifier achieved 94% accuracy on a validation set of 125 utterances. Human evaluation: 45 experienced Avrae users recruited; each scenario rated with at least 3-way redundancy; statistical significance assessed via Student's t-test (results reported in Appendix H). Additional validation via executing generated commands in Avrae and running hand-written unit tests on resulting state updates.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Robustness
- Accuracy
- Fairness
- Value Alignment
- Societal Impact

**Atlas Risks**:
- **Privacy**: Data privacy rights alignment
- **Robustness**: Hallucination
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Value Alignment**: Toxic output
- **Societal Impact**: Impact on human agency

**Potential Harm**: ['Generation of sexual or explicit content that may require age restrictions (explicitly mentioned as a prior observed issue in roleplaying LM systems).', 'Unfiltered violent or profane descriptions unsuitable for young players (noted; dataset filtered post-hoc).', 'Loss of player agency: model-generated narrations or actions that appear to act on behalf of or control player characters (explicit evaluator concern).']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Players provided informed consent; players were presented with a recording message when combat began and could opt out of individual combat instances; server admins could stop recording; a public form for data deletion requests was provided.

**Data Licensing**: Not Applicable

**Consent Procedures**: Data collection was approved by Wizards of the Coast and the authors' institution IRB; participants provided informed consent; players could opt out of individual combats and server admins could stop recording; deletion requests were supported via a public form.

**Compliance With Regulations**: IRB approval obtained; data collection approved by Wizards of the Coast; Bot Safety team at Discord was involved in the data collection process.
