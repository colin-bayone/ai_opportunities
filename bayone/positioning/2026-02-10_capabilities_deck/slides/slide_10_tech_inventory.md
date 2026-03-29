# Slide 10 Technology Inventory

## Purpose
Organize all technologies/techniques mentioned across slides 5-9 to determine what should appear on slide 10 (Technology Foundation).

---

## SUPERSET: All Technologies Mentioned Across Slides

### From Slide 5 (Developer Productivity)
- CI/CD pipeline monitoring
- Figma integration
- Design-to-code pipelines
- Pull request workflows

### From Slide 6 (Enterprise Automation)
- MCP (Model Context Protocol)
- Agent-to-Agent (A2A)
- Semantic Kernel
- Function calling / tool use
- Event-driven architectures
- Custom API integrations

### From Slide 7 (Data & Analytics)
- ETL pipelines
- MLOps infrastructure
- Real-time streaming
- Multi-source ingestion
- Data quality monitoring
- Lineage tracking
- Conversational BI / natural language interfaces
- Churn prediction
- Demand forecasting
- Customer segmentation
- Synthetic data generation

### From Slide 8 (Document Intelligence)
- RAG (Retrieval-Augmented Generation)
- Deterministic extraction
- Vision-based extraction
- KVP extraction
- Named entity recognition
- Semantic chunking
- Redaction
- Template-based generation
- Multi-modal understanding
- Chart interpretation
- Image captioning
- Cross-modal search

### From Slide 9 (Applied AI & Intelligent Systems)
- Defect detection
- Edge deployment
- Industrial hardware integration
- Gradient-boosted models
- Reinforcement learning
- Digital twin
- Time-series analysis
- Remaining useful life estimation
- On-premise deployment
- Air-gapped deployment
- Secure hybrid deployment

---

## CURRENT Slide 10 Categories & Items

### GenAI & LLM
- Custom model fine-tuning
- RAG architectures
- Prompt engineering
- Multi-model orchestration
- Local LLM deployment

### Agent Frameworks (updated)
- LangGraph/ LangChain
- CrewAI
- AutoGen
- Semantic Kernel
- OpenAI Agents SDK
- Model Context Protocol (MCP)

### Computer Vision
- R-CNN, YOLO architectures
- Defect detection systems
- Multi-modal vision-language
- Edge deployment
- Real-time inference

### Data Engineering
- ETL pipeline design
- Apache Kafka, Spark
- Vector databases
- Data quality frameworks
- Real-time streaming

### Cloud & MLOps
- Azure, AWS, GCP
- Kubernetes orchestration
- CI/CD for ML
- Model monitoring
- A/B testing infrastructure

### ML & Optimization (updated)
- Deep learning & reinforcement learning
- Gradient boosting & ensemble methods
- Time-series forecasting
- Anomaly detection
- Classification, regression & clustering
- Model explainability & interpretability
- Digital twin integration

---

## GAP ANALYSIS: What's Missing from Slide 10?

### Agent Frameworks - MISSING:
- [ ] Agent-to-Agent (A2A) - mentioned on slide 6
- [ ] Function calling / tool use - mentioned on slide 6
- [ ] LlamaIndex - not mentioned but relevant for RAG/data workflows

### Data Engineering - MISSING:
- [ ] Event-driven architectures - mentioned on slide 6
- [ ] Data lineage tracking - mentioned on slide 7
- [ ] Synthetic data generation - mentioned on slide 7

### GenAI & LLM - MISSING:
- [ ] Semantic chunking - mentioned on slide 8
- [ ] Named entity recognition (NER) - mentioned on slide 8

### Document Processing - NOT A CATEGORY YET:
- [ ] Deterministic extraction
- [ ] Vision-based extraction
- [ ] KVP extraction
- [ ] Redaction
- [ ] Template-based generation

### Cloud & MLOps - Possibly missing:
- [ ] On-premise deployment options
- [ ] Air-gapped deployment
- [ ] Secure hybrid deployment

---

## DECISIONS NEEDED

1. **Agent Frameworks** - Add A2A, function calling/tool use, LlamaIndex?

2. **Data Engineering** - Add event-driven architectures, lineage tracking, synthetic data?

3. **Document Processing** - Should this be its own category? Or fold into GenAI?

4. **Deployment options** - Should on-prem/air-gapped/hybrid be called out in Cloud & MLOps?

5. **Length balance** - Some cards have 5 items, some have 6-7. How consistent do we need to be?

---

## PROPOSED FINAL STATE (for discussion)

### GenAI & LLM (5 items)
- Custom model fine-tuning
- RAG architectures
- Prompt engineering
- Multi-model orchestration
- Local LLM deployment

### Agent Frameworks (7 items)
- LangGraph/ LangChain
- CrewAI
- AutoGen
- Semantic Kernel
- OpenAI Agents SDK
- Model Context Protocol (MCP)
- Agent-to-Agent (A2A)
- *(Consider: LlamaIndex, Function calling)*

### Computer Vision (5 items)
- R-CNN, YOLO architectures
- Defect detection systems
- Multi-modal vision-language
- Edge deployment
- Real-time inference

### Data Engineering (6-7 items)
- ETL pipeline design
- Apache Kafka, Spark
- Vector databases
- Data quality frameworks
- Real-time streaming
- Event-driven architectures
- *(Consider: Data lineage, Synthetic data)*

### Cloud & MLOps (5-6 items)
- Azure, AWS, GCP
- Kubernetes orchestration
- CI/CD for ML
- Model monitoring
- A/B testing infrastructure
- *(Consider: On-prem/hybrid deployment)*

### ML & Optimization (7 items)
- Deep learning & reinforcement learning
- Gradient boosting & ensemble methods
- Time-series forecasting
- Anomaly detection
- Classification, regression & clustering
- Model explainability & interpretability
- Digital twin integration

---

## Notes
- This is a working document to organize thoughts before making HTML changes
- Goal: Show breadth and depth without being exhaustive
- Balance: Specific enough to show technical credibility, not so specific it limits us
