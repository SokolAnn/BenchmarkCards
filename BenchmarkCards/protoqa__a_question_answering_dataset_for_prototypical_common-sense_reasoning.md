# ProtoQA: A Question Answering Dataset for Prototypical Common-Sense Reasoning

## 📊 Benchmark Details

**Name**: ProtoQA: A Question Answering Dataset for Prototypical Common-Sense Reasoning

**Overview**: This paper introduces a new question answering dataset for training and evaluating common sense reasoning capabilities of artificial intelligence systems in prototypical situations. The task is framed as a generative evaluation in which a model outputs a ranked list of answers; reference answers are collected from 100 crowd-workers per question and manually clustered to provide weighted answer clusters used for evaluation.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Common Consensus
- ConceptNet
- PiQA
- Social IQA
- Cosmos QA
- SWAG
- HellaSwag
- CommonsenseQA
- ARC dataset
- Winograd Schema Challenge

**Resources**:
- [GitHub Repository](https://github.com/iesl/protoqa-data)
- [Resource](http://protoqa.com)
- [Resource](https://arxiv.org/abs/2005.00771)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale dataset and robust evaluation methodology for generative question answering focused on prototypical common-sense situations, encouraging models to produce diverse, ranked lists of plausible answers and measuring both plausibility and coverage across answer categories.

**Target Audience**:
- Machine Learning Researchers
- Natural Language Processing Researchers
- Model Developers

**Tasks**:
- Question Answering
- Text Generation
- Common-sense Reasoning

**Limitations**: The dataset is grounded in US culture and may contain nuanced culturally-specific information and biases. Some types of stereotypical or taxonomic questions were removed, but the authors note that common-sense questions may still carry culturally-specific biases that are not fully removed.

## 💾 Data

**Source**: Training data: scraped FAMILY-FEUD questions and answer clusters from two publicly available fan websites. Evaluation data: newly created questions and 100 crowd-sourced answers per question collected via FigureEight (now Appen), then manually clustered by experts.

**Size**: Training: 9,762 questions after filtering and de-duplication (scraped from >10,000). Evaluation: 154 questions with 100 crowd-sourced answers each (15,400 answers); development set of 52 and test set of 102 questions.

**Format**: N/A

**Annotation**: Training data included answer clusters from scraped FAMILY-FEUD sources. Evaluation answers: 100 responses per question collected on FigureEight, low-quality workers filtered via test questions, each list manually clustered by two different experts and adjudicated by a third; invalid answers were marked and some questions were removed if clustering quality thresholds were not met.

## 🔬 Methodology

**Methods**:
- Automated metrics (exact match, WordNet similarity, RoBERTa-based similarity)
- Model-based evaluation (baseline QA models, language models, fine-tuned language models)
- Human evaluation (human baseline responses for comparison)

**Metrics**:
- Exact Match
- WordNet Similarity
- RoBERTa Similarity
- MAXANSWERS@k
- MAXINCORRECT@k
- BLANC (cluster agreement)
- Precision
- Recall
- F1 Score

**Calculation**: Models output a ranked list of answers. Each predicted answer is matched to at most one reference answer cluster using exact match, WordNet-based token/subpartition matching, or a RoBERTa vector-based cluster classifier (one-vs-all per cluster; membership threshold 0.1). A reward equal to the matched cluster size is assigned; a reward matrix is built and the Hungarian algorithm computes an optimal one-to-one assignment of predicted answers to clusters. Scores are reported as a percentage of the oracle (the maximum obtainable score given the number of guesses). MAXANSWERS@k limits total answers to k; MAXINCORRECT@k allows unlimited answers but stops after k unmatched answers.

**Interpretation**: Higher percentage of oracle score indicates better coverage of common/prototypical answers and better ranking quality. Metrics reward both common/popular answers and diversity of covered answer clusters. The authors recommend WordNet similarity as the primary similarity metric as a balance between precision and recall. Human performance remains substantially higher than the tested baselines, indicating a meaningful gap.

**Baseline Results**: Selected results on annotated test set (scores normalized by maximum obtainable): Exact Match (MaxAnswers@1): QA Model 2.1%, GPT-2 5.6%, GPT-2 Fine-Tune 29.4%, Human 78.4%. WordNet Similarity (MaxAnswers@1): QA Model 3.4%, GPT-2 6.2%, GPT-2 Fine-Tune 36.4%, Human 78.4%. RoBERTa Similarity (MaxAnswers@1): QA Model 49.1%, GPT-2 38.7%, GPT-2 Fine-Tune 55.0%, Human 81.2%.

**Validation**: Quality controls included: scoring perturbed test-question candidates by four experts and selecting top-scoring questions; collecting 100 answers per question with worker-location restricted to US and automatic detection of low-quality workers via test questions; manual clustering by two experts with adjudication; BLANC cluster-agreement averaged 83.17; questions removed if the top 8 clusters did not contain at least 85 of the 100 responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Data contamination

**Demographic Analysis**: N/A

**Potential Harm**: ['Stereotypical bias in dataset/questions']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
