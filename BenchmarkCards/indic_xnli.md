# INDIC XNLI

## 📊 Benchmark Details

**Name**: INDIC XNLI

**Overview**: We introduce INDIC XNLI, an NLI dataset for 11 Indic languages. It has been created by high-quality machine translation of the original English XNLI dataset and our analysis attests to the quality of INDIC XNLI. By fine-tuning different pre-trained LMs on this INDIC XNLI, we analyze various cross-lingual transfer techniques with respect to the impact of the choice of language models, languages, multi-linguality, mix-language input, etc.

**Data Type**: text (premise-hypothesis sentence pairs for Natural Language Inference)

**Domains**:
- Natural Language Processing

**Languages**:
- Assamese
- Gujarati
- Kannada
- Malayalam
- Marathi
- Odia
- Punjabi
- Tamil
- Telugu
- Hindi
- Bengali

**Similar Benchmarks**:
- XNLI
- XQUAD
- MLQA
- PAWS-X
- XTREME
- XTREME-R
- XGLUE
- IndicGLUE

**Resources**:
- [GitHub Repository](https://github.com/divyanshuaggarwal/indicxnli)

## 🎯 Purpose and Intended Users

**Goal**: Provide an NLI benchmark dataset for eleven prominent Indic languages by translating the English XNLI dataset, and to analyze cross-lingual transfer and training strategies for multilingual language models on these languages.

**Target Audience**:
- ML Researchers
- Model Developers
- Natural Language Processing Researchers

**Tasks**:
- Natural Language Inference

**Limitations**: INDIC XNLI is created via machine translation and the authors note machine translation is "prone to contain some 'translationese' errors"; the ideal strategy of creating an NLI dataset from scratch (human-authored in each Indic language) is noted as significantly more expensive and time-consuming.

## 💾 Data

**Source**: Translated from English XNLI using IndicTrans (Ramesh et al., 2021). IndicTrans is trained on the Samanantar parallel corpus.

**Size**: 392,702 training examples; 2,490 validation examples; 5,010 evaluation examples (per language)

**Format**: N/A

**Annotation**: Manual human validation: 2 annotators per language on 100 diverse sampled test instances using Determinantal Point Process sampling; annotators scored sentence pairs 0-5 (normalized to 0-1). Automatic validation: BERTScore comparisons (EngTrans and Multilingual strategies).

## 🔬 Methodology

**Methods**:
- Fine-tuning pre-trained multilingual language models (Indic-specific and generic)
- Human evaluation (manual validation of translations)
- Automated metrics evaluation (BERTScore)
- Cross-lingual transfer experiments (zero-shot, translate-train, translate-test, mix-language evaluation)

**Metrics**:
- Accuracy
- BERTScore (F1-based)
- Pearson correlation
- Spearman correlation

**Calculation**: Accuracy computed as in the original XNLI paper. Human validation scores: annotators assigned integer scores 0-5 which were normalized to a 0-1 probability range and averaged over sampled instances. BERTScore computed between English and translated sentences (both EngTrans and multilingual strategies as described). Pearson and Spearman correlations computed over annotation scores.

**Interpretation**: Higher Accuracy indicates better NLI performance. BERTScore is used as an automatic proxy that correlates with human judgment. Human validation average scores > 0.85 and Pearson > 0.7 and Spearman > 0.8 are reported as supporting high translation quality. The authors report English+Indic Train strategy yields best performance, and MuRIL performs best across Indic languages in many settings.

**Baseline Results**: Authors report comparative results across models and strategies: MuRIL generally performs best across Indic languages (except some English-eval scenarios where XLM-RoBERTa outperforms). English + Indic Train and Train All strategies give the best results; IndicBERT performs worse than mBERT attributed to smaller model size.

**Validation**: Validation includes (a) human validation: 2 expert annotators per language scored 100 DPP-sampled test instances following SemEval-2016 Task-I guidelines, with Pearson and Spearman correlations reported; (b) automatic validation using BERTScore via back-translation (EngTrans) and multilingual comparison (mBERT).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
