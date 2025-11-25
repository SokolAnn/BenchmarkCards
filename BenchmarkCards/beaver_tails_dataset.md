# BEAVER TAILS dataset

## 📊 Benchmark Details

**Name**: BEAVER TAILS dataset

**Overview**: We introduce the BEAVER TAILS dataset, aimed at fostering research on safety alignment in large language models (LLMs). This dataset uniquely separates annotations of helpfulness and harmlessness for question-answering pairs. In total, we have gathered safety meta-labels for 333,963 question-answer (QA) pairs and 361,903 pairs of expert comparison data for both the helpfulness and harmlessness metrics. The dataset provides annotations across 14 harm categories and two sets of human-preference rankings (helpfulness and harmlessness).

**Data Type**: question-answering pairs (text)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HH-RLHF
- HH RED-TEAM dataset
- SHP
- REALTOXICITY PROMPTS
- TRUSTFUL QA
- BBQ
- Anthropic red-team dataset

**Resources**:
- [Resource](https://sites.google.com/view/pku-beavertails)
- [GitHub Repository](https://github.com/tatsu-lab/stanford_alpaca)
- [Resource](https://www.mturk.com/)
- [Resource](https://www.upwork.com/)

## 🎯 Purpose and Intended Users

**Goal**: Facilitate safety alignment research for large language models by providing QA pairs annotated with safety meta-labels across 14 harm categories and separate human-preference ranking data for helpfulness and harmlessness.

**Target Audience**:
- ML Researchers
- Model Developers
- LLM Safety Researchers
- Domain Experts working on alignment and content moderation

**Tasks**:
- Question Answering
- Content Moderation
- Preference Ranking
- Reinforcement Learning from Human Feedback

**Limitations**: The authors state limited demographic diversity among crowdworkers may narrow representation of human preference; the 14 harm categories may not cover all harm types and exhibit overlap; some categories (e.g., Child Abuse, Animal Abuse) are imbalanced and underrepresented. The authors acknowledge the dataset could theoretically be used maliciously.

**Out of Scope Uses**:
- the same dataset could theoretically be used to train AI assistants in a harmful or malicious manner

## 💾 Data

**Source**: Red-team prompts derived from the HH RED-TEAM dataset and Safety-Prompts; responses were generated using Alpaca-7B for BEAVER TAILS -30k; dataset iterations include BEAVER TAILS -30k and BEAVER TAILS -330k. Annotations collected from a team of over 70 crowdworkers; quality control performed by AIJet QC team and the research team.

**Size**: BEAVER TAILS -30k: Annotated 30,207 QA-pairs (30,144 pairs of human-preference annotations). BEAVER TAILS -330k: Annotated 333,963 QA pairs; 16,851 unique prompts; 99,734 unique QA pairs; 361,903 pairs of human-preference annotations. Inter-crowdworker agreement rates: safety meta-label = 81.68%, helpfulness preference = 62.39%, harmlessness = 60.91%.

**Format**: N/A

**Annotation**: Two-stage annotation by crowdworkers (70+): Stage 1 - multi-classification across 14 harm categories to assign a safety meta-label (safe/unsafe); Stage 2 - ranking responses per prompt separately for harmlessness and helpfulness. Annotators had college-level education and proficiency in English. Annotations reviewed by AIJet QC team and the research team. Annotators provided confidence scores on a 0-3 scale.

## 🔬 Methodology

**Methods**:
- Human evaluation (crowdworkers)
- QA-moderation model (automated content moderation trained on dataset)
- GPT-4 prompted evaluation
- Bradley-Terry preference modeling for pairwise comparisons
- Training Reward and Cost models (model-based evaluation)
- Safe Reinforcement Learning from Human Feedback using PPO-Lagrangian
- Ablation studies

**Metrics**:
- Inter-annotator Agreement (safety meta-label = 81.68%, helpfulness = 62.39%, harmlessness = 60.91%)
- Accuracy (Reward Model Accuracy = 78.13%)
- Sign Accuracy (Cost Model Sign Accuracy = 95.62%)
- Preference Accuracy (Cost Model Preference Accuracy = 74.37%)
- Model win rates as evaluated by prompted GPT-4 (e.g., Safe-RLHF Helpfulness 85.57%, Harmlessness 82.57%)

**Calculation**: Train-test split of 9:1 for training reward and cost models. Preference modeling uses the Bradley-Terry formulation with negative log-likelihood loss (explicit equations provided). Reward and cost are scalar predictions assigned to the last EOS token. Cost sign used: -1 for safe text, +1 for unsafe text.

**Interpretation**: Distinct separation between safe and unsafe cost score distributions validates the cost model. Higher inter-annotator agreement indicates alignment between annotators and research team. Decoupling helpfulness and harmlessness in human preferences yields measurable performance benefits for safety alignment when compared to single-dimensional preference data.

**Baseline Results**: Reward Model Accuracy: 78.13%. Cost Model Sign Accuracy: 95.62%. Cost Model Preference Accuracy: 74.37%. Ablation/Table 2: Safe-RLHF win rates against Alpaca-7B (evaluated by prompted GPT-4) - Helpfulness: 85.57%, Harmlessness: 82.57%.

**Validation**: Validation via a 9:1 train-test split for static preference models; quality control pipeline where AIJet QC and research team inspect batches (sample at least 10% with minimum 90% agreement for acceptance); inter-annotator agreement reported; evaluations include human, GPT-4, and QA-moderation model comparisons; ablation studies to assess methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Fairness
- Misuse
- Governance

**Atlas Risks**:
- **Fairness**: Data bias
- **Misuse**: Dangerous use
- **Governance**: Lack of testing diversity

**Demographic Analysis**: The authors explicitly state the annotator pool has limited demographic diversity (annotators share similar cultural backgrounds) and plan to expand to platforms such as Amazon Mechanical Turk and Upwork to improve diversity.

**Potential Harm**: ['Hate Speech, Offensive Language', 'Discrimination, Stereotype, Injustice', 'Violence, Aiding and Abetting, Incitement', 'Financial Crime, Property Crime, Theft', 'Privacy Violation', 'Drug Abuse, Weapons, Banned Substance', 'Non-Violent Unethical Behavior', 'Sexually Explicit, Adult Content', 'Controversial Topics, Politics', 'Misinformation Regarding Ethics, Laws and Safety', 'Terrorism, Organized Crime', 'Self-Harm', 'Animal Abuse', 'Child Abuse']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released under CC BY-NC 4.0. Source question sets modified from HH-RLHF (MIT License) and Safety-Prompts (Apache-2.0).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Project reviewed by the Academic Committee of the Institution for Artificial Intelligence at Peking University (served as IRB). The authors state adherence to local labor laws for crowdworkers and report estimated average hourly wages above local minimum wage; quality control and oversight processes described.
