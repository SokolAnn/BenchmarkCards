# CoLAC - Corpus of Linguistic Acceptability in Chinese

## 📊 Benchmark Details

**Name**: CoLAC - Corpus of Linguistic Acceptability in Chinese

**Overview**: We introduce CoLAC - Corpus of Linguistic Acceptability in Chinese, the first large-scale acceptability dataset for a non-Indo-European language. It is verified by native speakers and is the first acceptability dataset that comes with two sets of labels: a linguist label and a crowd label.

**Data Type**: text (sentences with acceptability labels)

**Domains**:
- Natural Language Processing
- Linguistics

**Languages**:
- Mandarin Chinese

**Similar Benchmarks**:
- CoLA
- ItaCoLA
- RuCoLA
- BLiMP
- CLiMP
- SyntaxGym

**Resources**:
- [GitHub Repository](https://github.com/huhailinguist/CoLAC)
- [Resource](https://arxiv.org/abs/2305.14091)

## 🎯 Purpose and Intended Users

**Goal**: Introduce the first large-scale non-Indo-European acceptability dataset handcrafted by linguists to evaluate the grammatical proficiency of language models.

**Target Audience**:
- Machine Learning Researchers
- Computational Linguists
- Model Developers

**Tasks**:
- Text Classification
- Acceptability Judgment

**Limitations**: The paper notes that with only two datasets (CoLA and CoLAC) they are not able to ascertain how much acceptability ability is learned during pre-training versus how much comes from cross-lingual transfer during fine-tuning.

## 💾 Data

**Source**: Collected from one syntax textbook (The Syntax of Chinese, Huang et al. 2009, examples partitioned/verified by Chen et al. 2020b), one handbook (Handbook of Chinese Linguistics, Huang et al. 2018), and 68 linguistics journal articles (Hu et al., in preparation); all examples verified by native Mandarin speakers.

**Size**: 7,495 sentences

**Format**: N/A

**Annotation**: Each example has two labels: (1) a linguist label from the original source (label0), and (2) a crowd label (label1) mapped from mean ratings. Unverified sentences were rated by at least five native Mandarin speakers on a 4-point Likert scale (1 very unnatural to 4 very natural). 485 participants contributed to the annotation; the crowd label is adopted as the ground truth.

## 🔬 Methodology

**Methods**:
- Supervised fine-tuning
- Prompt-tuning
- Few-shot in-context learning
- Cross-lingual transfer experiments
- Human evaluation
- Ensembling

**Metrics**:
- Matthews Correlation Coefficient (MCC)
- Percentage of acceptable sentences (dataset statistics)

**Calculation**: Matthews Correlation Coefficient (MCC) is used for both human and model performance. MCC ranges from -1 to 1; in this work MCC is multiplied by 100 and presented between -100 and 100. Human MCC is computed by measuring each subject's annotation against the final aggregated labels for their assigned sentence list and averaging across all 485 contributors. For model results, reported values are medians across five random seeds where applicable.

**Interpretation**: Higher MCC indicates better correlation with ground truth acceptability labels. The paper reports human MCC of 65.11; supervised models score below human (e.g., ensembled Chinese RoBERTa 59.03 MCC on test), ChatGPT scores substantially below supervised models (48.30 MCC), and InstructGPT models perform near chance on CoLAC.

**Baseline Results**: Human performance: 65.11 MCC. Supervised baselines: XLM-R dev 56.45 MCC, XLM-R test 54.08 MCC; prompt-tuned XLM-R dev 54.66 MCC; Chinese RoBERTa dev 56.95 MCC; Chinese RoBERTa ensembled dev 58.07 MCC, test 59.03 MCC. ChatGPT dev 47.82 MCC, test 48.30 MCC.

**Validation**: Dataset split into train/dev/test with same label distributions; development set used to avoid overfitting and for most reported results. Inter-run variance mitigated by reporting medians across five random seeds for training. Human verification performed with 485 native speakers; developer-verified subsets and linguist labels retained for analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: The paper notes that dialectal background and individual interpretation can affect acceptability judgments and that there is inter-annotator disagreement, but no demographic breakdown of annotators is provided.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
