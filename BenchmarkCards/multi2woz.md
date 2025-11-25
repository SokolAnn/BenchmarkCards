# MULTI2WOZ

## 📊 Benchmark Details

**Name**: MULTI2WOZ

**Overview**: MULTI2WOZ is a new multilingual multi-domain task-oriented dialog (TOD) dataset, derived from the English MultiWOZ 2.1 data, that spans four typologically diverse languages (Chinese, German, Arabic, and Russian) and contains gold-standard dialogs directly comparable with the development and test portions of the English dataset to enable reliable and comparative estimates of cross-lingual transfer performance for TOD.

**Data Type**: dialog utterances and slot-value annotations (text)

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- German
- Arabic
- Russian

**Similar Benchmarks**:
- GlobalWOZ
- AllWOZ
- MultiWOZ

**Resources**:
- [GitHub Repository](https://github.com/umanlp/Multi2WOZ)
- [Resource](https://huggingface.co/umanlp/)

## 🎯 Purpose and Intended Users

**Goal**: Provide a reliable and large multilingual evaluation benchmark for multi-domain task-oriented dialog to enable reliable and comparable estimates of cross-lingual transfer performance for TOD.

**Target Audience**:
- ML Researchers
- Model Developers
- NLP Researchers

**Tasks**:
- Dialog State Tracking
- Response Retrieval

**Limitations**: MULTI2WOZ contains translations of the development and test portions of MultiWOZ only (2,000 dialogs in total: 1,000 development and 1,000 test dialogs; 14,748 and 14,744 utterances respectively).

## 💾 Data

**Source**: Translated from the development and test portions of MultiWOZ 2.1 (Eric et al., 2020). Automatic translation with Google Translate followed by manual post-editing by native/fluent speakers; parallel dialogs additionally compiled from OpenSubtitles and CCNet were used for model specialization (not for dataset creation).

**Size**: 2,000 dialogs (1,000 development, 1,000 test) containing 29,492 utterances (14,748 development, 14,744 test)

**Format**: JSON

**Annotation**: Two-step process: automatic translation (Google Translate) of utterances and slot values followed by manual post-editing by native/fluent annotators; additional quality control where two independent annotators reviewed a random sample of 200 dialogs (2,962 utterances) per language. Annotation effort: 16 annotators, 1,083 person-hours; reported cost $17,328.

## 🔬 Methodology

**Methods**:
- Zero-shot transfer evaluation
- Few-shot transfer evaluation
- Automated metrics (evaluation on test set)

**Metrics**:
- Joint Goal Accuracy
- Recall@1 (R100@1)

**Calculation**: Joint Goal Accuracy: at each dialog turn, compares predicted dialog states against manually annotated ground truth (a prediction is correct iff all predicted slot values exactly match the ground truth). Recall@1 (R100@1): given a dialog context and 100 candidate responses (1 true, 99 false), measures whether the true response is ranked at top-1.

**Interpretation**: Higher Joint Goal Accuracy and higher R100@1 indicate better performance. Large performance drops relative to English reference performance indicate poor cross-lingual transfer.

**Baseline Results**: Reference English TOD-XLMR: Dialog State Tracking joint goal accuracy 47.86%; Response Retrieval R100@1 64.75%. Zero-shot cross-lingual baselines: XLM-R zero-shot DST average 1.33% joint goal accuracy; TOD-XLMR zero-shot DST average 1.80% joint goal accuracy; TOD-XLMR zero-shot RR average 2.7% R100@1.

**Validation**: Quality control: two independent annotators per target language judged a random sample of 200 dialogs (2,962 utterances). Annotators answered whether the translated utterance is acceptable and whether translated slot values match the utterance. Annotators answered affirmatively for 99% of utterances on average. Inter-Annotator Agreement (Cohen's kappa): 0.824 (development), 0.838 (test).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on the environment

**Potential Harm**: ['Unfair stereotypical biases encoded in general-purpose and conversational pretrained language models', 'Exclusion of the larger spectrum of (gender) identities', 'Environmental harm from (pre)training and fine-tuning large-scale pretrained language models (carbon footprint)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
