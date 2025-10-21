# WebCode2M

## 📊 Benchmark Details

**Name**: WebCode2M

**Overview**: WebCode2M is a new dataset comprising 2.56 million instances, each containing a design image along with the corresponding webpage code and layout details, aimed at improving webpage code generation through Multimodal Large Language Models (MLLMs).

**Data Type**: design-image and HTML/CSS code pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Russian
- German
- Spanish
- French
- Chinese
- Dutch
- Japanese
- Italian
- Hindi
- Turkish
- Portuguese
- Bulgarian
- Urdu

**Similar Benchmarks**:
- Design2Code
- pix2code
- WebSight

**Resources**:
- [Resource](https://webcode2m.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To introduce a large-scale real-world dataset for generating webpage code from webpage designs to enhance the performance of Multimodal Large Language Models (MLLMs).

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Web pages sourced from the Common Crawl dataset, filtered and processed to collect design images and corresponding HTML/CSS code.

**Size**: 2,563,905 instances

**Format**: JSON

**Annotation**: Data quality ensured by a scoring model trained on a manually annotated subset of 10,000 entries, achieving validation accuracy of 90%.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- TreeBLEU
- Visual Score
- CLIP similarity

**Calculation**: Metrics calculated based on comparison between generated webpage structures and ground truth during the evaluation.

**Interpretation**: Higher scores indicate better performance in generating accurate and aesthetically pleasing webpage code.

**Baseline Results**: WebCoder significantly outperformed models like Design2Code-18B and WebSight VLM-8B.

**Validation**: The dataset was validated by comparing different baseline models against the newly introduced WebCoder model.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Exposing personal information

**Demographic Analysis**: The dataset includes diverse languages and different webpage styles, improving representation.

**Potential Harm**: The dataset may contain inappropriate content that requires careful handling.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Samples filtered for inappropriate content, including NSFW images and harmful keywords.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
