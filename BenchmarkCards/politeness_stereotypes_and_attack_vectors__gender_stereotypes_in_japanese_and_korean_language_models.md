# Politeness Stereotypes and Attack Vectors: Gender Stereotypes in Japanese and Korean Language Models

## 📊 Benchmark Details

**Name**: Politeness Stereotypes and Attack Vectors: Gender Stereotypes in Japanese and Korean Language Models

**Overview**: We study how grammatical gender bias relating to politeness levels manifests in Japanese and Korean language models. We analyze relative prediction probabilities of the male and female grammatical genders using templates and find that informal polite speech is most indicative of the female grammatical gender, while rude and formal speech is most indicative of the male grammatical gender. We introduce an attack dataset to (i) identify representational gender bias across politeness levels, (ii) demonstrate how gender biases can be abused to bypass cyberbullying detection models and (iii) show that allocational biases can be mitigated via training on our proposed dataset.

**Data Type**: text (template-generated sentences and modified tweets / attack examples)

**Domains**:
- Natural Language Processing
- Online Abuse / Social Media Moderation

**Languages**:
- Japanese
- Korean

**Similar Benchmarks**:
- CrowS-Pairs
- StereoSet
- HateCheck
- Multilingual HateCheck

**Resources**:
- [GitHub Repository](https://github.com/VSteinborn/politeness-attacks)
- [Resource](https://www.surgehq.ai)
- [Resource](https://www.jlpt.jp/e/)
- [Resource](https://www.topik.go.kr)
- [Resource](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2)

## 🎯 Purpose and Intended Users

**Goal**: Examine how politeness-level-related gender stereotypes manifest in Japanese and Korean pretrained language models; introduce an attack dataset to measure representational and allocational gender biases across politeness levels; demonstrate how politeness can be used to evade cyberbullying detection and show mitigation via few-shot training on the proposed dataset.

**Target Audience**:
- NLP Researchers
- NLP Practitioners
- Model Developers

**Tasks**:
- Bias Evaluation (representational bias probing of Masked Language Models)
- Toxicity / Cyberbullying Detection
- Few-shot Model Training (SetFit / SentenceBERT)

**Limitations**: Limited to a select set of verbs and basic politeness levels in Korean and Japanese; other classes of verbs and more nuanced politeness expressions (titles, alternative nouns, alternative politeness constructions) are not considered.

## 💾 Data

**Source**: Representational data: verbs taken from standardized language proficiency tests (142 Japanese verbs from JLPT and 107 Korean verbs from TOPIK) combined with template slots (speaker nouns, speaker verb endings, narrator verb endings) to generate sentences. Allocational (attack) data: balanced toxic tweet dataset from Surge AI (professional data labeling platform) which is template-modified by appending gender terms and politeness-level narrator verb forms to generate attack examples.

**Size**: Representational datasets: 3,852 sentences for Korean and 4,260 sentences for Japanese. Attack dataset: 39,160 sentences total (= (987 - 8) unique tweets × 8 gender terms × (6 - 1) politeness levels). Training (few-shot) set: 392 examples (8 original tweets + 384 template-modified examples). Additional counts: 142 JLPT verbs and 107 TOPIK verbs; 987 original tweets in Surge AI dataset.

**Format**: N/A

**Annotation**: Attack dataset examples were automatically generated via templates. The underlying tweet dataset from Surge AI is a balanced (50/50) toxic tweet dataset labeled via the professional data labeling platform Surge AI.

## 🔬 Methodology

**Methods**:
- Template-based probing of Masked Language Models (MLMs) using masked-token prediction
- Evaluation of cyberbullying detection models on template-modified attack data
- Few-shot training using SetFit with SentenceBERT
- Statistical analysis (ANOVA and F-/p-tests) to assess significance of differences

**Metrics**:
- F1 Score
- Log prediction probabilities (log p)
- ANOVA (F statistic, p-values)

**Calculation**: Representational bias measured as the average difference between the logs of prediction probabilities: logp(mask=she) - logp(mask=he) across sentences. ANOVA (F- and p-tests) used to test whether means across politeness levels differ. F1 scores computed to evaluate cyberbullying detection performance on original, attack, and gender-only test sets.

**Interpretation**: Negative mean log probability differences (logp(she) - logp(he)) indicate more male-biased predictions (i.e., models prefer 'he' over 'she'). Higher F1 Score indicates better cyberbullying detection performance. Drops in baseline F1 under politeness-level attacks indicate vulnerability; maintenance of high, gender-equal F1 indicates mitigation success.

**Baseline Results**: Baseline cyberbullying model (Shibata et al., 2022) tweets_only F1 = 0.40; proposed SentenceBERT model tweets_only F1 = 0.82. Table 3 in the paper reports F1 scores across politeness and gender terms showing the baseline degrades under attacks while SentenceBERT remains comparatively robust.

**Validation**: Verified approximate normality and similar variances of log probabilities across politeness levels before applying ANOVA; performed ANOVA tests with reported F and p values. Ensured no overlap between training and evaluation data for few-shot experiments by removing the 8 training tweets from evaluation. Default SetFit parameters were used for few-shot training; training/validation times and hardware reported.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Misuse
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias, Decision bias
- **Robustness**: Evasion attack
- **Misuse**: Improper usage
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Includes analysis of gender associations across ten stereotypical locations (male-dominated and female-dominated spaces) and reports mean log probability differences between 'she' and 'he' for each location.

**Potential Harm**: ['Enabling evasion of cyberbullying detection systems (attackers can abuse politeness-levels to bypass detection and push hate speech onto platforms)', 'Propagation and reinforcement of gender stereotypes via model behavior and publicly available attack vectors', 'Unequal detection rates across grammatical genders leading to allocational harms (different protection by moderation systems)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
