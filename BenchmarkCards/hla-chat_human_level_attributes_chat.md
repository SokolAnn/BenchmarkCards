# HLA-Chat (Human Level Attributes Chat)

## 📊 Benchmark Details

**Name**: HLA-Chat (Human Level Attributes Chat)

**Overview**: HLA-Chat is a dataset that combines dialogue lines for characters with Human Level Attributes (HLAs) derived from TV Tropes to model character profiles and enable dialogue agents to learn and recover characters' language styles based on these HLAs.

**Data Type**: text (dialogue lines paired with character HLA attribute labels)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- Persona-Chat
- Cornell Movie-Dialogs Corpus

**Resources**:
- [GitHub Repository](https://github.com/newpro/aloha-chatbot)
- [Resource](https://tvtropes.org)
- [Resource](https://arxiv.org/abs/1910.08293)

## 🎯 Purpose and Intended Users

**Goal**: Provide a dataset (HLA-Chat) traceable to character context and Human Level Attributes (HLAs) and a method (ALOHA) to recover character-specific language styles so dialogue agents can imitate fictional characters' personalities.

**Tasks**:
- Dialogue Response Retrieval

**Limitations**: Limited human evaluation participant pool (12 participants); limited HLA guidance during testing due to model memory constraints; evaluation confounded by multiple context-correct candidate responses.

## 💾 Data

**Source**: HLA data collected from TV Tropes (tvtropes.org); dialogue data scraped from various existing internet sources of clean dialogue for TV shows; dialogues collected for 327 major characters (subset) across 38 TV shows combined with HLA data drawn from a larger set of characters.

**Size**: 1,042,647 dialogue lines; 45,821 characters with HLA data; 12,815 unique HLAs; 945,519 total character-HLA pairs; average 20.64 HLAs per collected character

**Format**: N/A

**Annotation**: HLA attributes are community-contributed tropes collected from TV Tropes (viewer-determined). Characters were filtered to keep those with at least five HLAs. Dialogue lines were collected from existing online sources; no additional manual annotation procedure is described.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Five-Fold Cross Validation
- Model-based evaluation using BERT bi-ranker and Poly-encoder
- Collaborative filtering-based Character Space Module (CSM), Character Community Module (CCM), and Language Style Recovery Module (LSRM)

**Metrics**:
- Hits@1/20
- Hits@5/20
- Hits@10/20
- Mean Rank
- Mean Reciprocal Rank (MRR)
- F1 Score
- BLEU (average of 1-4 grams)

**Calculation**: Hits@n/N: accuracy of the correct ground truth response being within the top n ranked candidate responses out of N total candidates. MRR: mean of the multiplicative inverses of the rank of each correct answer (MRR = (1/|Q|) * sum_i 1/rank_i). F1: 2 * (precision * recall) / (precision + recall), where precision is fraction of words in chosen response contained in the ground truth and recall is fraction of words in the ground truth contained in the chosen response. BLEU: reported as average BLEU scores of 1- to 4-grams.

**Interpretation**: Higher Hits@n, MRR, F1, and BLEU indicate better retrieval and similarity. The paper reports human Hits@1/20 mean ~40.67% as a reference; ALOHA variations achieve Hits@1/20 comparable to or exceeding human performance on some evaluation characters. BLEU higher values indicate greater textual similarity.

**Baseline Results**: Baseline Hits@1/20 (average, from Table 4): Kvmemnn 0.1232, Feed yourself 0.0482, BERT bi-ranker 0.1759, Poly-encoder 0.2579, Uniform Model 0.3077. ALOHA results (average): ALOHA-BERT Hits@1/20 = 0.4063, ALOHA-Poly Hits@1/20 = 0.4117. Human average Hits@1/20 = 0.4067.

**Validation**: Five-Fold Cross Validation split by TV shows (training on 80% of shows, testing on 20%). For CSM, 30% of character-HLA pairs were masked during training and used as validation. Five evaluation characters (one per test fold) and human evaluation with prescreened participants were used for further validation.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
