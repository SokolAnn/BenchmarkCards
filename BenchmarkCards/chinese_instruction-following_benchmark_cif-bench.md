# Chinese Instruction-Following Benchmark (CIF-Bench)

## 📊 Benchmark Details

**Name**: Chinese Instruction-Following Benchmark (CIF-Bench)

**Overview**: A novel benchmark designed to evaluate the zero-shot generalizability of large language models (LLMs) to the Chinese language. CIF-Bench comprises 150 tasks and is constructed with native-speaker annotators to test complex reasoning and Chinese cultural nuances across 20 categories. To mitigate data contamination, half of the dataset is held private and the benchmark provides diversified instruction variants and a model-based automatic evaluation pipeline.

**Data Type**: instruction-input-output triplets (text)

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- Super Natural Instructions (SNI)
- FollowBench
- CLUE
- CUGE
- C-Eval
- C-MMLU

**Resources**:
- [Resource](https://yizhilll.github.io/CIF-Bench/)
- [Resource](https://openai.com/gpt-4)
- [Resource](https://stardust.ai)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the zero-shot instruction-following generalizability of LLMs in Chinese, exposing limitations in language transfer and mitigating evaluation bias from data contamination.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Natural Language Inference
- Question Answering
- Text Summarization
- Machine Translation
- Named Entity Recognition
- Text Classification
- Creative Generation
- Code Understanding/Generation
- Commonsense Reasoning
- Reasoning
- Sentiment Analysis
- Style Transfer
- Grammar Error Correction
- Dialogue Generation
- Structured Data Reasoning
- Paraphrase

**Limitations**: Recruiting human subjects for annotation limits the reproducibility of human evaluation; there may be more suitable baseline models not used in this study; despite expert annotation and checking, there may still be offensive content in the data due to human factors.

## 💾 Data

**Source**: Constructed from 113 existing tasks (sourced from Super Natural Instructions and other work) and 37 newly designed Chinese tasks; input-output annotations produced by native Chinese speakers with assistance from the Stardust.ai annotation platform; data instances drawn from open-source datasets and newly annotated examples (full task list and sources in Appendix A.1/A.2).

**Size**: 45,000 instances (7,500 public instances; 37,500 private instances); 15,000 input-output pairs (base pairs before instruction variants)

**Format**: N/A

**Annotation**: Manual annotation by native Chinese speakers with at least undergraduate degrees via the Stardust.ai platform; a three-stage pipeline: (1) annotators produce <instruction, input, output> triplets; (2) platform specialists conduct checking using GPT-4 as auxiliary verification (samples scoring lower than 6/10 deleted) and manual inspection; (3) final inspection by four NLP researchers sampling data points; annotation pipeline cost approximately $24K.

## 🔬 Methodology

**Methods**:
- Model-based automatic evaluation using GPT-4 as an evaluator for multi-class, multi-label, and creative generation tasks
- Automated semantic-similarity evaluation using BLEURT for applicable tasks
- Human expert evaluation for verification (pairwise agreement and Cohen's kappa reported)
- Use of diversified instruction variants (five private instructions per task, one public instruction) to measure robustness

**Metrics**:
- Accuracy (for multi-class classification)
- F1 Score (for multi-label classification)
- BLEURT score (semantic similarity for relevant tasks)
- Evaluator-provided scores for creativity, fluency, instruction-following, and evaluator confidence (for creative generation)

**Calculation**: Task-level scores are computed per task by averaging model scores across the applicable data samples and instruction variants; the overall model score is the average of task-level scores. Public split uses a single instruction variant; private split uses diversified instructions. All scores naturally range from 0 to 1 or are normalized to that range.

**Interpretation**: Scores are normalized to the 0–1 range; higher scores indicate better performance. The benchmark is challenging: the best-performing model on the private split obtained 52.9% overall, with few models exceeding 50%, indicating limited generalizability in less-familiar language and unseen data instances.

**Baseline Results**: Evaluated 28 LLMs. Best private-split overall score: Baichuan2-13B-Chat — 0.529 (52.9%). Other top private-split models include Qwen-72B-Chat (0.519) and Yi-34B-Chat (0.512). Public-split top scores differ (e.g., Qwen-72B-Chat 0.589 on public split).

**Validation**: Human expert verification on sampled model outputs: average pairwise agreement 0.49; Cohen's kappa 0.3729 across 153 questions; Spearman correlation between model predictions and human evaluation r = 0.4043. Additional validation: comparison of public-split results with external leaderboards (Open LLM Leaderboard and OpenCompass) and analysis of performance shifts between public and private splits to detect data contamination; variance analysis showing diversified instructions lower score variance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy
- Value Alignment

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Transparency**: Uncertain data provenance
- **Value Alignment**: Toxic output

**Demographic Analysis**: N/A

**Potential Harm**: ['Evaluation bias from data leakage/data contamination', 'Potential presence of offensive content in annotated data']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Annotation process was anonymous; annotators could withdraw; confidentiality of annotators was maintained; data were obtained from open-source datasets or resources.

**Data Licensing**: Not Applicable

**Consent Procedures**: Annotators were asked to read task guidelines and instructions before starting and could withdraw from the task at any time.

**Compliance With Regulations**: Not Applicable
