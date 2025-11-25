# Eye-Quality (EyeQ) and Fundus-iSee (iSee)

## 📊 Benchmark Details

**Name**: Eye-Quality (EyeQ) and Fundus-iSee (iSee)

**Overview**: The EyeQ and iSee datasets provide a foundation for exploring dataset quality effects on the performance of large foundation models in fundus disease diagnosis, focusing on various quality levels and the impact of dataset bias.

**Data Type**: retinal images

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- RETFound

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the influence of dataset quality and bias on large foundation models in medical diagnostic tasks.

**Target Audience**:
- Medical Researchers
- Machine Learning Researchers

**Tasks**:
- Image Classification

**Limitations**: N/A

## 💾 Data

**Source**: EyeQ dataset and iSee dataset comprising retinal images of varying quality.

**Size**: 38,574 images (28,785 from EyeQ and 9,789 from iSee)

**Format**: N/A

**Annotation**: Images annotated based on quality levels and diabetic retinopathy categories.

## 🔬 Methodology

**Methods**:
- Overall fine-tuning
- Linear Probe
- Tip-Adapter

**Metrics**:
- Area Under the Receiver Operating Characteristic curve (AUROC)

**Calculation**: Metrics are calculated by evaluating the models on subsets of the EyeQ and iSee datasets.

**Interpretation**: Higher AUROC values indicate better performance in detecting diabetic retinopathy and fundus diseases.

**Baseline Results**: RETFound demonstrates more stable performance across varying image quality compared to ResNet.

**Validation**: Each model's performance was validated across multiple quality subsets through repetitive trials.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
