# OpenWebMath

## 📊 Benchmark Details

**Name**: OpenWebMath

**Overview**: OpenWebMath is an open dataset containing 14.7B tokens of high-quality mathematical webpages extracted from Common Crawl, aimed at improving the reasoning capabilities of large language models.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Mathematics

**Languages**:
- English

**Similar Benchmarks**:
- MATH
- GSM8k
- ProofPile

**Resources**:
- [Resource](https://huggingface.co/datasets/open-web-math/open-web-math)

## 🎯 Purpose and Intended Users

**Goal**: To provide an open dataset for training large language models on mathematical texts to enhance their mathematical reasoning capabilities.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Pretraining
- Fine-tuning

**Limitations**: The dataset is limited to English mathematical content and may exclude important documents with non-English content.

## 💾 Data

**Source**: Extracted from Common Crawl.

**Size**: 6.3 million documents, 14.7B tokens

**Format**: Plain text

**Annotation**: No manual annotation; relies on extraction from source material.

## 🔬 Methodology

**Methods**:
- Text extraction from HTML
- Quality filtering
- Deduplication

**Metrics**:
- Perplexity

**Calculation**: Perplexity is calculated on variety of mathematics benchmarks to measure model performance.

**Interpretation**: Lower perplexity indicates better performance on mathematical reasoning tasks.

**Baseline Results**: Models trained on OpenWebMath outperform those trained on over 20x the amount of general data.

**Validation**: Performance validated through downstream task evaluations on mathematical benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Quality

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Limited to English sources; potential exclusion of non-English mathematical resources.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: ODC-By 1.0 license; users must also abide by Common Crawl terms of use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
