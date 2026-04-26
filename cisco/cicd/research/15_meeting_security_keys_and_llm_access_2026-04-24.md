# 15 - Meeting: Security Keys and LLM Access

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/source/week_2026-04-20/day_2026-04-24/srinivas_4-24-2026_formatted.txt
**Source Date:** 2026-04-24 (Friday afternoon Srinivas sync)
**Document Set:** 15 (Sixth Srinivas team meeting)
**Pass:** Focused deep dive on LLM credentialing, static key concerns, key rotation patterns, and the aerospace anecdote

---

## Overview

The Friday afternoon Srinivas sync produced the first substantive security-architecture conversation of the engagement. After the team walked through the deployment form decision, the Active Directory Service escalation path, and the incident posture, Srinivas pivoted to a question prompted by the BayOne demonstration. BayOne had shown a working WebEx bot calling a large language model to summarize content, and Srinivas wanted to understand exactly which credential was carrying the call.

That question surfaced an internal Cisco pain point Srinivas had not previously raised with BayOne: the absence of a key rotation mechanism for LLM secrets. Srinivas keeps a small number of static keys, shared with a tiny number of people, with no expiration, no automated rotation, and no audit trail. The conversation confirms that the bot keeps using a temporary circuit API token in the near term, that DeepSight credentials will follow once BayOne shows a working product, and that key rotation sits on Srinivas's list as a deferred workstream where BayOne is the named resource.

## LLM credentials question from Srinivas

Srinivas opened with a careful question framed around the planning board. He said, "one question on the board, right, of the LLM requirement, I was thinking we'll have some LLM department, right?" Colin confirmed, "That's right." Srinivas narrowed with a statement he already knew the answer to. "And I know you don't have access to the user brokers." Colin again confirmed, "Right."

The phrase "user brokers" is a dictation artifact for user accounts or user permissions. The point was that BayOne does not have direct access to the Cisco identity system and cannot, in the normal course, call Cisco's LLM endpoints with a properly provisioned account. So how was the demonstration working?

Srinivas asked plainly. "How did you just put your credential and test it right now?" Colin answered with equal plainness. "So I got like a circuit API token and I used that. That is just temporary." Srinivas closed the loop. "That's why I'm asking." Srinivas was not auditing BayOne. He was confirming that BayOne had bridged a gap to make the demonstration possible, and the two sides now needed to agree on how to provision a real credential going forward.

## DeepSight credential integration commitment

Srinivas committed Cisco to bringing BayOne onto the DeepSight credential plan. "So we need to bring you guys on the deep side plans. We'll get you guys that piece." The phrase "deep side" is a phonetic rendering of DeepSight, the Cisco internal LLM platform from earlier transcripts. The commitment was conditional. Srinivas added, "First I want to see what you have, then we'll see how we bring it on board. In this piece on the side." Colin replied, "Sounds good."

The sequence is straightforward. BayOne demonstrates the working product using the temporary circuit API token, and after the demonstration lands Srinivas issues DeepSight credentials so the bot can call the proper Cisco LLM endpoint with a properly provisioned identity. This is consistent with how Srinivas has managed risk throughout the engagement: he prefers to see something working before committing the next layer of access. The practical implication is that the temporary circuit API token must remain stable through the next-Friday demonstration.

## Srinivas raises the static key concern

After agreeing on the DeepSight path, Srinivas opened the underlying problem. "There is a model dependence. So we have some problem is we have a secret key. The secret key does not have a... key rotation build. And it's a static key and if I give it, that's the one." The disclosure is direct. Cisco's current LLM credentials are static keys with no rotation mechanism, no time limit, and no automated revocation.

Srinivas then asked the question that defined the rest of the conversation. "I don't know. Do you guys have experience on any of the security mods? Any chance?" The phrasing is informal but the request is genuine. He had not previously framed key rotation as a problem during BayOne meetings; raising it now, after watching BayOne run a successful demonstration, suggests he sees BayOne as someone who might be able to help.

## Colin offers two patterns

Colin answered immediately. "Yes, yes. And two ways to do it. One probably is the best fit for you if I had to guess. One really the easiest possible way to do this. It doesn't have rotation without something else attached to it, or just to do it in GitHub, so that you can provide one place for people to access."

Srinivas pushed back before Colin could finish describing the GitHub pattern. "No, not really. I don't know anyone to see the key, except for only the super user's app, which will have the right key." The "super user's app" is Srinivas's own term for the application or process that holds the master key.

