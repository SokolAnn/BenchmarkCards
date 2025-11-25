# UrBLiMP (Urdu Benchmark of Linguistic Minimal Pairs)

## 📊 Benchmark Details

**Name**: UrBLiMP (Urdu Benchmark of Linguistic Minimal Pairs)

**Overview**: UrBLiMP is a syntactically informed benchmark for evaluating the linguistic competence of multilingual language models in Urdu, comprising 5,696 minimal pairs targeting ten core syntactic phenomena.

**Data Type**: minimal pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Urdu

**Similar Benchmarks**:
- BLiMP
- CLiMP
- SLING
- TurBLiMP
- RuBLiMP
- JBLiMP
- BLiMP-NL

**Resources**:
- [Resource](https://huggingface.co/large-traversaal/Alif-1.0-8B-Instruct)

## 🎯 Purpose and Intended Users

**Goal**: To provide a linguistically grounded tool for identifying systematic weaknesses in LLMs' understanding of Urdu grammar.

**Target Audience**:
- ML Researchers
- Linguists
- NLP Practitioners

**Tasks**:
- Linguistic Evaluation

**Limitations**: The evaluation of linguistic phenomena in Urdu was limited primarily by the availability of annotated data.

## 💾 Data

**Source**: Urdu Treebank and in-house Urdu Corpus

**Size**: 5,696 pairs

**Format**: XML

**Annotation**: Manual verification by native Urdu speakers with inter-annotator agreement of 96.10%.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is defined as the proportion of minimal pairs in which the model assigns a lower (pseudo-)perplexity to the grammatically acceptable sentence.

**Interpretation**: Higher accuracy indicates better understanding of the Urdu linguistic phenomena.

**Validation**: Inter-annotator agreement was assessed, yielding a 96.10% agreement rate.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The benchmark includes evaluation of models on various demographic factors.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open-source under a permissive license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
