# Financial Language Understanding Evaluation (FLUE)

## 📊 Benchmark Details

**Name**: Financial Language Understanding Evaluation (FLUE)

**Overview**: Financial Language Understanding Evaluation (FLUE), an open-source comprehensive suite of benchmarks for the financial domain. FLUE includes new benchmarks across 5 NLP tasks in the financial domain as well as common benchmarks used in previous research.

**Data Type**: text (question-answering pairs, news headlines, sentence-level sentiment labels, token sequences for named entity recognition, structure boundary annotations)

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- GLUE (General Language Understanding Evaluation)
- FiQA
- Financial PhraseBank
- FinSBD3

**Resources**:
- [Resource](https://salt-nlp.github.io/FLANG/)
- [Resource](https://sites.google.com/nlg.csie.ntu.edu.tw/finweb2021/shared-task-finsbd-3)
- [Resource](https://sites.google.com/view/fiqa)
- [Resource](https://www.investopedia.com/financial-term-dictionary-4769738)
- [GitHub Repository](https://github.com/philipperemy/financial-news-dataset)

## 🎯 Purpose and Intended Users

**Goal**: Provide a comprehensive suite of benchmarks for evaluating language models in the financial domain across five NLP tasks and serve as a standard for evaluation of natural language tasks in the financial domain, subject to license and privacy considerations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Sentiment Analysis
- News Headline Classification
- Named Entity Recognition
- Structure Boundary Detection
- Question Answering

**Limitations**: 1) FLUE does not include abstractive generation or summarization tasks due to a lack of large, annotated datasets. 2) Social media data like Twitter and Reddit are not included in pre-training. 3) Models are trained and tested on English tasks and may not perform well on non-English text. 4) Difficulty obtaining vocabulary term lists for some domains may limit generalization. 5) Work is limited to encoder-based architectures.

## 💾 Data

**Source**: Financial PhraseBank (Malo et al., 2014); FiQA 2018 (Maia et al., 2018) Task-1 Sentiment and Task-2 QA; Gold news headline dataset (Sinha and Khandait, 2020); Financial NER dataset (Alvarado et al., 2015); FinSBD3 (FinWeb-2021).

**Size**: Financial PhraseBank: 3,488 train, 388 valid, 969 test; FiQA SA: 822 train, 117 valid, 234 test; Headline (Gold news): 7,989 train, 1,141 valid, 2,282 test; NER (Alvarado et al., 2015): 932 train, 232 valid, 302 test; FinSBD3: 460 train, 165 valid, 131 test; FiQA QA: 5,676 train, 631 valid, 333 test.

**Format**: N/A

**Annotation**: Financial PhraseBank: human-annotated sentiment labels; FiQA SA: aspect-based sentiment annotations; Headline: 9 binary labels; NER: token-level named entity annotations; FinSBD3: structure boundary annotations; FiQA QA: question-answer pairs (relevance labels).

## 🔬 Methodology

**Methods**:
- Model fine-tuning
- Automated metrics

**Metrics**:
- Accuracy
- Mean Squared Error (MSE)
- F1 Score
- Normalized Discounted Cumulative Gain (nDCG)
- Mean Reciprocal Rank (MRR)
- Precision
- R-squared (R2)

**Calculation**: Standard dataset-specific calculations: Accuracy for classification tasks; Mean Squared Error (MSE) and R-squared (R2) for regression; F1 Score for NER, structure boundary detection, and headline classification; nDCG, MRR, and Precision for question answering. Marginal increase in performance (ΔMP) is calculated as (Metric_Model - Metric_FinBERT) / (1 - Metric_FinBERT) as defined in Equation 1 for Financial PhraseBank and Headline datasets.

**Interpretation**: Higher metric values indicate better performance. For ranking metrics, a higher nDCG means more relevant documents are retrieved earlier and a higher MRR means the first relevant item is retrieved earlier. ΔMP denotes marginal improvement over FinBERT.

**Baseline Results**: BERT-base: FPB Accuracy 0.856; FiQA SA MSE 0.073; Headline Mean F-1 0.967; NER F1 0.79; FinSBD3 F1 0.95; FiQA QA nDCG 0.46. FinBERT: FPB 0.872; FiQA SA 0.070; Headline 0.968; NER 0.80; FinSBD3 0.89; FiQA QA 0.42. FLANG-BERT (ours): FPB 0.912; FiQA SA 0.054; Headline 0.972; NER 0.83; FinSBD3 0.96; FiQA QA 0.51. FLANG-ELECTRA (ours): FPB 0.919; FiQA SA 0.034; Headline 0.98; NER 0.82; FinSBD3 0.97; FiQA QA 0.55.

**Validation**: Average of 3 seeds used for reported results. Standard train/validation/test splits per dataset as listed in Table 1. Perplexity computed on validation set for pre-training ablation studies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Societal Impact

**Atlas Risks**:
- **Privacy**: Personal information in data, Exposing personal information
- **Societal Impact**: Impact on the environment

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All FLUE benchmark datasets have low ethical risks and do not expose any sensitive or personal identifiable information. Explicit permission was obtained from the authors of each dataset for inclusion in FLUE.

**Data Licensing**: Licensing per Table 1: Financial PhraseBank CC BY-SA 3.0; FiQA (public); Headline CC BY-SA 3.0; NER CC BY-SA 3.0; FinSBD3 CC BY-SA 3.0; FiQA QA (public).

**Consent Procedures**: Explicit permissions obtained from the authors of each dataset included in FLUE.

**Compliance With Regulations**: Not Applicable
