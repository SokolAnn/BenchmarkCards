# LSA-T: The ﬁrst continuous Argentinian Sign Language dataset for Sign Language Translation

## 📊 Benchmark Details

**Name**: LSA-T: The ﬁrst continuous Argentinian Sign Language dataset for Sign Language Translation

**Overview**: Presents LSA-T, the first continuous Argentinian Sign Language (LSA) dataset for Sign Language Translation. It contains 14,880 sentence-level video segments extracted from the CN Sordos YouTube channel with corresponding Spanish sentence labels and keypoint annotations per signer. The paper also provides a method to infer the active signer, a visualization tool, and a baseline neural SLT model using keypoints.

**Data Type**: sentence-level video segments with Spanish text labels and keypoint annotations

**Domains**:
- Human-Computer Interaction
- Computer Vision
- Natural Language Processing
- Machine Learning

**Languages**:
- Argentinian Sign Language
- Spanish

**Similar Benchmarks**:
- RWTH-Phoenix-Weather 2014 T
- SIGNUM
- Chinese Sign Language dataset (CSL)
- Greek Sign Language dataset (GSL)
- KETI

**Resources**:
- [Resource](https://arxiv.org/abs/2211.15481)
- [GitHub Repository](https://github.com/midusi/LSA-T)
- [GitHub Repository](https://github.com/midusi/keypoint-models)
- [Resource](https://www.youtube.com/channel/UCTi9woRHA4r8e3oEWF8hxTA)
- [GitHub Repository](https://github.com/voxel51/fiftyone)

## 🎯 Purpose and Intended Users

**Goal**: Provide and analyze LSA-T, the first continuous Argentinian Sign Language dataset to enable training and evaluation of Sign Language Translation models (video-to-text) and to serve as a baseline for future experiments.

**Target Audience**:
- Machine Learning Researchers
- Computer Vision Researchers
- Natural Language Processing Researchers
- Sign Language Translation researchers

**Tasks**:
- Sign Language Translation
- Text-to-sign video generation (mentioned, not focus)

**Limitations**: High proportion of unique sentences (≈95%) and a large fraction of singletons (≈50% of vocabulary) making training and evaluation challenging; a large portion of test samples contain tokens not present in the train set (≈60% in full version, ≈85% in reduced version); samples with signer-confidence score lower than 0.5 were discarded.

## 💾 Data

**Source**: Videos from the CN Sordos YouTube channel (videos annotated with subtitles by the channel authors / LSA experts).

**Size**: 14,880 video segments spanning 21.78 hours of video

**Format**: N/A

**Annotation**: Spanish sentence labels (subtitles provided by authors); keypoint annotations computed using AlphaPose with Halpe full-body format (136 keypoints, 42 hand keypoints); signer inference score and inferred active signer per sample.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (baseline neural SLT model using keypoint inputs and transformer layers)
- Automated metrics (WER and WER-N)
- Train-test evaluation with two default splits (full and reduced versions; 80% train / 20% test)

**Metrics**:
- Word Error Rate (WER)
- WER-N (proposed variant of WER that ignores errors for target tokens with training frequency lower than N)

**Calculation**: WER-N is computed via a variant of the Edit Distance algorithm where deletion and substitution costs are set to 0 for target tokens whose frequency in the training set is lower than N; otherwise costs follow standard definitions. The paper provides the recursive edit-distance formulation and defines C(D) and C(S) to be 0 when token frequency < N and 1 otherwise.

**Interpretation**: High WER indicates poor translation performance due to dataset difficulty (many rare tokens and unique sentences). WER-N mitigates penalization for rare tokens by ignoring errors on tokens seen fewer than N times in training; lower WER-N indicates better model handling of frequent tokens. The authors report that the baseline model performs poorly on this dataset, illustrating its challenging nature.

**Baseline Results**: Full version (Train/Test): WER 0.9387 / 0.9392; WER-5 0.8116 / 0.7892; WER-10 0.7547 / 0.7154. Reduced version (Train/Test): WER 0.9207 / 0.957; WER-5 0.7982 / 0.68; WER-10 0.7193 / 0.5904.

**Validation**: Two versions of train-test splits provided: full and reduced. Reduced version excludes labels with words of frequency lower than 5. Both use an 80% train / 20% test split. Samples with signer-confidence score < 0.5 were discarded. Train and test sets were constructed such that segments from the same video may appear in both sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Dataset contains 103 signers, with gender parity among signers; most signers are guests appearing once or twice. Videos contain varied locations, backgrounds, and lighting conditions.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
