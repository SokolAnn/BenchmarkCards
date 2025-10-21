# SCB-Dataset: A Dataset for Detecting Student and Teacher Classroom Behavior

## 📊 Benchmark Details

**Name**: SCB-Dataset: A Dataset for Detecting Student and Teacher Classroom Behavior

**Overview**: We constructed SCB-Dataset—a comprehensive dataset of student and teacher classroom behaviors covering 19 classes. SCB-Dataset is divided into two types: Object Detection and Image Classification. The Object Detection part includes 13,330 images and 122,977 labels, and the Image Classification part includes 21,019 images. We conducted benchmark tests on SCB-Dataset using YOLO series algorithms and Large vision-language model. We believe that SCB-Dataset can provide a solid foundation for future applications of artificial intelligence in education.

**Data Type**: image (object detection images with bounding box annotations; image classification images with single-label annotations)

**Domains**:
- Computer Vision
- Education

**Similar Benchmarks**:
- COCO
- AVA
- UCF101
- Kinetics400
- STBD-08
- ClaBehavior
- SCBehavior
- UKDatasets

**Resources**:
- [GitHub Repository](https://github.com/Whiffe/SCB-dataset)
- [Resource](https://arxiv.org/abs/2304.02488)
- [Resource](https://universe.roboflow.com/reddy-projects-zulke/classroom-dodzk)

## 🎯 Purpose and Intended Users

**Goal**: Establish a large-scale public dataset of student and teacher classroom behaviors (19 behavior types) to support automatic analysis of classroom performance and advance AI applications in education.

**Tasks**:
- Object Detection
- Image Classification

**Limitations**: Class imbalance across behavior classes; dense classroom scenes causing occlusion; large pixel-size differences between foreground and background students; coexistence of multiple behaviors in single images (multiple-label complexity for object detection); high similarity between some behaviors; overall dataset split procedure for object detection results in overlaps between training and validation sub-parts (reducing meaning of overall train/val counts).

## 💾 Data

**Source**: Collected from open class websites: bilibili, TikTok, 1s1k, and bjyhjy; frames extracted from classroom videos (includes data from China’s ethnic minorities).

**Size**: Object Detection: 13,330 images and 122,977 annotations; Image Classification: 21,019 images (21,019 labels).

**Format**: VIA JSON (annotations created/verified using VIA tool and viaJson counting/verification tools)

**Annotation**: Manual annotation using the VIA annotation tool with an extensible behavior annotation method; annotation verification via viaJson; multiple improvements to VIA were used (see Appendix A.1).

## 🔬 Methodology

**Methods**:
- Object Detection model evaluation using YOLO series (YOLOv5, YOLOv7, YOLOv8, YOLOv9–v13 tested)
- Image Classification / LVLM fine-tuning using Qwen2.5-VL-7B-instruct (via LLaMA Factory framework and LoRA)
- Automated evaluation metrics (precision, recall, mAP) and classification metrics (precision, recall, F1)

**Metrics**:
- Precision
- Recall
- Mean Average Precision (mAP@0.5)
- Mean Average Precision (mAP@0.95)
- Mean Average Precision (mAP@0.75)
- F1 Score

**Calculation**: mAP@0.5 represents mean Average Precision at Intersection over Union threshold of 0.5; mAP@0.95 represents mean Average Precision at Intersection over Union threshold of 0.95. Precision (P) and Recall (R) are reported per class; F1 is reported for image classification results.

**Interpretation**: The paper states that if mAP@0.5 reaches 70% for a behavior, that behavior can basically be used for practical applications.

**Baseline Results**: Object detection: YOLO series baselines reported. YOLOv7 achieved the highest reported teacher-behavior mAP@0.5 at 94.0% (YOLOv5 reported 88.1%, YOLOv8 reported 93.6%). Per-class YOLOv7 mAP@0.5 examples (from Table 2): hand-raising 79.2%, read 70.5%, write 72.2%, discuss 74.7%, blackboard-writing 96.4%, teacher 97.7%. Image classification: Qwen2.5-VL-7B-instruct (LLaMA Factory, LoRA) results (Table 3) report overall P=86.1%, R=83.4%, F1=83.8% with per-class P/R/F1 values listed in Table 3 (e.g., hand-raising F1 86.3, read and write F1 88.5, discuss F1 92.0).

**Validation**: For image classification, standard train/validation splits are used. For object detection, due to class imbalance and selective annotation (to reduce imbalance), the dataset was split into multiple sub-parts; each sub-part's train and validation sets were independently and randomly divided in a ratio of 4:1, resulting in overlaps between training and validation sets of different sub-parts; thus the overall object detection train/val counts are stated as having no practical reference significance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Transparency
- Intellectual Property
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Data contamination, Unrepresentative data
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Intellectual Property**: Copyright infringement
- **Robustness**

**Demographic Analysis**: Dataset includes diversity across shooting angles, class/course types, learning stages from kindergarten through university, and different ethnic backgrounds (including China's ethnic minorities).

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
