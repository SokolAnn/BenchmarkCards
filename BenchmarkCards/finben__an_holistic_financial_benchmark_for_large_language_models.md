# FinBen: An Holistic Financial Benchmark for Large Language Models

## 📊 Benchmark Details

**Name**: FinBen: An Holistic Financial Benchmark for Large Language Models

**Overview**: FinBen is the first extensive open-source evaluation benchmark for LLMs in the financial domain, including 36 datasets spanning 24 financial tasks and covering seven aspects: information extraction (IE), textual analysis (TA), question answering (QA), text generation (TG), risk management (RM), forecasting (FO), and decision-making (DM). FinBen introduces agent-based and Retrieval-Augmented Generation (RAG) evaluation, and three novel open-source datasets for text summarization, question answering, and stock trading.

**Data Type**: question-answering pairs; text summarization; text classification; time-series (historical stock prices); multimodal (news text + time-series)

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- PIXIU
- FinanceBench
- BizBench
- CFBenchmark
- Fin-Eva

**Resources**:
- [GitHub Repository](https://github.com/The-FinAI/PIXIU)
- [Resource](https://arxiv.org/abs/2402.12659)
- [Resource](https://sites.google.com/nlg.csie.ntu.edu.tw/finnlp-agentscen)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive open-source evaluation benchmark for LLMs in the financial domain, comprising 36 datasets across 24 tasks to assess LLM performance across seven aspects: information extraction, textual analysis, question answering, text generation, risk management, forecasting, and decision-making.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners
- Financial Domain Experts

**Tasks**:
- Named Entity Recognition
- Relation Extraction
- Causal Classification
- Causal Detection
- Numeric Labeling
- Textual Analogy Parsing
- Sentiment Analysis
- News Headline Classification
- Argument Unit Classification
- Argument Relation Detection
- Multi-class Classification
- Deal Completeness Classification
- ESG Issue Identification
- Question Answering
- Long-form Question Answering
- Multi-turn Question Answering
- Text Summarization
- Stock Movement Prediction
- Credit Scoring
- Fraud Detection
- Financial Distress Identification
- Claim Analysis
- Stock Trading (Agent-based Decision-Making)

**Limitations**: Limited dataset sizes for some tasks; computational constraints limited evaluation (e.g., constrained to LLaMA 70B in some evaluations); tasks are based on American market data and English texts which may limit global applicability; potential misuse such as financial misinformation or unethical market influence.

**Out of Scope Uses**:
- Not to be used as financial, legal, or investment advice

## 💾 Data

**Source**: Three primary sources: 1) open-sourced datasets from existing studies transformed into instruction-response pairs; 2) datasets from existing evaluation benchmarks (e.g., PIXIU) already transformed into instruction tuning format; 3) novel datasets introduced in this paper (EDTSum, FinTrade, Regulations).

**Size**: 36 datasets in total spanning 24 tasks. Examples: EDTSum: 2,000 news; FinTrade: 3,384 examples (stock trading); Regulations: 254 examples (long-form QA). Test set sizes for each dataset are provided in Table 2 of the paper.

**Format**: Instruction-response pairs (evaluation uses test splits); datasets originate from various source formats and have been transformed into an instruction tuning / evaluation format for zero-shot evaluation.

**Annotation**: Combination of dataset-specific annotations from source datasets and manual curation: EDTSum headlines were manually selected and cleaned; Regulations maps queries to relevant regulatory articles; other datasets retain original annotations from their sources. All datasets transformed into instruction-response format for evaluation.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Few-shot results (reported from previous papers)
- Agent-based evaluation
- Retrieval-Augmented Generation (RAG) evaluation
- Automated metrics (dataset-specific)

**Metrics**:
- F1 Score
- Entity F1 Score
- Exact Match Accuracy (EM Accuracy)
- Accuracy
- ROUGE (ROUGE-1, ROUGE-2, ROUGE-L)
- BERTScore
- BART Score
- Cumulative Return (CR)
- Sharpe Ratio (SR)
- Daily Volatility (DV)
- Annualized Volatility (AV)
- Maximum Drawdown (MD)
- Matthews Correlation Coefficient (MCC)
- RMSE
- Average F1

**Calculation**: Evaluations are performed on test sets; most results reported as averages over three runs. Trading performance metrics are reported with 95% confidence intervals. Dataset-specific metric calculations follow standard definitions (e.g., F1, ROUGE, BERTScore, MCC) as indicated in Table 2.

**Interpretation**: Higher values of F1, Entity F1, Accuracy, ROUGE, BERTScore, and BART Score indicate better performance on NLP tasks. For forecasting and trading, higher Cumulative Return and Sharpe Ratio and lower Daily/Annualized Volatility and Maximum Drawdown indicate better performance. Lower RMSE indicates better performance where applicable.

**Baseline Results**: Baseline evaluations include 15 representative LLMs (e.g., GPT-4, ChatGPT, Gemini, LLaMA2, LLaMA3, FinMA-7B, FinGPT). Examples of reported results: GPT-4 NER EntityF1 0.83 (Table 3), GPT-4 FinQA EMAcc 0.63 (Table 3), GPT-4 trading performance Cumulative Return 28.19% ±25.27 and Sharpe Ratio 1.51 ±1.08 (Table 4). Detailed per-model per-dataset results are provided in Tables 3-5.

**Validation**: Benchmark validated via systematic evaluation of 15 LLMs and by hosting the FinLLM shared task (FinNLP-AgentScen workshop at IJCAI-2024) with participating teams. A Data Leakage Test (DLT) was proposed for the shared task to detect potential data leakage; trading metrics reported with confidence intervals; authors provide code, data, and instructions to reproduce evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Misuse
- Legal Compliance
- Accuracy
- Governance

**Atlas Risks**:
- **Misuse**: Spreading disinformation
- **Legal Compliance**: Legal accountability
- **Accuracy**: Data contamination
- **Governance**: Unrepresentative risk testing, Lack of testing diversity

**Potential Harm**: ['Financial misinformation', 'Unethical market influence']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors state that all raw data used are publicly available and do not contain personal information; efforts were made to ensure privacy and anonymization where applicable.

**Data Licensing**: Datasets compiled within FinBen are shared under the MIT license; Table 2 lists licenses for individual datasets (examples include CC BY-SA 3.0, CC BY-NC 4.0, MIT License, CC0 1.0, Public).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
