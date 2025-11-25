# MATHDIAL

## 📊 Benchmark Details

**Name**: MATHDIAL

**Overview**: MATHDIAL is a dataset of ~3k one-to-one teacher-student tutoring dialogues grounded in multi-step math reasoning problems, collected by pairing human teachers with a Large Language Model prompted to represent common student errors. The dataset includes rich annotations (grounding, teacher moves, student profiles, step-by-step solutions, and resolution flags) and is released publicly to enable training and evaluation of dialogue tutoring models.

**Data Type**: text (teacher-student dialogues grounded in math word problems)

**Domains**:
- Education
- Natural Language Processing
- Mathematics

**Similar Benchmarks**:
- CIMA (Stasaski et al., 2020)
- TSCC (Caines et al., 2020)
- TalkMoves (Suresh et al., 2022)
- NCTE (Demszky and Hill, 2023)

**Resources**:
- [GitHub Repository](https://github.com/eth-nlped/mathdial)
- [Resource](https://arxiv.org/abs/2305.14536)

## 🎯 Purpose and Intended Users

**Goal**: Provide a pedagogically rich, large-scale dataset of teacher-student tutoring dialogues grounded in math word problems to enable building and evaluating dialogue tutoring models that are equitable and faithful (e.g., to finetune models to be more effective tutors rather than just problem solvers).

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Educational Technology Researchers

**Tasks**:
- Dialogue Response Generation
- Math Word Problem Solving
- Interactive Tutoring Simulation
- Tutor Modeling

**Limitations**: Explicit limitations stated by the authors: use of an LLM to simulate student confusion may under- or over-represent certain kinds of student confusions; teachers interacting with an LLM role-playing as a student may behave differently than in real classrooms; methodology instantiated for math reasoning only and may not generalize to other domains; teacher moves taxonomy covers a subset of tutoring goals (e.g., does not cover meta-cognitive support or rapport-building); text-only tutoring limits instructional practices like drawings; measuring immediate problem-solving success does not capture long-term learning.

## 💾 Data

**Source**: Grounded in GSM8k math word problems. Dialogues were collected by pairing human teachers (recruited via Prolific) with an LLM simulating students (InstructGPT text-davinci-003 for student turns; student confusions sampled from ChatGPT gpt-3.5-turbo). Teachers had access to the MWP, correct step-by-step solution, and the initial student confusion.

**Size**: 2,861 dialogues; 14,197 utterances

**Format**: N/A

**Annotation**: Annotations include: the math word problem (MWP), step-by-step ground-truth solution, the exact student solution attempt, the exact step that led to student confusion, student profile grounding (six student profiles), teacher move labels (taxonomy: Focus, Probing, Telling, Generic and finer-grained intents), whether confusion was resolved, teacher judgments of student simulation plausibility, flag for conceptual vs. arithmetic errors, and dialogue-level metadata (e.g., teacher-marked resolution).

## 🔬 Methodology

**Methods**:
- Model finetuning
- Zero-shot prompting
- Automated metrics evaluation
- Human evaluation (expert annotators)
- Interactive end-to-end tutoring simulation

**Metrics**:
- sacreBLEU (sBLEU)
- BERTScore
- Token-level F1 (KF1)
- Uptake
- Success@k
- Telling@k
- Human evaluation: Coherence, Correctness, Equitable tutoring

**Calculation**: sBLEU: sacrebleu implementation. BERTScore: computed between generated response and annotated response. KF1: token-level F1 between generated utterance and math word problem as a proxy for faithfulness. Uptake: measured following Demszky et al. Success@k: percentage of conversations where the student reaches the correct final answer at least once within the first k turns. Telling@k: percentage of conversations where the teacher explicitly tells the final answer before the student reaches it within the first k turns. Human evaluation: 3-point Likert for Coherence and Equitable tutoring, binary scale for Correctness.

**Interpretation**: Authors note that automatic metrics are relatively low for this task; an increase in BERTScore and lexical overlap can be caused by more overlap that may indicate increased 'telling' (revealing answers) and can be undesirable. Success@k and Telling@k are interpreted as a trade-off between student solving success and explicit revealing of solutions. Human evaluation metrics assess coherence, factual correctness, and equitable tutoring (giving students room to explore).

**Baseline Results**: Selected explicit results from the paper: finetuned models generally outperform zero-shot prompted ChatGPT on automatic metrics. Ablation: Flan-T5 780M with all grounding achieves sBLEU 9.7 and BERTScore 55.0. Human evaluation (n=50 responses by 3 expert annotators): Flan-T5 780M — Coherence 2.85, Correctness 0.89, Equitable 2.19; ChatGPT — Coherence 2.89, Correctness 0.43, Equitable 1.43; Ground-truth — Coherence 2.94, Correctness 0.98, Equitable 2.42. Interactive evaluation: Flan-T5 780M Success@5 30%, Telling@5 <1%; ChatGPT Success@5 29%, Telling@5 16%; Ground Truth Success@5 59%, Telling@5 <1%.

**Validation**: Data split: 80% training, 20% test; ~60% of test problems are 'seen' (also present in training set) and ~40% are 'unseen' to test generalization. Validation includes teacher judgments of the plausibility of LLM-generated student confusions, annotation agreement experiments (inter-annotator agreement κ reported for teacher move annotations and human evaluation), and human evaluations by expert annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Robustness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: Annotator demographics reported: 91 expert annotators (71 identify as female, 18 as male), majority nationals of the UK, followed by the USA, Canada, Australia, India, and Germany; median age 39.

**Potential Harm**: ['The dataset and evaluations target harms such as models providing factually incorrect feedback to students and revealing solutions too early, both of which are counterproductive to student learning.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors note privacy concerns with recording tutoring sessions as a motivation for their semi-synthetic collection method. They apply a safety filter using the Perspective API to filter out conversations containing toxic content (<1%).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
