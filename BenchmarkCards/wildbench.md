# WildBench

## 📊 Benchmark Details

**Name**: WildBench

**Overview**: WildBench is an automated evaluation framework designed to benchmark large language models (LLMs) using challenging, real-world user queries, consisting of 1,024 examples curated from human-chatbot conversation logs.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- AlpacaEval
- ArenaHard

**Resources**:
- [Resource](https://hf.co/spaces/allenai/WildBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a realistic, dynamic, contamination-resilient evaluation framework that accurately reflects the capabilities of LLMs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Coding & Debugging
- Creative Writing
- Data Analysis
- Information Seeking
- Reasoning
- Planning
- Editing

**Limitations**: N/A

## 💾 Data

**Source**: Sourced from the WildChat dataset, which includes one million human-chatbot conversations.

**Size**: 1,024 examples

**Format**: N/A

**Annotation**: Curated through a multi-step process including manual review and difficulty annotation by multiple LLMs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- WB-Score
- WB-Reward

**Calculation**: WB-Score evaluates each model's output individually and WB-Reward uses pairwise comparisons between model outputs.

**Interpretation**: Scores closer to 10 indicate a better performance, while scores below 5 indicate various levels of issues with the response.

**Baseline Results**: Three baseline models (GPT-4-Turbo, Claude-3-Haiku, Llama-2-70B-chat) are used for comprehensive evaluation.

**Validation**: The evaluation process includes structured checklists to ensure consistent and reliable judgments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released under AI2’s ImpACT license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
