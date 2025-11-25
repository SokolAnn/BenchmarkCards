# KMMLU (Measuring Massive Multitask Language Understanding in Korean)

## 📊 Benchmark Details

**Name**: KMMLU (Measuring Massive Multitask Language Understanding in Korean)

**Overview**: KMMLU is a new Korean benchmark consisting of 35,030 expert-level multiple-choice questions across 45 subjects, collected from original Korean exams to capture linguistic and cultural aspects of the Korean language. The dataset, prompts, and evaluation code are made publicly available on the Hugging Face Hub and integrated into EleutherAI's Language Model Evaluation Harness.

**Data Type**: question-answering pairs (multiple-choice)

**Domains**:
- Natural Language Processing
- Humanities and Social Science
- Science, Technology, Engineering, and Mathematics
- Applied Science

**Languages**:
- Korean

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- CMMLU
- KLUE
- Ko-H5
- KoBBQ
- HAE-RAE Benchmark
- CLIcK
- KorNAT

**Resources**:
- [Resource](https://huggingface.co/datasets/HAERAE-HUB/KMMLU)
- [GitHub Repository](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/kmmlu)

## 🎯 Purpose and Intended Users

**Goal**: Provide a comprehensive Korean benchmark of expert-level multiple-choice questions across 45 subjects sourced from original Korean exams to evaluate and track large language model performance on Korean language and Korea-specific knowledge and reasoning.

**Target Audience**:
- Korean NLP Community
- Researchers
- Model Developers

**Tasks**:
- Question Answering
- Knowledge and Reasoning Evaluation (multiple-choice)

**Limitations**: Copyright-related removals created coverage gaps (notably in Korean language, medical, and financial domains). Traditional benchmarks may not assess generative abilities and instruction-following skills. Potential misuse of benchmarks may produce models that perform poorly in real-world applications.

**Out of Scope Uses**:
- Assessing generative abilities and instruction-following skills (the authors note KMMLU is a traditional knowledge benchmark and recommend future work to expand to generative evaluation)

## 💾 Data

**Source**: Collected from 533 diverse sources including Public Service Aptitude Test (PSAT), Korean License Tests, and the College Scholastic Ability Test (CSAT).

**Size**: Total post-filtering collection: 243,777 questions; Training set: 208,522 questions; Validation set: 225 questions; Test set: 35,030 questions.

**Format**: N/A

**Annotation**: Original exam answer keys used as labels. Human accuracy data collected from actual test-takers when available (approximately 90% of exams include human performance data). Chain-of-Thought (CoT) exemplars elicited from GPT-4 and HyperCLOVA X with majority voting and manual selection/revision by authors; two workers per CoT question with ~87% initial agreement and iterative validation.

## 🔬 Methodology

**Methods**:
- Few-shot evaluation (5-shot)
- Direct prompting with greedy decoding
- Chain-of-Thought (CoT) prompting (greedy decoding for CoT)
- Contamination checks using paraphrasing and perplexity / n-gram accuracy
- Evaluation using EleutherAI's LM-Eval-Harness

**Metrics**:
- Accuracy
- Macro-average Accuracy (across subjects/categories)
- Perplexity
- n-gram accuracy
- Human accuracy (collected from exam takers)

**Calculation**: Accuracy is reported as macro-average accuracy across subjects within categories in a 5-shot setting; random guessing baseline is 25% (four choices). Perplexity is computed on original and paraphrased versions of samples. n-gram accuracy for proprietary models computed by sampling prompt prefixes and measuring prediction match for target n-grams as described in the paper.

**Interpretation**: Average human accuracy reported as 62.6%; many license exams require an 80% passing score, so achieving over 80% on KMMLU is considered equivalent to minimum human expert performance. Random baseline is 25%. Reported model accuracies should be interpreted against these baselines and human performance.

**Baseline Results**: Selected results (Direct method, 5-shot, macro/micro averages as reported): GPT-4 average accuracy 59.95%; HYPER CLOVA X average accuracy 53.40%. The paper notes the best public model scores approximately 50.5%.

**Validation**: Public release of dataset for six months for community feedback (five issues reported; 741 instances modified). Manual review of Test and Validation sets for copyright with 147 test instances replaced. Contamination checks performed via paraphrasing and perplexity/n-gram accuracy analysis. CoT exemplars validated with two workers per question (~87% initial agreement) and iterative conflict resolution.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Transparency
- Data Laws
- Intellectual Property
- Explainability
- Misuse
- Governance

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Transparency**: Lack of training data transparency
- **Data Laws**: Data usage restrictions
- **Intellectual Property**: Copyright infringement, Data usage rights restrictions
- **Explainability**: Unexplainable output
- **Misuse**: Improper usage
- **Governance**: Lack of data transparency

**Demographic Analysis**: The authors note variation in test origins and test-taker populations; comparing human accuracy directly may not be desirable due to these variations (human accuracy averages 62.6% but varies by exam source).

**Potential Harm**: ['The authors state that potential misuse of benchmarks may pose societal risks and caution that optimizing solely for benchmarks may produce models that perform poorly in real-world applications.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Authors report that manual review of Test and Validation subsets did not identify personally identifiable information or offensive content.

**Data Licensing**: Dataset released under a CC-BY-ND license. Evaluation code and prompts released under the MIT license (via EleutherAI's LM-Eval-Harness).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
