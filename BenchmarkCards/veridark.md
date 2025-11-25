# VeriDark

## 📊 Benchmark Details

**Name**: VeriDark

**Overview**: We release VeriDark: a benchmark comprised of three large scale authorship verification datasets and one authorship identification dataset obtained from user activity from either Dark Web related Reddit communities or popular illicit Dark Web market forums.

**Data Type**: text (forum comment pairs for authorship verification; single forum comments for author identification)

**Domains**:
- Natural Language Processing
- Cybersecurity
- Forensics

**Languages**:
- English

**Similar Benchmarks**:
- PAN authorship verification datasets
- PAN20-small
- PAN20-large
- CLEF Initiative

**Resources**:
- [GitHub Repository](https://github.com/bit-ml/VeriDark)
- [Resource](https://veridark.github.io/)
- [Resource](https://zenodo.org/record/6998371)
- [Resource](https://zenodo.org/record/7018853)
- [Resource](https://zenodo.org/record/6998375)
- [Resource](https://zenodo.org/record/6998363)

## 🎯 Purpose and Intended Users

**Goal**: To enable the development and evaluation of modern authorship verification models in a cybersecurity forensics context, and to facilitate the evaluation of existing authorship verification methods under a domain shift to Dark Web data.

**Target Audience**:
- Machine Learning Researchers
- Academic Researchers
- Law Enforcement Analysts
- Security Practitioners

**Tasks**:
- Authorship Verification
- Authorship Identification
- Authorship Attribution

**Limitations**: Noisy negative examples: distinct authorship labels may be wrong due to users having multiple accounts (Sybils). Noisy positive examples: multiple users may write under the same account. Shorter texts in Dark Web forums reduce per-sample information. No formal internal ethical review process was conducted.

**Out of Scope Uses**:
- Language Modeling or other generative model training (explicitly not recommended)
- Building algorithms to help criminals evade law enforcement
- Building algorithms that aim to unmask undercover law enforcement agents
- Exposing identities of reporters, whistleblowers, dissidents, or other vulnerable individuals
- Any use intended to discriminate or exacerbate bias against protected groups

## 💾 Data

**Source**: DarkReddit+: comments from the /r/darknetmarkets subreddit retrieved from a Reddit comments archive (Baumgartner et al.). Agora and SilkRoad1: comments extracted from archived DarkNet marketplace forums (Branwen / DNM-archives).

**Size**: Agora: 4,195,381 train, 216,570 validation, 219,171 test (total 4,631,122 examples). SilkRoad1: 614,656 train, 34,300 validation, 32,255 test (total 681,211 examples). DarkReddit+ (authorship verification): 106,252 train, 6,124 validation, 6,633 test (total 119,009 pairs). DarkReddit+ (author identification): 6,817 train, 2,275 validation, 2,276 test (total 11,368 examples).

**Format**: JSON Lines (.jsonl)

**Annotation**: Automatically generated labels: 'same author' pairs created by pairing comments from the same anonymized username; 'different author' pairs created by sampling comments from different anonymized usernames. Preprocessing: PGP signatures/keys removed, duplicate messages removed, non-English messages removed (langdetect), comments with less than 200 characters removed, usernames anonymized.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (BERT fine-tuning baselines)
- Automated metrics

**Metrics**:
- F1 Score
- F0.5 Score
- C@1
- Area Under ROC Curve (AUROC)
- avg (mean of F1, F0.5, C@1 and AUROC)

**Calculation**: For evaluation, documents are split into 254-token chunks; matching-index chunk pairs are fed to the model to obtain probabilities which are averaged across chunk pairs for final prediction. 'avg' is computed as the arithmetic mean of F1, F0.5, C@1 and AUROC. Models optimized with binary cross-entropy during training.

**Interpretation**: Higher metric values indicate better authorship verification performance. In-domain training (train and test on the same dataset) yields the best performance; cross-dataset performance is lower. Training on the aggregated All dataset yields more robust cross-dataset performance.

**Baseline Results**: BERT-based baselines (mean over 5 runs) achieved avg. scores when training/testing in-domain: DarkReddit+ avg = 77.2; SilkRoad1 avg = 84.6; Agora avg = 88.1. Training on All and testing on All yields avg = 87.1.

**Validation**: Train/validation/test splits are author-disjoint with approximate ratios 90%/5%/5% (open-set authorship verification). Experiments report mean and standard deviation over 5 runs. Evaluation uses chunk pairing and averaged probabilities as described in calculation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Misuse
- Societal Impact
- Accuracy
- Data Laws

**Atlas Risks**:
- **Privacy**: Personal information in data, Reidentification, Exposing personal information
- **Misuse**: Improper usage, Nonconsensual use
- **Societal Impact**: Impact on affected communities
- **Accuracy**: Data contamination
- **Data Laws**: Data usage restrictions

**Demographic Analysis**: The benchmark does not identify demographic subpopulations (age, gender, race, political opinion, etc.). The datasets may nevertheless contain sensitive attributes (race, political opinion, location, etc.).

**Potential Harm**: ['Facilitating detection of illicit activity on Dark Web forums (intended forensic use)', 'Supporting law enforcement forensic analysis (authors state this as a goal) ']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Usernames were anonymized, PGP signatures/keys/messages were removed, non-English messages removed, and comments under 200 characters removed. Access to datasets is restricted; users requesting access must disclose name/affiliation/intended use and acknowledge ethical use. A contact form is provided for removal requests.

**Data Licensing**: The VeriDark datasets are distributed under the CC-BY-4.0 license. The DarkNet archive used as a raw source was released under CC0 by its collector.

**Consent Procedures**: Individuals whose comments were used were not informed that their data would be used for this research (no direct consent obtained).

**Compliance With Regulations**: No formal data protection impact analysis has been performed. Access restrictions and ethical safeguards are applied at distribution, but explicit compliance with specific regulations (e.g., GDPR) is not stated.
