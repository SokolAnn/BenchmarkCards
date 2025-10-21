# CSL: A Large-scale Chinese Scientific Literature Dataset

## 📊 Benchmark Details

**Name**: CSL: A Large-scale Chinese Scientific Literature Dataset

**Overview**: CSL is a large-scale Chinese Scientific Literature dataset which contains the titles, abstracts, keywords and academic fields of 396k papers. Based on CSL, the authors build a benchmark to evaluate the performance of models across scientific-domain tasks, i.e., summarization, keyword generation and text classification.

**Data Type**: title, abstract, keywords, category and discipline metadata (text)

**Domains**:
- Natural Language Processing
- Scientific Literature

**Languages**:
- Chinese

**Similar Benchmarks**:
- S2ORC (2020)
- PubMed Central OAS
- unarXive (2020)
- Saier and Färber, 2019
- arXiv CS (2018)
- AAN (2013)

**Resources**:
- [GitHub Repository](https://github.com/ydli-ai/CSL)
- [Resource](https://nstr.escience.net.cn)
- [GitHub Repository](https://github.com/dbiir/UER-py)
- [Resource](https://arxiv.org)
- [Resource](http://www.pubmed.gov)
- [Resource](https://aclanthology.org)

## 🎯 Purpose and Intended Users

**Goal**: To provide the first large-scale Chinese scientific literature dataset (CSL) to serve as a Chinese corpus and pre-training resource, and to build a benchmark derived from CSL for evaluating Chinese scientific-domain NLP tasks (summarization, keyword generation, category/discipline classification).

**Target Audience**:
- Natural Language Processing researchers
- Model developers

**Tasks**:
- Text Summarization
- Keyword Generation
- Text Classification (Category Classification)
- Text Classification (Discipline Classification)

**Limitations**: To provide accurate category/discipline labels, we only use journals focused on one domain, which resulted in some data loss.

## 💾 Data

**Source**: Meta-information collected from the National Engineering Research Center for Science and Technology Resources Sharing Service (NSTR), filtered by the Catalogue of Chinese Core Journals (Peking University Library), using journal instructions to assign categories and disciplines (only journals focused on a single academic field are kept).

**Size**: 396,209 instances

**Format**: Represented as tuples <T; A; K; c; d> (title, abstract, keywords, category, discipline) as dataset meta-information

**Annotation**: Papers are labeled with categories and disciplines based on the journal in which they were published. Volunteers read journal introductions and assign the closest discipline following the guideline 'Disciplines of Conferring Academic Degrees (GB/T 13745-2009)'.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (text-to-text models)
- Multi-task training
- Prompt-based text-to-text evaluation
- Automated metrics

**Metrics**:
- Accuracy
- ROUGE-L
- Bpref

**Calculation**: A random subset of 10,000 samples is split into training/validation/test with ratio 0.8:0.1:0.1 (shared across tasks). Models are fine-tuned and evaluated with greedy decoding. Accuracy is reported for classification tasks; ROUGE-L is used for summarization; Bpref is used for keyword generation.

**Interpretation**: Higher metric values indicate better performance. The authors report that baseline models achieve acceptable results but are still not satisfactory for real-world applications. Domain-adaptive pre-training (CSL-T5) improves performance. Multi-task training slightly outperforms single-task fine-tuning on these tasks.

**Baseline Results**: Test results (CTGcls Acc., DCPcls Acc., TS ROUGE-L, KG Bpref): T5: 83.6, 67.1, 49.8, 54.2; PEGASUS: 81.7, 69.4, 49.4, 55.2; BART: 79.2, 65.7, 47.8, 49.9; T5 (single): 82.3, 63.2, 49.2, 54.1; CSL-T5: 82.9, 70.8, 52.1, 55.9.

**Validation**: The benchmark uses a shared train/validation/test split (0.8:0.1:0.1) on 10,000 randomly selected samples. Fine-tuning uses early stopping; results reported with greedy decoding. Multi-task and single-task fine-tuning comparisons are performed.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Intellectual Property

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Intellectual Property**: Data usage rights restrictions, Copyright infringement

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The corpus used is released by the Chinese government and has been anonymized wherever necessary. Only publicly available paper metadata are used and full texts are not accessed.

**Data Licensing**: The authors state they are licensed to use some of the papers' metadata for NLP research.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
