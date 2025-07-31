
Architectural Blueprint for an LLM-Powered ServiceNow Ticket Analysis & Automation Intelligence System


Part I: Strategic Imperative and System Overview


Section 1: Introduction and Executive Summary


1.1. Project Mandate

This document presents the comprehensive architectural and implementation plan for a Proof of Concept (POC) system. The system is designed to analyze ServiceNow IT support tickets, encompassing both CTasks and Incidents, by leveraging a custom-hosted Claude Sonnet 4 Large Language Model (LLM) on the AWS Bedrock platform. The blueprint details the end-to-end architecture, from data ingestion and processing to analysis and visualization, providing a clear roadmap for development and evaluation.

1.2. Core Objective

The primary objective of this initiative is to evolve beyond traditional, reactive IT Service Management (ITSM) paradigms. The system will transcend simple ticket categorization to deliver proactive, intelligent analysis. The central goal is to automatically identify recurring issue patterns within the ticket data and, most critically, to generate specific, actionable recommendations for automation. By achieving this, the system aims to significantly reduce manual toil, decrease Mean Time to Resolution (MTTR), and elevate overall IT operational efficiency and resilience.

1.3. Key Capabilities

The proposed system is architected to deliver a suite of advanced capabilities:
Dual Analysis: The system is designed to ingest, process, and analyze both ServiceNow CTask and Incident ticket types, providing a holistic view of operational workloads.
Intelligent Clustering: A semantic clustering engine will group tickets based on their underlying meaning and context, rather than simple keyword matching, to accurately identify thematic issues that may not be obvious through manual review.
Multi-Stage LLM Analysis: A hierarchical analysis framework will process tickets in stages, beginning with individual ticket triage and categorization, progressing to deep pattern analysis within clusters, and culminating in cross-cluster strategic insight generation.
Automation Intelligence: The system's core output will be concrete automation proposals. These will include recommendations for specific tools (e.g., Ansible, Bash scripts) and a logical outline for the proposed automation scripts, providing a clear starting point for development.
Actionable Visualization: A suite of purpose-built Grafana dashboards will provide tailored views for executive, managerial, and operational stakeholders, translating raw data into strategic insights and a clear operational picture.

1.4. Expected Business Impact (POC Scope - UNIX SA Team)

The initial POC will focus on the ticket workload of the UNIX SA team to validate the system's efficacy in a controlled environment. The expected outcomes are:
Demonstrate a quantifiable reduction in the time senior engineers spend manually analyzing ticket trends and identifying root causes.
Identify, categorize, and rank the top 5-10 automation opportunities for the UNIX SA team, complete with an estimated Return on Investment (ROI) for each.
Establish a robust baseline for system performance, processing throughput, and LLM analysis accuracy, which will inform the business case for an enterprise-wide deployment.
Industry analyses indicate that Generative AI technologies hold the potential to automate tasks that currently consume 60 to 70 percent of employee time.1 Furthermore, successful implementations in ITSM have demonstrated a 15% to 20% reduction in ticket volume through automated self-service solutions.2 This POC is designed to validate these industry benchmarks within our specific operational context and provide empirical data for future investment decisions.

Section 2: The AIOps Value Proposition for IT Service Management (ITSM)


2.1. Evolving from Reactive to Predictive ITSM

The application of advanced AI to IT operations, or AIOps, represents a fundamental paradigm shift. Traditional ITSM platforms have historically relied on methods such as manual feature engineering or rule-based systems for ticket routing and analysis. These approaches often struggle to effectively comprehend the rich, unstructured natural language contained within ticket descriptions and work notes, leading to difficulties in accurately identifying critical issues.3
The advent of powerful LLMs fundamentally changes this landscape. LLMs possess a remarkable capability to understand natural language, context, sentiment, and the nuanced relationships between disparate pieces of information.4 This enables a strategic evolution from a reactive posture—where teams primarily respond to incidents as they occur—to a predictive and prescriptive model. The system proposed here is designed not just to categorize what has already happened, but to analyze trends to predict future issues and prescribe specific, high-impact actions to prevent them.2 By uncovering hidden patterns and their root causes, the system facilitates proactive problem management, directly contributing to a more stable and efficient IT environment.6

2.2. Beyond ServiceNow's Native AI

ServiceNow offers a suite of native AI capabilities, including Predictive Intelligence (PI) and Now Assist, which provide functionalities like automated categorization, prioritization, and similar incident suggestions.1 While powerful, the strategic decision to build this POC using a custom Claude Sonnet 4 model on AWS Bedrock offers several distinct and compelling advantages that align with long-term goals:
Model Sovereignty and Customization: Utilizing a dedicated model on a platform like Bedrock provides complete control over its operational parameters. This is a critical advantage for future enhancements, such as fine-tuning the model on our organization's proprietary ticket data and knowledge base articles. This process, which is also a feature of ServiceNow's native tools 1, allows the model to learn the specific jargon, technologies, and resolution patterns unique to our environment, thereby significantly increasing its accuracy and relevance.3 This level of control mitigates the risks associated with cost escalation and data privacy concerns inherent in exclusive reliance on third-party, black-box solutions.9
Architectural Flexibility and Integration: The proposed architecture is built on an open and extensible technology stack (Linux, PostgreSQL, Python). This provides complete freedom to design and implement bespoke, complex processing pipelines that are not constrained by the ServiceNow platform's native architecture. It allows for seamless integration with other enterprise data systems and the implementation of custom logic, such as the advanced pre-clustering and representative sampling techniques detailed in this document, which are essential for cost and performance optimization.
Advanced Prompt Engineering: The system's effectiveness is heavily dependent on the quality of the prompts sent to the LLM. Using a direct API to a model like Claude Sonnet 4 allows for the development of highly sophisticated, multi-stage "prompt chains" that are explicitly designed to leverage the model's advanced reasoning capabilities. This goes beyond the pre-built, topic-based conversational models found in some ITSM tools 10, enabling a deeper and more nuanced analysis tailored precisely to our objectives of root cause identification and automation recommendation.

2.3. Quantifying the Opportunity - Initial ROI Framework

