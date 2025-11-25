# MORAL INTEGRITY CORPUS (MIC Ἲ4)

## 📊 Benchmark Details

**Name**: MORAL INTEGRITY CORPUS (MIC Ἲ4)

**Overview**: The MORAL INTEGRITY CORPUS (MIC Ἲ4) is a new dataset for benchmarking open-domain dialogue systems that captures the moral assumptions of 38k prompt-reply pairs using 99k distinct Rules of Thumb (RoTs). It represents interpretable RoT judgments with structured attributes (Alignment, Global Consensus, Violation Severity, Moral Foundations) and is intended to facilitate systematic understanding of the intuitions, values, and moral judgments reflected in chatbot utterances.

**Data Type**: prompt-reply pairs (text) and textual Rules of Thumb (RoTs)

**Domains**:
- Natural Language Processing
- Human-Computer Interaction

**Languages**:
- English

**Similar Benchmarks**:
- SOCIAL-CHEM-101
- MORAL STORIES
- ETHICS
- SCRUPLES
- Social Chemistry 101

**Resources**:
- [GitHub Repository](https://github.com/GT-SALT/mic)
- [GitHub Repository](https://github.com/FionnD/Reddit-QA-Corpus)
- [Resource](https://arxiv.org/abs/2204.03021)

## 🎯 Purpose and Intended Users

**Goal**: Provide a resource to systematically observe and benchmark the moral assumptions and normative social commonsense reasoning of conversational agents by collecting prompt-reply pairs annotated with Rules of Thumb (RoTs) and structured attributes.

**Target Audience**:
- Machine Learning Researchers
- Conversational AI / Chatbot Developers
- Domain Experts for moderation and safety

**Tasks**:
- Text Generation
- Text Classification
- Multi-label Classification
- Ordinal Regression

**Limitations**: Dataset limited to English-language prompts and U.S.-based Amazon Mechanical Turk annotators; annotations reflect annotators' worldviews; Reddit prompts are demographically skewed; RoTs are descriptive not authoritative.

**Out of Scope Uses**:
- Treating RoTs as global or universally binding ethical judgments is out-of-scope (RoTs are not designed to form a cohesive and universal ethical system).
- Using the Moral Transformers' judgments as moral advice is out-of-scope (the authors state judgments should not be taken as moral advice).

## 💾 Data

**Source**: Prompts were compiled from a pre-existing public collection of r/AskReddit posts (Fionn Delahunty, 2018). Each prompt was fed to three chatbot systems (BlenderBot, DialoGPT, GPT-Neo) to obtain replies; responses were filtered using keyword filtering (Expanded Moral Foundations Dictionary and subjective-word filter) and an ALBERT-based classifier for moral/sufficient content; retained examples were annotated by Amazon Mechanical Turk workers.

**Size**: 38,000 unique prompt-reply pairs; 99,000 distinct Rules of Thumb (RoTs); 114,000 annotated prompt-reply-RoT sets

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk. Three annotators independently drafted a RoT per prompt-reply pair; annotators answered attribute questions (Reply Alignment, Global Consensus, Violation Severity, Moral Foundations) and provided a Revised Answer. Secondary task: three annotators per RoT provided attribute annotations. Qualification test, staging round, automated and manual quality checks, and IRB review were used.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Model-based evaluation (fine-tuning language models, retrieval baselines)
- Transfer learning experiments

**Metrics**:
- ROUGE-1
- ROUGE-2
- ROUGE-L
- BLEU
- BERTScore
- Precision
- Recall
- F1 Score
- Mean Squared Error (MSE)
- Pearson correlation (r)
- Human evaluation: Well-formedness, Fluency (1-5), Relevance (1-5)
- Inter-annotator agreement (ICC, Krippendorf's alpha)

**Calculation**: For generation metrics, when three ground-truth RoTs exist per prompt-reply, the maximum score across the three ground truths was taken for each metric. Attribute tasks used train/dev/test splits and appropriate loss formulations: ordinal regression with MSE for Severity and Consensus, Binary Cross Entropy for multi-label Moral Foundations, and standard classification losses for alignment. Experiments used an 80-10-10 train-dev-test split ensuring no prompt-reply pair appears in multiple splits.

**Interpretation**: Models approaching human levels on well-formedness, fluency, and relevance are considered strong; ROUGE/BLEU/BERTScore and human ratings indicate quality. The paper notes that even top models generate irrelevant RoTs (relevance < 2) about 28% of the time, indicating that lower relevance or low human evaluation scores indicate poor performance.

**Baseline Results**: Best performing T5 model achieves ROUGE-L ≈ 52.6 (paper cites ROUGE-L ≈ 53). Attribute classification: ALBERT achieves r=0.59 (Severity), r=0.44 (Consensus), Alignment F1 = 76.0, Moral Foundations F1 scores vary (e.g., Care 75.3, Fairness 59.6, Liberty 58.0, Loyalty 62.7, Authority 54.3, Sanctity 40.8). RoT generation human-eval relevance for best models approaches human levels (relevance ≈ 4.03 for beam-decoded models in human eval).

**Validation**: 80-10-10 train-dev-test split with no overlap of prompt-reply pairs across splits; human evaluation with three workers per generation on sampled generations; inter-annotator agreement measured (ICC and Krippendorf's alpha reported for attributes); qualification tests and staging rounds for annotators; automated and manual quality control procedures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Misuse

**Atlas Risks**:
- **Data Laws**: Data usage restrictions
- **Misuse**: Improper usage
- **Societal Impact**: Human exploitation

**Demographic Analysis**: Annotators were U.S.-based English-speaking Amazon Mechanical Turk workers who self-reported political leaning and completed an abbreviated Moral Foundations Questionnaire. The worker pool is primarily liberal; the paper reports 25% of workers are conservative-leaning and 22% of annotations were written by conservative-leaning workers. Annotator MFQ scores correlate with political leaning (liberals emphasize Care and Fairness more).

**Potential Harm**: Detecting and preventing morally insensitive, hurtful, or incoherent chatbot replies; mitigating erosion of user trust in conversational agents; addressing potential emotional burden on annotators from exposure to disturbing content.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Study was reviewed and approved by an internal review board; annotator meta-data (self-reported political leaning and MFQ responses) were collected. No explicit anonymization protocol described in the paper text.

**Data Licensing**: Data Use Agreement is required for users of the data (linked in the project repository). No specific open-data license (e.g., CC BY) is specified in the paper.

**Consent Procedures**: Internal review board approval obtained; annotators received content warnings and could skip HITs; qualification test and staging round with feedback were used before granting access to main task.

**Compliance With Regulations**: IRB review/approval is reported. No explicit mention of GDPR, CCPA, or other legal/regulatory frameworks in the paper.
