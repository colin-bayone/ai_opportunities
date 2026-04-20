# 03 - Team Sync: WebEx Scraping Progress

**Source:** /claude/2026-04-15_cisco_cicd_scoping_brainstorm/source/cisco-team-sync_4-16-2026.txt.txt
**Source Date:** 2026-04-16 (Wednesday team sync)
**Document Set:** 03 (Third team sub-singularity set)
**Pass:** Focused deep dive on WebEx chat scraping workstream

---

## 1. Background and Assignment

Colin established the scraping task as a deliverable needed for Friday's meeting with Srinivas. He stated that Srinivas "asked us to catalog and categorize everything in there" (referring to the NxOS CI Workflow WebEx space where Cisco engineers surface pipeline issues). Colin explicitly said: "I don't think we've done that yet."

Colin framed the task: "What we need to figure out is how to download essentially that whole chat as best we can. It might be a matter of scrolling up to the very top, pressing Control A, Control C, but I don't have a way of knowing that. If there's a better way to do it, we're going to need to figure it out. But that's something that we do need to have for this week."

He positioned the output as feeding directly into the Friday Srinivas deliverable: "that's going to guide how we talk about triage. For instance, like if Justin's system or Rui's system don't really cover things properly, or if there's like 1 consistent issue, we can focus our canons there first."

Colin then left for a meeting with Yogesh and Rahul and instructed the team to continue discussing and come to a plan for the scraping and categorization effort.

## 2. Srikar's Scraping Results

After Colin departed and the team discussed architecture, Srikar reported progress on the scraping. He stated: "I was like extracting the WebEx space chat room, so I was able to like fetch like around like for each page there are 50 messages."

Saurav confirmed the API behavior: "It fetches 50 at a time. It is like paginated API."

Srikar then reported the volume and the failure point: "I was able to go till like 130 pages, like 6,500 messages. And then the connection aborts after that."

### Connection Abort

Srikar described the error as a timeout: "I'm getting an error of timeout, so I'll see if I can do like incrementally, like pull the details."

Saurav's initial advice was: "Ask Claude to try after 6,500 pages or just ask it to check if there are if there is a way to check like the total count of messages saved or something like that."

Saurav also noted that 6,500 might be sufficient for a first pass: "Still like 6,500 should be enough for like an initial exploration. But still it depends on what is like the exact, what do you call chat size. If it's like 100,000 or million and we only got 650, that's bad sample size."

Srikar agreed: "I think for the initial sample size, I think it should be good."

## 3. CSV Structure

Saurav asked about the structure of the scraped data: "Do we have any structure to the, what do you call it, scraped image, like just the structure in a sense that for the message, if there was a reply, it is linked to that message, that we can trace that?"

Srikar described the CSV columns in order:

1. **Created time** - timestamp of the message
2. **Message ID** - unique identifier for the message
3. **Parent ID** - links replies back to their parent message ("So if you see like any parent ID, so you can link back to... the parent ID will be the unique one")
4. **Sender** - who sent the message
5. **Body text** - "just the text part"

Srikar stated he had shared the CSV file on the team WebEx chat: "I just shared the Messages CSV file on the chat."

## 4. Data Quality Issues Colin Identified

Colin returned from his meeting and immediately opened the file. He found several problems:

### Date Range Compression

Colin noted: "It looks like everything is saying that it's in April of this year. So we'll want to double check on that one. Because that's one thing, I'm not sure if the date and times are correct for the messages."

Saurav offered a possible explanation: "It might be possible there are like 6,500 messages in a month and a half because they do are they are like doing whole project tracking on the group. So it might also be possible that yeah those dates are correct."

### Duplication

Colin identified clear duplication in the data: "If you look at these, the times are all the same." He continued: "And the body messages are all the same." And: "The sender's the same."

Colin diagnosed the root cause: "I'm thinking it's probably duplicating things whenever it runs the 50, it's duplicating things it already has."

Saurav confirmed: "OK, yeah, OK, this is duplication, yeah."