The value proposition of this system is grounded in tangible operational and financial improvements. The primary drivers of ROI are the reduction of manual labor costs, increased productivity of high-skilled personnel, and enhanced operational stability through the reduction of recurring incidents.
Cost-Saving Calculation: The most direct financial benefit comes from reducing the time spent on manual ticket analysis. This can be modeled with the formula:

ROISavings​=(Avg. time per manual ticket analysis)×(Number of tickets)×(Blended hourly rate of analyst)
Productivity Gain: By automating the repetitive and time-consuming tasks of pattern detection and root cause analysis, the system frees up senior engineers and subject matter experts. This allows them to focus on more complex, high-value strategic initiatives and innovation, rather than routine operational fire-fighting, a key benefit highlighted in industry case studies.2
Incident Reduction and Avoidance: Proactive problem management, fueled by the system's ability to identify systemic root causes, will lead to a reduction in the frequency and business impact of recurring incidents.6 This translates to improved service availability, reduced business disruption, and enhanced end-user satisfaction.
The Grafana dashboards are a core component of this ROI framework. They will be designed to continuously track these key metrics, providing real-time visibility into the value generated by the system and the automations it inspires.11
The strategic value of this POC extends far beyond the immediate benefits for the UNIX SA team. The proposed architecture establishes a reusable and extensible "Intelligence Factory" pattern. The system's design intentionally decouples the data ingestion module from the core processing and analysis pipeline. While the initial data extractor is specific to ServiceNow, it is a pluggable component. The remainder of the architecture—the message broker, the asynchronous task queue, the multi-stage LLM analysis framework, and the visualization layer—is fundamentally domain-agnostic.
This modularity means that by simply developing new data extractor modules, the entire powerful analysis pipeline can be repurposed to process any text-based operational data source across the enterprise. Future applications could include analyzing network device logs to predict outages, processing application performance monitoring (APM) alerts to identify software bugs, or synthesizing customer feedback from Jira tickets to inform product development.4 Consequently, this POC is not merely a project to build a cost-saving tool for a single team; it is the validation of a foundational AIOps capability for the entire IT organization. This perspective elevates the ROI discussion from a tactical, team-level optimization to a strategic, enterprise-wide investment in operational intelligence.

Part II: End-to-End Processing and Analysis Architecture


Section 3: System Architecture and Data Flow

The system is designed as a scalable, resilient, and modular pipeline that orchestrates data flow from ServiceNow to the final visualization layer in Grafana. Each component is chosen to fulfill a specific role, ensuring efficient and asynchronous processing of large volumes of ticket data.

3.1. Component Overview

The end-to-end architecture comprises the following key components, deployed within a secure Linux VM environment:
ServiceNow Instance: The authoritative source system for all CTask and Incident records. Data will be accessed via the ServiceNow Table API.
Data Extractor (Python/Cron): A scheduled Python script responsible for querying the ServiceNow API. It retrieves new and recently updated tickets based on predefined criteria (e.g., team_category, created_date) and prepares them for ingestion into the pipeline.
Message Broker (RabbitMQ): Serves as the asynchronous backbone of the system. The Data Extractor publishes ticket data as messages to a queue. This decouples the ingestion process from the analysis workload, creating a resilient buffer that can handle spikes in ticket volume and ensure no data is lost if downstream components are temporarily unavailable.12
Asynchronous Task Queue (Celery): A distributed task queue system that manages a pool of worker processes. These workers consume messages from the RabbitMQ queue and execute the computationally intensive analysis tasks, enabling parallel processing and horizontal scalability.14
Processing Core (Python): This is the logical heart of the system, implemented as a series of Celery tasks. It contains the code for text pre-processing, semantic embedding generation, pre-clustering, representative sampling, prompt construction, and interaction with the LLM.
LLM Endpoint (AWS Bedrock): The secure API endpoint for the custom Claude Sonnet 4 model. All interactions will be managed through the AWS SDK, ensuring proper authentication and security.
Data Persistence (PostgreSQL): A robust, open-source relational database that serves as the system's analytical data store. It will house the raw ticket data, all intermediate and final analysis results from the LLM, and pre-computed aggregate metrics for dashboarding.
Visualization Layer (Grafana): The user-facing component of the system. Grafana will connect directly to the PostgreSQL database to query the analysis results and render a suite of interactive, real-time dashboards for various stakeholder groups.

3.2. Data Flow Narrative

The journey of a ticket through the system follows a well-defined, asynchronous path:
Extraction: A cron job triggers the Python Data Extractor script. The script authenticates with ServiceNow and queries for tickets created or updated since its last run, focusing initially on the 'UNIX_SA' team.
Ingestion & Queuing: The extractor formats the raw ticket data (including ticket_number, description, work_notes, etc.) into a standardized JSON message and publishes it to a dedicated RabbitMQ queue (e.g., ticket_ingest_queue).
Task Consumption: A Celery worker, idle and listening to the queue, picks up the message. This triggers the first task in the processing pipeline.
Pre-processing & Embedding: The worker executes a task that cleans the text data and uses a Sentence-BERT model to generate a high-dimensional vector embedding representing the ticket's semantic meaning. This embedding is stored in the PostgreSQL database.
Clustering: On a scheduled basis (e.g., nightly), a separate Celery task is triggered. It gathers all new ticket embeddings from the database and runs a clustering algorithm to group semantically similar tickets, assigning a cluster_id to each.
LLM Analysis: For each identified cluster, a new Celery task is dispatched. This task performs representative sampling, constructs a series of hierarchical prompts, and makes one or more API calls to the Claude Sonnet 4 model on AWS Bedrock.
Persistence: The structured JSON responses from the LLM are parsed by the Celery task and written to the appropriate tables in the PostgreSQL database (ticket_analysis_results and pattern_insights).
Aggregation: Periodically, a final Celery task runs to pre-compute and aggregate key metrics from the analysis tables into a dedicated dashboard_metrics_precomputed table. This step is crucial for ensuring fast dashboard load times in Grafana.
Visualization: A user accesses a Grafana dashboard. Grafana issues optimized queries against the pre-computed metrics and detailed analysis tables in PostgreSQL and renders the visualizations, providing insights into automation opportunities and operational trends.

Section 4: The Asynchronous Processing Pipeline


4.1. Intelligent Batch Processing: The Cost and Context Optimization Layer

