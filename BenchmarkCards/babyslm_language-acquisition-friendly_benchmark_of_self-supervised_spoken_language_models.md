# BabySLM (language-acquisition-friendly benchmark of self-supervised spoken language models)

## 📊 Benchmark Details

**Name**: BabySLM (language-acquisition-friendly benchmark of self-supervised spoken language models)

**Overview**: We propose BabySLM, a language-acquisition-friendly benchmark to probe spoken language models at the lexical and syntactic levels, both of which are compatible with the vocabulary typical of children’s language experiences. The benchmark relies on zero-shot behavioral probing and includes a spot-the-word lexical task and a grammatical acceptability judgment syntactic task.

**Data Type**: audio (spoken minimal pairs: synthesized speech stimuli for lexical and syntactic minimal pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Zero Resource Speech Benchmark 2021
- BabyLM challenge

**Resources**:
- [GitHub Repository](https://github.com/MarvinLvn/BabySLM)
- [Resource](https://arxiv.org/abs/2306.01506)

## 🎯 Purpose and Intended Users

**Goal**: To provide a language-acquisition-friendly evaluation suite for spoken language models that probes lexical knowledge (spot-the-word) and syntactic knowledge (grammatical acceptability) using vocabulary and sentence types compatible with children's language experiences.

**Target Audience**:
- Research teams
- Machine Learning Researchers
- Cognitive scientists / Language acquisition researchers

**Tasks**:
- Lexical decision (spot-the-word)
- Grammatical acceptability judgment (syntactic acceptability)

**Limitations**: The benchmark focuses on English.

## 💾 Data

**Source**: Lexical and syntactic items derived from CHILDES (high-frequency words and utterances). Pseudo-words generated with the Wuggy pipeline. Minimal-pair stimuli synthesized using Google Text-To-Speech. Evaluation stimuli filled from high-frequency CHILDES words and syntactic templates.

**Size**: Lexical: >90,000 minimal pairs across 18,000 words; Syntactic: 10,800 minimal pairs. Development/test split: 20% development, 80% test. Stimuli synthesized using 10 voices (5 male, 5 female).

**Format**: Audio files synthesized with Google Text-To-Speech; metadata of minimal pairs (lexical and syntactic) indicating pair labels and phonetic/orthographic forms.

**Annotation**: Automatically generated minimal pairs with labels derived from generation procedure (real word vs pseudo-word for lexical task; grammatical vs ungrammatical for syntactic task). Pseudo-words produced by Wuggy; syntactic items generated from templates filled with high-frequency CHILDES words.

## 🔬 Methodology

**Methods**:
- Zero-shot behavioral probing
- Lexical decision (spot-the-word) evaluation
- Grammatical acceptability judgment evaluation
- Development/Test split (20% dev / 80% test; voice-based split: 1 male and 1 female voice for development, 8 remaining voices for test)

**Metrics**:
- Accuracy (percent) — lexical accuracy
- Accuracy (percent) — syntactic accuracy

**Calculation**: Lexical: for each minimal pair (real word vs pseudo-word), the model scores 1 if it assigns a higher probability to the real word and 0 otherwise; scores averaged across pseudo-words to yield per-word accuracy, then averaged across words to yield lexical accuracy. Syntactic: for each minimal pair (grammatical vs ungrammatical), the model scores 1 if it assigns a higher probability to the grammatical sentence and 0 otherwise; scores averaged within each syntactic phenomenon, then averaged across phenomena to yield syntactic accuracy.

**Interpretation**: Higher accuracy indicates greater lexical or syntactic knowledge as measured by the tasks. Chance level is approximately 50%; performances near 50% indicate no evidence of lexical/syntactic knowledge under the probe.

**Baseline Results**: STELA trained on 1,024 hours of audiobooks: syntactic accuracy 52.8% (reported). STELA trained on 1,024 hours of child-centered long-forms (SEEDLingS): syntactic accuracy 50.3% (reported). STELA trained on SEEDLingS and STELA trained on Providence obtained lexical and syntactic accuracies close to chance. Text-based LMs (LSTM on phonemes/words, BabyBERTa) perform above chance; BabyBERTa obtained the highest syntactic accuracy among evaluated models.

**Validation**: Development/test split: randomly selected 1 male and 1 female voice for development and the remaining 8 voices for test. Randomly selected 20% of lexical and syntactic minimal pairs for development and 80% for test. Standard errors computed across mutually exclusive training sets (reported in figures).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Societal Impact

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Impact on cultural diversity

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