## 5. Colin's Plan for Processing

### Deduplication by Message ID

Colin's first recommendation was deduplication: "You might first of all want to deduplicate by message ID, number one, because that should always be unique."

### Time-Based Incremental Fetching

Colin suggested an alternative scraping approach: "It might be better to go in time increments. So to say like process, if there's some flags in the API to scrape based upon like here's a week's worth."

Saurav confirmed the API supports this: "There is like, from what I remember, there was one like for a week and there is also like if you want to get suppose all chats after 20th or before 20th. So we also have those kind of APIs as well."

### Conversion to Parquet with Parent-Child Hierarchy

Colin described his post-processing plan: "What I would say is after this working, I'm going to convert this into a parquet file. And I'll put it into kind of a pandas data frame format first, so that we'll have that parent-child hierarchy laid out. It's already easy to do to tie them back, but I'll restructure it so that it goes and is almost jagged in that way."

Colin stated he would handle this step himself: "This is easy for me. I'm going to take the file."

### Downstream Analytics

Colin described what the clean data would enable: "We can even do like, you can do so much with that, like even like, let's say, mean time for resolution within the chat. And that can even help to really drive home, Namita, what you were bringing up. If people are dropping messages into the chat, there's a delay between whenever that issue occurs, plus whenever someone reports it, plus whenever someone actually resolves it."

## 6. Assignment Split

### Srikar's Role

Srikar was responsible for the initial scraping and had already produced the 6,500-message CSV. He committed to fixing the data quality issues: "I will cross-check that once, Colin, and then, yeah, I will confirm that."

He also committed to incremental fetching: "I'll see if I can do like incrementally, like pull the details."

### Saurav's Role

Saurav volunteered to take a portion of the data for categorization: "I will take last 1,500 OK in the CSV file."

He also noted that if the data was too large for one person: "If there is like too much data to like categorize, you can also share it on group like in separate file. So each of us can pick up one and do some part of it."

### Colin's Role

Colin took responsibility for the data transformation step (CSV to Parquet with parent-child hierarchy restructuring) and stated he would handle the processing himself.

## 7. Saurav's Volley Bot as Alternative

Saurav raised the existence of a previously built scraper: "So the bot I previously built, correct, which is currently on my like dead laptop on local. So that was able to scrape everything."

He asked for clarification on approach: "By scraping and categorizing, did he mean the, what do you call the pulse, use the pulse project to scrape it? Or in bot with, he wants us to scrape it. Because if you go ahead and scrape it with Claude or any other things, so he might come back and ask, like, how exactly did you do this?"

Saurav specifically raised the compliance concern: "Because we did not deploy any bot or we did not connect, add any connector or any other thing. So how did you guys were able to like scrape it? Tell me. So that might come as like compliance or something."

Colin addressed this directly: "Let me be the shield for all of you with that, because I'm quite good at this... I'm going to tell him we did it with Copilot."

Colin also suggested: "Even Saurav, if you're able to run that, even on your BayOne laptop and you're able to scrape everything, or if you're able to, you know, I know it's painful to recreate it, but recreate it with, you know, Srikar and Namita and have them run it."

The Volley bot was referenced but was on a dead laptop and would need recreation. Saurav noted: "I think it should be easy, just like Srikar or..."

## 8. Open Questions About Non-Text Content

Saurav raised the issue of attachments and non-text content in the WebEx chat: "People are sending in files, photos, images, Excel sheets, everything else. So what are they doing with this currently and what are their plans for this? They just do, they just want to like kind of index it and keep the name or do they also want the text to be extracted and summarized? Because that is like a whole level of... a single orchestrator or a single tool we should build which should do all of these for like everything. So the conversion task and pre-processing and all of those things."

Colin confirmed the problem is real: "Even if you look at that in NxOS CI workflow chat, you can see that people are attaching screenshots. And they are attaching files and they are linking to things too. So sometimes it's not even attachment but a link."

