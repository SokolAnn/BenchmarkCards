# DIALOCONAN (DIALOgiCOunter-NArratives collectioN)

## 📊 Benchmark Details

**Name**: DIALOCONAN (DIALOgiCOunter-NArratives collectioN)

**Overview**: The paper presents a hybrid human-machine approach to collect dialogical data for hate speech countering and introduces DIALOCONAN, the first dataset comprising over 3,000 fictitious multi-turn dialogues between a hater and an NGO operator covering 6 targets of hate, obtained by combining human expert annotators over machine-generated dialogues produced with 19 different configurations.

**Data Type**: text (multi-turn dialogues: hate speech and counter-narrative turns)

**Domains**:
- Natural Language Processing
- Social Media

**Languages**:
- English

**Similar Benchmarks**:
- Fanton et al. (2021) dataset
- Qian et al. (2019) (A benchmark dataset for learning to intervene in online hate speech)
- CONAN (COunter NArratives through nichesourcing)

**Resources**:
- [GitHub Repository](https://github.com/marcoguerini/CONAN)
- [Resource](https://getthetrollsout.org/stoppinghate)
- [GitHub Repository](https://github.com/PrithivirajDamodaran/Styleformer)
- [Resource](https://arxiv.org/abs/2211.03433)

## 🎯 Purpose and Intended Users

**Goal**: To create a multi-turn dialogue dataset (DIALOCONAN) of counter narratives to hate speech by testing 19 hybrid human-machine data collection strategies, enabling training and analysis of models for counter narrative generation in dialogical scenarios.

**Target Audience**:
- Researchers
- Natural Language Processing researchers
- Model developers
- NGO practitioners

**Tasks**:
- Dialogue Generation
- Counter Narrative Generation
- Natural Language Generation

**Limitations**: The dataset is English-only; seed DIALO gold is small (222 dialogues) and PAIRS gold is a subset extracted from Fanton et al. (2021). The dataset dialogues have strictly controlled numbers of turns (4, 6, or 8) which might not reflect more natural turn counts. The final data obtained via human-machine collaboration may not match the quality obtainable by niche sourcing the whole dataset to skilled NGO operators. Translating the dataset to other languages may lose cultural and contextual nuances.

**Out of Scope Uses**:
- Use of the trained models as part of a live system (the paper states the models are not meant to be deployed as part of a live system).
- Use of the dialogue dataset beyond research purposes without appropriate safeguards (the paper states the dialogue dataset will be made available for research purposes).

## 💾 Data

**Source**: Created from two expert-based seed resources and machine generation: (i) DIALO gold: 222 fictitious dialogues written by two expert NGO operators; (ii) PAIRS gold: HS/CN pairs extracted from the Fanton et al. (2021) dataset (originally 5,000 HS/CN pairs) aligned to the 6 targets; plus machine-generated dialogues produced via 19 hybrid author configurations (concatenation, paraphrasing, and LM generation) and post-edited by trained reviewers.

**Size**: 3059 dialogues (total), 16,625 turns; seed DIALO gold: 222 dialogues; PAIRS gold: 5,000 HS/CN pairs (subset used for the 6 targets).

**Format**: N/A

**Annotation**: Post-editing by trained annotators: three annotators (internship students) were extensively trained following Fanton et al. (2021) methodology and session-specific guidelines; annotators post-edited machine-generated dialogue candidates in an author-reviewer pipeline; mitigation procedures for annotator welfare were applied (work limits, breaks, weekly meetings, explanation of prosocial research aims).

## 🔬 Methodology

**Methods**:
- Human-in-the-loop data collection (author-reviewer pipeline: machine author strategies + human reviewer post-editing)
- Concatenation strategies (random, Jaccard similarity, cosine similarity, keyword matching)
- Paraphrasing strategies (Protaugment, Style paraphraser, Styleformer with style transfer)
- Language Model generation (DialoGPT, T5-based configurations) with fine-tuning and Top-p decoding
- Human post-editing and reviewer guidelines per session

**Metrics**:
- Human-targeted Translation Edit Rate (HTER)
- Turn deletion (percentage)
- Turn swap (percentage)
- Novelty (Jaccard-based similarity)
- Repetition Rate (RR, rate of non-singleton n-gram types)
- Syntactic metrics: Maximum Syntactic Depth (MSD), Average Syntactic Depth (ASD), average turn length, average number of sentences (NST)

**Calculation**: HTER measures post-editing effort (used as efficiency metric); a value above 0.4 is considered to indicate low quality outputs. Novelty is computed via Jaccard similarity against reference dialogues. Repetition Rate (RR) measures language diversity using the rate of non-singleton n-gram types. Syntactic metrics are computed at turn-level as reported in the paper.

**Interpretation**: Higher HTER and higher turn deletion indicate lower efficiency/higher post-editing effort (HTER > 0.4 generally signals low-quality outputs). Higher turn swap indicates need to reorder content; higher Novelty indicates greater lexical difference from reference/gold data; lower RR after post-editing indicates increased diversity. Syntactic depth metrics indicate complexity of generated turns.

**Baseline Results**: Session 3 baseline model results (selected figures from Table 3): DGPT_b: 50.179 deleted turns, HTER 0.678, swap 8.214, RRgen 7.815, RRed 3.976, NOV t-g 0.793, t-e 0.804, g-g 0.787, g-e 0.793. DGPT_mt: 16.786 deleted turns, HTER 0.408, swap 10.714, RRgen 8.587, RRed 6.110, NOV t-g 0.757, t-e 0.759, g-g 0.798, g-e 0.799. T5b-1m: 76.875 deleted turns, HTER 0.655, swap 0, RRgen 16.672, RRed 5.651, NOV t-g 0.789, t-e 0.817, g-g 0.783, g-e 0.804. (Additional model variations and metrics are reported in the paper's tables.)

**Validation**: Training/dev/test splits for generation models used an 8:1:1 ratio. Annotators practiced on a small training set and guidelines were updated iteratively. A senior NGO expert performed a qualitative evaluation on a random sample of post-edited dialogues and approved dialogues from each session. Annotator training and session-specific reviewing procedures were used to validate data quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Robustness
- Misuse
- Accuracy
- Societal Impact

**Atlas Risks**:
- **Privacy**: Reidentification
- **Robustness**: Hallucination
- **Misuse**: Improper usage
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Human exploitation

**Demographic Analysis**: The dataset includes explicit target labels and distribution across six targets: JEWS (468 dialogues), LGBT+ (591 dialogues), MIGRANTS (534 dialogues), MUSLIMS (505 dialogues), POC (493 dialogues), WOMEN (462 dialogues); total 3,059 dialogues (see Table 5).

**Potential Harm**: ['Aims to detect and provide training data to counter online hate speech and reduce linguistic violence against protected groups', 'Aims to support NGOs and researchers in producing counter narratives to mitigate spread and effects of hateful content']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset is created from scratch via fictitious dialogues to avoid exposing NGO operators; scraping NGO operators' real interactions was explicitly avoided to prevent doxing/reidentification. The paper states the dataset 'does not pose any threat to personal privacy or individual rights' due to this approach.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
