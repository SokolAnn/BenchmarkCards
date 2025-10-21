# ALARB (Arabic Legal Argument Reasoning Benchmark)

## 📊 Benchmark Details

**Name**: ALARB (Arabic Legal Argument Reasoning Benchmark)

**Overview**: ALARB is a dataset and suite of tasks designed to evaluate the reasoning capabilities of large language models (LLMs) within the Arabic legal domain, comprising over 13K commercial court cases from Saudi Arabia, with a focus on legal reasoning tasks.

**Data Type**: structured legal cases

**Domains**:
- Legal

**Languages**:
- Arabic

**Similar Benchmarks**:
- LegalBench
- ArabicMMLU

**Resources**:
- [Resource](https://huggingface.co/datasets/name)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark legal reasoning capabilities in Arabic LLMs while addressing the gap in datasets focusing on multistep reasoning for Arabic legal contexts.

**Target Audience**:
- ML Researchers
- Legal Professionals

**Tasks**:
- Verdict Prediction
- Legal Argument Completion
- Article Identification

**Limitations**: The dataset is limited to a particular area of law, obtained from a single country, and is relatively limited in size.

## 💾 Data

**Source**: Commercial court cases from Saudi Arabia as scraped from the KSA Ministry of Justice website.

**Size**: 13,344 legal cases

**Format**: Structured text

**Annotation**: Manually curated and cleaned, with facts and reasoning steps structured for clarity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the alignment of predicted verdicts with actual court rulings.

**Interpretation**: Correct verdicts indicate a complete match with actual court rulings.

**Validation**: Performance was validated using a subset of 1,329 legal cases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Future work will focus on expanding demographic diversity in the dataset.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset has been anonymized to remove identifying information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
