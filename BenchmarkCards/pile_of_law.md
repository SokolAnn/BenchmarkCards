# Pile of Law

## 📊 Benchmark Details

**Name**: Pile of Law

**Overview**: We gather and make available the Pile of Law, a ≈256GB (and growing) dataset of open-source English-language legal and administrative data, covering court opinions, contracts, administrative rules, and legislative records. We also distill legal norms about privacy and toxicity into actionable lessons for researchers and demonstrate that implicit sanitization rules can be learned from the Pile of Law.

**Data Type**: text (legal and administrative documents: court opinions, filings, statutes, regulations, contracts, legislative records, hearings, casebooks, and related legal text)

**Domains**:
- Legal
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- The Pile
- EuroParl
- CaseHOLD
- LexGLUE

**Resources**:
- [Resource](https://huggingface.co/datasets/pile-of-law/pile-of-law)
- [Resource](https://huggingface.co/pile-of-law/legalbert-large-1.7M-2/)
- [Resource](https://huggingface.co/pile-of-law/legalbert-large-1.7M-1/)
- [Resource](https://huggingface.co/datasets/pile-of-law/eoir_privacy)
- [Resource](https://huggingface.co/pile-of-law/distilbert-base-uncased-finetuned-eoir_privacy)
- [GitHub Repository](https://github.com/Breakend/Pileoflaw)

## 🎯 Purpose and Intended Users

**Goal**: Provide the Pile of Law dataset (≈256GB) of open-source English legal and administrative data; to catalog legal norms for handling privacy and offensive content; and to demonstrate how filtering rules can be learned from legal text to inform responsible data sanitization for language model pretraining.

**Target Audience**:
- Researchers
- Legal Researchers
- Model Developers

**Tasks**:
- Language Model Pretraining
- Masked Language Modeling
- Text Classification (Pseudonymity Prediction)
- Toxicity Classification / Filtering Evaluation

**Limitations**: Due to the expertise of the authors and the availability of data, this work focuses on the U.S. legal system; the collation is concentrated on U.S. texts because of licensing restrictions. The dataset may contain sensitive material that escaped administrative scrutiny. Pretraining experiments reported were run on a limited sample (≈30GB sample for pretraining) and initial models may be undertrained.

## 💾 Data

**Source**: Compiled from 35 data sources including CourtListener (opinions, docket entries, filings), RECAP, U.S. Supreme Court dockets and oral argument transcripts, Board of Veterans' Appeals decisions, Department of Labor ECAB, EOIR (immigration decisions), U.S. Code and Federal Regulations, EUR-Lex, European Court of Human Rights, Canadian court opinions, congressional hearings, Founders letters, contracts (Edgar, Atticus), Terms of Service, Reddit r/legaladvice and r/legaladviceofftopic (filtered), open-source casebooks and bar exam outlines, and other governmental and legal publications (see Appendix E and Table 4).

**Size**: ≈256GB total; ≈30 billion words; ≈10 million documents

**Format**: N/A

**Annotation**: Mostly raw/unannotated legal text; select labeled subsets and derived datasets provided for experiments (e.g., EOIR pseudonymity masked and labeled dataset available at the EOIR privacy HuggingFace dataset).

## 🔬 Methodology

**Methods**:
- Masked Language Modeling (pretraining)
- Fine-tuning
- Text Classification (DistilBERT pseudonymity prediction)
- Masked Language Model Scoring (MLM Score)
- Perturbation Analysis
- Causal Lexicon Induction
- Automated Toxicity Filter Evaluation (comparing multiple toxicity detectors)

**Metrics**:
- F1 Score
- Masked Language Model (MLM) Score
- Cohen's Kappa
- Perplexity
- Toxicity Probability (>50%)

**Calculation**: F1 measured on held-out validation sets (e.g., ≈80% F1 reported for the distil-BERT pseudonymity task). MLM Score computed as in Masked Language Model Scoring (difference in score between variants, e.g., 'Jane Doe' vs random name). Cohen's Kappa computed for inter-model agreement across time bins (10-year bins). Toxicity reported as model-assigned probability with >50% threshold for classification. Perplexity reported for pretrained models.

**Interpretation**: Higher F1 indicates better pseudonymity prediction performance; larger MLM score differences indicate stronger encoding of pseudonymity norms; low Cohen's Kappa indicates disagreement between toxicity filters (i.e., inconsistent filtering); reductions in toxicity probability when adding context indicate sensitivity of filters to context length. The paper presents these interpretations in discussing model behavior and filter agreement.

**Baseline Results**: Distil-BERT pseudonymity model: ≈80% F1 on validation. CaseHOLD evaluation (Table 7): CaseLaw-BERT (tuned) 78.5 F1; CaseLaw-BERT 75.4 F1; PoL-BERT-Large (tuned) 75.0 F1; Bert-Large-Uncased (tuned) 71.3 F1.

**Validation**: Used held-out validation sets; CaseHOLD experiments used the train/validation/test split from the referenced work [30]; toxicity context experiments report 95% confidence intervals. Reproducibility materials (code and datasets) and experiment data/models are provided via HuggingFace and GitHub links.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Toxicity
- Fairness
- Robustness
- Intellectual Property

**Atlas Risks**:
- **Privacy**: Personal information in data, Reidentification, Data privacy rights alignment
- **Fairness**: Data bias
- **Intellectual Property**: Copyright infringement, Data usage rights restrictions
- **Robustness**: Extraction attack

**Demographic Analysis**: Includes analysis of protections and practices for juveniles/minors and contextual factors (e.g., asylum, torture, criminal history) affecting pseudonymity decisions; experiments examine how features like asylum or torture perturbations influence pseudonymity predictions.

**Potential Harm**: ['Privacy violations (exposure of personally sensitive information in training data)', 'Exposure and propagation of toxic or offensive content', 'Potential copyright infringement from copyrighted exhibits or materials included in docket entries']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors run filters to validate no Social Security Numbers using Microsoft Presidio; restrict search engine indexing of the dataset where possible; provide instructions and a mechanism for requesting content removal via the HuggingFace community feature (and follow upstream takedown procedures); they do not perform broad additional redactions beyond upstream sources in order to preserve fidelity and legal references.

**Data Licensing**: The dataset compilation is placed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International; underlying data subsets remain subject to their original licenses (including many public domain sources and various Creative Commons and other licenses as enumerated in Table 6).

**Consent Procedures**: Consent for curated data is implicit in each subset via public availability or the license under which the subset was released; the paper documents license sources and provides a takedown/request removal procedure tied to upstream sources.

**Compliance With Regulations**: The paper discusses applicability of GDPR, HIPAA, and other regulations and notes that much of the data is governmental/public record; GDPR applicability is discussed (e.g., EU materials are from sources that must comply with applicable provisions); HIPAA is noted as not applying to many administrative decisions included. The authors provide mechanisms to request content removal and describe alignment with upstream legal standards.
