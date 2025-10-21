# A Benchmark for Understanding Dialogue Safety in Mental Health Support

## 📊 Benchmark Details

**Name**: A Benchmark for Understanding Dialogue Safety in Mental Health Support

**Overview**: This paper develops a theoretically and factually grounded sequential taxonomy that prioritizes positive impact on help-seekers, and creates a benchmark corpus with fine-grained labels for each dialogue session to facilitate research on dialogue safety in mental health support.

**Data Type**: text (multi-turn dialogue sessions)

**Domains**:
- Natural Language Processing
- Mental Health

**Languages**:
- Chinese

**Similar Benchmarks**:
- SafetyKit
- SOLID
- Ruddit
- ToxiGen

**Resources**:
- [GitHub Repository](https://github.com/qiuhuachuan/DialogueSafety)
- [Resource](https://arxiv.org/abs/2307.16457)
- [Resource](https://huggingface.co/bert-base-chinese)
- [Resource](https://huggingface.co/hfl/chinese-roberta-wwm-ext-large)

## 🎯 Purpose and Intended Users

**Goal**: Develop a sequential and inclusive dialogue safety taxonomy grounded in theoretical and factual knowledge and provide a benchmark dataset with fine-grained labels to analyze and detect unsafe responses in mental health support conversations.

**Target Audience**:
- ML Researchers
- Model Developers
- Conversation Agent Designers
- Mental Health Domain Experts

**Tasks**:
- Text Classification
- Binary Classification (safe vs. unsafe)
- Fine-grained Safety Classification

**Limitations**: Class imbalance: some categories (e.g., Toxic Language and Nonfactual Statement) have very few training and test samples.

## 💾 Data

**Source**: An online Chinese text-based counseling platform (collected 2,382 multi-turn dialogues) combined with 2,000 blog titles crawled from Yixinli's public QA column (https://www.xinli001.com/qa). Data were divided into multi-turn dialogue sessions concluding with the help-seeker's last utterance.

**Size**: 7,935 multi-turn dialogue sessions (train: 7,135 examples; test: 800 examples)

**Format**: N/A

**Annotation**: Manual annotation by three fixed annotators with one year of psychological counseling experience each, using a sequential annotation framework. Annotators received training; annotation proceeded iteratively every 200 sessions. Inter-rater agreement measured by Fleiss' kappa = 0.52; if κ < 0.4 annotators independently review and discuss discrepancies.

## 🔬 Methodology

**Methods**:
- Human annotation for dataset creation (sequential taxonomy)
- Model-based evaluation: fine-tuning pre-trained models (BERT-base, RoBERTa-large)
- Zero-shot and few-shot prompt evaluation with ChatGPT (GPT-3.5-TURBO variants)

**Metrics**:
- Accuracy
- Weighted Precision
- Recall
- F1 Score

**Calculation**: Training uses weighted cross-entropy with class weights [2.0, 2.0, 0.5, 2.0, 2.0, 2.0, 2.0, 0.5] corresponding to the eight categories. Evaluation metrics reported as mean and standard deviation over five seeds; best checkpoint by highest accuracy retained for test evaluation.

**Interpretation**: Higher Accuracy / Precision / Recall / F1 indicate better detection of unsafe responses. The authors interpret fine-tuned models (BERT-base, RoBERTa-large with ~70% accuracy) as more suitable for detecting unsafe responses in mental health support than ChatGPT in zero- and few-shot settings (~43–48% accuracy).

**Baseline Results**: ChatGPT (GPT-3.5-TURBO-0301) zero-shot: Accuracy 47.5%; few-shot: Accuracy 48.4%. ChatGPT (GPT-3.5-TURBO-0613) zero-shot: Accuracy 43.1%; few-shot: Accuracy 44.7%. BERT-base (fine-tuned): Accuracy 70.3%. RoBERTa-large (fine-tuned): Accuracy 70.4%. (Values reported as mean accuracy over five runs; full table includes precision, recall, F1 and standard deviations.)

**Validation**: Data split via Stratified Shuffle Split (90% train, 10% test per category). Model fine-tuning experiments run with five seeds; reported mean and standard deviation across runs. Annotation reliability validated via Fleiss' kappa (0.52) and iterative review when κ < 0.4.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Fairness
- Societal Impact
- Misuse

**Atlas Risks**:
- **Value Alignment**: Toxic output, Harmful output
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Misuse**: Dangerous use
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: ['Physical harm: provision of harmful or illegal instructions (examples cited: robbery, suicide, murder).', 'Psychological harm: toxic language, unamiable judgment, implicit verbal abuse harming help-seekers.', 'Societal harm: dishonest anthropomorphism leading to physiological and societal risks.', 'Misinformation: nonfactual statements that may mislead help-seekers.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Study granted ethics approval by the Institutional Ethics Committee. Access to the dataset is restricted to researchers who agree to comply with ethical guidelines and sign a confidentiality agreement.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
