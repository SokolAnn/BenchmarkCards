# FLARE (Financial Language Understanding And PRediction Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: FLARE (Financial Language Understanding And PRediction Evaluation Benchmark)

**Overview**: A standardized evaluation benchmark for financial LLMs covering financial natural language understanding and prediction tasks. FLARE covers 4 financial NLP tasks with 6 datasets and 1 financial prediction task with 3 datasets (test and validation splits per dataset are provided in Table 4).

**Data Type**: multimodal (text, tables, time-series)

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FLUE
- BBT-CFLEB

**Resources**:
- [GitHub Repository](https://github.com/chancefocus/PIXIU)
- [Resource](https://arxiv.org/abs/2306.05443)

## 🎯 Purpose and Intended Users

**Goal**: Provide a standardized evaluation benchmark for financial LLMs covering financial natural language understanding and prediction tasks.

**Target Audience**:
- ML Researchers
- Model Developers
- Financial Researchers
- Industry Practitioners

**Tasks**:
- Financial Sentiment Analysis
- News Headline Classification
- Named Entity Recognition
- Question Answering
- Stock Movement Prediction

**Limitations**: 1. Model and Training Constraints: only present FinMA models up to 30B; FinMA-30B has not been fine-tuned on the full dataset. 2. Complex Task Performance: FinMA struggles with tasks requiring quantitative reasoning (e.g., financial question answering) due to limitations of the LLaMA backbone. 3. Resource Constraints and Generalizability: development is influenced by available resources and handcrafted instructions, potentially affecting model diversity and generalizability. 4. Potential Negative Impacts: possible spread of financial misinformation or unethical market influence.

## 💾 Data

**Source**: Assembled from open-sourced datasets: Financial Phrase Bank (FPB), FiQA-SA, Headline (Gold news headline), FIN (NER), FinQA, ConvFinQA, BigData22, ACL18, CIKM18. Instruction tuning data (FIT) is created by converting these datasets into instruction-response samples using domain-expert written instructions.

**Size**: 136,609 examples (FIT instruction tuning data)

**Format**: N/A

**Annotation**: Original datasets annotated by domain experts (where applicable); instruction templates and instructions written by domain experts to convert raw dataset samples into instruction-response pairs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Zero-shot evaluation
- Few-shot evaluation (5-shot or 20-shot for some models)
- Human evaluation (for some baseline results)

**Metrics**:
- Accuracy
- F1 Score
- Average F1 Score (weighted over categories)
- Entity F1 Score
- Exact Match Accuracy
- Matthews correlation coefficient (MCC)

**Calculation**: Sentiment classification (FPB, FiQA-SA): Accuracy and weighted F1 Score. News headline classification: weighted average F1 over nine categories (Avg F1). NER: entity-level F1 score (Entity F1). Question Answering (FinQA, ConvFinQA): Exact Match Accuracy (EM Acc). Stock movement prediction (BigData22, ACL18, CIKM18): Accuracy and Matthews correlation coefficient (MCC).

**Interpretation**: Higher metric values indicate better performance on the corresponding task/metric. No absolute thresholds for 'good' vs 'poor' performance are provided in the paper; relative comparisons across models are used.

**Baseline Results**: Table 5 reports baseline results for multiple models (GPT-NeoX, OPT-66B, BLOOM, ChatGPT, GPT-4, BloombergGPT, FinMA variants). Examples: FPB - FinMA-30B Accuracy 0.87, F1 0.88; FiQA-SA - FinMA-30B F1 0.87; Headline - FinMA variants Avg F1 ~0.97; FinQA - GPT-4 EM Acc 0.63 vs FinMA-30B EM Acc 0.11; ConvFinQA - GPT-4 EM Acc 0.76, FinMA-30B EM Acc 0.40. (See Table 5 in paper for full per-model, per-dataset numbers.)

**Validation**: Validation sets are randomly selected from FIT and used to select the best model checkpoint (validation splits per dataset are provided in Table 4).

## ⚠️ Targeted Risks

**Risk Categories**:
- Misuse
- Societal Impact
- Governance
- Accuracy

**Atlas Risks**:
- **Misuse**: Spreading disinformation
- **Societal Impact**: Impact on affected communities
- **Governance**: Lack of testing diversity
- **Accuracy**: Poor model accuracy

**Potential Harm**: ['Spread of financial misinformation', 'Unethical market influence']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Per Table 2: FPB: CC BY-SA 3.0; FiQA-SA: Public; Headline: CC BY-SA 3.0; NER: CC BY-SA 3.0; FinQA: MIT License; ConvFinQA: MIT License; BigData22: Public; ACL18: MIT License; CIKM18: Public.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
