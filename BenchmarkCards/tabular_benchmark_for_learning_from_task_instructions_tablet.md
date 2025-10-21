# TAbular Benchmark for LEarning from Task instructions (TABLET)

## 📊 Benchmark Details

**Name**: TAbular Benchmark for LEarning from Task instructions (TABLET)

**Overview**: TABLET is a benchmark of 20 diverse tabular datasets annotated with instructions that vary in their phrasing, granularity, and technicality; TABLET also includes the instructions' logic and structured modifications to the instructions. It is designed to evaluate how effectively large language models (LLMs) utilize natural language instructions to perform tabular prediction tasks in zero-shot and few-shot (in-context) settings.

**Data Type**: tabular

**Domains**:
- Healthcare
- Finance
- Manufacturing
- Climate Science

**Similar Benchmarks**:
- DDXPlus
- UCI ML Repository

**Resources**:
- [Resource](https://dylanslacks.website/Tablet)
- [Resource](https://arxiv.org/abs/2304.13188)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate how effectively large language models learn from natural language instructions to perform tabular prediction tasks (in zero-shot and few-shot in-context settings) and to characterize benefits and limitations of instruction-based approaches for tabular prediction.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Tabular Prediction
- Binary Classification
- Multi-class Classification
- Differential Diagnosis

**Limitations**: LLMs often ignore instructions and fail to predict specific instances correctly; models are highly biased against classifying certain instances correctly and do not always follow instructions provided in-context, even with examples.

## 💾 Data

**Source**: 20 tasks: 10 datasets from the UCI ML Repository and 10 differential diagnosis (DDX) tasks derived from DDXPlus. Naturally occurring instructions for DDX tasks were collected from consumer sources (e.g., MedlinePlus) and a professional reference (Merck Manual). Generated instructions for UCI tasks were produced via templates derived from simple classifiers (rulesets and prototypes) and revised with GPT-3.

**Size**: 20 tasks total. DDX tasks were down-sampled to 10,000 instances per task for TABLET; datasets are split with an 80/20 train/test split. Full training sets are included in TABLET to permit comparison to fully supervised models.

**Format**: N/A

**Annotation**: Each task is annotated with instructions and prompt components per the TABLET schema. For DDX: 3 naturally occurring instructions per dataset (two consumer sources, one professional). For UCI: 10 generated instructions per dataset generated from rule-set and prototype templates and revised with GPT-3. TABLET also includes instruction logic representations and flipped (label-permuted) instruction variants.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation (instructions only)
- Few-shot evaluation (in-context examples: 0, 2, 4 shots)
- In-context learning with LLMs (Flan-T5 11b, Tk-Instruct 11b, GPT-J 6b, ChatGPT)
- Baseline comparison to LIFT (no instructions)
- Comparison to fully supervised models (XGBoost)
- Instruction faithfulness evaluation (flipped instructions)
- Statistical significance testing (Wilcoxon signed-rank test with Holm–Bonferroni correction)

**Metrics**:
- Macro averaged F1 Score

**Calculation**: Models are evaluated using macro averaged F1 score to compare across unbalanced labels. Statistical significance between conditions was tested using the Wilcoxon signed-rank test with Holm–Bonferroni correction for multiple comparisons.

**Interpretation**: Higher macro averaged F1 indicates better predictive performance on the tabular tasks. Percent lift in F1 over the LIFT (no-instruction) baseline or over fully supervised baselines indicates the benefit of instructions and few-shot examples. Instruction faithfulness is measured by how predictions change under flipped instruction variants.

**Baseline Results**: Examples reported in the paper: zero-shot Flan-T5 11b with naturally occurring instructions outperforms LIFT by 20% average F1 (ChatGPT outperforms LIFT by 10% zero-shot). With 4 in-context examples, Flan-T5 11b improves on average 44% over the baseline and ChatGPT improves 13%. Fully supervised XGBoost on all training data scores 0.94 F1 on average on the DDX tasks; ChatGPT 4-shot scores 0.68 F1 and Flan-T5 11b 4-shot scores 0.66 F1. XGBoost with only 4-shot examples scores 0.38 F1.

**Validation**: Used multiple seeds and sampling (e.g., 30 random seeds for instance-level analyses), down-sampling and rebalancing for DDX tasks, and statistical significance testing (Wilcoxon signed-rank test with Holm–Bonferroni correction). Few-shot evaluations included repeated sampling and KNN-based selection experiments to estimate upper bounds.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Data Laws**: Data transfer restrictions
- **Fairness**: Output bias
- **Value Alignment**: Over- or under-reliance
- **Accuracy**: Poor model accuracy

**Potential Harm**: Reduce reliance on costly data collection and mitigate barriers to model development caused by privacy-sensitive data sharing restrictions in domains such as medicine and finance.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
