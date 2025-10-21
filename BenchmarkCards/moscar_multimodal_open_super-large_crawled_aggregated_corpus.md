# mOSCAR (Multimodal Open Super-large Crawled Aggregated corpus)

## 📊 Benchmark Details

**Name**: mOSCAR (Multimodal Open Super-large Crawled Aggregated corpus)

**Overview**: mOSCAR is the first large-scale multilingual and multimodal document corpus, covering 163 languages, with 303M documents, 200B tokens, and 1.15B images, specifically developed to support research in multimodal large language models.

**Data Type**: document-level corpus containing text-image pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Spanish
- French
- Chinese
- German
- Japanese
- Russian
- Hindi
- Arabic
- Portuguese

**Similar Benchmarks**:
- WIT
- Conceptual Captions
- LAION-400M

**Resources**:
- [Resource](https://oscar-project.github.io/documentation/versions/mOSCAR/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, high-quality multilingual and multimodal dataset for training and evaluating multilateral large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering
- Image Captioning
- Multimodal Machine Translation

**Limitations**: N/A

## 💾 Data

**Source**: Crawled from the web using Common Crawl datasets with extensive filtering for quality and safety.

**Size**: 303M documents, 200B tokens, 1.15B images

**Format**: Mixed (text and images)

**Annotation**: Manual filtering and evaluation steps to ensure dataset safety and quality.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- CideR
- Accuracy
- BLEU Score

**Calculation**: Metrics calculated based on standard evaluation protocols for image-text tasks.

**Interpretation**: Results are compared against models trained on standard captions and evaluated on various multilingual tasks.

**Validation**: Extensive filtering and evaluation procedures to ensure reliability and quality of the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Documents processed to remove PII and toxic content.

**Data Licensing**: Creative Commons CC BY 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
