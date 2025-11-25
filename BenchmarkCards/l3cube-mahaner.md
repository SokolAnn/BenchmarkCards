# L3Cube-MahaNER

## 📊 Benchmark Details

**Name**: L3Cube-MahaNER

**Overview**: Presents L3Cube-MahaNER, the first major gold standard named entity recognition dataset in Marathi. The dataset contains 25,000 manually tagged sentences across eight entity classes, annotated in IOB and non-IOB notation, with sentences sourced from a news domain corpus.

**Data Type**: text (token-level NER annotated sentences, IOB and non-IOB)

**Domains**:
- Natural Language Processing

**Languages**:
- Marathi

**Similar Benchmarks**:
- IIT Bombay Marathi NER Corpus
- WikiAnn NER Corpus

**Resources**:
- [GitHub Repository](https://github.com/l3cube-pune/MarathiNLP)
- [Resource](https://huggingface.co/l3cube-pune/marathi-ner)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large manually annotated Marathi named entity recognition dataset (L3Cube-MahaNER) and benchmark a range of models to establish baselines for future comparisons.

**Tasks**:
- Named Entity Recognition

**Limitations**: The dataset does not preserve the context of the news, such as publication profiles, regions, and so on.

## 💾 Data

**Source**: Base sentences taken from the L3Cube-MahaCorpus, a monolingual Marathi dataset primarily from the news domain.

**Size**: 25,000 sentences (Train: 21,500 sentences; Test: 2,000 sentences; Validation: 1,500 sentences)

**Format**: N/A

**Annotation**: Manual annotation by human annotators following established annotation guidelines; annotated in IOB and non-IOB notation. First 200 sentences were tagged together for consistency among four annotators; ambiguous cases were resolved by majority vote.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (training/evaluating CNN, LSTM, biLSTM, and transformer models such as mBERT, IndicBERT, XLM-RoBERTa, RoBERTa-Marathi, MahaBERT, MahaRoBERTa, MahaALBERT)
- Automated metrics (Precision, Recall, F1 Score, Accuracy)

**Metrics**:
- F1 Score (macro)
- Precision
- Recall
- Accuracy

**Calculation**: F1 Score reported as macro F1 (noted in table header as 'F1 score(macro)'); precision and recall reported as in the tables; accuracy reported as overall accuracy as shown in results tables.

**Interpretation**: Higher F1 Score/Precision/Recall/Accuracy indicates better NER performance. Reported results identify MahaRoBERTa as yielding the best performance for IOB notation and MahaBERT as yielding the best performance for non-IOB notation.

**Baseline Results**: IOB (selected): MahaRoBERTa — F1 Score 85.30, Precision 84.27, Recall 86.36, Accuracy 97.18; MahaBERT — F1 Score 84.81, Precision 84.55, Recall 85.07, Accuracy 97.10. Non-IOB (selected): MahaBERT — F1 Score 86.80, Precision 84.62, Recall 89.09, Accuracy 97.15; MahaRoBERTa — F1 Score 86.60, Precision 84.30, Recall 89.04, Accuracy 97.24.

**Validation**: Dataset split into Train (21,500), Test (2,000), Validation (1,500). Inter-annotator consistency ensured by jointly tagging the first 200 sentences and resolving ambiguous cases by majority vote.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