Srinivas then explained the gap in his own words. "the idea is that the deep side, because time to market, right? But now more apps makes like this. You need to create an auth, meaning you temporarily release a key and you get something and you use that to do the current job. And say that will die for one hour. And after that, if it expires, you do the math. So that kind of rotation we have not done yet. So we have a problem."

The pattern is a temporary key issuance flow: a client requests a key, the system issues a short-lived key, the client uses it for one job, and the key expires automatically, typically after one hour. Cisco has not built this flow yet.

## Colin's GitHub secrets approach

Colin returned to the GitHub pattern with more detail. "There is a way to do it in GitHub without letting anyone see the value of that key. They just get the idea of the key and they still have to be authenticated in GitHub to actually use it." This is the GitHub Actions secrets model: a secret is stored in the organization or repository configuration, workflows reference it by name, and the value is resolved at runtime inside the runner. The secret is never exposed to the human user.

The pattern removes the static value from human view and enforces authenticated identity for any use of the key, providing an audit trail. It does not solve the rotation problem; the secret is still effectively static unless paired with a separate rotation mechanism.

## Colin's Azure Key Vault reference

Colin then offered the heavier pattern. "The way that we do it, which might be too heavy for you, but it's very good to do from an organization standpoint, we actually use Azure Key Vault for everything. I don't know if that's an option for you. At the same time, if you wanted a custom solution, we can talk about that as well."

The reference positioned BayOne as an organization that has solved this problem internally at scale and opened the door to a custom solution if Azure Key Vault did not fit. Colin did not push either option; he laid them on the table.

## Srinivas's pushback on cost and audit

Srinivas declined the Azure Key Vault option immediately. "No, I don't want to open it. That has dollar amount and so many other things." Adding a new managed service requires vendor approval, procurement, and ongoing operating cost.

He then refined the framing of the problem. "Let me see if there is a... The problem is, it's not about saving the key, except about the keys. Meaning, once you get access to the key, you can do many things. I want to remove that power from the user." Colin reflected the framing back. "I see, you said expiring the keys." Srinivas confirmed. "Yeah, yeah, yeah, exactly."

This is the analytical center of the conversation. Srinivas is not concerned about key storage; he is concerned about key power. A static key, regardless of where it is stored, gives the holder unlimited capability for as long as the key remains valid. Storage protections like Azure Key Vault or GitHub Actions secrets reduce casual exposure but do not bound the power of the key once legitimately retrieved. The only mechanism that bounds the power is expiration.

## Srinivas on audit trail

Srinivas added the second half of the gap. "that expiration is not there, number one. And there's no audit trail to say which application requested for that. And then what he did with it. So that audit trail is not there. Because he said it was, yeah, we wanted to do it, but never did it." The reference to "he said it was" suggests someone inside Cisco previously committed to building an audit trail for LLM key usage and never completed the work.

The two gaps together define the requirement. Cisco needs short-lived keys that expire automatically and an audit log that records which application requested each key and what each key was used for. Without both, Srinivas cannot answer the question of who used what credential when something goes wrong.

## Colin offers Open Web UI pattern

Colin offered a third reference, this time aimed directly at the pattern Srinivas had described. "Are you familiar with this free and open source? It's really nice. It's called Open Web UI. Have you ever seen that?" Srinivas answered, "Yes, so that I don't know the way they always in our internal secret of course, of course, of course, so they have an approach to that that we could just replicate."

Srinivas described the pattern as he understood it. "So can you guess? Yeah, well, what is that we can do? But I mean, what hasn't that there is a way clients request for a temporary key apps in this case. Like a lot of people, and they'll give, and there'll be an inspiring default. And after it's done, they have to re-ask again." The phrase "inspiring default" is a dictation artifact for "expiring default." Srinivas was confirming that Open Web UI implements exactly the temporary key issuance pattern he wants.

The reference was tactical. Colin was not proposing Cisco adopt Open Web UI. He was pointing to a free and open source reference implementation of the pattern Srinivas wanted, which would give Cisco something to study and replicate without committing to a vendor.

## Srinivas on revocation

Srinivas connected the pattern to a revocation capability he already has elsewhere. "we have a controller who gets access on both computers." Colin acknowledged, "Right. Right." Colin added, "So you can grant your vote." Srinivas confirmed, "Yeah. Yeah. We can revoke the licenses or revoke the access and so the other thing."

The dictation is rough, but the meaning is clear. Cisco already has a controller pattern for granting and revoking access in other parts of the environment. The temporary LLM key flow Srinivas wants is an extension of that pattern into the LLM credential space.

