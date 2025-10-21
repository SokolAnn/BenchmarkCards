# DialogStudio: Towards Richest and Most Diverse Unified Dataset Collection for Conversational AI

## 📊 Benchmark Details

**Name**: DialogStudio: Towards Richest and Most Diverse Unified Dataset Collection for Conversational AI

**Overview**: A comprehensive collection aggregating more than 80 publicly available dialogue datasets unified under a consistent JSON format while preserving original information. DialogStudio covers Open-Domain Dialogues, Task-Oriented Dialogues, Natural Language Understanding, Conversational Recommendation, Dialogue Summarization, and Knowledge-Grounded Dialogues; it identifies dataset licenses, constructs external knowledge and domain-aware prompts for selected dialogues, and is made publicly accessible to support dataset- and task-based research and language model pre-training.

**Data Type**: text (multi-turn dialogue examples, dialogue context-response pairs, question-answering pairs, dialogue schemas, and external knowledge strings)

**Domains**:
- Natural Language Processing
- Conversational AI
- Task-Oriented Dialogue
- Knowledge-Grounded Dialogue
- Dialogue Summarization
- Recommendation Systems

**Similar Benchmarks**:
- Flan collection
- InstructDial
- ParlAI
- OPT

**Resources**:
- [GitHub Repository](https://github.com/salesforce/DialogStudio)
- [Resource](https://arxiv.org/abs/2307.10172)

## 🎯 Purpose and Intended Users

**Goal**: Provide the largest and most diverse unified collection of dialogue datasets to enable comprehensive and standardized training and evaluations of dialogue models, support dataset- and task-based research, and facilitate language model pre-training.

**Target Audience**:
- ML Researchers
- Model Developers
- Conversational AI Researchers

**Tasks**:
- Response Generation
- Dialogue State Tracking
- Intent Classification
- Question Answering (conversational)
- Dialogue Summarization
- Conversational Recommendation

**Limitations**: Optimizing user experience for the substantial volume of datasets is a challenge; the collection is built upon public research datasets and the authors did not hire external annotators; while dataset licenses are provided, there remains a possibility that some works might not fully comply with the licenses.

## 💾 Data

**Source**: Aggregated from more than 80 publicly available dialogue datasets (see Appendix Table 4 and Table 5 for dataset lists; examples include MultiWOZ, CoQA, SODA, ShareGPT, SGD, KVRET, AirDialogue, FRAMES, SParC, FeTaQA, MultiModalQA, etc.).

**Size**: At most 11,000 dialogues sampled per dialogue dataset; additionally ~11,000 dialogue turns were extracted from question-answering datasets (exact total aggregate size not specified).

**Format**: Unified JSON dictionary format (per-dialogue JSON with fields such as dialogue ID, split label, domain, task, utterances, dst, dst knowledge, intent, intent knowledge, external knowledge, prompt).

**Annotation**: Preserves original dataset annotations when available; manual fixes applied for faulty/missing utterances (<0.5% dialogues); manual construction of prompt templates, schema extraction/creation for dialogue states and intents; no external annotators hired.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation (expert researchers)
- Model-based evaluation (ChatGPT/GPT-3.5-turbo for dialogue quality scoring)
- Zero-shot and few-shot model evaluation

**Metrics**:
- ROUGE-L
- F1 Score (Unigram F1 overlap)

**Calculation**: ROUGE-L measures longest common subsequence between prediction and reference; F1 measures Unigram F1 overlap between the prediction and ground-truth response. Scores for quality evaluation (Understanding, Relevance, Correctness, Coherence, Completeness, Overall) are on a 1-5 scale (higher is better) when using ChatGPT for quality rating.

**Interpretation**: Higher ROUGE-L and F1 indicate better response generation performance. For ChatGPT quality ratings, scores >3 are considered high quality after alignment with human expert ratings. Model comparisons are made in zero-shot and few-shot scenarios against listed baselines.

**Baseline Results**: Zero-shot results on CoQA and MultiWOZ (ROUGE-L / F1): Flan-T5-3B: CoQA 37.1 / 37.2, MultiWOZ 7.0 / 7.4; Flan-T5-Large: CoQA 22.5 / 22.3, MultiWOZ 15.9 / 17.6; GODEL-Large: CoQA 43.2 / 43.3, MultiWOZ 18.5 / 19.3; DialogStudio-T5-Large: CoQA 61.2 / 61.5, MultiWOZ 32.4 / 34.5; DialogStudio-Flan-T5-Large: CoQA 63.3 / 63.5, MultiWOZ 33.7 / 35.9. (Results taken from Table 1 in the paper.)

**Validation**: To harmonize ChatGPT and human ratings, 50 training dialogues per selected dataset were rated by three expert researchers and used to align ChatGPT; CoQA and MultiWOZ 2.2 were excluded from pre-training to prevent data leakage; evaluation includes zero-shot and few-shot tests on held-out datasets and unseen tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data licensing / usage
- Dataset quality / annotation issues

**Atlas Risks**:
- **Data Laws**: Data usage restrictions

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: DialogStudio is built upon public research datasets without individual or private information; the authors state they did not hire external annotators.

**Data Licensing**: Original licenses for all datasets are identified and included; the authors state that all datasets support academic research and some permit commercial usage. The code is released under the Apache 2.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
