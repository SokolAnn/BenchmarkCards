# ROBUST LR: A Diagnostic Benchmark for Evaluating Logical Robustness of Deductive Reasoners

## 📊 Benchmark Details

**Name**: ROBUST LR: A Diagnostic Benchmark for Evaluating Logical Robustness of Deductive Reasoners

**Overview**: A deductive reasoning-based diagnostic benchmark that evaluates the robustness of language models to minimal logical edits in the inputs and different logical equivalence conditions. ROBUST LR contains two evaluation sets (Logical Contrast and Logical Equivalence) that probe robustness across logical operators (conjunction, disjunction, negation) and logical equivalences.

**Data Type**: text: theory (rules and facts) and statement entailment pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RuleTaker
- ReClor
- LogiQA
- CLUTRR
- FaiRR
- RICA
- ProofWriter

**Resources**:
- [GitHub Repository](https://github.com/INK-USC/RobustLR)
- [Resource](https://arxiv.org/abs/2205.12598)

## 🎯 Purpose and Intended Users

**Goal**: To test the logical robustness of deductive reasoning models by evaluating consistency under minimal logical contrast edits and logical equivalence (paraphrase) transformations, focusing on conjunction, disjunction, and negation.

**Target Audience**:
- Machine Learning Researchers
- Model Developers

**Tasks**:
- Deductive Reasoning (theory-statement entailment)
- Natural Language Inference (3-class entailment classification: True, False, Unknown)

**Limitations**: Synthetic nature of the dataset; uses fairly simple logical rules and constructs; does not explore more complex or natural theories. (Section 9 Limitation)

## 💾 Data

**Source**: Synthetic dataset generated via templates of predicates, facts, and rules using a modified Label-Priority sampling algorithm. Training datasets provided: NOT, AND+NOT, OR+NOT, All. Evaluation sets: Logical Contrast (C-CS, D-CS, N-CS) and Logical Equivalence (C-ES, D1-ES, D2-ES).

**Size**: Training: four datasets (NOT, AND+NOT, OR+NOT, All) each with 50,000 training, 10,000 dev, 10,000 test examples. Evaluation: six subsets (C-CS, D-CS, N-CS, C-ES, D1-ES, D2-ES) each with 20,000 instances (total 120,000 evaluation instances).

**Format**: N/A

**Annotation**: Automatically generated / synthetic labels derived from the symbolic proof set of a theory (labels: True, False, Unknown) via the dataset generation procedure and sampling algorithm (no human annotation for the main dataset).

## 🔬 Methodology

**Methods**:
- Fine-tuning pre-trained language models (RoBERTa, T5 variants)
- In-context learning evaluation (GPT-3 with demonstrations)
- Automated metric evaluation (weighted-F1 score from Scikit-learn)
- Human evaluation (3 annotators labeling sampled instances for upper-bound and validation)

**Metrics**:
- Weighted-F1 score
- Fleiss' kappa (inter-annotator agreement)

**Calculation**: Weighted-F1 score from Scikit-learn computed at a theory level: use model predictions for the base theory and all its perturbations to compute F1 at the theory level, then average across all theories. Weighted-F1 modifies macro-F1 to account for label imbalance.

**Interpretation**: Higher weighted-F1 indicates greater logical robustness (consistency across logical perturbations). The authors use gap to human performance as an upper bound; lower scores indicate lack of robust logical reasoning and potential reliance on spurious correlations.

**Baseline Results**: Selected results (weighted-F1 average): From scratch: Contrast 0.14, Equivalence 0.45. RoBERTa-Large: Contrast 0.47, Equivalence 0.76. T5-Large: Contrast 0.46, Equivalence 0.89. T5-3B: Contrast 0.58, Equivalence 0.84. T5-11B (finetuned on All): Contrast 0.61, Equivalence 0.83. GPT-3 (in-context): Contrast 0.36, Equivalence 0.67. Human (3 annotators): Contrast 0.88, Equivalence 0.91. (Table 5 and related tables)

**Validation**: Human validation: 3 Computer Science graduate students annotated 30 randomly sampled theories from each test subset; inter-annotator Fleiss' kappa = 0.79. Dataset filtering and sampling checks applied to control statistical features (Appendix D); label distribution per theory controlled during sampling.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
