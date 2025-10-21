# STEPS: A Benchmark for Order Reasoning in Sequential Tasks

## 📊 Benchmark Details

**Name**: STEPS: A Benchmark for Order Reasoning in Sequential Tasks

**Overview**: To verify the order reasoning capability of current neural models in sequential tasks, we propose a challenging benchmark, named STEPS. STEPS involves two subtask settings: (1) a classification setting that determines the rationality of a given next step in recipes given previous steps, and (2) a multi-choice setting that selects the reasonable next step from two candidate steps. The paper describes data construction, task formulations, and benchmarks of several large language models.

**Data Type**: text (previous steps and candidate next-step pairs for classification; previous steps with two candidate next-step options for multi-choice)

**Domains**:
- Natural Language Processing
- Robotics

**Similar Benchmarks**:
- Piqa
- Commonsenseqa
- Lila

**Resources**:
- [GitHub Repository](https://github.com/Victorwz/STEPS)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate the action order (sequence order) commonsense reasoning capability of language models on sequential tasks (recipes) via two subtasks: next-step rationality classification and multi-choice next-step selection.

**Tasks**:
- Text Classification
- Multiple-Choice Question Answering
- Commonsense Reasoning (Order reasoning)

**Limitations**: Recipes with fewer than four action steps or more than ten action steps were filtered out due to input context length limitations of language models.

## 💾 Data

**Source**: FOOD.COM RECIPES dataset (web-crawled recipes from 'food.com' collected and released by Majumder et al., 2019). The STEPS datasets are constructed from these recipes using the original train/dev/test splits.

**Size**: STEPS-CLS: 2.68M train examples, 1,000 dev examples, 1,000 test examples; STEPS-MC: 298K train examples, 1,000 dev examples, 1,000 test examples.

**Format**: N/A

**Annotation**: Automatically constructed from recipe step sequences: for classification, true samples are (previous steps, ground-truth next step) and false samples are (previous steps, later steps); for multi-choice each sample is (previous steps, true next step, randomly selected later step).

## 🔬 Methodology

**Methods**:
- Zero-shot prompting
- One-shot prompting
- Few-shot in-context learning (K=4 demonstrations; evaluation averaged over six random seeds)
- Full fine-tuning of models
- Perplexity-based scoring for multi-choice (language modeling scorer)

**Metrics**:
- Accuracy
- Sensitivity
- Specificity
- Geometric Mean (G-Mean) of Sensitivity and Specificity
- Perplexity (used as scorer for multi-choice)

**Calculation**: For classification: Sensitivity = class-wise accuracy on positive class; Specificity = class-wise accuracy on negative class; G-Mean = geometric mean(Sensitivity, Specificity). For multi-choice: compute language modeling perplexity PPL(q) for each (previous steps + option) query and select the option with lower PPL; report Accuracy.

**Interpretation**: Higher Accuracy, Sensitivity, Specificity, and G-Mean indicate better order reasoning capability. Authors note that LLM performance on these tasks lies in the 70%-80% accuracy range, which may indicate a potential performance upper-bound for pre-trained LLMs without additional knowledge sources.

**Baseline Results**: Multi-Choice Accuracy (selected baselines): GPT2-Small 59.3; GPT2-Medium 63.5; GPT2-Large 65.1; OPT-1.3B 66.0; GPT2-XL 65.4; BLOOM-3B 68.4; BLOOM-7b1 69.8; OPT-13B 71.3; OPT-30B 71.7. Classification: in zero-shot many GPT-2 models predicted the positive class for all test samples (perfect Sensitivity but near-zero Specificity); fine-tuning improved Specificity substantially (e.g., authors report a 73% Specificity increase for GPT2-Large compared with zero-shot).

**Validation**: Kept original train/dev/test splits from the source recipes. Filtered recipes with fewer than four or more than ten steps. For few-shot ICL, evaluation averaged over six random seeds for demonstration selection. For fine-tuning: up-sampling positive samples to balance classes, truncate resampled training set into segments of length 1024 tokens, fine-tune for 6000 updates with batch size 8, validate every 300 updates and save checkpoint with best validation performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
