# HARRISON (HAshtag Recommendation for Real world Images in SOcial Networks)

## 📊 Benchmark Details

**Name**: HARRISON (HAshtag Recommendation for Real world Images in SOcial Networks)

**Overview**: We introduce the HARRISON dataset, a benchmark on hashtag recommendation for real world images in social networks. The HARRISON dataset is a realistic dataset, composed of 57,383 photos from Instagram and an average of 4.5 associated hashtags for each photo.

**Data Type**: image-hashtag pairs

**Domains**:
- Computer Vision
- Social Networks

**Similar Benchmarks**:
- ImageNet
- Places Database
- ILSVRC (ImageNet Large Scale Visual Recognition Challenge)

**Resources**:
- [GitHub Repository](https://github.com/minstone/HARRISON-Dataset)
- [Resource](http://top-hashtags.com/instagram)
- [Resource](https://netlytic.org/index.php)

## 🎯 Purpose and Intended Users

**Goal**: Provide a benchmark dataset for hashtag recommendation for real-world images in social networks.

**Target Audience**:
- Machine Learning Researchers
- Model Developers

**Tasks**:
- Hashtag Recommendation
- Multi-label Classification
- Image Annotation

**Limitations**: Only the 1,000 most frequently used hashtags are included as classes; hashtags containing non-alphabetic characters were rejected; images with no hashtag or more than 10 hashtags were excluded; inferential or trending hashtags remain challenging for vision-only models.

## 💾 Data

**Source**: Images and associated hashtags collected from Instagram public posts via the platform's public APIs using netlytic.org; initial hashtag selection from http://top-hashtags.com/instagram.

**Size**: 57,383 images; approximately 260,000 hashtags; average 4.5 hashtags per image

**Format**: N/A

**Annotation**: User-provided hashtags from Instagram, post-processed: hashtags containing non-alphabetic characters removed; lemmatization applied; repeated hashtags per image removed; only the top 1,000 most frequent hashtags retained as classes.

## 🔬 Methodology

**Methods**:
- Model-based evaluation using CNN visual feature extractor (VGG-16 trained on ImageNet and Places) + multi-label neural network classifier
- Automated metrics (Precision, Recall, Accuracy)

**Metrics**:
- Precision@1
- Recall@5
- Accuracy@5

**Calculation**: Precision@K = |Result(K) ∩ GT| / |Result(K)|. Recall@K = |Result(K) ∩ GT| / |GT|. Accuracy@K = 1 if Result(K) ∩ GT ≠ ∅ else 0. (Result(K) is the set of top K predicted hashtags; GT is the set of ground truth hashtags.)

**Interpretation**: Precision measures how well hashtags are predicted (portion of top-K predictions that match ground truth). Recall measures coverage of ground truth by top-K predictions. Accuracy@K indicates whether at least one predicted hashtag matches ground truth. In experiments K is set to 1 for precision and 5 for recall and accuracy.

**Baseline Results**: VGG-Object: Precision@1 = 28.30%, Recall@5 = 20.83%, Accuracy@5 = 50.70%. VGG-Scene: Precision@1 = 25.34%, Recall@5 = 18.66%, Accuracy@5 = 46.30%. VGG-Object + VGG-Scene: Precision@1 = 30.16%, Recall@5 = 21.38%, Accuracy@5 = 52.52%.

**Validation**: Random split into 52,383 training images and 5,000 test images.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
