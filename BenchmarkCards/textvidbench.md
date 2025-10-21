# TextVidBench

## 📊 Benchmark Details

**Name**: TextVidBench

**Overview**: TextVidBench is the first benchmark specifically designed for long-video text question answering, addressing the limited video duration and evaluation scopes of existing datasets, by spanning 9 categories with an average video length of 2306 seconds.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- M4-ViteVQA
- NewsVideoQA
- RoadTextVQA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation platform for text understanding in long video scenarios.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Text Needle-in-Haystack
- Text Temporal Grounding
- Text Dynamics Captioning

**Limitations**: Due to rapid evolution in multimodal model architectures, the proposed model may not fully match the performance of rapidly emerging models.

## 💾 Data

**Source**: Video samples crawled from YouTube spanning nine domains rich in textual information.

**Size**: 30 hours of video

**Format**: N/A

**Annotation**: Semi-automatic annotation framework utilizing a lightweight multimodal model and GPT-4 for question generation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Average Normalized Levenshtein Similarity (ANLS)

**Calculation**: Metrics calculated based on the model's output compared to ground truth.

**Interpretation**: Higher scores indicate better model performance in understanding long video text.

**Baseline Results**: Comparative results showing improvements over existing models.

**Validation**: Extensive experiments on multiple public datasets and the proposed benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