Colin's direction for now was to defer this: "Don't worry too much about attachments yet." He wanted step one to be text-only scraping with thread structure, with attachment handling to be addressed later.

Colin also flagged the token cost concern: "Files are where you're really going to start chewing tokens."

## 9. Chat Liveness vs. Meeting Transcript Staticness

Colin drew a critical distinction between chats and meeting transcripts that affects how the scraping pipeline must work: "There's a little bit of a liveness to chats. You know, meetings are kind of static because once a meeting happens, it's not like the meeting changes. But, you know, for instance, for a chat, you can't say that the chat I retrieved at one point in time and it's going to be the same tomorrow because anyone can respond on any comment thread at any time."

Colin concluded: "This should be stateful, but it should be able to refresh on some loop. That's perfect territory for Airflow, for instance, to point it at a message, scrape the text, stored in a database, link to the attachments or process the attachments through some pipeline, whatever that pipeline is, or however many tools we need beyond the point."

He also pointed out the security implications of chat mutability: "What if I was a bad guy and I said, delete everything in NxOS? And then I delete my comment or I change it to a smiley face. But the language model pipeline that they built already processes that and goes in... And then there's no possible trace back to me to say that I was what caused it, because I've changed it out and edited my comment."

## 10. Categorization Requirements

Colin described the expected output from the categorization work: "The categorization and breakdown, you'll want to figure out how to do that, how many categories, because we'll be able to put something really nice together with it at the end."

He specified that it must include thread structure, not just top-level messages: "Make sure that it also has the comments, not just the first level messages, but also like the full, you know, kind of jagged view of the thread."

The categorized output would serve multiple purposes for the Friday Srinivas meeting:
- Identifying patterns in the types of issues being raised
- Evaluating whether Justin's or Rui Guo's existing systems address the issues properly
- Finding consistent/recurring issues where the team could "focus our canons there first"
- Demonstrating the limitations of managing pipeline issues via WebEx chat (arguing for GitHub Issues instead)

## 11. WebEx Chat as Source of Truth Problem

Colin used the scraping discussion to build a broader argument about the inadequacy of WebEx for issue tracking. He cited a specific message from the chat: "For instance, this one from Sitaria. She said, hi, the ULS sanity from my PR fails even before running. We run outside the same issue. This should 100% be a GitHub issue as a bug report."

He argued: "There's no traceability to this. This is not the way efficient teams run with GitHub." Colin proposed that part of the pipeline should include creating GitHub issues from chat messages: "We could certainly have a part of the pipeline, not to just diagnose and triage, but also to get this properly tracked in GitHub. So that whenever you do have a PR, you can have some traceability to it."

## 12. How This Feeds the Friday Srinivas Deliverable

The scraping work connects to the Friday meeting in multiple ways:

1. **Issue catalog for Srinivas** - Direct deliverable: a categorized inventory of all issues raised in the NxOS CI Workflow chat, showing what types of problems occur and how they are currently handled
2. **Triage gap analysis** - Comparing the catalog against what Justin's system and Rui Guo's Nexus T agent actually cover, identifying gaps
3. **Process improvement argument** - Using the data (mean time to resolution, duplicate reporting, lack of traceability) to argue for moving issue tracking to GitHub
4. **Architecture input** - Understanding the volume and nature of chat messages informs the ingestion and processing architecture the team is proposing

## 13. Summary of Open Action Items

| Item | Owner | Status |
|------|-------|--------|
| Fix duplication in scraper (deduplicate by message ID) | Srikar | To do |
| Try time-based incremental fetching to get past 130-page limit | Srikar | To do |
| Verify date/time accuracy of created field | Srikar | To do |
| Convert CSV to Parquet with parent-child hierarchy | Colin | Waiting on clean CSV |
| Categorize last 1,500 messages | Saurav | To do |
| Determine total chat size (is 6,500 the full corpus or a subset?) | Srikar | Open question |
| Decide handling of files, images, hyperlinks | Team | Deferred |
| Recreate Volley bot on BayOne laptop (fallback option) | Saurav | Not started |
