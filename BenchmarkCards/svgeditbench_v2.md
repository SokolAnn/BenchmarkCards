# SVGEditBench V2

## 📊 Benchmark Details

**Name**: SVGEditBench V2

**Overview**: SVGEditBench V2 is a benchmark dataset for instruction-based SVG editing, comprising triplets of an original image, a ground truth image, and the editing prompt, created to evaluate editing models.

**Data Type**: image-triplet pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- SVGEditBench

**Resources**:
- [GitHub Repository](https://github.com/mti-lab/SVGEditBenchV2)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate editing models that take an image and an editing prompt as input to output the modified image.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image Editing

**Limitations**: N/A

## 💾 Data

**Source**: Public SVG emoji datasets including Noto Emoji, Twemoji, and Fluent Emoji.

**Size**: 1,683 triplets

**Format**: N/A

**Annotation**: Editing prompts generated via GPT-4o

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Mean Squared Error (MSE)
- DINO features cosine similarity
- CLIPScore
- Chamfer distance

**Calculation**: Metrics compared output images from editing with ground truth images.

**Interpretation**: A lower MSE indicates better visual similarity, higher CLIPScore indicates better semantic similarity.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Noto Emoji: Apache 2.0, Twemoji: CC BY 4.0, Fluent Emoji: MIT.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