A naive approach of sending every ticket to the LLM for analysis would be prohibitively expensive and would grossly underutilize the model's large context window. The cornerstone of this architecture is an intelligent pre-processing and batching strategy designed to maximize analytical insight while minimizing API calls and associated costs. This is achieved through a two-step process of pre-clustering and representative sampling.

4.1.1. Pre-clustering with Semantic Embeddings

Rationale: The analysis of individual tickets in isolation often overlooks broader patterns. Research confirms that uncovering the relationships among tickets provides a more comprehensive overview and mitigates the risk of overlooking critical systemic issues.3 Therefore, the first step is to group tickets based on their semantic meaning before engaging the more powerful and costly LLM.
Methodology:
Text Preparation: For each incoming ticket, the description and work_notes fields are concatenated to form a single text document. Minimal pre-processing is applied, such as removing standard boilerplate text (e.g., automated email signatures), but crucial technical terms, error codes, and contextual details are preserved. Aggressive traditional NLP techniques like stop-word removal or stemming are avoided, as they can strip away context that is valuable for modern transformer-based models.16
Embedding Generation: A Sentence-BERT (S-BERT) model, such as paraphrase-distilroberta-base-v1, is used to transform each ticket's text into a dense vector embedding. S-BERT models are specifically fine-tuned for semantic similarity tasks, making them significantly more effective than older methods like TF-IDF or standard BERT for understanding the nuanced meaning of sentences and short paragraphs typical of ticket data.17 The resulting vectors are stored in the PostgreSQL database, linked to their respective tickets.
Clustering Algorithm Selection: A clustering algorithm is applied to the collection of vector embeddings to group similar tickets.
K-Means (MiniBatchKMeans): This algorithm is exceptionally fast and memory-efficient, making it the ideal choice for handling the target scale of 10,000+ tickets annually. Its use for document clustering is well-established.19 The primary consideration is determining the optimal number of clusters (
k). For the POC, an initial k value will be determined by applying analytical methods like the "elbow method" or silhouette score analysis to a sample of historical data. This k value will remain a configurable parameter for future tuning.
Alternative (Agglomerative Clustering): This hierarchical method does not require pre-specifying the number of clusters and can be useful for discovering the "natural" grouping in the data. However, its computational complexity makes it less suitable for large datasets and is therefore not the primary choice for this POC.21

4.1.2. Representative Sampling Strategies

Rationale: Once tickets are grouped into semantically coherent clusters, it is not necessary to send every single ticket from a cluster to the LLM for pattern analysis. Instead, a small, carefully selected sample can represent the central theme and variations of the entire cluster. This sampling step is the primary mechanism for managing the 30,000-token context window and controlling API costs.
Methodology:
Centroid Calculation: For each cluster generated by K-Means, the geometric centroid (the average of all vectors in the cluster) is calculated. This centroid represents the semantic "center of gravity" for that cluster's topic.
Representative Selection: The system selects the N tickets whose embeddings have the smallest cosine distance to the cluster's centroid. These are the most typical or "archetypal" examples of the issue represented by the cluster.
Outlier Inclusion: To ensure the analysis captures the full breadth of a cluster, especially for large and diverse clusters, the system will also select one or two tickets that are farthest from the centroid. These outliers can represent edge cases or variations of the main problem, providing a more robust context for the LLM's analysis. This hybrid sampling strategy ensures the selected sample is both representative and comprehensive.22
Batch Construction: The selected representative and outlier tickets from a single cluster are then combined into a single payload, formatted, and passed to the LLM in one API call, thus making optimal use of the available context window. The number of samples, N, is a dynamic parameter, calculated to maximize the number of tickets included without exceeding the 30,000-token limit.
The creation and storage of vector embeddings for every ticket yields a powerful secondary benefit. By enabling the pgvector extension in PostgreSQL, these embeddings can be indexed for efficient similarity searches.24 This capability can be exposed to support agents through a simple interface, allowing them to perform natural language searches for historically similar incidents. For example, an agent working on a new, complex issue could ask the system to "find the five most similar resolved incidents to this one." This provides immediate access to relevant knowledge and past resolution steps, transforming the system from a purely backend analytical tool for managers into a real-time, agent-assist platform that empowers frontline staff.2 This feature, a practical application of Retrieval-Augmented Generation (RAG) principles 26, can be implemented with minimal additional development effort, as the core data asset—the embeddings—is already being generated for the primary analysis pipeline.

4.2. Scalable Task Execution with Celery and RabbitMQ

