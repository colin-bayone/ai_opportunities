# Meeting 4 - Verbatim Key Quotes

## Overview

Exact quotes from the meeting transcript, organized by theme. All transcription corrections have been applied.

---

## Expectation Mismatch & Recovery

**Gariashi (surfacing the disconnect):**
> "I think we were excited to see the demo today. The struggles of the team is... we want to automate and make things easier using AI agent in this whole journey of data ingestion, aggregation, and reports built."

**Colin (acknowledging the gap):**
> "So I think that's probably where our disconnect is today. I think for the demo perspective, we won't be able to do that until we get some more information. Because for us, everyone's environment's different."

**Neha (diplomatic recovery):**
> "I apologize if there was a little... I thought we left off that discussion intending to have a technical discussion with your architect so that when we do the demo, whatever information we need to make sure that the demo is going to be relevant to you."

**Andrew (rescuing the meeting):**
> "Again, you know, I don't think we necessarily need to have support data to actually demo, but it's really about demoing the capability, right? Whether you guys can or whether it's even possible to create all those different smaller agents and have a kind of an orchestrator agent to orchestrate all the smaller agents."

**Colin (relief):**
> "Thank you for that because I was like, oh no, I messed up today."

---

## Cognos/DataStage Integration Research

**Colin (announcing good news):**
> "So the first thing is I did some homework on this. On Cognos and on DataStage both - very good news for you. Beautiful, perfect, all-inclusive APIs or SDKs for both of them. These are old enough that they weren't APIs yet. They were just pure SDKs. They're available in both Java and .NET."

**Colin (on version compatibility):**
> "That goes all the way back to even the earliest versions of Cognos. So as long as you're using a version that's after 2003, we're in good shape."

**Colin (on MCP servers):**
> "The way that we do this, we build what's called an MCP server. These don't typically already exist. So these are things that we build from scratch as part of what we do. This is not uncommon for us at all. We have to do this very often when it comes to legacy platforms."

---

## Current Manual Workflow

**Gariashi (on current AI usage):**
> "Right now we're doing all of this manually, like exporting the XML from the Cognos and then extracting all the joints, the source tables, everything. We are using Claude right now to help us do all of that extraction. But getting that XML, that is still manual effort, we have to log into Cognos, go to report studio, download the XML."

**Gariashi (on the gap):**
> "We haven't really come up with any agent yet that can do this process end to end. Because this is pretty standard that we have to do for all the Cognos reports."

---

## Andrew's Workflow Explanation

**Andrew (on Framework Model reports):**
> "In the Cognos report today, we have two options. Either you have the report point to the IBM Framework Manager Model, which is really the kind of the quote unquote metadata, right? That actually behind the scenes, that whole model is pointing to all those different tables with all the different joins in the SQL server."

**Andrew (on Freehand SQL reports):**
> "We also have another second half set of the report that actually doesn't just point to the Framework Manager Model. By default, when you create a report, you have to point to your Framework Manager Model. Fine, we point it. But we actually don't leverage the Framework Manager Model to generate the SQL. In reality, in every query within the report, we actually write a free-hand SQL."

**Andrew (on agent vision):**
> "Is there any way throughout this step that we can create agents? Again the agent doesn't... I'm not expecting one agent do it and I think I actually wanted an agent just every... it's like a lot of smaller agents, agents do a small little thing, you have a lot of this small little agent, and then they just do their own responsibility, do the whole thing, and then you have that one orchestrator to just orchestrating this whole entire all the smaller agents."

---

## Schema Mapping & Confidence

**Colin (on why deterministic first):**
> "If a table doesn't exist in Databricks, I don't need to go try to find it. I can say deterministically, no, it doesn't exist before I ever get AI involved. So that way we don't end up kind of... I call it a telephone game here."

**Colin (on confidence-based routing):**
> "How do you know that confidence is high? What does that really mean? That's where AI... I think especially with language models suffers quite a bit because it can say I'm 100% confident in something. A lot of the times we call that a hallucination."

**Colin (defining real confidence):**
> "Whenever a human goes and reinforces a decision made by AI, that is confidence. So if you say yes, you are correct or no, you are wrong, that is what determines confidence. And even when it's wrong, now it knows what's wrong about it, so confidence still increases."

