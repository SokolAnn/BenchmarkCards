# GEC dataset for Brazilian Portuguese

## 📊 Benchmark Details

**Name**: GEC dataset for Brazilian Portuguese

**Overview**: We introduce a GEC dataset for Brazilian Portuguese with four categories: Grammar, Spelling, Internet, and Fast typing. We investigate the effectiveness of GPT-3.5 and GPT-4 as Grammatical Error Correction (GEC) tools for Brazilian Portuguese and compare their performance against Microsoft Word and Google Docs.

**Data Type**: text (incorrect-correct sentence pairs)

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Portuguese

**Similar Benchmarks**:
- CoNLL-2014

**Resources**:
- [Resource](https://arxiv.org/abs/2306.15788)
- [Resource](https://chat.openai.com)
- [Resource](https://docs.google.com)
- [Resource](https://onedrive.live.com)

## 🎯 Purpose and Intended Users

**Goal**: Investigate the effectiveness of GPT-3.5 and GPT-4 as Grammatical Error Correction (GEC) tools for Brazilian Portuguese and provide a GEC dataset for evaluation divided into four categories (Grammar, Spelling, Internet, Fast typing).

**Target Audience**:
- Machine Learning Researchers
- Educational researchers and practitioners

**Tasks**:
- Grammatical Error Correction

**Limitations**: The dataset may reflect the biases of the human curators and may not fully encompass the complexities and variations present in real-world data; limited availability of corpora for Brazilian Portuguese motivated creation of this relatively small dataset; dataset examples were manually written by native speakers and may not capture real-world error distributions.

## 💾 Data

**Source**: Created by native Brazilian Portuguese speakers who manually wrote multiple sentences. The dataset lists incorrect sentences and their correct pairs across four categories: Grammar, Spelling, Fast typing, and Internet language.

**Size**: 282 sentence pairs (102 grammar pairs, 100 spelling pairs, 40 fast typing pairs, 40 internet pairs)

**Format**: N/A

**Annotation**: Manually created and paired incorrect and correct sentences by native Brazilian Portuguese speakers.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Human qualitative analysis
- Model-based evaluation (GPT-3.5, GPT-4)
- Comparative evaluation against Microsoft Word and Google Docs

**Metrics**:
- Precision
- Recall
- F0.5 Score
- True Negative Rate (TNR)

**Calculation**: Precision — From the phrases modified by the GEC tool, how many were successfully corrected. Recall — From the ungrammatical phrases, how many were successfully corrected by the GEC tool. F0.5 Score — Combines precision and recall, emphasizing precision twice as much as recall. True Negative Rate (TNR) — From the grammatical phrases, how many were successfully not modified by the GEC tool.

**Interpretation**: Higher recall with lower precision indicates overcorrection by LLMs (they detect errors but also make unnecessary edits). GPT-4 achieves higher F0.5 scores than other methods, indicating a better balance (with emphasis on precision) compared to GPT-3.5 and the editors evaluated. Lower TNR values for LLMs indicate a tendency to modify correct phrases.

**Baseline Results**: Selected results from Table 3: INTERNET recall — MS Word 12.5%, Google Docs 5.0%, GPT-3.5 78.3±1.3%, GPT-4 89.3±1.3%. FAST TYPING recall — MS Word 27.5%, Google Docs 40.0%, GPT-3.5 85.0±0.0%, GPT-4 90.0±1.3%. GRAMMAR — MS Word: Precision 89.1%, Recall 40.2%, F0.5 71.7%, TNR 95.1%. Google Docs: Precision 97.4%, Recall 36.3%, F0.5 72.8%, TNR 99.0%. GPT-3.5: Precision 67.5±0.2%, Recall 63.7±1.7%, F0.5 66.7±0.5%, TNR 69.3±0.6%. GPT-4: Precision 86.8±0.7%, Recall 75.5±1.7%, F0.5 84.3±1%, TNR 88.5±0.6%. SPELLING — MS Word: Precision 94.9%, Recall 74.0%, F0.5 89.8%, TNR 96.0%. Google Docs: Precision 100%, Recall 66.0%, F0.5 90.7%, TNR 100%. GPT-3.5: Precision 79.7±1.7%, Recall 85±3.5%, F0.5 80.7±2%, TNR 78.3±1.5%. GPT-4: Precision 99.3±0.6%, Recall 92.0±6.1%, F0.5 97.7±1.8%, TNR 99.3±0.6%.

**Validation**: GPT-3.5 and GPT-4 results are averages (with standard deviation) over three runs. For Grammar and Spelling categories, GEC tools were also run on grammatically correct phrases to evaluate false positives. A qualitative analysis was performed, classifying behaviors (over-correction, omission, grammatical miscorrection, ungrammatical miscorrection).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness
- Accuracy
- Misuse

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Privacy**: Exposing personal information
- **Robustness**: Prompt injection attack, Hallucination
- **Accuracy**: Poor model accuracy
- **Misuse**: Spreading disinformation

**Potential Harm**: ['Perpetuation of harmful stereotypes', 'Spreading misinformation']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The paper notes a privacy risk when interacting with LLMs that require sending requests to third-party servers (internet connection) but does not describe anonymization procedures.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
