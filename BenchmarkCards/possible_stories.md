# Possible Stories

## 📊 Benchmark Details

**Name**: Possible Stories

**Overview**: A new multiple-choice question answering dataset for situated commonsense reasoning. Possible Stories consists of 4,533 multiple-choice questions over 1,313 short story passages in English, where each question asks which of four possible story endings is most plausible under a specified condition; the benchmark is designed to evaluate commonsense reasoning over multiple possible alternatives and to minimize annotation artifacts by collecting alternative endings and multiple questions per set of endings.

**Data Type**: question-answering pairs (story passages with multiple-choice endings)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RACE
- CosmosQA
- QuAIL
- Story Cloze Test
- ROCStories

**Resources**:
- [GitHub Repository](https://github.com/nii-cl/possible-stories)
- [Resource](https://arxiv.org/abs/2209.07760)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate commonsense reasoning over multiple possible alternatives for single passages by asking multiple questions that select the most plausible ending among four candidate endings under specified conditions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering
- Reading Comprehension
- Commonsense Reasoning

**Limitations**: Limited diversity: some systemic biases during data collection; dataset limited to English.

## 💾 Data

**Source**: ROCStories (source passages); crowdsourced alternative endings and questions collected via Amazon Mechanical Turk (MTurk).

**Size**: 4,533 multiple-choice questions over 1,313 passages; 8,885 alternative endings. Split: Train 3,404 questions (984 passages), Dev 458 questions (133 passages), Test 671 questions (196 passages).

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk: workers produced alternative endings and questions; six to eight alternative endings collected per passage then three alternatives + original ending selected; each question validated by three workers and retained when majority vote matched writer's answer; content validation to flag biased or objectionable content; reasoning-type annotations performed on sampled questions by authors.

## 🔬 Methodology

**Methods**:
- Human evaluation (crowdworker labels used to compute human accuracy and consistency)
- Model-based evaluation with pretrained language models (fine-tuned on RACE for unsupervised setting and fine-tuned on the Possible Stories training set for supervised setting)
- Heuristic baselines (perplexity-based using GPT-2 and GPT-Neo, semantic similarity using sentence transformers, entailment scores using RoBERTa-large fine-tuned on MNLI)

**Metrics**:
- Accuracy
- Consistency (passage-wise accuracy: percentage of passages for which all questions are answered correctly)

**Calculation**: Accuracy: percentage of questions for which the model's prediction matches the validated gold answer (human accuracy computed from majority of three additional crowdworker labels). Consistency: percentage of passages for which the majority-vote answers are correct for all questions referring to the passage.

**Interpretation**: Higher Accuracy and Consistency indicate better performance on situated commonsense reasoning. The paper reports human accuracy (92.5%) and human consistency (76.5%) as references; large gaps between model and human scores indicate dataset difficulty.

**Baseline Results**: Unsupervised (models fine-tuned on RACE): DeBERTa-large (v3) 60.2% accuracy, 19.9% consistency; DeBERTa-base 45.3% accuracy, 8.2% consistency; RoBERTa-large 50.5% accuracy, 13.8% consistency. Heuristics: Perplexity GPT-2 large 30.4% accuracy; Perplexity GPT-Neo 29.5% accuracy; Semantic Similarity 37.3% accuracy; Entailment 23.1% accuracy. Supervised (fine-tuned on Possible Stories training set): DeBERTa-large 92.1% accuracy, 74.7% consistency; Human 92.5% accuracy, 76.5% consistency.

**Validation**: Passages do not overlap across train/dev/test. Dev and test sets exclude questions produced by workers who received negative comments. Question-answer validation: each question annotated by three workers and retained if majority vote matched the writer's answer. Content validation: workers flagged biased or objectionable content; flagged items discarded. Quality control included multiple collection batches, worker qualification tasks, and manual checks of worker comments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Human exploitation, Impact on affected communities

**Potential Harm**: ['Perpetuation of unethical opinions or unfair descriptions of social groups (mitigated via content validation and discarding flagged questions)', 'Worker exploitation (addressed by paying above U.S. federal minimum wage and a worker recruitment process intended to be fairer)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Study approved by internal review board; no explicit mention of GDPR or CCPA compliance in the paper.
