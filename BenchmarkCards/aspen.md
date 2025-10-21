# ASPEN

## 📊 Benchmark Details

**Name**: ASPEN

**Overview**: Specifically, we introduce a new task of crosslingual story generation: given a plan in English, generate a coherent narrative in a target language which is consistent with the contents of the plan.

**Data Type**: text (English plans and parallel target-language stories)

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Amdo Tibetan
- Haitian Creole
- Polish
- Arabic
- Hindi
- Punjabi
- Bengali
- Hungarian
- Romanian
- Chinese
- Italian
- Russian
- Danish
- Japanese
- Spanish
- Dutch
- Khams Tibetan
- Swedish
- Esperanto
- Korean
- Tibetan
- German
- Kurdish
- Turkish
- Greek
- Pashto
- Urdu
- Gujarati
- Persian
- Vietnamese
- Yue Chinese

**Similar Benchmarks**:
- MTG
- ROCStories

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Given a plan in English, generate a coherent narrative in a target language which is consistent with the contents of the plan.

**Target Audience**:
- Researchers

**Tasks**:
- Story Generation
- Crosslingual Generation

**Limitations**: Given its small size, ASPEN is intended primarily as an evaluation corpus. We mainly focused on three Indo-European languages, namely Russian, German, and Italian. Another limitation concerns the use of the large language model itself which is feasible only with large computational resources. Throughout this paper, we have assumed that the plans are provided to the PLM (i.e., plans are not generated).

**Out of Scope Uses**:
- Benchmarking LLMs on ASPEN is out of scope of this paper

## 💾 Data

**Source**: Collated from the Global African Storybook Project (Global ASP). ASPEN is based on Global ASP.

**Size**: Global ASP consists of over 40 stories and translations into 55 languages. ASPEN contains stories in 31 languages. Focus languages: English: 28 stories; German: 28 stories; Italian: 28 stories; Russian: 10 stories.

**Format**: N/A

**Annotation**: Plans are created manually based on English stories. Target-language stories are parallel translations (manual native speaker translations).

## 🔬 Methodology

**Methods**:
- Few-shot prompting (in-context learning) with PaLM
- Fine-tuning mT5-XL baseline
- Automatic metrics
- Human evaluation (crowdworkers, 3 annotators per story)

**Metrics**:
- Vocabulary-to-token ratio
- Intra-story repetition (proportion of repeated trigrams)
- Inter-story repetition (proportion of trigrams repeated between stories)
- MAUVE
- SentencePiece-ROUGE
- Human evaluation: Relevance, Fluency, Coherence, Engagement (3-point Likert scale)
- Average story length (SentencePiece tokens)
- Percentage of stories containing direct speech

**Calculation**: MAUVE is computed with GPT-2 and uses gold reference stories in the target language as the set of human-written texts. SentencePiece-ROUGE uses language-independent SentencePiece tokenization. Repetition metrics are measured as proportions of trigrams repeated (intra- and inter-story). Human evaluation uses three annotators per story on a 3-point Likert scale.

**Interpretation**: For vocabulary-to-token ratio higher is better (less repetitive vocabulary). For intra- and inter-story repetition lower is better. MAUVE measures similarity between distributions of human-written and machine-generated text (higher is better). SentencePiece-ROUGE measures similarity to reference stories. Human ratings: 3 is best, 1 is worst.

**Baseline Results**: Baselines include mT5-XL (fine-tuned) and Google Translate as an upper bound. The paper reports that Google Translate (upper bound) performs quite well, approaching human parity on some automatic metrics, while mT5 performs poorly on inter-story repetition and ROUGE. (See paper tables for detailed per-model numerical results.)

**Validation**: Few-shot setup: three plan-story examples per language used as demonstrations; remaining stories in ASPEN treated as test data. Human evaluation: each story evaluated by three native-speaker annotators on Relevance, Fluency, Coherence, and Engagement. Automatic metrics computed against gold reference translations.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