**Colin (on the flywheel):**
> "If I've said, yes, you can do this five times in a row, and time number six, you don't need to ask me to do it. You can just go and do it as long as you're tracking and remaining traceable with the actions taken."

---

## MCP and Tool Integration

**Colin (MCP indicator):**
> "A very good indication that you need MCP in the mix is if you find a human being copying and pasting or taking screenshots of something and passing it out to a language model. It's a very good indication that there's something that should be there with MCP that might not be there yet."

**Maher (clarifying question):**
> "So you're building a custom MCP server to talk to Cognos SDK. And what does that, in this scenario, what's the outcome of this activity?"

---

## Databricks Environment Status

**Gariashi (on migration progress):**
> "It's very less, Colin. Probably a few tables I would say. Out of, we have around 1,000 tables sitting on EDW. So we have tackled very less percentage-wise."

**Andrew (clarifying Databricks maturity):**
> "If your question is if the Databricks environment is up and running, it's very mature. We have a lot of other tables on it, we have catalogs and it is very mature. We have critical reports, P1 applications running on it. So it is a very developed environment."

**Andrew (on timeline):**
> "We just started the project this January."

---

## DataStage Framework Requirements

**Sergei (on existing framework):**
> "On Databricks, we developed frameworks, color-based, where you don't need to do, let's say, Python development or something. So you just need to do configuration. And we have, let's say, thousands of jobs running in production today."

**Sergei (on ideal agent output):**
> "Main question right now, how to teach these agents to understand that, okay, we need to create three YAML files with some configuration inside. Let's say 20, 50 different parameters like source table name, connection details and so on. So you don't need to write code itself, just to create config file."

**Sergei (on Lakehouse problems):**
> "This is also a problem with Lakehouse. So we're just converting some, be honest, spaghetti code. When you have Databricks notebook with hundreds of notebooks inside this notebook and how to maintain it, I don't know, it will be nightmare to debug."

**Sergei (ideal world):**
> "If we can ask him in the brackets. Ask him, hey man, we have 10 jobs, please convert them, generate YAML files, commit them to repo. After that, some developer can quickly review that it's good and that's it. So this is like ideal world."

---

## Security Constraints

**Maher (on security blocks):**
> "We will probably have to go through the whole security thing at Sephora if we want an external agent to run on our environment."

**Maher (on previous attempts):**
> "We tried to run our own agent on the independent record, we get blocked by security."

**Colin (offering help):**
> "We do this all the time, so we're used to talking to IT and security teams to kind of tell them, no, we're not crazy. No, we're not going to hurt anything."

---

## Demo Scoping Agreement

**Maher (practical proposal):**
> "The agent can do the work, the migration work, without having access, without validating whether it's working or not."

**Maher (simplifying scope):**
> "Pick a Cognos report that doesn't need any kind of query restructuring. Just lift and shift, point to Databricks."

**Colin (accepting the scope):**
> "So it sounds like if we can get one of the Cognos reports, what we will be able to do is we can take that, build the MCP for it, make sure that we can A, connect to it, B, dissect it, and be able to get into it."

---

## Healthy Skepticism

**Sergei (grounded reality check):**
> "It's easy said than done. I worked with Collins, I wrote code for the BI server, and that's a complicated word."

**Maher (on needing proof):**
> "We need to see a demo, really. To see if this will work or not. Because we didn't have success."

---

## Playbook Creation Approach

**Colin (on documentation options):**
> "If there's a well-defined task that humans already have known and documented, that is a good set of instructions for the agent."

**Colin (alternative approach):**
> "We get on a call, we hit the record button on the call to enable the transcript, and essentially someone walked through the exact process calling out those details. That's it. And then I have one of our team on just asking some questions along the way. It's usually something that's like 30 minutes to 45 minutes."

---

## Closing

**Neha (summarizing next steps):**
> "Just waiting on those reports from you, and then we set up a time for that first level demo to showcase capabilities."

**Gariashi (agreement):**
> "Yeah, that sounds good."

**Colin (off-call reaction):**
> "Whoo!"
