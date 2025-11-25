# a new multilingual dataset in English, French, and Dutch composed of newspaper ads from the early modern colonial period reporting on enslaved people who liberated themselves from enslavement

## 📊 Benchmark Details

**Name**: a new multilingual dataset in English, French, and Dutch composed of newspaper ads from the early modern colonial period reporting on enslaved people who liberated themselves from enslavement

**Overview**: A new multilingual dataset in English, French, and Dutch composed of newspaper ads from the early modern colonial period reporting on enslaved people who liberated themselves from enslavement. The dataset is designed for event extraction (attribute extraction) and is formatted as extractive QA examples.

**Data Type**: text (extractive question-answering pairs, contexts and answer spans); image (scans of adverts and extracted text)

**Domains**:
- Natural Language Processing
- Digital Humanities
- History

**Languages**:
- English
- French
- Dutch

**Similar Benchmarks**:
- Runaway Slaves in Britain
- BRAD
- SQuAD-v2
- PIAF-v1.1
- FQuAD
- SQuAD-FR
- SQuAD-NL

**Resources**:
- [GitHub Repository](https://github.com/nadavborenstein/EE-from-historical-ads)
- [Resource](https://www.runaways.gla.ac.uk)
- [Resource](http://www.marronnage.info/fr/index.html)
- [Resource](https://www.delpher.nl)
- [Resource](https://arxiv.org/abs/2305.10928)

## 🎯 Purpose and Intended Users

**Goal**: To construct a new multilingual dataset in English, French, and Dutch of 'freedom-seeking events' (newspaper adverts reporting on enslaved people who escaped) and to evaluate approaches (framing event attribute extraction as extractive QA) including zero-shot, few-shot, semi-supervised and cross-lingual methods for event extraction from historical newspaper adverts.

**Target Audience**:
- Historians
- Natural Language Processing Researchers
- Digital Humanities Researchers

**Tasks**:
- Event Extraction
- Attribute Extraction
- Question Answering (Extractive)

**Limitations**: 1) Evaluated on events of a single type only. 2) Dataset contains documents from one language family and period; extending to other language families may pose further challenges. 3) Method relies heavily on automatic translation tools which are biased toward modern language and can negatively affect performance. 4) Most tested datasets are relatively clean; real-world OCR-noisy texts were not the primary focus.

## 💾 Data

**Source**: Annotated English data: Runaway Slaves in Britain (Newman et al., 2019). Translated training splits: English training split automatically translated into French and Dutch (Google Translate) with fuzzy-matching alignment. Unannotated datasets: Marronage dans le monde atlantique (French and English ads) and De Curaçaosche courant scraped from Delpher (Dutch). Manually annotated multilingual evaluation sets: 41 French adverts (Marronage) and 44 Dutch adverts (Delpher) annotated by historians.

**Size**: Runaway Slaves in Britain (English annotated): 835 labeled ads; Translated training splits: 834 labeled ads (French), 834 labeled ads (Dutch). Marronage: more than 20,000 manually transcribed ads (unannotated); Marronage (French) reported: 41 labeled ads and 19,066 unlabeled ads (per Table 1). Marronage (English) reported: 3,026 unlabeled ads (per Table 1). Delpher (Dutch): 2,742 full issues; manually annotated Dutch evaluation: 44 adverts. Train/validation split for the Runaways dataset: 70/30.

**Format**: SQuAD-v2 style JSON (context, question, answer spans); additionally raw scans of adverts (images) and extracted OCR text were used.

**Annotation**: Manual annotation by domain experts/historians following the Runaways dataset annotation scheme (50 attributes). Most ads annotated by a single historian; a random sample of 15 ads per language was annotated by a second annotator to compute inter-annotator agreement (pairwise F1). The translated training split was aligned using fuzzy string matching when needed; translation quality was evaluated by human raters and with COMET.

## 🔬 Methodology

**Methods**:
- Extractive Question Answering (formulating attribute extraction as extractive QA)
- Zero-shot inference
- Few-shot training
- Semi-supervised training (further MLM pre-training; simultaneous MLM+QA; tri-training)
- Cross-lingual training (simple cross-lingual and MLM cross-lingual)
- Fine-tuning pre-trained language models (monolingual, multilingual, historical-domain models)
- Human annotation and inter-annotator agreement evaluation

**Metrics**:
- SQuAD-v2 F1
- Pairwise F1 (inter-annotator agreement)
- Perplexity (MLM pseudo-perplexity as described in Appendix A.1)

**Calculation**: Primary evaluation uses the standard SQuAD-v2 F1 metric. Inter-annotator agreement was computed using pairwise F1 on a 15-ad sample per language (Tang et al., 2021). Perplexity for language models computed via masked language model pseudo-perplexity as described in Appendix A.1.

**Interpretation**: Higher SQuAD-v2 F1 indicates better extractive attribute extraction performance. Authors interpret higher F1 as better performance and analyze differences across languages, data regimes, model sizes, and training strategies. Perplexity is used to compare fit of language models to the dataset (lower perplexity = better fit).

**Baseline Results**: Zero-shot baseline results (Table 2): English - OneIE: 51.90 F1; T0++: 33.69 F1; RoBERTa-base (fine-tuned on SQuAD-v2): 54.35 F1; RoBERTa-large (SQuAD-v2): 56.42 F1. French and Dutch baseline numbers reported in Table 2 and further results in Tables 3, 6, 7 (see paper for detailed tables).

**Validation**: Train/validation split: 70/30 for the Runaways dataset. Translation quality evaluated automatically with COMET and by human raters (20 translations rated for accuracy and fluency). Inter-annotator agreement computed on 15 dual-annotated ads per language, yielding pairwise F1 scores of 91.5 (English), 83.2 (French), and 80.7 (Dutch).

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Value Alignment
- Accuracy
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Value Alignment**: Toxic output
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: ['Reproduction or perpetuation of racist and demeaning language', 'Potential harm to affected communities by exposing or reproducing racist historical language']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors state that the enslaved people described were alive centuries ago, so immediate privacy and personal data protection issues do not apply. The dataset contains many examples of highly racist and demeaning language and the authors note ethical concerns about reproducing such language.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
