# CDialog

## 📊 Benchmark Details

**Name**: CDialog

**Overview**: We release a high-quality multi-turn Medical Dialog dataset relating to Covid-19 disease named CDialog, with around 1K conversations collected from online medical counselling websites. Each utterance is annotated with seven categories of medical entities (diseases, symptoms, medical tests, medical history, remedies, medications and other aspects). The dataset is intended to support development and evaluation of entity-aware medical dialog generation models.

**Data Type**: text (multi-turn dialog conversations with entity annotations)

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- DX (Dxy)
- COVID-EN
- MedDialog-EN
- MedDG
- KaMed
- Ext-CovidDialog

**Resources**:
- [GitHub Repository](https://github.com/deekshaVarshney/CDialog)
- [Resource](https://arxiv.org/abs/2212.06049)

## 🎯 Purpose and Intended Users

**Goal**: To build and release CDialog, a multi-turn medical dialog dataset related to Covid-19 with entity annotations to evaluate and develop entity-aware medical dialog generation systems.

**Target Audience**:
- Researchers

**Tasks**:
- Dialog Generation
- Named Entity Recognition
- Entity-aware Response Generation

**Limitations**: Modelling medical entities is a challenging task in dialog generation. Detailed cases of limitations by our model are described in Section 6.3.

**Out of Scope Uses**:
- The dataset is solely for academic research purposes.

## 💾 Data

**Source**: Extended from CovidDialog and Ext-CovidDialog; crawled from online medical counselling websites such as icliniq.com and healthcaremagic.com; converted and annotated by annotators with medical expertise.

**Size**: 1,012 conversations; 7,982 utterances; 1,085,204 tokens; average 8.0 utterances per conversation (max 48, min 2).

**Format**: N/A

**Annotation**: Manual annotation by four annotators with medical expertise. Each utterance labeled with seven medical entity categories: Diseases, Symptoms, Medications, Medical Tests, Medical History, Remedies, Other Aspects. Inter-annotator agreement: Fleiss' kappa 0.89 for entity annotation; Fleiss' kappa 0.85 for dialog conversion task.

## 🔬 Methodology

**Methods**:
- Automated metrics (BLEU, ROUGE-L, Perplexity, Unigram F1, embedding-based metrics)
- Human evaluation (fluency, adequacy, entity relevance rated 1-5 by human annotators and validation by a medical doctor)

**Metrics**:
- BLEU
- ROUGE-L
- Perplexity (PPL)
- Unigram F1-score
- Embedding-based metrics (Greedy Matching, Vector Extrema, Embedding Average)
- Human evaluation: Fluency (1-5), Adequacy (1-5), Entity Relevance (1-5)

**Calculation**: BLEU computes the amount of word overlap with the ground-truth response. ROUGE-L measures the longest matching sequence of words using longest common subsequence. Perplexity (PPL) measures how well the system models the dialog data. Unigram F1 is computed between predicted sentences and ground-truth sentences. Embedding-based metrics (Greedy Matching, Vector Extrema, Embedding Average) assign a vector to each word using word embeddings and compute similarity-based scores. Human metrics use a 1-5 scale where the higher number is better.

**Interpretation**: Higher BLEU, ROUGE-L, Unigram F1, and embedding metric scores and lower Perplexity indicate better automatic performance. For human evaluation, ratings run from 1 to 5 with higher values indicating better Fluency, Adequacy, and Entity Relevance. The paper reports statistical significance (t-test) with p-value < 0.001 when comparing BioBERT-Entity to baselines.

**Baseline Results**: Automatic (test set): BioBERT-Entity: PPL 22.97, F1 17.60, BLEU-1 0.217, BLEU-2 0.126, BLEU-3 0.094, BLEU-4 0.078, ROUGE-L 0.191, Embedding Average 0.865, Vector Extrema 0.404, Greedy Matching 0.667. BioBERT (strongest baseline): PPL 22.67, F1 15.68, BLEU-4 0.051. Human evaluation (average scores): BioBERT-Entity Fluency 3.55, Adequacy 2.86, Entity Relevance 2.33 (see Tables 2 and 3 for full baseline comparisons).

**Validation**: Dataset split into 80:10:10 for training, test and validation. Annotation agreement measured via Fleiss' kappa (0.85 for dialog conversion, 0.89 for entity annotation). Human evaluation performed on 50 dialogs per model with three human annotators; model outputs also validated by a doctor with a postgraduate degree in medicine.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Intellectual Property

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data
- **Intellectual Property**: Copyright infringement

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Annotators were asked to remove any names to anonymize the data. Dataset is medically verified by the institute health department. Data collection and annotation process was reviewed by the university review board.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The authors state they followed the policies of the public websites used and did not violate copyright issues. The data collection and annotation process was reviewed by the university review board.
