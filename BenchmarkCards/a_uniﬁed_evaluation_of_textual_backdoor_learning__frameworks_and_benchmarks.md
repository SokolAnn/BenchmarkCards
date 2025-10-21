# A Uniﬁed Evaluation of Textual Backdoor Learning: Frameworks and Benchmarks

## 📊 Benchmark Details

**Name**: A Uniﬁed Evaluation of Textual Backdoor Learning: Frameworks and Benchmarks

**Overview**: Textual backdoor attacks are a kind of practical threat to NLP systems. The paper (1) categorizes existing works into three practical release scenarios (released datasets, pre-trained models, fine-tuned models) and proposes scenario-specific evaluation methodologies; (2) extends evaluation metrics beyond effectiveness (ASR and CACC) to include stealthiness (perplexity difference and grammar error increase) and validity (sentence similarity using USE); and (3) develops an open-source toolkit OpenBackdoor to implement, reproduce, and benchmark attack and defense methods and performs extensive benchmark experiments under the proposed frameworks.

**Data Type**: text (poisoned and clean training and test text samples)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TrojanZoo
- Back-doorBox
- BackdoorBench

**Resources**:
- [GitHub Repository](https://github.com/thunlp/OpenBackdoor)
- [Resource](https://openbackdoor.readthedocs.io/)
- [Resource](https://arxiv.org/abs/2206.08514)

## 🎯 Purpose and Intended Users

**Goal**: To unify and formalize rigorous evaluation frameworks for textual backdoor learning across realistic release scenarios, introduce additional metrics for stealthiness and validity of poisoned samples, provide a standardized toolkit (OpenBackdoor) for implementing and reproducing attacks and defenses, and perform comprehensive benchmark experiments to evaluate attack and defense methods.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Poisoned Sample Detection

**Limitations**: The paper notes limitations including (a) evaluation metrics are not complete (perplexity and grammar error are not exhaustive measures of stealthiness); (b) validity is hard to measure and USE is not sufficient; and (c) experiments simulate practical scenarios in lab settings without full real deployment and industrial concerns (Appendix E).

## 💾 Data

**Source**: Datasets used in benchmark experiments: SST-2, IMDB, HSOL, OffensEval, LingSpam, AG's News; plus plain (unlabelled) text corpora used for pre-trained-model poisoning scenarios. All these datasets are available in OpenBackdoor.

**Size**: Per Table 3: SST-2: 6,920 train, 872 dev, 1,821 test examples; IMDB: 22,500 train, 2,500 dev, 25,000 test examples; HSOL: 5,823 train, 2,485 dev, 2,485 test examples; OffensEval: 11,915 train, 1,323 dev, 859 test examples; LingSpam: 2,604 train, 289 dev, 580 test examples; AG's News: 108,000 train, 12,000 dev, 7,600 test examples.

**Format**: N/A

**Annotation**: Existing dataset labels provided by the original datasets (classification labels as listed in Table 3).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Toolkit-based benchmarking using OpenBackdoor
- Scenario-specified evaluations (Dataset release, Pre-trained model release, Fine-tuned model release)
- Clustering-based training-time defense evaluation (CUBE)
- Detection evaluation using False Acceptance Rate (FAR) and False Rejection Rate (FRR)

**Metrics**:
- Attack Success Rate (ASR)
- Clean Accuracy (CACC)
- Perplexity (PPL) / Perplexity difference (ΔPPL)
- Grammar Error (GE) / Grammar error increase (ΔGE)
- Universal Sentence Encoder similarity (USE)
- False Acceptance Rate (FAR)
- False Rejection Rate (FRR)
- F1 Score

**Calculation**: Effectiveness: ASR and CACC as in prior works. Stealthiness: average perplexity increase (ΔPPL) computed by a pre-trained language model (e.g., GPT-2) and grammar error increase (ΔGE) measured by grammar-checking tools. Validity: semantic similarity between clean and poisoned samples computed using the Universal Sentence Encoder (USE). Detection metrics: FAR and FRR computed by mixing poisoned and clean samples and measuring misclassification rates as described in §6.3. Many experiments report averages over 5 runs; dataset poisoning rates are varied (e.g., {0, 0.01, 0.05, 0.1, 0.2}) and label-consistency settings are controlled.

**Interpretation**: High ASR with preserved CACC indicates effective attacks. Low ΔPPL and low ΔGE indicate higher stealthiness. High USE similarity indicates semantic-preserving (valid) poisoned samples. Detection performance is interpreted via FAR and FRR (lower is better). Scenario-specific behaviors (e.g., transferability across tasks, effects of fine-tuning on large datasets) are used to interpret practical threat levels.

**Baseline Results**: OpenBackdoor reproduces 12 attack methods and 5 defense methods and reports comprehensive results across scenarios; results are presented in Tables 4-11 (examples include per-attacker stealthiness and validity in Table 4, poisoned pre-trained model results in Table 5, and defense results including CUBE in Table 9).

**Validation**: Benchmarks validated by averaging results over 5 runs for many experiments, evaluating across multiple poison rates and label-consistency settings, testing transferability across multiple downstream datasets, and measuring detection metrics (FAR/FRR) for inference-time defenses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Security

**Atlas Risks**:
- **Robustness**: Data poisoning
- **Governance**: Unrepresentative risk testing, Incomplete usage definition

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
