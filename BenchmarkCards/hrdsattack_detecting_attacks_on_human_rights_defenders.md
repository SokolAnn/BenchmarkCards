# HRDsAttack (Detecting Attacks on Human Rights Defenders)

## 📊 Benchmark Details

**Name**: HRDsAttack (Detecting Attacks on Human Rights Defenders)

**Overview**: A new dataset (HRDsAttack) of crowdsourced annotations on 500 online news articles for detecting attacks on human rights defenders. Annotations include 13 fine-grained event attributes capturing perpetrator, violation type, victim information, location, and time. The dataset is used to train and evaluate baseline models on several sub-tasks to predict the annotated characteristics.

**Data Type**: text (news articles: article title, article body text, publication time)

**Domains**:
- Natural Language Processing
- Human Rights

**Languages**:
- English

**Similar Benchmarks**:
- ACE05
- ERE
- ACE05-E
- ACE05-E+
- ACLED

**Resources**:
- [GitHub Repository](https://github.com/dataminr-ai/HRDsAttack)
- [Resource](https://www.gdeltproject.org/)
- [Resource](https://www.ohchr.org/Documents/Issues/HRIndicators/SDG_Indicator_16_10_1_Guidance_Note.pdf)
- [Resource](https://arxiv.org/abs/2306.17695)

## 🎯 Purpose and Intended Users

**Goal**: Enable automatic extraction of fine-grained event details about attacks on human rights defenders from news articles to support retrospective analyses over time and by location, and to facilitate NLP research and AI for Social Good applications in the human rights domain.

**Target Audience**:
- Human Rights Organizations
- ML Researchers
- Model Developers
- AI for Social Good researchers

**Tasks**:
- Event Extraction
- Information Extraction
- Question Answering

**Limitations**: English-only dataset; limited number of documents (500 articles); some label imbalance remains (e.g., PERPETRATOR TYPE); annotation ambiguity for some attributes (e.g., REGION vs CITY) and instruction quality could be improved.

## 💾 Data

**Source**: Online news articles sampled from the GDELT database following the CAMEO codebook; initial scrape of 80,112 articles from 2019/09/01 to 2022/05/01, filtered and targeted-sampled for minority classes.

**Size**: 500 annotated news articles; train: 300, dev: 100, test: 100; total tokens: 509,607; total number of victims: 1,163.

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk with a qualification task to recruit top-performing Turkers (US-based Turkers with HIT approval rate >90% and >500 approved HITs, recruited Turkers required >=75% average accuracy on qualification); full annotation by qualified Turkers (no replication during full tasks); compensation final pay rate $15.00 per hour.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation (baseline models)
- Multi-task Sequence-to-Sequence Question Answering evaluation using T5

**Metrics**:
- Precision
- Recall
- F1 Score
- Accuracy
- Fuzzy Match Precision
- Fuzzy Match Recall
- Fuzzy Match F1

**Calculation**: Precision, Recall, and F1 Score are used for PERPETRATOR MENTION and VIOLATION TYPE. Accuracy (percentage correct) is used for PERPETRATOR TYPE, VICTIM TYPE, VICTIM SEXTYPE, VICTIM AGE GROUP, COUNTRY, REGION, CITY, YEAR, MONTH, and DAY. For VICTIM NAME, both exact-match precision/recall/F1 and fuzzy-match precision/recall/F1 (a predicted name is correct if it has overlapping tokens with a ground-truth name) are reported.

**Interpretation**: Higher Precision/Recall/F1 and Accuracy indicate better model performance on the respective event attributes. The paper selects a hybrid T5-based model based on dev set performance; attributes with low scores (e.g., REGION, DAY) indicate areas needing improvement.

**Baseline Results**: Test set (selected metrics for Hybrid model): Perpetrator Mention Precision 93.81, Recall 100.00, F1 96.81; Perpetrator Type Accuracy 62.00; Victim Name Exact Match F1 47.44, Fuzzy Match F1 51.16; Violation Type F1 71.39; Country Accuracy 66.00; Region Accuracy 3.00; City Accuracy 23.00; Year Accuracy 46.00; Month Accuracy 33.00; Day Accuracy 14.00. (Full results reported in Table 5 of the paper.)

**Validation**: Data split into train/dev/test with a 3:1:1 ratio (300/100/100). Dev set used for model selection (hybrid strategy). Pilot studies computed Turker agreement (average pair-wise Cohen-Kappa scores) and informed qualification criteria; targeted sampling used to mitigate class imbalance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Governance
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Governance**: Lack of data transparency
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Detecting and summarizing attacks on human rights defenders (e.g., Arbitrary Detention, Enforced Disappearance, Killing, Kidnapping, Torture, Sexual violence and other harmful acts)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
