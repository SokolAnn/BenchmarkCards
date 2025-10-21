# testbed of six publicly available data sources (YFCC, LAION, Conceptual Captions, WIT, RedCaps, Shutterstock)

## 📊 Benchmark Details

**Name**: testbed of six publicly available data sources (YFCC, LAION, Conceptual Captions, WIT, RedCaps, Shutterstock)

**Overview**: We introduce a testbed of six publicly available data sources—YFCC, LAION, Conceptual Captions, WIT, RedCaps, Shutterstock—to investigate how pre-training distributions induce robustness in CLIP. We measure zero-shot accuracy on ImageNet and several ImageNet-derived distribution shifts and study how individual sources, dataset combinations (input mixing), output ensembling, and filtering affect robustness.

**Data Type**: image-text pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ImageNet
- ImageNet-V2
- ImageNet-R
- ImageNet-Sketch
- ObjectNet
- WILDS

**Resources**:
- [GitHub Repository](https://github.com/mlfoundations/clip_quality_not_quantity)
- [Resource](https://commoncrawl.org/)
- [Resource](https://laion.ai/laion-5b-a-new-era-of-open-large-scale-multi-modal-datasets/)
- [Resource](https://doi.org/10.5281/zenodo.5143773)

## 🎯 Purpose and Intended Users

**Goal**: Investigate the impact of pre-training dataset composition on the robustness of CLIP models to natural distribution shifts, and study interactions of data sources, mixing strategies, and filtering.

**Target Audience**:
- ML Researchers
- Model Developers
- Dataset Designers
- Practitioners interested in dataset design and robust pre-training

**Tasks**:
- Zero-shot Image Classification
- Robustness Evaluation / Out-of-distribution Evaluation (distribution shift)

**Limitations**: The pre-training datasets used in the testbed range from 5M to 15M samples, which is smaller than current state-of-the-art web-scale datasets; full-scale experiments were not performed due to resource constraints (see Section 7.1).

## 💾 Data

**Source**: Six publicly available image-text datasets collected from web sources: YFCC (Flickr), LAION (Common Crawl), Conceptual Captions (web HTML alt-text), RedCaps (curated Reddit subreddits), Shutterstock (Shutterstock website), WIT (Wikipedia reference descriptions).

**Size**: YFCC: 14,826,000 examples; LAION: 15,504,742 examples; CC-12M (Conceptual Captions): 9,594,338 examples; RedCaps: 11,882,403 examples; WIT: 5,038,295 examples; ShutterStock: 15,540,452 examples.

**Format**: N/A

**Annotation**: Image-text pairs as provided by original sources (e.g., Flickr captions, HTML alt-text, Wikipedia reference descriptions, Shutterstock captions); no additional manual annotation procedure for labels reported.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Automated metrics (top-1 accuracy)
- Effective Robustness analysis (probit-transformed accuracy and linear trend)
- Input mixing (randomly combining samples from multiple sources)
- Output mixing / Ensembling (ensembling logits of separately trained models)
- Theoretical analysis (simple binary classification model to explain empirical phenomena)

**Metrics**:
- Top-1 Accuracy
- Zero-shot Accuracy
- Effective Robustness (probit-transformed accuracy; linear trend between accuracies on two test sets)

**Calculation**: Robustness is measured by comparing zero-shot Top-1 Accuracy on a reference test set (ImageNet) and several related distribution-shifted test sets (ImageNet-V2, ImageNet-R, ImageNet-Sketch, ObjectNet). Effective Robustness is analyzed via probit-transforming accuracies and examining linear trends/slopes between paired test distributions.

**Interpretation**: Models closer to the y=x line (or with a slope closer to 1 in the probit-transformed accuracy plot) are considered more robust to distribution shift. Mixtures interpolate between individual-source trends; ensembling outputs of single-source models predicts the trend of input-mixed training.

**Baseline Results**: Qualitative baseline comparisons reported: no single pre-training source dominates across shifts; Shutterstock shows best out-of-distribution performance on ImageNet-Sketch, RedCaps shows strongest effective robustness on ObjectNet, and LAION/CC-12M/Shutterstock perform relatively well on ImageNet-R. No single numeric universal baseline reported for all settings.

**Validation**: Experiments were repeated with multiple sample sizes per source (1M to 15M) and averaged over 3 random seeds for data-efficiency plots (Figure 17). Evaluation uses multiple standard distribution-shift test sets (ImageNet-V2, ImageNet-R, ImageNet-Sketch, ObjectNet). Theoretical results (Theorems 1-3) complement empirical findings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Transparency
- Value Alignment
- Governance
- Societal Impact

**Atlas Risks**:
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Governance**: Lack of data transparency, Incomplete usage definition
- **Value Alignment**: Harmful output
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential presence of harmful content (paper cites concerns such as misogyny, pornography, and malignant stereotypes as discussed in Birhane et al.)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The paper notes dataset curation steps such as ensuring LAION-chosen samples have NSFW tags marked 'UNLIKELY' and discusses broadly the potential presence of harmful content in web-crawled multimodal datasets. No systematic anonymization procedures are described.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
