# Hokkien-Mandarin CM Dataset

## 📊 Benchmark Details

**Name**: Hokkien-Mandarin CM Dataset

**Overview**: The paper proposes a method to construct a Hokkien-Mandarin code-mixing (CM) dataset, introduces a linguistics-based Hokkien word segmentation method using the Articut toolkit, synthesizes multiple code-mixed corpora (parallel and non-parallel), and uses the proposed dataset with transfer learning on XLM for Hokkien-Mandarin translation, showing improved CM translation while maintaining monolingual translation quality.

**Data Type**: text (code-mixed sentences; parallel and non-parallel Hokkien-Mandarin sentence pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- Taiwanese Hokkien
- Mandarin

**Similar Benchmarks**:
- iCorpus
- MoE’s Dictionary
- PHINC
- CoMeT

**Resources**:
- [Resource](https://arxiv.org/abs/2301.08937)
- [GitHub Repository](https://github.com/alznn/Taiwanese-Hokkien_Mandarin_CM_Dataset)
- [GitHub Repository](https://github.com/Taiwanese-Corpus/icorpus_ka1_han3-ji7)
- [GitHub Repository](https://github.com/g0v/moedict-webkit)
- [GitHub Repository](https://github.com/Taiwanese-Corpus/Linya-Huang_2014_taiwanesecharacters)
- [GitHub Repository](https://github.com/Taiwanese-Corpus/kok4hau7-kho3pun2)
- [Resource](https://language110.eduweb.tw/Module/Question/Index.php)
- [GitHub Repository](https://github.com/ckiplab/ckiptagger)

## 🎯 Purpose and Intended Users

**Goal**: To construct and release Hokkien-Mandarin code-mixed corpora (parallel and non-parallel), provide a linguistics-based Hokkien word segmentation method, and demonstrate use of the corpora for Hokkien-Mandarin machine translation using adapted XLM and transfer learning.

**Target Audience**:
- Academic researchers
- Natural Language Processing researchers
- Model developers
- Computational linguists

**Tasks**:
- Machine Translation
- Word Segmentation
- Data Augmentation / Data Synthesis

**Limitations**: Our research is designed for the Sino-Tibetan language family. However, the language features may not be generalized to other language families well. Furthermore, in our case, Hokkien has officially defined Mandarin characters. Without officially defined characters, it might be difficult to eliminate the differences between writing systems and create useful datasets. Finally, during data construction, we can directly mark the language, so we can assume language identification has 100% accuracy in the translation model. Without a good language identification system, the performance of the translation model might be affected.

## 💾 Data

**Source**: Monolingual Mandarin: Wikipedia (latest) and Taiwan news (2018-2019). Monolingual Hokkien: Taiwanese songs, elementary school textbooks, Hokkien Reading Competition articles, subtitles of Hokkien television programs. Parallel Hokkien-Mandarin: iCorpus (Academia Sinica) and MoE’s Dictionary example sentences. Synthesized CM datasets: iCorpus-CM, iCorpus-CMDA, MoeDict-CM, MoeDict-CMDA produced by applying linguistic constraints and Articut-based Hokkien segmentation.

**Size**: Parallel CM corpus: 76,013 Hokkien-Mandarin CM sentences; Non-parallel CM data: 75,150 examples. Mandarin monolingual corpus for training: 2.2 GB. iCorpus parallel: 64,110 sentences. MoE’s Dictionary: ~14,985 example sentences. Hokkien subtitles: 126,578 sentences (as reported). Additional monolingual Hokkien sources: 30 songs; 349 elementary school textbook articles; 550 Hokkien Reading Competition articles.

**Format**: N/A

**Annotation**: Hokkien word segmentation performed via Articut with a custom dictionary (MoE’s Dictionary) and linguistic rules; synthesized code-mixing uses language-tagging by appending '_@' to Hokkien characters. Human evaluation: three annotators scored sampled CM sentences (overall 1-5 scale and metrics colloquialism/intelligibility/coherence on 1-3 scales); inter-rater agreement (kappa) computed (~0.740).

## 🔬 Methodology

**Methods**:
- Rule-based linguistic synthesis (matrix language frame, equivalence constraint, functional head constraint)
- Hokkien word segmentation using Articut with custom dictionary
- Data augmentation / synthetic CM generation
- Human evaluation (annotator scoring)
- Model-based evaluation using XLM with Dynamic Language Identification and transfer learning
- Automated metrics evaluation (BLEU, BERT-Score)

**Metrics**:
- BLEU
- BERT-Score (Precision, Recall, F1)
- Code-Mixing Index (CMI)
- Switch Point Fraction (SPF)
- Human quality score (1–5)
- Colloquialism / Intelligibility / Coherence (1–3 scales)
- Fleiss' kappa (inter-rater agreement)

**Calculation**: Data split into training/validation/test with 8:1:1 in each parallel corpus. Evaluation metrics BLEU and BERT-Score computed on test sets and on a reserved PAD (823 sentences) not used in pre-training. Experiments run three times and average scores reported. Human evaluation: annotators scored sampled CM sentences (1,879 from iCorpus-CM and 179 from MoeDict-CM) with defined instructions; kappa calculated on an additional 100 sentences.

**Interpretation**: Higher BLEU and BERT-Score indicate better translation quality. Authors report that Dynamic Language Identification (DLI) and transfer learning (CLM/MLM stages) improve CM translation performance while preserving monolingual translation quality. Human scores and kappa are used to assess dataset fluency, colloquialism, coherence, and intelligibility.

**Baseline Results**: The paper reports multiple XLM configuration results (see Table 13). Examples: XLM M_M (+AE +DLI) PAD BLEU 75.46, CM BLEU 51.42, BERT-Score F1 88.585. XLM MT_M (+AE +DLI) PAD BLEU 83.15, CM BLEU 62.59, BERT-Score F1 91.097. XLM MT_CT (+AE +DLI) PAD BLEU 95.65, CM BLEU 61.18, BERT-Score F1 90.964. All reported results are averages over three runs.

**Validation**: Human evaluation by three annotators sampling 1,879 sentences from iCorpus-CM and 179 sentences from MoeDict-CM; annotators anonymous and informed of purpose. Inter-rater Fleiss' kappa reported ~0.740. A reserved PAD of 823 sentences (CM preserved assessment dataset) was held out and not used in any pre-training stage; experiments averaged over three runs.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Annotators come from three different generations (elders, middle-aged, youngsters). Annotator ratings differed (notably annotator C gave lower colloquialism scores due to unfamiliarity with WTH pronunciation). Inter-rater kappa is ~0.740.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Annotators are anonymous and were informed of the purpose and use of the experiment prior to annotating. Data sources are open-source resources or public government data and organized by the authors for academic research.

**Data Licensing**: All data used and created are described as open source and for academic purposes only (no specific license type provided).

**Consent Procedures**: Annotators were clearly informed of the purpose and use of the entire experiment before annotating (no additional formal consent procedure described).

**Compliance With Regulations**: Not Applicable
