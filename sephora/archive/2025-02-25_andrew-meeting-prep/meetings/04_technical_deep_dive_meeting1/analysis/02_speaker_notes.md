# Speaker Notes: Meeting 4 (Sephora Technical Deep Dive)

Quick reference for who said what and their areas of ownership.

---

## Colin Moore (Director of AI, BayOne)

**Present:** Full meeting, primary presenter

### On Cognos/DataStage Integration

> "On Cognos and on DataStage both - very good news for you. Beautiful, perfect, all-inclusive APIs or SDKs for both of them. These are old enough that they weren't APIs yet. They were just pure SDKs. They're available in both Java and .NET."

> "That goes all the way back to even the earliest versions of Cognos. So as long as you're using a version that's after 2003, we're in good shape."

### On MCP Servers

> "The way that we do this, we build what's called an MCP server. These don't typically already exist. So these are things that we build from scratch as part of what we do. This is not uncommon for us at all."

> "A very good indication that you need MCP in the mix is if you find a human being copying and pasting or taking screenshots of something and passing it out to a language model."

### On Schema Mapping

> "If a table doesn't exist in Databricks, I don't need to go try to find it. I can say deterministically, no, it doesn't exist before I ever get AI involved."

> "Whenever a human goes and reinforces a decision made by AI, that is confidence. So if you say yes, you are correct or no, you are wrong, that is what determines confidence."

> "If I've said, yes, you can do this five times in a row, and time number six, you don't need to ask me to do it."

### On Expectation Mismatch

> "So I think that's probably where our disconnect is today. I think for the demo perspective, we won't be able to do that until we get some more information."

> "Thank you for that because I was like, oh no, I messed up today."

### Key Commitments

- Build demo using provided Cognos report XML and Databricks schema
- Build MCP server for Cognos integration
- Help with IT/security conversations if needed

---

## Andrew Ho (Sr. Director, Sephora)

**Present:** Full meeting, key contributor

### On Meeting Recovery

> "Again, you know, I don't think we necessarily need to have support data to actually demo, but it's really about demoing the capability, right?"

> "Today is really an opportunity for you to come back and ask our expertise here questions. We have an enterprise architect. We have Sergey Shtypuliak, who actually really is our SME on all our IBM tools."

### On Framework Model vs Freehand SQL

> "In the Cognos report today, we have two options. Either you have the report point to the IBM Framework Manager Model, which is really the kind of the quote unquote metadata, right?"

> "We also have another second half set of the report that actually doesn't just point to the Framework Manager Model... In reality, in every query within the report, we actually write a free-hand SQL."

### On Agent Vision

> "Is there any way throughout this step that we can create agents? I'm not expecting one agent do it... it's like a lot of smaller agents, agents do a small little thing, you have a lot of this small little agent, and then they just do their own responsibility, do the whole thing, and then you have that one orchestrator to just orchestrating this whole entire all the smaller agents."

### On Project Scope

> "This agent that we are looking to create, my assumption is not only handling the Cognos migration track, we're also looking for agents to help even the table data migration from SQL Server to Databricks. Are you aligned with that?"

### Key Commitments

- Confirmed agents should cover both Cognos and data migration tracks
- Will regroup internally on additional demo needs

---

## Gariashi Chakrabarty (Director, Data Engineering, Sephora)

**Present:** Full meeting

### On Expectations

> "I think we were excited to see the demo today. The struggles of the team is... we want to automate and make things easier using AI agent in this whole journey."

### On Current AI Usage

> "Right now we're doing all of this manually, like exporting the XML from the Cognos and then extracting all the joints, the source tables, everything. We are using Claude right now to help us do all of that extraction."

> "But getting that XML, that is still manual effort, we have to log into Cognos, go to report studio, download the XML."

> "We haven't really come up with any agent yet that can do this process end to end."

### On Migration Progress

> "It's very less, Colin. Probably a few tables I would say. Out of, we have around 1,000 tables sitting on EDW."

