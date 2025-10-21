# Concept Drift and Long-Tailed Distribution (CDLT)

## 📊 Benchmark Details

**Name**: Concept Drift and Long-Tailed Distribution (CDLT)

**Overview**: A novel fine-grained visual categorization dataset that focuses on concept drift and long-tailed distribution in real-world scenarios. The dataset is collected by gathering 11,195 images of succulent plant instances across 258 subclasses over 47 consecutive months in natural contexts, with season information recorded as auxiliary data. The dataset is intended to facilitate research on concept drift and long-tailed recognition and to benchmark algorithms under these challenges.

**Data Type**: image (image-label pairs)

**Domains**:
- Computer Vision

**Similar Benchmarks**:
- ImageNet-LT
- Places-LT
- LVIS
- Long-tailed CIFAR-10
- Long-tailed CIFAR-100
- CUB 200-2011
- Stanford Dogs
- Oxford Pets
- NABirds
- Stanford Cars

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Provide a dataset (CDLT) that exposes concept drift and long-tailed distribution issues in fine-grained visual categorization to promote development of practical FGVC methods and to serve as a benchmark for these challenges.

**Target Audience**:
- Researchers in Fine-grained Visual Categorization
- Computer Vision Researchers
- Model Developers

**Tasks**:
- Fine-grained Visual Categorization
- Image Classification
- Long-tailed Recognition
- Concept Drift Evaluation

**Limitations**: Collected data relating to sudden drift is limited; not every subclass exhibits significant periodic drift and the authors plan to provide specific drift labels in future work.

## 💾 Data

**Source**: Photographing in real scenes from 38 cities in 17 provincial-level administrative regions in China over 47 consecutive months; data collected by dozens of crowd workers and labeled/verified by domain experts.

**Size**: 11,195 images (final released dataset); 14,512 raw collected samples prior to selection; 258 subclasses; dataset collected over 47 consecutive months.

**Format**: Image files resized to have a maximal dimension of 1200px.

**Annotation**: Manual annotation by domain experts: labels include family, genus, and species; auxiliary information records the season at photographing time. Each sub-class's images were examined by four experts and retained if affirmed by more than two examiners.

## 🔬 Methodology

**Methods**:
- Automated metrics (Top-1 and Top-5 accuracy)
- Model benchmarking using state-of-the-art FGVC models and backbones (ResNet-50, Inception-v4, VGG-16, ViT) and FGVC methods (B-CNN, HBP, NTS-Net, MCL, MOMN, etc.)
- Evaluation of long-tailed specialized methods (re-sampling, focal loss, range loss, class-balanced loss)
- Evaluation of vision-language models (CLIP) with and without fine-tuning
- Maximum Mean Discrepancy (MMD) to quantify distributional shift between training and test

**Metrics**:
- Top-1 Accuracy
- Top-5 Accuracy
- Maximum Mean Discrepancy (MMD)

**Calculation**: Top-1 and Top-5 accuracies computed on provided train/test splits (6:4 split selected empirically). MMD computed per subclass between training and test sets with 100 independent permutations to obtain 95% confidence interval.

**Interpretation**: Higher Top-1/Top-5 accuracy indicates better classification performance. MMD values above the 95% confidence bound indicate a 'significant' distributional change (concept drift). Training on single-season data significantly impairs generalization compared to training on all-season data. The authors report a performance gap of about 5% when drifted data is ignored in training for many models.

**Baseline Results**: Selected results on CDLT: B-CNN (ResNet-50) 72.79% (Top-1), HBP (ResNet-50) 75.64%, NTS-Net (ResNet-50) 78.20%, MCL (ResNet-50) 75.42%, MOMN (ResNet-50) 69.76%, OURS (ResNet-50) 78.82%; ViT (ViT-B-16) 77.81%, OURS (ViT-B-16) 79.20%. CLIP on CDLT: Pre-trained baseline 3.03%, CLIP(B) 2.02%, CLIP(L) 2.32%.

**Validation**: Experiments repeated three times independently and averaged. Random-label experiment: when training labels are randomized, Top-1/Top-5 accuracies drop to 0.53% and 2.18%, validating label meaningfulness. MMD analysis uses 100 permutations to compute 95% confidence bounds for significance testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