## Colin's posture: valuable but not urgent

Srinivas closed the substantive part of the conversation by setting expectations on urgency. "that's good. Not urgent, but something to add to your list. It's not really urgent. We can unlock ourselves with whatever we have. But there's one problem and it's all wrong." Colin responded, "Okay. Yeah, happy to do it."

The framing is precise. The key rotation problem is real and Srinivas knows it. Cisco can continue to operate around it; the current static key approach unblocks the team. The problem is wrong, but it is not an emergency. Srinivas is asking BayOne to keep the problem on the list, not to drop everything and fix it.

For BayOne, the framing is favorable. It keeps key rotation work out of the next-Friday deployment target while creating optionality. If Srinivas later decides to scope the work, BayOne is already positioned as the resource he would ask.

## The aerospace anecdote

Colin reinforced the relevance of the topic with a brief personal story. "If you want a quick, funny Friday story, it'll take 30 seconds, I promise." He told it. "My prior organization, doing aerospace and defense things and really classified work, we had something for the A&E servers that was exactly this. It was like the global admin key for OpenAI. And it was on the government restricted server. After I left the company, they had given me that key. After I left the company, they never expired the key."

The phrase "A&E servers" is a dictation artifact for AI/ML servers. Colin's prior employer in a classified aerospace and defense environment had granted Colin a global administrative key for OpenAI on a government-restricted server, and after Colin left the key was never expired or revoked.

Colin closed with the consequence. "I actually ended up saying something to the guy because I didn't want to get in trouble on my side. But I was like you realize I could just you know, you know way too early for open claw back then but I was like, oh man I could have really racked up your bill if I wanted to because no one's looking for it." The phrase "open claw" is a dictation artifact for Open Web UI. Colin contacted his former employer to flag the unrevoked key, both to protect himself and because the company was not monitoring usage.

Srinivas's response confirmed the anecdote landed. "Yeah, it's possible, yeah. That's the thing right now. How do we protect this? Oh, oh, okay. Oh, that's what I can say. We'll find out. Yeah, we'll find out." The story validated his concern with a real example from a more classified environment than Cisco's. If a defense contractor working on government-restricted servers had the same problem, Cisco's exposure was not unique. The anecdote also functioned as a relationship-building moment: a thirty-second story did the work a paragraph of credentials would not have done.

## Srinivas's social framing

Srinivas added one more piece of context that revealed the social weight of the credential. "Many times someone asks me the super key I get. I was guarding with my heart right now. If you want to know... I've shared only two people I think so far. Only one guy and three people actually after all the 34 degrees working. So it's very hard."

Srinivas guards the super key personally. Across thirty-four years of working relationships, he has shared the key with somewhere between two and four people. People ask him for the key regularly and he refuses. The absence of expiration and audit makes guarding the key a personal responsibility, which is why the gap is a real organizational pain point. If the system itself enforces expiration and audit, Srinivas no longer has to be the human firewall; the pattern transfers responsibility from a person to a process.

## Closing: agreement to find a solution

Srinivas closed with a commitment to himself rather than to BayOne. "So first, I'll look at the keys." He returned to the topic at the end of the conversation. "I want to get it unblocked, but still we'll find some solution." Colin responded, "Yes, absolutely." The next move sits with Srinivas; BayOne is on his list as a resource when he chooses to engage.

## Strategic reading

The conversation establishes BayOne as a source of security-architecture competence in Srinivas's mental model. The CI/CD engagement scope does not include security architecture, but Colin's references to GitHub Actions secrets, Azure Key Vault, and Open Web UI demonstrated breadth across three different solution patterns at three different levels of cost and complexity. Srinivas heard the breadth without BayOne committing to any of it. The "not urgent, but something to add to your list" framing keeps the work out of the present scope while preserving the future option, and the aerospace anecdote validated Srinivas's concern with an example from a more classified environment.

## Implications for the engagement

The near-term posture is unchanged. BayOne continues to use the circuit API token for WebEx bot testing through the next-Friday demonstration, and DeepSight credentials follow rather than precede it. The medium-term posture introduces a deferred workstream: key rotation and audit trail work for Cisco's LLM credentials sits on Srinivas's list as a real but non-urgent item, with BayOne as the named resource.

BayOne entered the meeting positioned primarily as a CI/CD delivery resource and left also positioned as a security-architecture resource within the LLM credential space. The expansion happened without scope creep or commitment, because Colin answered a procedural question carefully, listened to the underlying concern, and offered three reference patterns calibrated to Srinivas's actual environment and constraints.
