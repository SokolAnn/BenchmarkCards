# MultiTACRED: A Multilingual Version of the TAC Relation Extraction Dataset

## 📊 Benchmark Details

**Name**: MultiTACRED: A Multilingual Version of the TAC Relation Extraction Dataset

**Overview**: We introduce the MultiTACRED dataset, covering 12 typologically diverse languages from 9 language families, which is created by machine-translating TACRED instances and automatically projecting their entity annotations. We analyze translation and annotation projection quality, identify error categories, and experimentally evaluate fine-tuned pre-trained mono- and multilingual language models in common transfer learning scenarios.

**Data Type**: text (sentence-level relation extraction instances: sentences with token-level head and tail entity span annotations and relation labels)

**Domains**:
- Natural Language Processing
- Information Extraction

**Languages**:
- Arabic
- German
- Spanish
- French
- Finnish
- Hindi
- Hungarian
- Japanese
- Polish
- Russian
- Turkish
- Chinese

**Similar Benchmarks**:
- TACRED (TAC Relation Extraction Dataset)
- Re-TACRED
- DiS-ReX
- RelX-Distant
- SMiLER
- BizRel
- IndoRE

**Resources**:
- [GitHub Repository](https://github.com/DFKI-NLP/MultiTACRED)
- [Resource](https://arxiv.org/abs/2305.04582)
- [Resource](https://catalog.ldc.upenn.edu/LDC2018T24)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale, supervised multilingual version of the TACRED relation extraction dataset by machine-translating TACRED instances and projecting entity annotations, and to analyze translation/projection quality and model performance across monolingual, cross-lingual and mixed training scenarios.

**Target Audience**:
- Research community
- Multilingual Natural Language Processing researchers
- Model developers

**Tasks**:
- Relation Extraction
- Cross-lingual transfer evaluation

**Limitations**: Dependence on machine translation quality and automatic annotation projection; token-level alignment is inadequate for compounding and highly inflectional languages; lack of original-language test instances for full evaluation; dataset limited to person- and organization-related relations from news and web text.

## 💾 Data

**Source**: Created by machine-translating the TACRED dataset instances and automatically projecting their token-offset head and tail entity annotations; uses TACRED labels (with option to apply label corrections such as Alt et al. (2020) or Stoica et al. (2021)).

**Size**: Original TACRED splits: 68,124 train; 22,631 dev; 15,509 test (per language before validation); intersection test set available in all languages: 11,874 instances. Total translated source characters: 22.9 million characters. On average 2.3% of instances discarded due to invalid entity tag markup after translation.

**Format**: JSON (same format as original TACRED: tokens, entity types and offsets, label, instance id)

**Annotation**: Entity span annotations and relation labels are automatically projected from the translated token offsets. Manual validation was performed on random samples (100 instances per language) by native speakers; no large-scale manual re-annotation of the full dataset.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Fine-tuning pre-trained language models (mono- and multilingual BERT variants)
- Cross-lingual transfer evaluation (train on English, test on target language)
- Mixed/multilingual training (train on English + varying portions of target language data)
- Back-translation evaluation
- Manual human judgment for translation quality (native speaker judgments on sampled instances)

**Metrics**:
- Micro-F1
- Precision
- Recall

**Calculation**: Micro-F1 is used as the primary evaluation metric. Report median micro-F1 (and precision/recall) over 5 runs with fixed random seeds. Micro-F1 on dev set used for hyperparameter selection.

**Interpretation**: Higher micro-F1 indicates better relation extraction performance. Authors note that absolute scores are not directly comparable across languages due to differences in valid training/test instance counts introduced by translation/validation; therefore they additionally report scores on the intersection test set (instances available in all languages).

**Baseline Results**: English BERT monolingual baseline: median micro-F1 = 77.1 on the original English test set. Monolingual target-language BERT models achieve median micro-F1 scores (testL) ranging, e.g., from 65.1 (Hindi) to 76.4 (Finnish) as reported in Table 2. Cross-lingual and mixed training results and per-language scores are reported in the paper (Tables 2-5).

**Validation**: Automatic validation: check correctness of XML-style entity markup after translation and discard invalid translations (on average 2.3% discarded). Manual validation: for each language, 100 random training instances were judged by a single native speaker answering Q1 (semantic relation preserved) and Q2 (linguistic acceptability). Average Q1 = 87.5% and average Q2 = 83.7%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: ['Possible sensitive content in the data (explicitly noted by authors)', 'Propagation of biases from original TACRED annotations and from MT models (explicitly noted by authors)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors state that they use the original TACRED data "as is"; translations thus reflect biases of the original dataset and of MT models. The authors note that the TACRED authors have not stated measures that prevent collecting sensitive text, and therefore they do not rule out the possible risk of sensitive content in the data.

**Data Licensing**: Publication of the translated dataset is planned depending on LDC requirements for the original TACRED and the underlying TAC corpus. Original TACRED is available under LDC catalog entry LDC2018T24.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
