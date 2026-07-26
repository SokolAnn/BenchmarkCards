# ClawBench

## 📊 Benchmark Details

**Name**: ClawBench

**Overview**: ClawBench evaluates AI browser agents on everyday online tasks performed against live websites. Its V1 and V2 suites contain 283 tasks, and each run preserves synchronized evidence for end-to-end task-completion evaluation.

**Data Type**: Multimodal browser-interaction tasks and execution traces

**Domains**:
- Browser automation
- Computer use
- Agent evaluation
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WebArena
- VisualWebArena
- Online-Mind2Web
- OSWorld
- WebVoyager

**Resources**:
- [Project page](https://claw-bench.com/)
- [Paper](https://arxiv.org/abs/2604.08523)
- [GitHub repository](https://github.com/TIGER-AI-Lab/ClawBench)
- [Task dataset](https://huggingface.co/datasets/NAIL-Group/ClawBench)
- [Leaderboard](https://huggingface.co/spaces/TIGER-Lab/ClawBench)

## 🎯 Purpose and Intended Users

**Goal**: To measure whether a model-and-harness combination can complete realistic, multi-step browser workflows on production websites while preserving auditable evidence and blocking the final irreversible request by default.

**Target Audience**:
- AI agent researchers
- Browser-agent developers
- Model and harness evaluators
- Reliability and observability engineers

**Tasks**:
- Multi-step web navigation
- Search and comparison
- Form completion
- Booking and shopping workflows
- Email and productivity workflows
- Job-application workflows

**Limitations**: Live websites can change layout, availability, anti-bot behavior, or workflow paths over time. Full-suite runs are costly, public tasks can become familiar to models, and results depend on the selected task suite, model, harness, judge, and run date. The benchmark does not provide demographic fairness coverage.

**Out of Scope Uses**:
- Treating browser-task pass rate as a general intelligence score
- Comparing results produced with different suites, harnesses, or judging configurations without reporting those differences
- Using the benchmark as a safety, fairness, or cybersecurity certification
- Allowing intercepted irreversible requests to reach production services without separate authorization and controls

## 💾 Data

**Source**: Manually authored everyday online tasks executed on live websites. V1 contains 153 tasks across 144 websites and 15 life categories; V2 adds 130 tasks. V1 Lite links 20 selected V1 tasks for lower-cost iteration.

**Size**: 283 tasks across the V1 and V2 suites, plus a 20-task linked V1 Lite subset

**Format**: JSON task definitions and evaluation schemas; run artifacts include JSONL browser actions, HTTP requests, and agent messages, PNG screenshots, and MP4 session recordings.

**Annotation**: Task authors define natural-language instructions and interception schemas. V1 evaluation can compare agent trajectories with human reference runs; V2 and newer leaderboard runs combine request-schema matching with an LLM judge of the captured request payload.

## 🔬 Methodology

**Methods**:
- Containerized execution against live websites
- Selectable agent harnesses
- Final-request interception
- Five-layer execution-trace capture
- Post-session trajectory evaluation

**Metrics**:
- Task pass rate
- Completed-task count
- Intercepted-request rate

**Calculation**: Pass rate is the number of tasks judged successful divided by the number evaluated. For original V1 results, an agentic evaluator reviews the recorded trajectory against human references. For V2 and newer runs, the interceptor first checks the final blocked request against the task schema, then an LLM judge evaluates whether its payload fulfills the instruction.

**Interpretation**: Higher pass rates indicate stronger end-to-end completion for the reported model, harness, suite, judge, and run configuration. Scores should not be attributed to a model alone when the harness or evaluation setup differs.

**Baseline Results**: Results evolve with new models and harnesses; the project publishes configuration-specific results on its live leaderboard.

**Validation**: Runs preserve session video, action screenshots, HTTP traffic, browser actions, and agent messages. Published task definitions, evaluation schemas, run metadata, and trace datasets support audit and reproduction, while repeated runs can reveal live-site drift.

## ⚠️ Targeted Risks

**Risk Categories**:
- Task failure
- Unintended external action
- Evaluation instability from live-site drift
- Performance overgeneralization

**Atlas Risks**:
No specific Atlas risks defined

**Demographic Analysis**: Not applicable; ClawBench evaluates browser-task completion and does not include a demographic fairness analysis.

**Potential Harm**: A misconfigured run could submit a purchase, message, application, or other external action. The default request interceptor is designed to capture and block irreversible final requests, but operators remain responsible for credentials, trace data, and any configuration that relaxes those controls.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The benchmark uses a shared test profile and benchmark credentials. Five-layer traces can still contain session or service data and should be stored, shared, and deleted under appropriate access controls.

**Data Licensing**: The ClawBench repository is released under Apache License 2.0. Third-party websites, services, and converted datasets retain their own terms and licenses.

**Consent Procedures**: No human-subject consent procedure is specified for the benchmark tasks. Human reference runs are benchmark artifacts rather than participant studies.

**Compliance With Regulations**: Users are responsible for complying with applicable website terms, privacy obligations, and laws. The default interceptor blocks purchases, account creation, outbound messages, and similar irreversible actions before they reach the service.
