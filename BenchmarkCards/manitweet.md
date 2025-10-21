# MANITWEET

## 📊 Benchmark Details

**Name**: MANITWEET

**Overview**: Introduces the task "identifying manipulation of news on social media" and presents MANITWEET, a curated dataset of 3.6K tweets paired with corresponding news articles to detect whether and how social media posts manipulate information presented in associated news articles.

**Data Type**: text (tweet-article pairs)

**Domains**:
- Natural Language Processing
- Social Media

**Similar Benchmarks**:
- FakeNewsNet
- FEVER
- SCIFACT
- LIAR
- X-Fact
- NEWS-DISCOURSE

**Resources**:
- [Resource](https://huggingface.co/allenai/led-base-16384)
- [Resource](https://sharegpt.com/)
- [GitHub Repository](https://github.com/tatsu-lab/stanford_alpaca)

## 🎯 Purpose and Intended Users

**Goal**: Determine whether and how a social media post (tweet) manipulates the associated news article, and localize the manipulating span and the pristine span.

**Target Audience**:
- Researchers

**Tasks**:
- Text Classification (Tweet manipulation detection)
- Span Extraction (Manipulating span localization)
- Span Extraction (Pristine span localization)

**Limitations**: Training set is largely machine-generated while the test set is human-written, introducing distributional discrepancies. The dataset and annotation pipeline focus on three entity types (LOCATION, PEOPLE, EVENT) and may fail for complex manipulations beyond entity-level perturbations. Data creation uses LLMs (ChatGPT), which may introduce biases and artifacts. Prompting strategies for LLM baselines were limited to ICL and CoT as described.

**Out of Scope Uses**:
- The fake news and manipulating tweets in MANITWEET cannot be used to train text generators for malicious purposes.
- Use the manipulation prompts discussed in this paper to generate tweets and spread false information.
- The fake news in MANITWEET should not be used as evidence for fact-checking claims.

## 💾 Data

**Source**: Repurposed news articles and associated tweets from the FakeNewsNet dataset (Shu et al., 2020). Machine-generated tweets were produced using ChatGPT for training/dev data; human-written tweets from FakeNewsNet were annotated for the test set.

**Size**: 3,636 tweets associated with 2,688 news articles (dataset total: 3,636 examples)

**Format**: N/A

**Annotation**: Two-stage annotation: (1) ChatGPT-generated tweets validated by Amazon Mechanical Turk (AMT) workers with graduate student re-validation (first round) to collect machine-generated, human-validated samples; (2) a seq2seq model trained on round-1 data used to identify candidate human-written MANI/NOMANI tweets which were then annotated/validated by AMT (second round). Annotator qualification: U.S.-based, >10,000 HITs, 99% acceptance. Inter-annotator agreement: Fleiss' κ = 62.4% during qualification; graduate student vs. MTurk validation Cohen's κ = 93.1% (first round) and 73.0% (second round).

## 🔬 Methodology

**Methods**:
- Automated metrics (Exact Match, ROUGE-L, Overlap F1, Macro F1)
- Model-based evaluation (fine-tuned seq2seq LED-FT and LLM prompting: ChatGPT, Vicuna, GPT-4)
- Human evaluation (graduate student annotation as an approximate human performance estimate)

**Metrics**:
- Macro F1
- Exact Match
- Macro Overlap F1
- ROUGE-L

**Calculation**: Subtask 1 (binary classification): Macro F1. Subtasks 2 and 3 (span localization): Exact Match, Macro Overlap F1, and ROUGE-L to allow partial credit for partially-correct spans.

**Interpretation**: Higher Macro F1 indicates better manipulation detection. For span localization, higher Exact Match, Overlap F1, and ROUGE-L indicate better identification of manipulating/pristine spans; partial credit is allowed via overlap and ROUGE-L. Human performance (graduate student) is reported as a reference upper bound; LLM prompting (zero-/few-shot) generally underperforms compared to fine-tuned models on this dataset.

**Baseline Results**: Key results on the MANITWEET test set: Human (approximate) Subtask1 Macro F1 = 89.92%. Vicuna Zero-shot Subtask1 Macro F1 = 47.09%. ChatGPT Zero-shot Subtask1 Macro F1 = 52.49%; ChatGPT Two-shot ICL Subtask1 Macro F1 = 65.28%. LED-FT (Ours, fine-tuned) Subtask1 Macro F1 = 72.62%. LLM + LED-FT (Ours) Subtask1 Macro F1 = 73.46%. (See Table 2 and Table 4 in the paper for full per-subtask and per-metric results, including GPT-4 evaluations.)

**Validation**: Test set consists of human-written tweets annotated in the second round. Validation included annotator qualification, inter-annotator agreement measurements (Fleiss' κ and Cohen's κ), and graduate student re-validation; samples where graduate student disagreed with MTurk annotation were discarded in round 1. The 3K machine-validated samples were split (2,316:800) for training and validation of the seq2seq model used to select human-written candidates for round 2.

## ⚠️ Targeted Risks

**Risk Categories**:
- Misuse
- Privacy

**Atlas Risks**:
- **Misuse**: Spreading disinformation
- **Privacy**: Personal information in data

**Potential Harm**: ['Malicious users could utilize the manipulating tweets or fake news articles to train a text generator for creating deceptive content.', 'Using the manipulation prompts or generated tweets to spread false information.', 'Fake news in MANITWEET should not be used as evidence for fact-checking claims.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset's human-written tweets are anonymized; all associated news articles were already publicly available. The authors state the dataset does not pose significant privacy concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
