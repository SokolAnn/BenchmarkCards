# MAT CH dataset

## 📊 Benchmark Details

**Name**: MAT CH dataset

**Overview**: A task consisting in matching a proof to a given mathematical statement. The paper presents a dataset for the task (the MAT CH dataset) consisting of over 180k statement-proof pairs extracted from modern mathematical research articles, intended to support Mathematical Information Retrieval and modelling of mathematical reasoning.

**Data Type**: statement-proof pairs (text with mathematical formulae)

**Domains**:
- Natural Language Processing
- Mathematics
- Information Retrieval

**Languages**:
- English

**Similar Benchmarks**:
- LEANSTEP
- NaturalProofs
- synthetic dataset of Polu and Sutskever (2020)

**Resources**:
- [GitHub Repository](https://github.com/waylonli/MATcH)
- [Resource](https://arxiv.org/abs/2302.09350)
- [Resource](https://mir.fi.muni.cz/MREC/)
- [Resource](https://www.w3.org/Math/)

## 🎯 Purpose and Intended Users

**Goal**: Given a collection of mathematical statements and a separate equal-size collection of mathematical proofs, the task consists in finding and assigning a proof to each mathematical statement.

**Target Audience**:
- Mathematicians
- Researchers in Mathematical Information Retrieval
- Theorem proving researchers

**Tasks**:
- Information Retrieval
- Text Matching
- Premise Selection

**Limitations**: 1) The symbol replacement procedure simulates different authors but cannot alter broader mathematical 'dialects' and writing-style differences; 2) Computational limitations prevented exploring the full potential of global training for large models (batch size limits on available GPUs); 3) The symbol replacement method is coarse and can be imprecise because symbol meaning is context-dependent.

## 💾 Data

**Source**: MREC corpus (Líska et al., 2011) containing articles from ArxMLiV (an arXiv to XML conversion project). Statement-proof pairs are identified via XML meta tags ('theorem' and 'proof') and filtered by heuristics.

**Size**: 184,094 statement-proof pairs; 27,841 extracted articles with statement-proof pairs; MREC corpus ~439,423 articles. Train/dev/test split: 147,278 training pairs; 18,408 development pairs; 18,408 test pairs.

**Format**: N/A

**Annotation**: Automatically extracted using XML meta tags and filtering heuristics (no manual annotation).

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation (ranking and top-1)
- Local greedy decoding (per-statement ranking)
- Global bipartite matching decoding (maximum weighted bipartite matching / Linear Assignment Problem)
- Symbol replacement evaluation procedure (several replacement levels)

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Accuracy

**Calculation**: MRR: MRR = (1/N) * sum_{i=1..N} (1 / r_hat_i) where r_hat_i is the rank of the gold proof for statement i. Accuracy: proportion of statements whose first-ranked proof is correct.

**Interpretation**: MRR measures ranking quality (higher is better); Accuracy measures top-1 correctness (higher is better).

**Baseline Results**: Best reported MRR: 73.73 (SCRATCH BERT - Local - Local on Conservation symbol replacement). Best reported Accuracy: 74.68 (SCRATCH BERT - Local - Global on Conservation symbol replacement).

**Validation**: Dataset shuffled and split 80%/10%/10% for train/development/test. Models are evaluated on the validation set periodically during training and the best model is selected based on validation performance.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
