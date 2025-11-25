# MilkQA

## 📊 Benchmark Details

**Name**: MilkQA

**Overview**: We introduce MilkQA, a question answering dataset from the dairy domain dedicated to the study of consumer questions. The dataset contains 2,657 pairs of questions and answers, written in the Portuguese language and originally collected by the Brazilian Agricultural Research Corporation (Embrapa). The dataset was filtered and anonymized by three human annotators and is intended for research on the answer selection task.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Agriculture

**Languages**:
- Portuguese

**Similar Benchmarks**:
- SelQA
- SQuAD
- WikiQA
- MS MARCO
- TREC-QA
- InsuranceQA
- Págico

**Resources**:
- [Resource](http://nilc.icmc.usp.br/nilc/index.php/milkqa)
- [Resource](https://arxiv.org/abs/1801.03460)
- [Resource](https://code.google.com/p/word2vec/)
- [Resource](http://nilc.icmc.usp.br/embeddings)
- [Resource](http://trec.nist.gov/trec_eval/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a realistic dataset of consumer questions in the dairy domain for the task of answer selection, filling a gap where existing datasets focus on short factoid questions.

**Target Audience**:
- Machine Learning Researchers
- Model Developers

**Tasks**:
- Answer Selection
- Question Answering

**Limitations**: Current (first) version contains 2,657 anonymized question-answer pairs. The unusually long lengths of questions and answers impose high computational requirements on answer selection models.

## 💾 Data

**Source**: Collected from Embrapa Dairy Cattle customer service message archive (email message pairs) collected from 2003 to 2012 by the Brazilian Agricultural Research Corporation (Embrapa).

**Size**: 2,657 pairs of questions and answers

**Format**: N/A

**Annotation**: Manual selection, cleaning and anonymization by three human annotators; ground-truth answers are original answers provided by Embrapa specialists. Candidate answer pools constructed via clustering to produce 50-candidate pools with one ground truth each.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (answer selection models: baselines and CNN architectures)
- Automated metrics (ranking evaluation using P@1 and MAP)
- Baseline comparisons

**Metrics**:
- Precision at top one (P@1)
- Mean Average Precision (MAP)

**Calculation**: P@1 computed by the authors' evaluation script. MAP computed using the official TREC scorer (trec_eval). Answer selection treated as a ranking task where each candidate answer receives a relevance score.

**Interpretation**: Higher P@1 and MAP indicate better ranking performance. P@1 is the fraction of questions with a correct answer ranked first. MAP measures how well a system places correct answers near the top across the rank list. The authors interpret, for example, P@1 = 0.57 as only 57% of questions correctly answered and indicative of room for improvement.

**Baseline Results**: Results on WikiQA and MilkQA (P@1 and MAP): WWM — WikiQA P@1 0.5062 MAP 0.5100; MilkQA P@1 0.2467 MAP 0.3836. WSE — WikiQA P@1 0.3951 MAP 0.5838; MilkQA P@1 0.1733 MAP 0.2552. CNN-STD — WikiQA P@1 0.4135 MAP 0.5746; MilkQA P@1 0.4100 MAP 0.5573. CNN-LDC — WikiQA P@1 0.5485 MAP 0.6848; MilkQA P@1 0.5700 MAP 0.6899.

**Validation**: Dataset partitioned into train/dev/test subsets with 2,307 training questions, 50 development questions, and 300 test questions. Candidate answer pools of 50 answers were constructed with one ground truth per pool. MAP computed with trec_eval; early stopping on the dev set used during model training.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy

**Atlas Risks**:
- **Privacy**: Personal information in data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Messages were anonymized and cleaned by three annotators. Particular data such as people names and contact information and unrelated content (corporate signatures, advertisements) were removed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
