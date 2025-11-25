# A Gold Standard Dataset for the Reviewer Assignment Problem

## 📊 Benchmark Details

**Name**: A Gold Standard Dataset for the Reviewer Assignment Problem

**Overview**: Collects and publicly releases a novel gold-standard dataset of reviewers' self-reported expertise (similarity scores) for reviewer-paper pairs to enable principled comparison and development of similarity-computation algorithms. The released dataset consists of 477 self-reported expertise evaluations provided by 58 researchers who evaluated papers they have read previously.

**Data Type**: text (paper titles, abstracts, optional full texts, paper metadata) and numeric self-reported expertise ratings

**Domains**:
- Computer Science

**Resources**:
- [GitHub Repository](https://github.com/niharshah/goldstandard-reviewer-paper-match)
- [Resource](https://forms.gle/SP1Rh8eivGz54xR37)
- [Resource](https://arxiv.org/abs/2303.16750)

## 🎯 Purpose and Intended Users

**Goal**: Collect and release a high-quality dataset of reviewers' expertise that can be used for training and/or evaluation of similarity-computation algorithms for assigning reviewers to papers.

**Target Audience**:
- Research community
- Venue organizers
- Natural Language Processing researchers

**Tasks**:
- Reviewer Assignment
- Expertise Estimation
- Similarity Computation between reviewer profiles and submissions

**Limitations**: Size limitation: 477 data points from 58 researchers. Prominent geographical skew with 74% of participants from the USA. Potential sampling bias (e.g., about 40% of participants affiliated with a certain university). Reliance on Semantic Scholar profiles which are automatically constructed and may be inaccurate. Survey design can influence collected data. Many papers in the dataset are published in or after 2020; citations and incoming citations available in dataset may not reflect information available in real-time conference settings.

## 💾 Data

**Source**: Self-reported expertise evaluations collected via a survey from 58 researchers. Reviewer profiles and paper metadata were obtained from Semantic Scholar (Semantic Scholar IDs and complete bibliographies crawled on May 1, 2022). Papers reported by participants are freely available online where possible (PDF links provided when available).

**Size**: 477 expertise evaluations from 58 participants; 463 unique papers

**Format**: N/A

**Annotation**: Self-reported expertise ratings by participants on a scale from 1.0 to 5.0 with 0.25 step size (1.0 = I am not qualified to review this paper; 5.0 = I have background necessary to evaluate all aspects).

## 🔬 Methodology

**Methods**:
- Human survey (self-reported expertise by participants)
- Automated evaluation metrics (rank-based and ranking metrics)
- Bootstrapping to compute confidence intervals
- Comparative algorithmic evaluation (TPMS, OpenReview algorithms ELMo/Specter/Specter+MFR/Specter2, ACL algorithm, off-the-shelf LLMs)

**Metrics**:
- Weighted Kendall’s Tau distance (normalized loss)
- Accuracy (pairwise ordering accuracy on easy and hard triplets)
- Mean Reciprocal Rank (MRR)@k
- Normalized Discounted Cumulative Gain (NDCG)@k
- Precision@k

**Calculation**: Loss defined as sum over participants of pairwise penalties: for each pair of papers reported by a participant, if algorithm ordering disagrees with ground-truth expertise ordering, penalize by the absolute difference in reported expertise (|ε_i - ε_j|); if algorithm indicates a tie while expertise differs, penalize by half the difference. The unnormalized sum is normalized by the loss of an adversarial algorithm that reverses ground-truth ordering to obtain a final loss in [0,1]. 95% confidence intervals computed by bootstrapping participants (1,000 iterations). Profile construction randomness averaged by repeating profile construction 10 times (or 5 times in some experiments).

**Interpretation**: Lower values of the normalized loss indicate better performance. Higher values of accuracy, MRR, NDCG, and Precision indicate better performance. Authors report error rates corresponding to pairwise comparisons: algorithms make 12%-30% mistakes in easy cases and 36%-43% mistakes in hard cases (as reported in the paper).

**Baseline Results**: Key results reported: Trivial baseline loss 0.50. TPMS loss 0.28 [0.23,0.33]. Specter loss 0.27 [0.21,0.34]. Specter+MFR loss 0.24 [0.18,0.30]. Specter2 (Max Pool) loss 0.22 [0.18,0.26]. ACL loss 0.30 [0.25,0.36]. Off-the-shelf LLMs: o1-mini loss 0.25 [0.21,0.29], Claude Sonnet 3.5 loss 0.31 [0.27,0.35], Gemini 2 Flash loss 0.38 [0.34,0.41]. Easy-triplet accuracies: Specter2 Max Pool 0.89 [0.82,0.94], TPMS (Title+Abstract) 0.80 [0.72,0.87], TPMS (Full Text) 0.84 [0.76,0.91]. Hard-triplet accuracies: TPMS (Title+Abstract) 0.62 [0.54,0.69], TPMS (Full Text) 0.64 [0.56,0.70]; best algorithms on hard triplets reach ~62%-64% accuracy.

**Validation**: Validation via bootstrapping participants (1,000 iterations) to build 95% confidence intervals. Randomness in reviewer profile construction averaged by repeating procedure 10 times (5 times for some TPMS experiments). Exclusions: removed papers not freely available (6 papers) and excluded participants without arXiv-linked papers for certain experiments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness
- Accuracy
- Transparency
- Governance

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Data poisoning
- **Accuracy**: Poor model accuracy, Data contamination
- **Transparency**: Uncertain data provenance
- **Governance**: Unrepresentative risk testing, Lack of testing diversity

**Demographic Analysis**: Participant demographics (Table 1): 58 participants; 78% male; 74% from USA; positions: 45% PhD students, 28% faculty, 12% post-PhD (non-faculty); publications: min 2, max 492, mean 54, median 20.

**Potential Harm**: The dataset and evaluations aim to detect and reduce incorrect reviewer assignments which can lead to poor review quality and negatively impact authors' careers (incorrect reviews may lead to rejection and hurt careers).

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Study performed under Institutional Review Board (IRB) approval. Data will be publicly released in non-anonymized form except email addresses will not be released. The authors explicitly avoid releasing sensitive data and note prior works that could not be released due to privacy concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: IRB approval obtained. No explicit mention of GDPR, CCPA, or other legal/regulatory compliance in the paper.
