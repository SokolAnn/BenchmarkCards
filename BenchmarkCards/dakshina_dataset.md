# Dakshina Dataset

## 📊 Benchmark Details

**Name**: Dakshina Dataset

**Overview**: This paper describes the Dakshina dataset, a new resource consisting of text in both the Latin and native scripts for 12 South Asian languages. The dataset includes, for each language: (1) native-script Wikipedia text; (2) a romanization lexicon; and (3) full-sentence parallel data in both a native script of the language and the basic Latin alphabet. The paper documents methods used for preparation and selection of the Wikipedia text, collection of attested romanizations for sampled lexicons, and manual romanization of held-out sentences, and provides baseline results on single-word transliteration, full-sentence transliteration, and language modeling.

**Data Type**: text (native-script Wikipedia sentences; romanization lexicons; native-script ↔ romanized sentence pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- Bengali
- Gujarati
- Hindi
- Kannada
- Malayalam
- Marathi
- Punjabi
- Sindhi
- Sinhala
- Tamil
- Telugu
- Urdu

**Resources**:
- [GitHub Repository](https://github.com/google-research-datasets/dakshina)

## 🎯 Purpose and Intended Users

**Goal**: Provide a publicly available Wikipedia-derived resource to enable training and validation of models for processing South Asian languages written in the Latin script, including single-word transliteration, full-sentence transliteration, and language modeling of native-script and romanized text.

**Target Audience**:
- ML Researchers
- Natural Language Processing Researchers
- Model Developers

**Tasks**:
- Single-word Transliteration
- Full-sentence Transliteration
- Language Modeling

**Limitations**: Dataset is derived from Wikipedia (extracted March 2019) and therefore may not represent informal Latin-script text (e.g., SMS, WhatsApp, social media). Parallel romanized sentence data is limited to 10,000 manually romanized sentences per language. Romanization lexicon sizes are 30,000 entries per language except Sindhi which has 20,000 entries; lexicons sample words with frequency>1 in the training Wikipedia partition.

## 💾 Data

**Source**: Wikipedia text extracted March 2019 in 12 South Asian languages; romanization lexicons elicited from native-speaker annotators; 10,000 manually romanized sentences per language sampled from the validation partition of the native-script Wikipedia collections (then split into dev/test).

**Size**: Varies by language: example nativescript sentence counts in Table 1 include Hindi 1,065,000 sentences, Tamil 1,144,400 sentences, Urdu 507,300 sentences, Sindhi 77,928 sentences. Romanization lexicon: 30,000 entries per language (20,000 for Sindhi). Romanized Wikipedia (manually romanized sentences): 10,000 sentences per language. Lexicon validation: 5,000 validation entries per language.

**Format**: Tab-delimited text examples shown (e.g., tab-delimited Hindi dev set); dataset includes intermediate data and README on the GitHub repository.

**Annotation**: Manual annotation by native-speaker annotators: lexicon entries elicited by asking annotators to romanize a native-script word and to provide additional alternative romanizations (attested counts recorded); 10,000 sentences per language manually romanized; validation round-trip where romanizations were transcribed back into native script and assessed (character error rate reported).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Baseline modeling: finite-state pair n-gram (joint multi-gram) models
- Neural sequence-to-sequence models (LSTM and Transformer)
- Noisy-channel combination of word transliteration + language model
- Character-level language modeling (LSTM)
- Human annotation (for collecting romanizations and sentence romanizations)

**Metrics**:
- Character Error Rate (CER)
- Word Error Rate (WER)
- Bits-per-character (BPC)
- Bits-per-native-character (BPNC)

**Calculation**: CER and WER: number of substitutions, deletions or insertions within a minimum-error alignment of system output with the reference, per token in the reference. Tokens: individual Unicode characters for CER; whitespace-delimited substrings for WER. Reported as percentages (mean and standard deviation over 5 trials). BPC: total negative log base 2 probability of the correct output character sequence divided by the number of characters in the output string. BPNC: same as BPC but divided by the number of native-script characters.

**Interpretation**: Lower CER and WER percentages indicate better transliteration performance. Lower BPC and BPNC indicate better language-modeling performance. Results are reported as means and standard deviations over 5 trials.

**Baseline Results**: Representative baseline numbers from the paper: Single-word transliteration (CER) examples from Table 2 — Bengali: pair6g 14.2% (std .02), transformer 13.2% (std .07), LSTM 13.9% (std .15); Gujarati transformer CER 11.9% (std .15); Urdu transformer CER 19.5% (std .10). Full-sentence transliteration (WER, whitespace evaluation) examples from Table 4 — Bengali: pair6g 35.0% (std .11), transformer 32.5% (std .71), noisy-channel 18.6% (std .02); Hindi noisy-channel 11.0% (std .01). Language modeling (BPC) examples from Table 5 — nativescript Bengali BPC 1.64; romanized Viterbi-sampled Bengali BPC 2.58; nativescript Tamil BPC 1.46.

**Validation**: Data partitioning by Wikipedia page to ensure sentences in validation sets do not come from the same pages as training. Romanized sentences validated via a round-trip: annotators transcribed romanizations back into native script; an assessment of match after extensive visual normalization yielded a mean character error rate of 0.054 (std 0.012) across languages. Five trial averages reported for model baselines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Data Laws

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Data Laws**: Data usage restrictions, Data acquisition restrictions

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
