# BanglaParaphrase: A High-Quality Bangla Paraphrase Dataset

## 📊 Benchmark Details

**Name**: BanglaParaphrase: A High-Quality Bangla Paraphrase Dataset

**Overview**: We present BanglaParaphrase, a high-quality synthetic Bangla Paraphrase dataset curated by a novel filtering pipeline. The dataset ensures quality by preserving both semantics and diversity, aimed at alleviating the low-resource status of the Bangla language in Natural Language Processing and useful to enhance other Bangla datasets.

**Data Type**: text (parallel paraphrase pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- Bangla

**Similar Benchmarks**:
- IndicParaphrase
- IndicNLG Suite
- OpusParcus
- TaPaCo
- Finnish paraphrase corpus

**Resources**:
- [GitHub Repository](https://github.com/csebuetnlp/banglaparaphrase)
- [Resource](https://arxiv.org/abs/2210.05109)

## 🎯 Purpose and Intended Users

**Goal**: To introduce BanglaParaphrase, a synthetic Bangla paraphrase dataset curated via an automated filtering pipeline that ensures both diversity and semantics, to improve Bangla NLP resources.

**Tasks**:
- Paraphrase Generation

**Limitations**: N/A

## 💾 Data

**Source**: Scraped high-quality representative sentences from the RoarBangla website, translated Bangla->English using the model from Hasan et al. (2020), back-translated to Bangla using beam search; candidate pairs selected using LaBSE similarity and further filtered via a pipeline of PINC score filter, BERTScore filter (with BanglaBERT embeddings), N-gram repetition filter, and punctuation filter. Additional augmentation performed via masked language modeling using BanglaBERT and XLM-RoBERTa, then filtered with same pipeline.

**Size**: Initial candidate set > 1.364M sentences; filtered dataset 466,630 parallel paraphrase pairs; after MLM augmentation dataset 603,672 parallel pairs (551,324 training pairs; 29,016 validation pairs; 23,332 test pairs).

**Format**: N/A

**Annotation**: Automatically generated via pivoting/back-translation and filtered by automated metrics (LaBSE similarity, PINC, BERTScore with BanglaBERT, N-gram repetition, punctuation). Manual human evaluation of 300 randomly chosen samples was used to select BERTScore threshold.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation (fine-tuning and evaluation of mT5-small, BanglaT5, IndicBART, IndicBARTSS)

**Metrics**:
- sacreBLEU
- ROUGE-L
- PINC
- BERTScore F1 (with BanglaBERT embeddings)
- BERT-iBLEU (modified hybrid score)

**Calculation**: sacreBLEU and ROUGE-L reported as percentages (F1 for ROUGE-L). PINC reported as arithmetic mean over test set. BERTScore F1 computed using BanglaBERT embeddings. BERT-iBLEU is a modified hybrid score combining BERTScore and 1-selfBLEU as a weighted harmonic mean; the authors used alpha = 4.0 in the formula.

**Interpretation**: Higher sacreBLEU and ROUGE-L indicate higher quality (semantic adequacy and fluency). Higher PINC indicates greater syntactic diversity (less n-gram overlap). Higher BERTScore indicates greater semantic correctness. Higher BERT-iBLEU indicates semantic similarity while penalizing syntactic similarity.

**Baseline Results**: Selected results on the BanglaParaphrase test set (percentages where applicable): mT5-small: sacreBLEU 20.9, ROUGE-L 53.57, PINC 80.5, BERTScore 94.20, BERT-iBLEU 92.67. mT5-small-aug: sacreBLEU 19.90, ROUGE-L 53.63, PINC 80.72, BERTScore 94.00, BERT-iBLEU 92.54. BanglaT5: sacreBLEU 32.8, ROUGE-L 63.58, PINC 74.40, BERTScore 94.80, BERT-iBLEU 92.18. BanglaT5-aug: sacreBLEU 32.5, ROUGE-L 63.43, PINC 74.41, BERTScore 94.80, BERT-iBLEU 92.18. IndicBART: sacreBLEU 5.60, ROUGE-L 35.61, PINC 80.26, BERTScore 91.50, BERT-iBLEU 91.16. IndicBARTSS: sacreBLEU 4.90, ROUGE-L 33.66, PINC 82.10, BERTScore 91.10, BERT-iBLEU 90.95.

**Validation**: Dataset split randomly into 80:10:10 (train:validation:test). Thresholds for filters (PINC and BERTScore) were chosen via experiments varying thresholds and examining validation and test metrics; final model selection based on validation sacreBLEU. Human evaluation of 300 samples was used to choose initial BERTScore threshold.

## ⚠️ Targeted Risks

**Risk Categories**:
- Intellectual Property
- Legal Compliance

**Atlas Risks**:
- **Intellectual Property**: Copyright infringement
- **Legal Compliance**: Model usage rights restrictions

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: To be released under a non-commercial license (as stated in the paper).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Paper cites the Bangladesh Copy Right Act, 2000 and states dataset/model release under a non-commercial license in accordance with this act.
