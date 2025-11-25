# STructured REasoning and Explanation Multi-Task benchmark (STREET)

## 📊 Benchmark Details

**Name**: STructured REasoning and Explanation Multi-Task benchmark (STREET)

**Overview**: We introduce STREET, a unified multi-task and multi-domain natural language reasoning and explanation benchmark. Unlike most existing question-answering (QA) datasets, we expect models to not only answer questions, but also produce step-by-step structured explanations (reasoning graphs) describing how premises in the question are used to produce intermediate conclusions that can prove the correctness of a certain answer.

**Data Type**: question-answering pairs with associated structured reasoning graphs (reasoning steps / textual entailments)

**Domains**:
- Natural Language Processing
- Mathematics
- Analytical Reasoning
- Deductive Reasoning
- Science

**Similar Benchmarks**:
- Entailment Trees
- Entailment Bank
- GLUE
- SUPER-GLUE
- Massive Multitask Language Understanding (MMLU)
- BIG-Bench
- CLUTRR
- RuleTaker

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Provide a multi-task and multi-domain benchmark to evaluate models on multi-step reasoning and generation of structured explanations (reasoning graphs) in the context of question answering.

**Target Audience**:
- Research community

**Tasks**:
- Question Answering
- Reasoning Graph Generation
- State Prediction

**Limitations**: The benchmark focuses on problems where most relevant knowledge is contained within the question/context/answers and does not address retrieval of external premises. Not all questions from original datasets were used due to annotation cost.

**Out of Scope Uses**:
- Retrieval of premises is out of the scope of this work
- Datasets that require external domain knowledge were disregarded

## 💾 Data

**Source**: Built upon existing QA datasets: AI2 Reasoning Challenge (ARC) with Entailment Bank premises, SCONE, GSM8K, AQUA-RAT, and AR-LSAT. Reasoning graphs were created either programmatically, taken from existing annotations (Entailment Bank), or annotated by expert annotators.

**Size**: 35,800 questions; 151,100 reasoning steps total; 14,730 reasoning steps annotated by expert annotators

**Format**: N/A

**Annotation**: Manual annotation by expert annotators (undergraduate or graduate level) for GSM8K, AQUA-RAT, and AR-LSAT with two passes and a third pass to break ties; Fleiss Kappa κ = 0.79 reported. For SCONE, reasoning steps extracted programmatically. ARC uses gold premises from Entailment Bank.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Model-based evaluation (fine-tuned T5, few-shot GPT-3)

**Metrics**:
- Answer Accuracy (Exact Match)
- Reasoning Graph Accuracy
- Reasoning Graph Similarity (normalized graph edit distance)

**Calculation**: Answer Accuracy: exact match for multiple-choice or numerical answers (state prediction uses combined state). Reasoning Graph Accuracy: align predicted and gold graphs via premises and topological ordering, then test matched reasoning step nodes with task-specific textual similarity functions. Reasoning Graph Similarity: compute (approximate) graph edit distance using insertion/deletion/substitution costs (cost 1 per edit), use text similarity for node matching; normalized sim(Gp,Gg)=1 - edit_cost / max(|Np|+|Ep|,|Ng|+|Eg|). If generated answer is incorrect, similarity is set to 0. Approximations use networkx implementation.

**Interpretation**: Answer Accuracy is an upper bound for graph metrics (incorrect answer makes graph metrics incorrect). Reasoning Graph Accuracy is a strict metric (small deviations from gold graph render prediction incorrect). Reasoning Graph Similarity is normalized to [0,1], with 0 if the answer is incorrect.

**Baseline Results**: Main test results (percentages) from Table 2: Answer Accuracy — T5-large (fine-tuned): ARC 93.5, SCONE 69.6, GSM8K 10.4, AQUA-RAT 28.7, AR-LSAT 28.0. GPT-3 (davinci, few-shot): ARC 72.9, SCONE 2.3, GSM8K 34.8, AQUA-RAT 40.2, AR-LSAT 19.0. Reasoning Graph Accuracy — T5-large: ARC 17.1, SCONE 60.0, GSM8K 0.7, AQUA-RAT 0.0, AR-LSAT 0.0. GPT-3 (davinci): ARC 1.7, SCONE 1.2, GSM8K 0.7, AQUA-RAT 0.0, AR-LSAT 0.0. Graph Similarity — T5-large: ARC 44.1, SCONE 67.0, GSM8K 5.4, AQUA-RAT 0.9, AR-LSAT 0.3. GPT-3 (davinci): ARC 15.1, SCONE 1.9, GSM8K 16.0, AQUA-RAT 5.2, AR-LSAT 1.1.

**Validation**: Annotation quality measured via Fleiss Kappa κ = 0.79 (two annotation passes with third pass to break ties). Human performance estimated by asking expert annotators to author reasoning graphs for 100 randomly selected test questions across tasks.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
