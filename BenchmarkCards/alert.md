# ALERT

## 📊 Benchmark Details

**Name**: ALERT

**Overview**: ALERT, a benchmark and suite of analyses for evaluating reasoning skills of language models. ALERT enables comparing pre-trained and finetuned models on complex tasks that require reasoning skills to solve them. The benchmark provides a test bed to assess any language model on fine-grained reasoning skills, spanning over 20 datasets and covering 10 different reasoning skills.

**Data Type**: text (question-answering pairs and generation tasks)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- Natural Instruction V2 (NIV2)
- BIG-Bench
- MMLU
- Curriculum benchmark

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark different large language models on various fine-grained reasoning skills and provide analyses to assess reasoning abilities, the role of finetuning, data memorization, reasoning skill transfer, and prompt template memorization.

**Tasks**:
- Question Answering
- Text Generation
- Text Classification
- Textual Entailment

**Limitations**: Missing some reasoning skills such as symbolic reasoning and compositionality reasoning. Limited compute prevented training larger models. Some datasets contain noise where even human experts are unable to provide accurate answers for certain instances.

## 💾 Data

**Source**: Selected tasks from Natural Instruction V2 (NIV2) and public datasets; ALERT is constructed from over 20 datasets covering 10 reasoning skills (detailed in Table 4).

**Size**: 20 datasets (individual dataset sizes vary); total aggregated size not provided

**Format**: Various formats as provided by original datasets (examples include CSV and JSONL)

**Annotation**: Reasoning-skill labels were manually checked and corrected; for each task only the predominant reasoning skill label is retained.

## 🔬 Methodology

**Methods**:
- Prompt-based evaluation (zero-shot, few-shot, chain-of-thought)
- Automated metrics (ROUGE-L, Exact Match, Relaxed Match)
- Reasoning-chain evaluation using ROSCOE suite
- Model comparison (pretrained OPT vs meta-finetuned OPT-FT vs CoT-finetuned OPT-CoT)
- Template-variation evaluation (five prompt templates; report average and max across templates)

**Metrics**:
- ROUGE-L
- Exact Match
- Relaxed Match (normalize to lowercase, remove punctuation and extra whitespace)
- ROSCOE suite (e.g., Faithfulness-Step, Faithfulness-Token, Info-Step, Repetition-Token, Info-Chain, Repetition-Step, Source Consistency, Self-Consistency, Perplexity-Step, Perplexity-Chain, Grammar)

**Calculation**: Classification tasks are treated as generation by appending choices to prompts. For each dataset, scores are reported as the average and max among five templates; aggregated results are averages across datasets. Relaxed-match normalizes predictions and references to lowercase and removes punctuation and extra whitespace.

**Interpretation**: Default score refers to the aggregated max score among the five templates. Exact Match is sensitive to format adherence; Relaxed Match reduces sensitivity to formatting differences. ROSCOE metrics evaluate chain quality across multiple perspectives (faithfulness, similarity, logical inference, language coherence).

**Baseline Results**: Rationale-based finetuning (OPT-CoT) improves 1.3B model by 3.89% aggregated max ROUGE-L and 3.83% aggregated max Exact Match; for 13B, OPT-CoT improves by 15.22% aggregated max ROUGE-L and 12.64% aggregated max Exact Match. OPT-FT sometimes yields worse results than pretrained OPT. ROSCOE averaged metrics are reported in Table 10 (examples: ROSCOE- SA Faithfulness-Token: OPT-13B=0.936, OPT-FT-13B=0.923, OPT-CoT-13B=0.940).

**Validation**: Checkpoint selection uses a development set compiled from NIV2 tasks that do not overlap with finetuning or evaluation data (dev datasets: task 247 Dream, task 118 SemEval, task 10 open-vocabulary math, and anli r1 entailment).

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Value Alignment
- Fairness

**Atlas Risks**:
- **Multi-category**: Prompt priming
- **Accuracy**: Unrepresentative data
- **Value Alignment**: Toxic output
- **Fairness**: Data bias

**Potential Harm**: ['Generation of toxic and unwanted content', 'Reduced robustness to different prompt templates leading to poor generalization']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Various dataset licenses are used across ALERT datasets and are listed in Appendix D, including but not limited to MIT, Apache 2.0, CC BY-NC 4.0, CC BY-SA 3.0, CC BY 4.0, CC BY-NC-3.0, AFL 3.0, BSD-3-Clause. Refer to Appendix D for per-dataset licensing details.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
