# Scaling Robot Supervision to Hundreds of Hours with RoboTurk: Robotic Manipulation Dataset through Human Reasoning and Dexterity

## 📊 Benchmark Details

**Name**: Scaling Robot Supervision to Hundreds of Hours with RoboTurk: Robotic Manipulation Dataset through Human Reasoning and Dexterity

**Overview**: We leverage and extend the RoboTurk platform to scale up data collection for robotic manipulation using remote teleoperation to (1) increase the total quantity of manipulation data collected through human supervision by an order of magnitude without sacrificing the quality of the data and (2) collect data on challenging manipulation tasks across several operators and observe a diverse set of emergent behaviors and solutions. We collected over 111 hours of robot manipulation data across 54 users and 3 challenging manipulation tasks in 1 week, resulting in the largest robot dataset collected via remote teleoperation.

**Data Type**: multimodal: RGB images, depth images, robot sensor time-series (joint and end-effector readings), and teleoperator video streams

**Domains**:
- Robotics
- Robotic Manipulation
- Computer Vision

**Similar Benchmarks**:
- JIGSAWS
- Deep Imitation
- DAML
- MIME
- PbD

**Resources**:
- [Resource](https://arxiv.org/abs/1911.04052)

## 🎯 Purpose and Intended Users

**Goal**: Scale remote human-supervised data collection on physical robots to increase quantity and diversity of high-quality robotic manipulation demonstrations and evaluate the platform and dataset utility.

**Target Audience**:
- Robotics researchers
- Machine Learning researchers
- Model developers

**Tasks**:
- Object Search
- Tower Creation
- Laundry Layout

**Limitations**: Our attempts to learn from the entire dataset were ultimately unsuccessful due to the diverse nature of the demonstrations; addressing the diversity of the dataset for policy learning is left for future work.

## 💾 Data

**Source**: Collected via the extended RoboTurk platform through remote teleoperation on three Sawyer robot arms across 54 users performing the three tasks (Object Search, Tower Creation, Laundry Layout).

**Size**: 111.25 hours total; 2,144 demonstrations; 54 users; collected over 1 week.

**Format**: ROS rosbags containing RGB images (front-facing camera) at 30Hz, RGB and Depth images (top-down Kinectv2) at 30Hz, and robot sensor readings (joint and end-effector) at approximately 100Hz.

**Annotation**: Recorded teleoperation demonstrations by human operators; no additional manual annotations beyond recorded sensor streams are specified.

## 🔬 Methodology

**Methods**:
- Quantitative user performance analysis
- Qualitative user feedback (NASA TLX)
- Embedding learning via modified Time-Contrastive Networks (TCN) for reward inference
- Behavioral Cloning experiments
- Comparative dataset analysis against prior human-supervised robot datasets

**Metrics**:
- Task completion time (seconds)
- NASA Task Load Index (NASA TLX) scores (mental demand, physical demand, temporal demand, performance, effort, frustration, total workload)
- Average effort (square L2 norm of phone translations)
- Average orientation change
- Total demonstration time (hours)
- Number of demonstrations

**Calculation**: Total workload (NASA TLX) was computed as the sum of the averaged subscales. Average user exertion was estimated by the square L2 norms of phone translations. Embedding-based reward used negative L2 distance in the learned embedding space (modified TCN).

**Interpretation**: Decreasing task completion time indicates improved user performance; higher NASA TLX scores indicate higher workload; smaller embedding distance to a terminal (successful) frame indicates closer task progress or success; average effort (L2 norm) largely invariant with experience while orientation change increases with experience.

**Validation**: Validated the platform and dataset via quantitative analyses (skill improvement over experience, task completion time, effort, orientation change), qualitative analyses (diversity of demonstrations), NASA TLX user studies, and comparative dataset statistics (Table I) against prior human-supervised robot datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness
- Data Quality

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Misuse**: Dangerous use

**Demographic Analysis**: N/A

**Potential Harm**: Ensuring operational safety to prevent damage to robot arms and workspaces when operated by novice remote users.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
