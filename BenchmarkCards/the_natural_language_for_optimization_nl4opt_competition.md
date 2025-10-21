# The Natural Language for Optimization (NL4Opt) Competition

## 📊 Benchmark Details

**Name**: The Natural Language for Optimization (NL4Opt) Competition

**Overview**: The Natural Language for Optimization (NL4Opt) Competition was created to investigate methods of extracting the meaning and formulation of an optimization problem based on its text description. Specifically, the goal of the competition is to increase the accessibility and usability of optimization solvers by allowing non-experts to interface with them using natural language. We separate this challenging goal into two sub-tasks: (1) recognize and label the semantic entities that correspond to the components of the optimization problem; (2) generate a meaning representation (i.e. a logical form) of the problem from its detected problem entities.

**Data Type**: text (linear programming word problem descriptions; entity span annotations; canonical meaning/ formulation representations)

**Domains**:
- Sales
- Advertising
- Investment
- Production
- Transportation
- Sciences

**Similar Benchmarks**:
- MeasEval
- MultiCoNER
- NL2Bash
- MAWPS

**Resources**:
- [Resource](https://nl4opt.github.io/)
- [GitHub Repository](https://github.com/nl4opt/nl4opt-competition)
- [GitHub Repository](https://github.com/nl4opt/nl4opt-subtask1-baseline)
- [GitHub Repository](https://github.com/nl4opt/nl4opt-subtask2-baseline)

## 🎯 Purpose and Intended Users

**Goal**: To investigate methods of converting a natural language description of an optimization problem into a mathematical formulation and to increase the accessibility and usability of optimization solvers by allowing non-experts to interface with them using natural language.

**Target Audience**:
- Research community
- Competition participants
- Operations Research practitioners

**Tasks**:
- Named Entity Recognition
- Semantic Parsing (Problem Formulation Generation)

**Limitations**: The datasets used in this competition have had a lower level of complexity compared to real-world problems. Specialized knowledge is required to create the dataset, increasing the cost of dataset creation. The task is low-resource (limited number of expert-annotated examples), which constrains learning.

## 💾 Data

**Source**: 1101 annotated linear programming word problems (LPWPs) created by the competition organizers (no third-party datasets were used). Domains: sales, advertising, investment (source domains included in all splits) and production, transportation, sciences (target domains reserved for dev/test).

**Size**: 1,101 examples total; 713 training examples, 99 development examples, 289 test examples.

**Format**: NER labels provided in SpaCy format and BIO tagging format; generation annotations provided as XML-like intermediate representations / Problem Formulation dataclass; conversion and parsing scripts provided in repository.

**Annotation**: Manually annotated using the Prodigy tool by a team of 20 AI engineers and Operations Research experts; new annotations were verified and corrected by at least two experts; a preliminary NER model was used to generate suggested annotations for part of the dataset.

## 🔬 Methodology

**Methods**:
- Automated metrics (micro-averaged F1 for NER)
- Application-specific automated metric (declaration-level mapping accuracy for generation)
- Human verification for ChatGPT outputs (OR experts manually verified generated models)

**Metrics**:
- Micro-averaged F1 Score
- Declaration-level mapping Accuracy

**Calculation**: For NER: micro-averaged F1 computed as F1 = 2 * P * R / (P + R), where P and R are the average precision and average recall averaged over all entity types. For generation: declaration-level mapping accuracy defined as Acc = 1 - (sum over test problems of min(FP_i + FN_i, D_i) / sum over test problems of D_i), where for each LPWP i, D_i is the number of ground-truth declarations, FP_i is the number of non-matched predicted declarations, and FN_i is the number of ground-truth declarations without a match. Canonical representation is used to compare ground-truth and predicted formulations.

**Interpretation**: Higher micro-averaged F1 indicates better entity recognition. Higher declaration-level mapping accuracy indicates more accurate predicted formulations (closer match to ground-truth declarations). The canonical representation is used to determine matches between predicted and ground-truth declarations.

**Baseline Results**: Sub-task 1 baseline (XLM-RoBERTa-base) achieved F1 = 0.906 on the test split. Sub-task 2 baseline (BART encoder-decoder with prompt-guided generation and copy mechanism) achieved declaration-level mapping accuracy = 0.610 on the test set. Winning results: Sub-task 1 top F1 = 0.939 (Infrrd AI Lab). Sub-task 2 top accuracy = 0.899 (UIUC-NLP). ChatGPT (gpt-3.5-turbo) achieved 0.927 declaration-level accuracy on the combined task test set in post-competition experiments.

**Validation**: To ensure the development set was not used for training, organizers reviewed final submitted code and re-trained all submissions prior to announcing winners. Annotations for new problems were verified and corrected by at least two experts. A canonical representation was defined and used for comparison/scoring of generated formulations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Governance

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination
- **Governance**: Lack of model transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
