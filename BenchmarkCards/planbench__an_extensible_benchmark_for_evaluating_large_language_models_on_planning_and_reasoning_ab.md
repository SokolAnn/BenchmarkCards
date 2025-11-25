# PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change

## 📊 Benchmark Details

**Name**: PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change

**Overview**: PlanBench is an extensible benchmark suite based on domains used in the automated planning community (especially International Planning Competition domains) to test the capabilities of large language models (LLMs) in planning and reasoning about actions and change. The benchmark provides diversity in task domains and specific planning capabilities, includes obfuscated domain versions, and is initialized with two IPC domains (Blocksworld and Logistics). The dataset contains approximately 26,250 prompts and the authors provide tools and scripts to reproduce prompts and results.

**Data Type**: text (natural language planning/problem prompts and plan descriptions)

**Domains**:
- Natural Language Processing
- Automated Planning

**Languages**:
- English

**Similar Benchmarks**:
- BIG-BENCH
- GSM8K
- AQUA
- SVAMP
- CommonsenseQA
- StrategyQA

**Resources**:
- [GitHub Repository](https://github.com/karthikv792/LLMs-Planning)
- [Resource](https://arxiv.org/abs/2206.10498)

## 🎯 Purpose and Intended Users

**Goal**: Establish an extensible assessment framework and benchmark to evaluate planning and reasoning-about-change capabilities of large language models using planning domains and mechanistic automated generation and validation of prompts.

**Target Audience**:
- Researchers

**Tasks**:
- Plan Generation
- Cost Optimal Planning
- Plan Verification
- Reasoning about Plan Execution
- Robustness to Goal Reformulation
- Ability to Reuse Plans
- Replanning
- Plan Generalization

**Limitations**: Current version initialized with two IPC domains (Blocksworld and Logistics); evaluation metrics do not incorporate partial-correctness metrics (authors note such metrics could be incorporated in future). The authors explicitly state there is no guarantee that deploying models for external planning, based solely on their performance on this benchmark, will result in correct or safe plans.

**Out of Scope Uses**:
- Using PlanBench performance alone as justification to deploy models for external planning or safety-critical planning tasks (the paper states this may not result in correct or safe plans).

## 💾 Data

**Source**: Auto-generated from PDDL-based IPC domains (Blocksworld and Logistics) using a problem generator, translators (PDDL <-> natural language), a domain-independent planner and a plan validator; includes obfuscated versions of domains (misleading words or random alphanumeric strings). Blocksworld initialized with 600 instances (+ 500 additional plan-generalization instances); Logistics initialized with 285 instances.

**Size**: 26,250 prompts (approximate total across test cases and domains, including obfuscated versions); 600 Blocksworld instances; 500 Blocksworld plan-generalization instances; 285 Logistics instances.

**Format**: Natural language text (templated prompts and plan strings); scripts and tools provided to generate prompts and parse LLM outputs.

**Annotation**: Automatically generated ground-truth plans and labels using an automated planner and validated using a plan validator (authors used Fast-Downward planner and VAL plan validator as stated in the paper).

## 🔬 Methodology

**Methods**:
- Automated plan generation and validation using a domain-independent planner and plan validator
- Few-shot prompting (examples + target instance) to LLMs
- Model-based evaluation using LLMs accessed via OpenAI API (evaluated Instruct-GPT3 and GPT-4 as specimen baselines)

**Metrics**:
- Accuracy (instances correct / total instances)
- Plan validity (as determined by plan validator)
- Plan optimality (cost) for Cost Optimal Planning

**Calculation**: For plan-related tasks, LLM-generated plans are parsed and validated by an automated plan validator; an instance is marked correct if the generated plan is valid. For Cost Optimal Planning, the plan's cost is computed and compared to the optimal plan cost; correctness requires both validity and matching optimal cost. For verification and reasoning tasks, LLM outputs are compared against expected validation results or resulting states produced by plan executor/validator.

**Interpretation**: Higher percentages of correct instances indicate better planning and reasoning capability on the tested facets. Cost-Optimal Planning requires matching optimal cost in addition to validity. The authors interpret low accuracy on many tasks as evidence that current LLMs fall short on planning and reasoning-about-change capabilities; PlanBench is intended as a marker of progress.

**Baseline Results**: Specimen evaluation (Table 1) using Blocksworld domain: Plan Generation: GPT-4 206/600 (34.3%), Instruct-GPT3 41/600 (6.8%). Cost-Optimal Planning: GPT-4 198/600 (33%), Instruct-GPT3 35/600 (5.8%). Plan Verification: GPT-4 352/600 (58.6%), Instruct-GPT3 72/600 (12%). Reasoning About Plan Execution: GPT-4 191/600 (31.8%), Instruct-GPT3 4/600 (0.6%). Replanning: GPT-4 289/600 (48.1%), Instruct-GPT3 40/600 (6.6%). Plan Generalization: GPT-4 141/500 (28.2%), Instruct-GPT3 49/500 (9.8%). Plan Reuse: GPT-4 392/600 (65.3%), Instruct-GPT3 102/600 (17%). Robustness to Goal Reformulation (Shuffling goal predicates): GPT-4 461/600 (76.8%), Instruct-GPT3 467/600 (77.8%). Robustness (Full→Partial): GPT-4 522/600 (87%), Instruct-GPT3 467/600 (77.8%). Robustness (Partial→Full): GPT-4 348/600 (58%), Instruct-GPT3 363/600 (60.5%).

**Validation**: Automatic validation using a domain-independent planner (Fast-Downward) to generate/verify ground-truth and VAL plan validator to validate LLM outputs; authors also used domain-model relaxations (delete-relaxation and precondition-relaxation) for failure-mode analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Value Alignment

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack
- **Value Alignment**: Over- or under-reliance

**Demographic Analysis**: N/A

**Potential Harm**: Using model performance on PlanBench alone to deploy LLMs for external planning could lead to incorrect or unsafe plans.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: PlanBench does not contain any personally-identifiable or privacy-related information (as stated in the paper).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
