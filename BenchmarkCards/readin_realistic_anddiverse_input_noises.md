# READIN (REalistic AndDiverse Input Noises)

## 📊 Benchmark Details

**Name**: READIN (REalistic AndDiverse Input Noises)

**Overview**: READIN is a Chinese multi-task benchmark that measures model robustness to realistic and diverse user-generated input noises by collecting noisy test sets for four diverse tasks where annotators re-enter original test data using two common Chinese input methods: Pinyin keyboard input (with different IMEs) and speech input (recorded and processed by ASR).

**Data Type**: text (Pinyin keyboard input re-entries and ASR-converted speech transcripts; includes question-answering pairs, sentence pairs, natural language to SQL queries, and parallel sentences for translation)

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- NoiseQA
- CLUE

**Resources**:
- [GitHub Repository](https://github.com/thunlp/READIN)
- [Resource](https://arxiv.org/abs/2302.07324)

## 🎯 Purpose and Intended Users

**Goal**: To create a Chinese multi-task benchmark with realistic and diverse input noises (keyboard Pinyin and speech input) to evaluate and stress-test model robustness and fairness under real-world user-generated noisy inputs.

**Target Audience**:
- ML Researchers
- Model Developers
- Chinese NLP community

**Tasks**:
- Paraphrase Identification
- Machine Reading Comprehension
- Semantic Parsing (Text-to-SQL)
- Machine Translation

**Limitations**: The authors acknowledge it is impossible to cover all possible input noises; they did not cover the impact of different input devices (phones, tablets, keyboards used in annotation) and speed-limit constraints in keyboard annotation may not capture exactly how users type in real applications.

## 💾 Data

**Source**: Derived from existing datasets: AFQMC (Xu et al., 2020), CMRC2018 (Cui et al., 2019), CSpider (Min et al., 2019), and WMT2021 news translation shared task (Akhbardeh et al., 2021).

**Size**: AFQMC: 18,000 train / 2,000 dev / 4,317 test; CMRC2018: 8,871 train / 1,271 dev / 3,219 test; CSpider: 7,500 train / 1,159 dev / 1,034 test; WMT2021: test 1,948 (no train/dev annotated for READIN).

**Format**: N/A

**Annotation**: Crowdsourced re-entry annotation: each test example annotated with two input-method tracks (keyboard Pinyin and speech). For keyboard: each sentence annotated by three annotators using three different commercial Pinyin IMEs (Microsoft, QQ, Sogou); speed limit of 40 characters per minute; post-editing disallowed; typing interface recorded. For speech: 10 speakers from diverse dialectal groups recorded on mobile devices at 16kHz in natural environments; each sentence annotated by three different annotators; ASR post-processing performed by commercial iFlytek; raw audio recordings released.

## 🔬 Methodology

**Methods**:
- Automated metrics (task-specific)
- Micro-Average evaluation across multiple noisy annotations
- Worst-Average evaluation (worst-case across annotations)
- Human preference selection experiment for data quality

**Metrics**:
- Accuracy
- Exact Match
- BLEU Score
- F1 Score
- Micro-Average
- Worst-Average

**Calculation**: Micro-Average (MA): average over the three annotations per example, then averaged across examples. MA = (1/3) * (mean performance on annotator1 + mean on annotator2 + mean on annotator3). Worst-Average (WA): for each example take the minimum performance among its three annotations, then average across examples. WA = (1/N) * sum_i min(p_i1, p_i2, p_i3). Character-level error rate for noise measured via Levenshtein distance: error = levenshtein(s, t) / len(s).

**Interpretation**: Higher metric values indicate better performance. Micro-Average measures average robustness across annotators; Worst-Average measures worst-case robustness across annotator variations and is a more challenging evaluation.

**Baseline Results**: Baseline experiments (Tables 5-7) show significant performance drops on READIN noisy test sets compared to clean test sets. Baselines include RoBERTa-wwm, MacBERT, mBART50, and DG-SQL; see paper Tables 5-7 for detailed per-dataset numbers (e.g., RoBERTa-wwm AFQMC positive: clean accuracy 78.92, keyboard micro-average 42.75, worst-average 15.17).

**Validation**: Human evaluation: preference selection experiment on 160 paired sentences comparing crowdsourced noises vs. automatically constructed typos; additional human quality annotation on sampled examples; error rates computed by Levenshtein distance; micro-average and worst-average measures used to validate evaluation stability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: Speech annotators: 10 speakers from diverse regions of China covering different dialectal groups; ages range from 32 to 64; 4 males and 6 females. The authors recruited annotators to maximize accent diversity and recorded annotator hometowns in Appendix Table 8.

**Potential Harm**: The benchmark aims to detect and reduce unequal model performance across accent and dialect variations and to improve accessibility of language technologies for users from diverse backgrounds.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Annotators were explicitly informed about how the collected data will be used; the authors made adjustments in data collection and release protocol to avoid privacy concerns; raw audio recordings are released but authors state steps were taken to avoid privacy issues.

**Data Licensing**: Not Applicable

**Consent Procedures**: Annotators were informed about data usage and compensation was discussed and agreed upon before annotation; all annotators were properly paid (total annotation cost ~30K RMB).

**Compliance With Regulations**: Not Applicable
