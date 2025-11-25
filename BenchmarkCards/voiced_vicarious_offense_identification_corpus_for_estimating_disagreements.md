# VOICED (Vicarious Offense Identification Corpus for Estimating Disagreements)

## 📊 Benchmark Details

**Name**: VOICED (Vicarious Offense Identification Corpus for Estimating Disagreements)

**Overview**: Annotator-level dataset where annotators label both first-person (personal) and vicarious offense to study disagreement between human moderators of different political leanings and machine moderators in political social web discourse. The dataset "VOICED" consists of 2,310 social web posts and sheds critical insights into how well political groups understand each other's perception of offense, including when sensitive issues such as reproductive rights or gun control/rights are involved.

**Data Type**: text (social web comments / YouTube comments)

**Domains**:
- Natural Language Processing
- Computational Social Science

**Languages**:
- English

**Similar Benchmarks**:
- AHSD
- HASOC
- HatEval
- HateXplain
- OLID
- TRAC
- OHS
- TCC
- Unintended Bias in Toxicity Classification (Jigsaw)

**Resources**:
- [GitHub Repository](https://github.com/Homan-Lab/voiced)

## 🎯 Purpose and Intended Users

**Goal**: To study disagreement in offense perception across human moderators with different political leanings and across multiple machine moderators, introduce the notion of vicarious offense, conduct a large-scale noise audit of offensive speech classifiers, and release the VOICED dataset to enable research on these phenomena.

**Target Audience**:
- Academic researchers
- Industry researchers
- Social media platforms
- Media
- Social web users
- Politicians

**Tasks**:
- Text Classification
- Offensive Language Identification
- Vicarious Offense Prediction
- Annotation for Subjective Labels

**Limitations**: Dataset limited to English posts and primarily focused on one platform (YouTube). Political identities are limited to three categories (Democrat, Republican, Independent); political identities can be far more nuanced than these three options. Annotator population was recruited via Amazon Mechanical Turk and may have demographic biases.

## 💾 Data

**Source**: Annotated subset of social web posts sampled from YouTube comments on official channels of three US cable news networks (CNN, Fox News, MSNBC). The VOICED annotated dataset contains 2,310 social web posts sampled from a larger corpus of 92 million comments on 241,112 news videos; noise-audit experiments used a 3,000,000-comment sample (1,000,000 per channel).

**Size**: 2,310 annotated social web posts (annotated subset); underlying collection: 92,000,000 comments across 241,112 videos; noise-audit sample: 3,000,000 comments (1,000,000 per channel)

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk using Qualtrics. Each instance annotated by 20 annotators with political-identity quotas: at least six annotators from each political identity (Democrat, Republican, Independent). Annotators provided labels for both first-person (personal) offense and vicarious offense (how they think others from another political identity would find the post). Study reviewed by an Institutional Review Board and deemed exempt.

## 🔬 Methodology

**Methods**:
- Human evaluation (crowdsourced annotation of personal and vicarious offense)
- Noise audit (automated evaluation across multiple machine moderators)
- Machine-based evaluation (training BERT-LARGE-CASED models on eight offensive language datasets and using Detoxify ROBERTA and ChatGPT API for comparisons)

**Metrics**:
- Cohen's kappa
- Fleiss' kappa
- Percentage of comments flagged by machine moderators
- Confusion matrices
- offenseScore (count of machine moderators labeling an instance as offensive)

**Calculation**: Pairwise agreement between moderators computed using Cohen's κ. Overall agreement across machine moderators computed using Fleiss' κ. offenseScore(d) is defined as the number of machine moderators that deem a comment d offensive (range [0, N], N=9). Stratified sampling to create DnotOffensive, Ddebated, and Doffensive based on offenseScore thresholds.

**Interpretation**: No machine moderator pair exhibits substantial agreement (κ ≥ 0.81); only a few pairs exhibit moderate agreement (0.41 ≤ κ ≤ 0.60), with many pairs showing fair, slight, or no agreement. A large fraction of content is not flagged by any machine moderators; a very small fraction is flagged by all. offenseScore = 1 indicates high volatility in moderation outcomes; comments with offenseScore in {4,5} represent maximal disagreement among machine moderators.

**Baseline Results**: Overall Fleiss' κ across CNN, Fox, and MSNBC (Dcnn, Dfox, Dmsnbc) are 0.27, 0.25, and 0.22, respectively. Highest human-human Cohen's κ reported between Independents and Democrats is 0.43. Approximately half of content is not flagged by any machine moderators; 0.03% is flagged by all machine moderators. OffenseScore=1 comprises ≈17.5% of content; 10.1% of content has offenseScore in {4,5}.

**Validation**: Pilot study of 270 examples (117 unique annotators) to estimate political representation; enforced minimum annotator quotas (≥6 per political identity) for final study. Final study conducted in 37 batches of 30 items each; each item annotated by 20 annotators. Re-ran pilot batches to ensure quotas. Conducted noise audits across multiple other datasets/platforms (YouTube channels, Twitter, Reddit, Gab) with qualitatively similar results to validate findings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Misuse
- Societal Impact
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Misuse**: Improper usage
- **Societal Impact**: Human exploitation
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Final annotator pool: 35% Democrats (267), 35% Republicans (266), 30% Independents (220). Gender: 47% Female, 53% Male, 1 Non-binary annotator. Race: majority White or Caucasian with limited representation from Asian, Black or African American, and American Indian communities. Age: annotators from all adult age groups with majority in 25-34.

**Potential Harm**: ['Risks of unjust censorship across political groups due to disagreement in offense perception', 'Potential mental-health harms to human moderators exposed to offensive content']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The study used publicly available YouTube API data and the authors state they do not collect or reveal any identifiable information about the annotators.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The annotation study was reviewed by the Institutional Review Board and was deemed exempt.
