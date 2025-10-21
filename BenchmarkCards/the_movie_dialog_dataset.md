# The Movie Dialog Dataset

## 📊 Benchmark Details

**Name**: The Movie Dialog Dataset

**Overview**: We propose a suite of new tasks of much larger scale that attempt to bridge the gap between synthetic tasks and real dialog data. Choosing the domain of movies, we provide tasks that test the ability of models to answer factual questions (utilizing OMDb), provide personalization (utilizing MovieLens), carry short conversations about the two, and finally to perform on natural dialogs from Reddit. We provide a dataset covering ∼75k movie entities and with ∼3.5M training examples.

**Data Type**: dialog exchanges (question-answering pairs and conversation turns)

**Domains**:
- Natural Language Processing
- Entertainment

**Similar Benchmarks**:
- bAbI tasks
- Ubuntu Dialog Corpus
- SimpleQuestions
- WEBQUESTIONS

**Resources**:
- [Resource](http://fb.ai/babi)
- [Resource](https://arxiv.org/abs/1511.06931)
- [Resource](http://en.omdb.org)
- [Resource](http://beforethecode.com/projects/omdb/download.aspx)
- [Resource](http://grouplens.org/datasets/movielens/)
- [Resource](https://www.reddit.com/r/movies)
- [Resource](https://www.reddit.com/r/datasets/comments/3bxlg7)

## 🎯 Purpose and Intended Users

**Goal**: To provide a collection of four tasks in the movie domain to evaluate prerequisite qualities of end-to-end dialog systems: (1) question answering, (2) recommendation, (3) QA + recommendation (multi-turn), and (4) chit-chat using real Reddit dialogs, and a joint task combining all four.

**Target Audience**:
- Machine learning researchers
- Model developers

**Tasks**:
- Question Answering
- Recommendation
- Dialogue (Chit-chat)
- Conversational multi-turn Question Answering / Recommendation

**Limitations**: Dataset is focused on the movie domain (authors note nothing specific to task design prevents transfer but dataset itself is single-domain). Performance of joint training is degraded compared to best per-task baselines; Memory Networks do not outperform specialized QA systems on Task 1. The authors explicitly note remaining limitations in model performance and the need for future work to create new tasks in other domains.

## 💾 Data

**Source**: Constructed from Open Movie Database (OMDb), MovieLens, and Reddit (r/movies). QA used OMDb combined with MovieLens tags and SimpleQuestions annotations; recommendation uses MovieLens ratings and templates; Reddit conversations are real posts from r/movies, flattened to parent/comment pairs.

**Size**: Overall: ∼75k movie entities and ∼3.5M training examples. Task breakdown (explicitly stated): QA: ∼15k movies; QA splits ∼96k training, 10k development, 10k test. Recommendation: ∼11k movies; ∼1M training examples, 10k development, 10k test; ∼110k users in training. QA+Recommendation: ∼1M training examples, ∼10k development, ∼10k test. RedditDiscussion: ∼1M dialogs with 10k development and 10k test. Joint: combined examples sampled from all tasks.

**Format**: N/A

**Annotation**: QA: used SimpleQuestions human annotations expanded by substituting entities to cover KB; Recommendation: generated dialog exchanges via fixed natural language templates using MovieLens user×item ratings; Reddit: raw conversation data processed and flattened to parent/comment pairs; overall generation is automatic using sources and templates as described.

## 🔬 Methodology

**Methods**:
- Automated metrics (ranking evaluation)
- Model-based evaluation (compare supervised embedding models, Memory Networks, LSTMs, SVD, IR, specialized QA system)

**Metrics**:
- Hits@k (Hits@1, Hits@10, Hits@100)

**Calculation**: For each task models produce a ranked list of candidate answers. QA ranks candidate entities/words (vocabulary); Recommendation ranks candidate movies and measures whether the correct movie is within top 100 (Hits@100); QA+Recommendation uses Hits@10 over candidate responses; Reddit ranks the true response among 10001 candidates (true response + 10k negatives) using Hits@10/Hits@1 as reported. Hits@k is reported as percentage.

**Interpretation**: Higher Hits@k indicates better performance. Authors note Hits@k for Recommendation and Reddit should be viewed as a lower bound due to incomplete labeling (missing ratings or missing plausible responses). Different tasks use different k (e.g., Hits@1 for QA, Hits@100 for Recommendation, Hits@10 for QA+Recommendation and Reddit).

**Baseline Results**: Reported test results (Table 6): QA (Hits@1): QA SYSTEM (Bordes et al., 2014) 90.7; MEMN2N 79.3; SUPERVISED EMBEDDINGS 50.9; LSTM 6.5; JOINTMEMN2N 83.5; JOINTSUPERVISED EMBEDDINGS 43.6. Recommendation (Hits@100): SUPERVISED EMBEDDINGS 29.2; MEMN2N 28.6; LSTM 27.1; SVD 19.2; JOINTMEMN2N 26.5; JOINTSUPERVISED EMBEDDINGS 28.1. QA+Recommendation (Hits@10): MEMN2N 81.7; SUPERVISED EMBEDDINGS 65.9; LSTM 19.9; JOINTMEMN2N 78.9; JOINTSUPERVISED EMBEDDINGS 58.9. Reddit (Hits@10): MEMN2N 29.2; SUPERVISED EMBEDDINGS 27.6; IR 23.7; LSTM 11.8; JOINTMEMN2N 26.6; JOINTSUPERVISED EMBEDDINGS 14.5.

**Validation**: Datasets split into training / development / test sets (counts provided per task). Hyperparameters selected via grid search on the development sets. Evaluation performed on held-out test sets. Additional validation: Memory Networks also evaluated on the Ubuntu Dialog Corpus for cross-dataset validation.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