### Key Commitments

- Provide Cognos report XML from Finance folder (coordinating with Vlad)
- Agreed to demo scope ("Yeah, that sounds good")

---

## Maher Burhan (Enterprise Architect - Consultant, Sephora)

**Present:** Full meeting, first time in engagement

### On MCP Server Clarification

> "So you're building a custom MCP server to talk to Cognos SDK. And what does that, in this scenario, what's the outcome of this activity?"

### On Security Constraints

> "We will probably have to go through the whole security thing at Sephora if we want an external agent to run on our environment."

> "We tried to run our own agent on the independent record, we get blocked by security."

### On Practical Workaround

> "The agent can do the work, the migration work, without having access, without validating whether it's working or not."

> "Pick a Cognos report that doesn't need any kind of query restructuring. Just lift and shift, point to Databricks."

### On Demo Scope

> "One of the DataStage... we probably can have a simple DataStage job that we can share."

### Key Commitments

- Provide Databricks schema/catalog information
- Consider providing simple DataStage job sample

---

## Sergey Shtypuliak (SME - IBM Tools - Consultant, Sephora)

**Present:** Full meeting, first time in engagement

### On DataStage Framework

> "On Databricks, we developed frameworks, color-based, where you don't need to do, let's say, Python development or something. So you just need to do configuration. And we have, let's say, thousands of jobs running in production today."

> "Main question right now, how to teach these agents to understand that, okay, we need to create three YAML files with some configuration inside. Let's say 20, 50 different parameters like source table name, connection details and so on."

> "So you don't need to write code itself, just to create config file. It's even simpler than write code."

### On Lakehouse Problems

> "This is also a problem with Lakehouse. So we're just converting some, be honest, spaghetti code. When you have Databricks notebook with hundreds of notebooks inside this notebook and how to maintain it, I don't know, it will be nightmare to debug."

### On Healthy Skepticism

> "It's easy said than done. I worked with Collins, I wrote code for the BI server, and that's a complicated word."

### On Ideal Outcome

> "If we can ask him in the brackets. Ask him, hey man, we have 10 jobs, please convert them, generate YAML files, commit them to repo. After that, some developer can quickly review that it's good and that's it. So this is like ideal world."

### Key Commitments

- Defined success criteria: YAML config output, not code

---

## Neha Malhotra (VP Growth & Customer Success, BayOne)

**Present:** Full meeting, facilitator role

### On Expectation Mismatch

> "I apologize if there was a little... I thought we left off that discussion intending to have a technical discussion with your architect so that when we do the demo, whatever information we need to make sure that the demo is going to be relevant to you."

### On Next Steps

> "Just waiting on those reports from you, and then we set up a time for that first level demo to showcase capabilities."

### Key Commitments

- Schedule demo session after materials received

---

## Zahra Syed (Sales, BayOne)

**Present:** Full meeting, minimal speaking role

No significant quotes captured.

---

## Transcription Corrections

| Transcript Shows | Actually Means |
|------------------|----------------|
| "Shaka" | Zahra Syed |
| "my hair", "Mahir", "Malika" | Maher Burhan |
| "Sir" | Sergey Shtypuliak |
| "Gaurishi", "Garishia", "Karish" | Gariashi Chakrabarty |
| "Cardinals", "Card notes", "coughing" | Cognos |
| "Lake bridge" | Lakehouse |

---

## Quick Reference

| Speaker | Main Topics | Key Takeaway |
|---------|-------------|--------------|
| Colin | MCP, schema mapping, confidence routing | Technical approach validated, research completed |
| Andrew | Workflow walkthrough, agent vision | Internal champion, rescued meeting |
| Gariashi | Current state, expectations | Demo needed to gain confidence |
| Maher | Security, practical workarounds | Pragmatic problem-solver |
| Sergey | DataStage framework, YAML requirements | Defined success criteria for agent output |
| Neha | Meeting facilitation | Will coordinate demo scheduling |