Rationale: The various stages of the analysis pipeline—embedding, clustering, and LLM interaction—are computationally intensive and involve I/O latency. To handle the required scale and ensure the system remains responsive, these operations must be executed asynchronously. Celery is a mature and feature-rich distributed task queue for Python, and RabbitMQ is a highly reliable, enterprise-grade message broker that serves as an excellent transport layer for Celery tasks.12
Celery Task Design: The processing logic will be encapsulated within a series of distinct Celery tasks, promoting modularity and maintainability:
tasks.initial_ticket_processing: Triggered for each new ticket message from RabbitMQ. This task is responsible for text preparation, generating the S-BERT embedding, and saving the initial record to the database.
tasks.run_clustering: A periodic task, scheduled via Celery Beat (Celery's scheduler), that runs nightly. It collects all new embeddings and re-calculates the cluster assignments for the entire dataset.
tasks.llm_analysis_pipeline: The core multi-stage analysis worker. It is triggered for each cluster identified by tasks.run_clustering. It performs representative sampling, constructs the prompts for each analysis stage, executes the API calls to Bedrock, parses the responses, and persists the structured results to the PostgreSQL database.
tasks.update_dashboard_metrics: Another scheduled task that runs periodically (e.g., every hour). It aggregates the detailed results from the analysis tables into the dashboard_metrics_precomputed table to ensure Grafana dashboards load quickly and efficiently.
Pipeline Management and Resilience:
Error Handling and Retries: Celery has robust, built-in support for automatic task retries with exponential backoff. This will be configured to handle transient failures, such as temporary network issues or Bedrock API unavailability, making the pipeline more resilient.28
Rate Limiting: Celery's task rate-limiting features will be used to ensure that calls to the Bedrock API do not exceed the provisioned throughput, preventing API throttling errors.
Monitoring and Observability: The system will include Flower, a real-time web-based monitoring tool for Celery. Flower provides detailed visibility into worker status, task execution times, and queue lengths. This operational data is essential for debugging and performance tuning and will be the source for the "Operational Metrics" dashboard in Grafana.29

Section 5: The Hierarchical LLM Analysis Framework

Rationale: Attempting to perform a complex, multi-faceted analysis with a single, monolithic prompt is an anti-pattern that often leads to unreliable, inconsistent, and difficult-to-debug results.30 A more robust and effective approach is to decompose the problem into a series of smaller, more focused tasks. This system adopts a "prompt chaining" or multi-agent architectural pattern, where the structured output from one stage of LLM analysis becomes the precise input for the next.32 This hierarchical method improves the reliability and transparency of the model's reasoning process and yields more accurate, targeted insights at each level of abstraction.

5.1. Stage 1: Initial Categorization & Triage (Analysis of Individual Tickets)

Input: A batch of up to 20 individual tickets, respecting the API call limit. These can be new, unclustered tickets or a sample from a low-confidence cluster.
Goal: To perform a rapid, low-level assessment of each ticket to generate foundational metadata for further analysis and prioritization.
LLM Tasks:
Problem Classification: Assign a set of fine-grained, structured tags to each ticket (e.g., ['storage', 'filesystem_full', 'data_purge'], ['authentication', 'password_lockout']).
Automation Score (Initial): Provide a preliminary score on a 1-5 scale, assessing the likelihood that the described task is repetitive and scriptable.
Complexity Assessment: Rate the complexity of the issue on a 1-5 scale to help distinguish between simple, repetitive tasks and complex, multi-step incidents.
Sentiment Analysis: Analyze the language in the ticket description to gauge the user's level of frustration or the urgency of the issue. This data point is valuable for intelligent prioritization.2
Output: A structured JSON object for each ticket, which is then written to a new row in the ticket_analysis_results table in PostgreSQL.

5.2. Stage 2: Intra-Cluster Pattern Analysis (Analysis of Representative Samples)

Input: A curated collection of representative tickets (both archetypes and outliers) from a single, high-density cluster identified in the pre-clustering phase.
Goal: To synthesize the information from multiple, similar tickets to move beyond identifying what the problem is to understanding why it is happening and how it can be automated.
LLM Tasks:
Cluster Theme & Root Cause: Generate a concise, human-readable title for the cluster (e.g., "Recurring Failures of Nightly Backup Job on DB Servers") and provide a detailed analysis of the likely root cause based on the collective evidence in the work notes.
Automation Opportunity Mapping: This is the most critical task. The LLM will be instructed to identify the precise, repeatable resolution steps documented in the work_notes. It will then generate a structured recommendation, including:
Recommended Tool: Suggest a specific technology (e.g., "Ansible playbook," "Bash script," "ServiceNow Flow").
Script Logic: Provide a high-level, step-by-step pseudo-code or logical outline for the automation script.
Impacted Systems: List the servers, applications, or components involved.
Process Improvement Recommendation: Suggest non-technical changes to IT processes, documentation, or user training that could prevent this category of tickets from being created in the future.
Output: A single, detailed JSON object that summarizes the entire cluster. This output is stored in the pattern_insights table, linked to the cluster_id.

5.3. Stage 3: Cross-Cluster Insight Synthesis (Meta-Analysis)

Input: The summarized insights (themes, root causes, and automation opportunities) from multiple distinct clusters, drawn from the pattern_insights table.
Goal: To perform a meta-analysis that identifies strategic, high-level trends and systemic issues that may not be apparent when looking at individual problem clusters. This provides a "30,000-foot view" of the operational landscape.
LLM Tasks:
Systemic Trend Identification: Identify overarching themes that connect multiple, seemingly unrelated clusters. For example, the LLM might observe that a cluster of "Filesystem Full" tickets, a cluster of "Application Slowness" tickets, and a cluster of "Log Rotation Failure" tickets all point to a systemic issue with the default server build template's disk partitioning scheme.
Strategic Recommendations: Propose broad, high-impact initiatives based on these trends. Examples include: "Recommend a comprehensive review of the standard server build process," or "Propose investment in a centralized, self-service password reset portal to address multiple categories of authentication-related tickets."
Cross-Team Impact Analysis: Identify causal chains that span multiple support teams. For instance, the analysis might reveal that a pattern of network configuration changes (handled by the Network team) consistently precedes a spike in application connectivity incidents (handled by the UNIX SA team), highlighting a need for improved change management communication.
Output: High-level strategic insights, which are appended to the relevant records in the pattern_insights table and are specifically surfaced on the Executive Summary dashboard.

Part III: Implementation Details and Technical Specifications


Section 6: Advanced Prompt Engineering for Claude Sonnet 4

The quality and reliability of the system's output are directly proportional to the sophistication of the prompts provided to the LLM. The following principles and templates are designed to elicit accurate, structured, and actionable responses from the Claude Sonnet 4 model.

6.1. Core Prompting Principles

A set of best practices will be consistently applied across all prompt templates to maximize performance and reliability:
Role-Playing: Each prompt will begin by assigning a specific, expert persona to the LLM (e.g., "You are an expert IT Operations Analyst and Automation Architect specializing in identifying systemic issues from support ticket data."). This primes the model to respond from a knowledgeable and relevant context.
Structured Output: To ensure the LLM's responses can be reliably parsed and ingested by the downstream application, all prompts will explicitly instruct the model to format its output as a JSON object conforming to a predefined schema. This is a critical practice for building robust LLM-powered applications.35
Few-Shot Learning: To guide the model's behavior and improve the quality of its output, each prompt will include one or two high-quality examples (i.e., "shots") of a sample input and the corresponding desired JSON output. This in-context learning technique is highly effective for adapting LLMs to specific tasks without the need for fine-tuning.3
Chain-of-Thought (CoT) Reasoning: For tasks that require analysis and justification, such as providing a rationale for an automation score or explaining a root cause, the prompt will instruct the model to "think step-by-step" before providing the final JSON output. This encourages a more logical and transparent reasoning process, which typically results in higher-quality answers.3

6.2. Prompt Template Library

The following table outlines the core prompts that will be used in the hierarchical analysis framework. These templates will be stored as configurable files within the application, allowing for easy iteration and improvement.
Stage
Prompt Name
Objective
Key Inputs
Expected Output Schema (Key Fields)
1
TICKET_TRIAGE_V1
To perform rapid, individual analysis of a batch of tickets.
A list of up to 20 tickets, each with ticket_number, description, and work_notes.
A JSON array, with one object per ticket containing: ticket_number, automation_score, automation_rationale, complexity_score, sentiment_score, category_tags.
2
CLUSTER_PATTERN_ANALYSIS_V1
To synthesize insights from a cluster of similar tickets to identify root cause and a specific automation opportunity.
A list of representative tickets from a single cluster.
A single JSON object containing: cluster_theme, root_cause_analysis, process_improvement_suggestion, and a nested automation_opportunity object with recommended_tool, script_logic_steps, and estimated_effort.
3
STRATEGIC_INSIGHT_SYNTHESIS_V1
To perform a meta-analysis across multiple cluster summaries to find high-level, systemic trends.
A list of cluster_theme and root_cause_analysis summaries from multiple clusters.
A JSON object containing: cross_cluster_trends (an array of identified trends) and strategic_initiatives (an array of high-level recommendations).


Section 7: Data Persistence and Schema Design (PostgreSQL)


7.1. Database Design Philosophy

The PostgreSQL database schema is purpose-built for an analytical workload. The design prioritizes data integrity through normalization where appropriate (e.g., separating raw tickets from analysis results) while leveraging features suited for semi-structured data and query performance. The use of the JSONB data type is central to this design, as it provides an efficient and indexable way to store the variable and nested JSON outputs from the LLM.37 Consistent naming conventions, appropriate data type selection, and a clear indexing strategy are foundational to ensuring the database is maintainable, scalable, and performant.38

7.2. Schema Definitions (DDL)

The following SQL CREATE TABLE statements define the core schema for the POC.

SQL


-- Table to store raw ticket data fetched from ServiceNow
CREATE TABLE raw_tickets (
    id SERIAL PRIMARY KEY,
    ticket_number VARCHAR(20) UNIQUE NOT NULL,
    ticket_type VARCHAR(10) NOT NULL, -- 'ctask' or 'incident'
    description TEXT,
    work_notes TEXT,
    team_category VARCHAR(50),
    created_date TIMESTAMPTZ,
    resolved_date TIMESTAMPTZ,
    ingested_at TIMESTAMPTZ DEFAULT NOW(),
    embedding VECTOR(768) -- Assuming S-BERT model with 768 dimensions; requires pgvector extension
);

-- Table to store per-ticket analysis results from Stage 1
CREATE TABLE ticket_analysis_results (
    id SERIAL PRIMARY KEY,
    ticket_id INTEGER NOT NULL REFERENCES raw_tickets(id) ON DELETE CASCADE,
    analysis_timestamp TIMESTAMPTZ DEFAULT NOW(),
    cluster_id INTEGER,
    automation_score SMALLINT CHECK (automation_score BETWEEN 1 AND 5),
    automation_rationale TEXT,
    complexity_score SMALLINT CHECK (complexity_score BETWEEN 1 AND 5),
    sentiment_score FLOAT CHECK (sentiment_score BETWEEN -1.0 AND 1.0),
    category_tags TEXT,
    llm_output JSONB -- Store the full, raw JSON response from the LLM
);

-- Table to store synthesized insights from Stage 2 and Stage 3
CREATE TABLE pattern_insights (
    id SERIAL PRIMARY KEY,
    cluster_id INTEGER UNIQUE NOT NULL,
    insight_timestamp TIMESTAMPTZ DEFAULT NOW(),
    cluster_theme TEXT,
    root_cause_analysis TEXT,
    automation_opportunity JSONB,
    cross_cluster_trends JSONB,
    llm_output JSONB -- Store the full, raw JSON response from the LLM
);

-- Denormalized table for fast Grafana dashboard queries
CREATE TABLE dashboard_metrics_precomputed (
    id SERIAL PRIMARY KEY,
    metric_name VARCHAR(100) NOT NULL,
    metric_value FLOAT NOT NULL,
    team_category VARCHAR(50),
    metric_timestamp TIMESTAMPTZ NOT NULL,
    tags JSONB
);



7.3. Indexing Strategy

To ensure efficient data retrieval for both the processing pipeline and the Grafana dashboards, a strategic set of indexes will be created:
Primary and Foreign Keys: Indexes are automatically created on primary keys. Additional indexes will be created on all foreign key columns (e.g., ticket_analysis_results.ticket_id) to accelerate joins.
Time-Series Data: B-tree indexes will be created on all timestamp columns (created_date, analysis_timestamp, metric_timestamp) as these will be frequently used in WHERE clauses for time-based filtering in Grafana.
JSONB Data: To accelerate queries that filter based on the content of the LLM's output, GIN (Generalized Inverted Index) indexes will be created on the JSONB columns in the ticket_analysis_results and pattern_insights tables. This allows for efficient lookups of records based on specific keys or values within the JSON structure.37
Vector Embeddings: To enable the high-performance semantic search capability, a HNSW (Hierarchical Navigable Small World) index will be created on the embedding column in the raw_tickets table. This specialized index is provided by the pgvector extension and is essential for fast nearest-neighbor searches.

Section 8: Visualization and Actionable Dashboards in Grafana

The insights generated by the analysis pipeline are only valuable if they are presented in a clear, intuitive, and actionable manner. The Grafana dashboards are designed with specific user personas in mind, ensuring that each stakeholder group receives the information most relevant to their role. The design will adhere to dashboarding best practices, emphasizing clarity, logical navigation between related dashboards, and providing context through descriptions and annotations.40 While Grafana is beginning to incorporate AI for dashboard generation 41, this POC will focus on manually crafted dashboards tailored to our specific metrics.

8.1. Dashboard 1: Executive Summary

Audience: IT Leadership, CIO, Business Stakeholders.
Objective: Provide a high-level, at-a-glance overview of operational health and the impact of automation initiatives.
Key Visualizations:
Overall Automation Potential: A large gauge or stat panel displaying the percentage of all analyzed tickets that have been identified as automatable (score of 4 or 5).
Ticket Volume & Trends: A time-series graph showing ticket creation vs. resolution rates over time, with trend lines to highlight improvements.
Top 5 Recurring Problem Areas: A bar chart displaying the most frequent cluster themes, ranked by ticket volume, to focus attention on the most impactful issues.
Estimated Cost Savings from Automation: A stat panel showing a running monetary value, calculated based on the number of tickets avoided by implemented automations multiplied by the average cost per ticket.

8.2. Dashboard 2: Automation Insights & Roadmap

Audience: IT Managers, Automation Team Leads, Service Owners.
Objective: To serve as a tactical planning tool for prioritizing and tracking automation development efforts.
Key Visualizations:
High-Priority Automation Candidates: A detailed table populated from the pattern_insights table. It will be sortable by a calculated "Opportunity Score" (a function of ticket frequency, business impact, and automation feasibility score). The table will display the cluster theme, root cause, and the LLM's specific automation recommendation.
Automation ROI Projections: A bar chart or table comparing the estimated development effort (from the LLM analysis) against the potential time savings (ticket volume x avg. resolution time) for each automation candidate.
Implementation Success Tracking: A time-series graph that allows users to select a specific automation initiative. The graph will display the ticket volume for the related category, showing a clear before-and-after impact once the automation is deployed.

8.3. Dashboard 3: Pattern Analysis Deep Dive

Audience: Senior Engineers, Subject Matter Experts, Problem Managers.
Objective: To provide a rich, interactive environment for exploring identified patterns and conducting deep root cause analysis.
Key Visualizations:
Root Cause Distribution: A treemap or pie chart visualizing the prevalence of different root cause categories identified by the LLM across all clusters.
Temporal Pattern Heatmap: A calendar-style heatmap that visualizes ticket volume by day of the week and hour of the day. This can reveal critical time-based patterns, such as a spike in incidents every Monday morning or following a weekly deployment.
Cross-Team Impact Graph: A node graph visualization (using a suitable Grafana plugin) that shows the relationships between problem clusters affecting different teams. For example, a line could connect a "Network Latency" cluster to an "Application Performance" cluster, visually representing the dependency.

8.4. Dashboard 4: Operational & System Health

Audience: System Administrators, AI/ML Engineers responsible for maintaining the analysis platform.
Objective: To monitor the health, performance, and cost of the analysis pipeline itself.
Key Visualizations:
Pipeline Status: A series of stat panels and time-series graphs showing metrics from the Celery/RabbitMQ monitoring, including the number of tasks in the queue, the number of active workers, and the task failure rate.
LLM Utilization & Cost: Gauges and graphs tracking key metrics from AWS Bedrock, such as API calls per minute, average response latency, API error rate, and, most importantly, a running total of token consumption to monitor operational costs.
Database Performance: Standard database monitoring panels showing query latency, active connections, and index hit rates for the PostgreSQL instance.
Data Quality Indicators: A stat panel showing the percentage of tickets that were successfully processed end-to-end versus those that failed at some stage in the pipeline, providing a high-level view of system reliability.

Part IV: POC Roadmap and Future Considerations


Section 9: POC Implementation and Evaluation Plan

A phased approach will be employed to build, test, and validate the POC, ensuring that each component is robust before the next is built upon it. The entire process will culminate in a formal evaluation against predefined success metrics.

9.1. Phased Rollout

Phase 1 (Weeks 1-2): Infrastructure Setup & Data Pipeline Foundation
Provision the Linux VM, install and configure PostgreSQL (with pgvector), RabbitMQ, and the required Python environment.
Develop and test the ServiceNow Data Extractor script.
Establish the basic Celery application structure, defining the task queues in RabbitMQ and ensuring workers can consume messages.
Phase 2 (Weeks 3-4): Core Analysis Engine Development
Implement the pre-clustering logic, including S-BERT embedding generation and MiniBatchKMeans clustering.
Develop the representative sampling algorithm.
Craft and rigorously test the Stage 1 (Triage) and Stage 2 (Pattern Analysis) prompt templates against a sample dataset, iterating on the prompts to optimize for accuracy and structure.
Integrate the AWS Bedrock API calls into the Celery pipeline.
Phase 3 (Weeks 5-6): Visualization, Validation, and Reporting
Develop the four specified Grafana dashboards, connecting them to the PostgreSQL data sources.
Execute a full run of the end-to-end pipeline on a significant historical dataset (e.g., 3-6 months) of UNIX SA tickets.
Conduct validation sessions with UNIX SA subject matter experts to review the LLM's analysis, root cause identifications, and automation recommendations, gathering qualitative feedback and quantitative accuracy scores.
Prepare a final POC summary report detailing the findings, performance metrics, and recommendations for the next phase.

9.2. Success Metrics

The success of the POC will be measured against the following quantitative and qualitative criteria:
Automation Score Accuracy: The LLM's assigned automation score should have a greater than 85% agreement with the score assigned independently by a human expert for a randomly selected sample of 100 tickets.
Root Cause Identification Precision: For the top 10 identified clusters, more than 80% of the LLM-generated root causes must be deemed correct and relevant by the UNIX SA team.
Pipeline Throughput: The system must demonstrate the ability to process at least 1,000 historical tickets per hour in a sustained run.
Dashboard Usability: A survey of target users (managers and engineers) must yield positive feedback on the clarity, usefulness, and actionability of the Grafana dashboards.

Section 10: System Extensibility and Future Vision

This POC is designed not as a terminal solution, but as the foundational first step towards a broader, more integrated AIOps strategy. The architecture is intentionally modular to facilitate future expansion and enhancement.

10.1. Expanding to New Teams and Data Sources

The system's design makes expansion to other IT domains, such as the network team, a straightforward configuration change rather than a major development effort. The process involves:
Updating the ServiceNow Data Extractor's query to include the new team_category (e.g., 'Network').
Optionally, providing a few team-specific examples in the prompt templates (few-shot learning) to attune the LLM to the new domain's jargon and common issues.
The core pipeline—clustering, analysis stages, data storage, and visualization—is domain-agnostic and requires no modification, demonstrating the "Intelligence Factory" pattern's power.

10.2. Closing the Loop: Towards Automated Remediation

The ultimate vision is to evolve the system from an analysis and recommendation engine into a platform that can trigger automated actions. The structured automation_opportunity JSON output is designed to be machine-readable and can serve as the payload for an automation trigger. Future integrations could include:
ServiceNow Automation: Automatically creating a pre-populated Change Request or triggering a ServiceNow Flow Designer workflow to execute the remediation.
Infrastructure as Code: Triggering a job in an automation platform like Ansible Tower or a CI/CD pipeline to apply a configuration change or run a remediation script.
Agile Backlog Integration: Automatically creating a new user story or task in a developer's backlog (e.g., in Jira or GitHub Issues) with the LLM's analysis and script logic, streamlining the handoff from operations to development.42

10.3. Continuous Improvement and Model Fine-Tuning

The system is designed to learn and improve over time. A crucial future enhancement is the implementation of a feedback loop. When an engineer reviews an LLM-generated recommendation in the Grafana dashboard, they can provide a simple "accept" or "reject" rating. This feedback, captured and stored in the database, creates a valuable dataset of high-quality human-labeled judgments. Over time, this dataset can be used to perform supervised fine-tuning on the base Claude Sonnet 4 model.3 This process will continuously improve the model's accuracy and its understanding of our specific operational domain, a best practice also employed by ServiceNow's native AI platform.1

Section 11: Risk Analysis and Mitigation

A proactive assessment of potential risks is essential for the successful delivery and adoption of the POC.

11.1. LLM Hallucination and Accuracy

Risk: LLMs can occasionally generate responses that are plausible-sounding but factually incorrect or nonsensical, a phenomenon known as "hallucination." An inaccurate root cause analysis or a flawed automation script recommendation could lead to wasted effort or, in a worst-case scenario, create a new incident.30
Mitigation:
Human-in-the-Loop (HITL): The POC is designed as a decision-support tool, not an autonomous agent. All outputs, particularly automation recommendations, are subject to mandatory review and approval by qualified human experts before any action is taken.
Data Grounding: The hierarchical prompt chaining methodology ensures that the LLM's analysis is always grounded in the specific text provided from the tickets. This significantly reduces the likelihood of ungrounded or speculative responses.
Model Parameter Tuning: The temperature parameter in the Bedrock API call will be set to a low value (e.g., 0.1). This instructs the model to produce more deterministic and factual outputs, reducing its tendency for creative (and potentially inaccurate) generation.

11.2. Data Privacy and Security

Risk: ServiceNow tickets can contain sensitive data, including Personally Identifiable Information (PII), user credentials, or internal system configurations. Transmitting this data to an external service poses a potential security and compliance risk.9
Mitigation:
Secure Infrastructure: The entire processing pipeline, including the Linux VM and PostgreSQL database, will be deployed within our secure Virtual Private Cloud (VPC). Data remains within this trusted environment.
Secure API Endpoint: The connection to the AWS Bedrock endpoint is over a secure, encrypted channel within the AWS ecosystem, not over the public internet.
Data Masking (Future Enhancement): For a production system, a data masking or PII redaction pre-processing step could be added to the pipeline. This would use pattern matching or a specialized NLP model to identify and remove sensitive information before the data is sent to the LLM.

11.3. Operational Costs and Scalability

Risk: LLM API calls are metered by token usage, and uncontrolled use can lead to significant and unexpected operational costs. The system must also be able to scale to handle future increases in ticket volume without performance degradation.45
Mitigation:
Intelligent Batching Architecture: The pre-clustering and representative sampling strategy is the primary architectural control for managing costs. It ensures that the expensive LLM is used surgically on high-value, representative data, rather than wastefully on every single ticket.
Asynchronous Scalability: The use of Celery and RabbitMQ provides a clear path for horizontal scaling. If processing demand increases, more Celery worker processes or even additional VMs can be added to the pool to increase throughput.
Cost and Performance Monitoring: The "Operational & System Health" Grafana dashboard is a critical governance tool. It will provide real-time visibility into token consumption, API call volume, and pipeline performance, allowing for proactive management of both costs and system resources.

Works cited
HARNESSING MACHINE LEARNING APPROACH IN SERVICENOW PREDICTIVE INTELLIGENCE | Infosys, accessed on July 31, 2025, https://www.infosys.com/content/dam/infosys-web/en/services/experience-transformation/documents/servicenow-predictive-intelligence.pdf
GenAI for ITSM – 4 Ways LLMs Improve IT Ticket Handling and User Experience - Tiger Analytics, accessed on July 31, 2025, https://www.tigeranalytics.com/perspectives/blog/genai-for-itsm-4-ways-llms-improve-it-ticket-handling-and-user-experience/
\name: Leveraging Large Language Models for Automated Ticket Escalation - arXiv, accessed on July 31, 2025, https://arxiv.org/html/2504.08475v1
Leveraging LLMs to Analyze Engineering Escalations | by Dharmik - Medium, accessed on July 31, 2025, https://medium.com/engineering-cloudera/leveraging-llms-to-analyze-engineering-escalations-4101651dce13
Generative AI in ITSM - Enhance the Service Management Experience - Workativ, accessed on July 31, 2025, https://workativ.com/ai-agent/blog/generative-ai-itsm
LLMs: 5 Uses of Large Language Models in ITSM Tools, accessed on July 31, 2025, https://itsm.tools/llms-in-itsm/
Autonomous Incident Resolution with ServiceNow AI Agents - XenonStack, accessed on July 31, 2025, https://www.xenonstack.com/blog/autonomous-incident-resolution-with-servicenow-ai-agents
Predictive Intelligence in ServiceNow: A low/no code approach to ML, accessed on July 31, 2025, https://www.servicenow.com/community/intelligence-ml-forum/predictive-intelligence-in-servicenow-a-low-no-code-approach-to/m-p/2644073
LLM-Based Insight Extraction for Contact Center Analytics and Cost-Efficient Deployment, accessed on July 31, 2025, https://arxiv.org/html/2503.19090v1
ITSM Virtual Agent pre-built LLM topics - ServiceNow, accessed on July 31, 2025, https://www.servicenow.com/docs/bundle/xanadu-it-service-management/page/product/now-assist-itsm/concept/itsm-va-prebuilt-topics.html
Industrial IoT visualization: How Grafana powers industrial automation and IIoT, accessed on July 31, 2025, https://grafana.com/blog/2025/01/27/industrial-iot-visualization-how-grafana-powers-industrial-automation-and-iiot/
RabbitMQ and Celery: Background Task Processing - Alibaba Cloud, accessed on July 31, 2025, https://www.alibabacloud.com/tech-news/a/rabbitmq/4oc45nlvhy9-rabbitmq-and-celery-background-task-processing
Rabbitmq vs Celery | Svix Resources, accessed on July 31, 2025, https://www.svix.com/resources/faq/rabbitmq-vs-celery/
Choosing The Right Python Task Queue - Judoscale, accessed on July 31, 2025, https://judoscale.com/blog/choose-python-task-queue
Best Practices for Setting Up Celery with RabbitMQ - Reintech, accessed on July 31, 2025, https://reintech.io/blog/best-practices-celery-rabbitmq-setup
Short Text Clustering Algorithms, Application and Challenges: A Survey - MDPI, accessed on July 31, 2025, https://www.mdpi.com/2076-3417/13/1/342
Text clustering based on pre-trained models and autoencoders - Frontiers, accessed on July 31, 2025, https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2023.1334436/full
How to cluster similar sentences using BERT - Stack Overflow, accessed on July 31, 2025, https://stackoverflow.com/questions/55619176/how-to-cluster-similar-sentences-using-bert
Clustering text documents using k-means - Scikit-learn, accessed on July 31, 2025, https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html
How to cluster text documents using BERT - theaidigest.in, accessed on July 31, 2025, https://theaidigest.in/how-to-cluster-text-documents-using-bert/
Clustering — Sentence Transformers documentation, accessed on July 31, 2025, https://sbert.net/examples/sentence_transformer/applications/clustering/README.html
What is a cluster sample? - WorldSupporter, accessed on July 31, 2025, https://www.worldsupporter.org/en/tip/what-cluster-sample-66637
Selecting Representative Samples From Complex Biological Datasets Using K-Medoids Clustering - PMC, accessed on July 31, 2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC9335369/
postgresml/postgresml: Postgres with GPUs for ML/AI apps. - GitHub, accessed on July 31, 2025, https://github.com/postgresml/postgresml
Using Postgresql pg_vector for AI: Part 2, Using vectors For Natural Language Processing, accessed on July 31, 2025, https://dev.to/jjn1056/using-postgresql-pgvector-for-ai-part-2-using-vectors-for-natural-language-processing-b40
Streamline Your Support Tickets with Snowflake's AI-Powered Ticket Automation Agent, accessed on July 31, 2025, https://medium.com/snowflake/streamline-your-support-tickets-with-snowflakes-ai-powered-ticket-automation-agent-d148527ecd84
Diagnosing and Resolving Cloud Platform Instability with Multi-modal RAG LLMs - arXiv, accessed on July 31, 2025, https://arxiv.org/html/2505.21419v2
First Steps with Celery — Celery 5.5.3 documentation, accessed on July 31, 2025, https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html
Why use Celery instead of RabbitMQ? - Stack Overflow, accessed on July 31, 2025, https://stackoverflow.com/questions/9077687/why-use-celery-instead-of-rabbitmq
LLM-Based Open-Domain Integrated Task and Knowledge Assistants with Programmable Policies - arXiv, accessed on July 31, 2025, https://arxiv.org/html/2407.05674v1
The Ultimate Guide to Prompt Engineering in 2025 | Lakera – Protecting AI teams that disrupt the world., accessed on July 31, 2025, https://www.lakera.ai/blog/prompt-engineering-guide
From Unstructured Communication to Intelligent RAG: Multi-Agent Automation for Supply Chain Knowledge Bases - arXiv, accessed on July 31, 2025, https://arxiv.org/html/2506.17484v1
Prompt Chaining | Prompt Engineering Guide, accessed on July 31, 2025, https://www.promptingguide.ai/techniques/prompt_chaining
Customer Support Efficiency through Automated Ticket Triage, accessed on July 31, 2025, https://www.analyticsvidhya.com/blog/2023/11/enhancing-customer-support-efficiency-through-automated-ticket-triage/
Prompt Engineering Showcase: Your Best Practical LLM Prompting Hacks, accessed on July 31, 2025, https://community.openai.com/t/prompt-engineering-showcase-your-best-practical-llm-prompting-hacks/1267113
How to Categorize Support Tickets Using LLMs - GetCensus, accessed on July 31, 2025, https://www.getcensus.com/blog/how-to-categorize-support-tickets-using-llms
When designing databases, what's a piece of hard-earned advice you'd share? : r/PostgreSQL - Reddit, accessed on July 31, 2025, https://www.reddit.com/r/PostgreSQL/comments/1jeaqaa/when_designing_databases_whats_a_piece_of/
Top 10 Database Schema Design Best Practices - Bytebase, accessed on July 31, 2025, https://www.bytebase.com/blog/top-database-schema-design-best-practices/
Complete Guide to Database Schema Design - Integrate.io, accessed on July 31, 2025, https://www.integrate.io/blog/complete-guide-to-database-schema-design-guide/
Grafana dashboard best practices, accessed on July 31, 2025, https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/best-practices/
Building AI Into Observability Workflows: Automating Dashboards, Alerts with MCP & Agents | Grafana - YouTube, accessed on July 31, 2025, https://www.youtube.com/watch?v=qipWEGaTWsg
PR-Agent (Qodo Merge open-source): An AI-Powered Tool for Automated Pull Request Analysis, Feedback, Suggestions and More! - GitHub, accessed on July 31, 2025, https://github.com/qodo-ai/pr-agent
Github Issues vs ServiceNow: Which Ticketing Tool is Best for You? | Guru, accessed on July 31, 2025, https://www.getguru.com/reference/github-issues-vs-servicenow
With RAG+LLM, are most of the issues in domain-specific intelligent customer service essentially resolved? | ResearchGate, accessed on July 31, 2025, https://www.researchgate.net/post/With_RAG_LLM_are_most_of_the_issues_in_domain-specific_intelligent_customer_service_essentially_resolved
What Are the Common Challenges Businesses Face in LLM Training and Inference? : r/devops - Reddit, accessed on July 31, 2025, https://www.reddit.com/r/devops/comments/1iobdm4/what_are_the_common_challenges_businesses_face_in/
