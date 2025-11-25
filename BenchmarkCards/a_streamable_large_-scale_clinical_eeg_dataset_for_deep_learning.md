# A streamable large -scale clinical EEG dataset for Deep Learning

## 📊 Benchmark Details

**Name**: A streamable large -scale clinical EEG dataset for Deep Learning

**Overview**: We are publishing the first large -scale clinical EEG dataset that simplifies data access and management for Deep Learning. This dataset contains eyes-closed EEG data prepared from a collection of 1,574 juvenile participants from the Healthy Brain Network.

**Data Type**: time-series (EEG recordings; 2-second epochs, 24 channels x 256 time points)

**Domains**:
- Neuroscience
- Biomedical Research

**Similar Benchmarks**:
- Healthy Brain Network

**Resources**:
- [GitHub Repository](https://github.com/sccn/HBN-rest-DL)
- [Resource](https://childmind.s3.us-west-1.amazonaws.com/python/childmind_python.zip)
- [Resource](https://childmind.s3.us-west-1.amazonaws.com/matlab/childmind_matlab.zip)
- [Resource](https://childmind.s3.us-west-1.amazonaws.com/python/childmind_train.tar)
- [Resource](http://coins.mrn.org/dx)
- [Resource](http://data.healthybrainnetwork.org/)
- [Resource](http://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/sharing.html)

## 🎯 Purpose and Intended Users

**Goal**: Publish a large-scale EEG dataset prepared in a format that is readily used by current Deep Learning models, simplifying data access and management (including streaming from AWS S3) to accelerate Deep Learning research on EEG.

**Target Audience**:
- Neuroscience researchers
- Deep Learning researchers
- Non-EEG experts

**Tasks**:
- Classification (biological sex classification)
- Self-Supervised Learning (temporal context prediction)
- Representation Learning

**Limitations**: Model training when streaming the data suffers from a significant slowdown as compared to loading the entire dataset locally. Dataset uses only eye-closed segments (~170s per subject) and was sub-selected to 24 channels out of 128 for the benchmark experiment.

## 💾 Data

**Source**: Subset of EEG data (eyes-closed resting state) from the Healthy Brain Network (HBN) by the Child Mind Institute; 1,574 subjects (juvenile participants, ages 5-21).

**Size**: 1,574 subjects; 127,174 samples total (71,300 training samples from 885 participants; 39,868 validation samples from 492 participants; 16,006 test samples from 197 participants); each subject provided about 81 2-second samples (mean 80.8 ± 3.32).

**Format**: MAT file (.mat) for MATLAB; NumPy array files (.npy) for Python; packaged as POSIX tar archives for WebDataset streaming. Original recording sampled at 500 Hz then downsampled to 128 Hz; final samples are 24 x 256 (channels x timepoints).

**Annotation**: Labels provided from subject metadata: biological sex (binary 0=Male, 1=Female), age, handedness, within-subject segment position, and original subject IDs. Clinical phenotypes available on request via COINS or HBN LORIS subject to a Data Usage Agreement (DUA).

## 🔬 Methodology

**Methods**:
- Model training and evaluation (supervised deep learning) using a modified VGG-16 architecture for biological sex classification
- Data streaming during training using MATLAB imageDatastore and PyTorch WebDataset

**Metrics**:
- Accuracy (per-subject)
- 95% confidence interval for Accuracy

**Calculation**: Per-subject classification Accuracy reported; authors report Accuracy with a 95% confidence interval (86.6% - 87.4%).

**Interpretation**: Authors report a per-subject classification accuracy of 87% (95% CI 86.6% - 87.4%) on the biological sex classification task and interpret this result as achieving state-of-the-art performance for this task on their dataset.

**Baseline Results**: Modified VGG-16 model achieved per-subject classification accuracy of 87% (95% confidence interval 86.6% - 87.4%) on the test set.

**Validation**: Dataset split into training, validation, and test sets with size ratio 60:30:10 (71,300 samples, 39,868 samples, and 16,006 samples respectively); evaluation performed on held-out test set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Data Laws

**Atlas Risks**:
- **Data Laws**: Data usage restrictions
- **Privacy**: Personal information in data, Exposing personal information

**Demographic Analysis**: Provides demographic breakdowns: biological sex roughly 50% female in train/validation/test; age statistics per split (Train: min 5.02 max 21.9 mean 10.5 median 9.74 stdev 3.61; Validation: min 5.04 max 21.7 mean 10.5 median 9.88 stdev 3.68; Test: min 5.06 max 21.2 mean 10.7 median 10.3 stdev 3.37). Handedness statistics provided per split (Train mean 57.9 median 75.6 stdev 50.0; Validation mean 58.6 median 75.6 stdev 49.4; Test mean 54.3 median 76.7 stdev 56.1).

**Potential Harm**: ['Breaches of participant privacy/confidentiality']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Original subject IDs are provided; clinical phenotypes and high-dimensional phenotypic data are protected and require a Data Usage Agreement (DUA) to access. The DUA is intended to ensure users protect participant confidentiality and take measures to prevent breaches of privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
