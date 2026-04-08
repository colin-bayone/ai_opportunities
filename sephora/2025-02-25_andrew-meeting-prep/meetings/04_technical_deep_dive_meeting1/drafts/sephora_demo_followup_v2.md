Hi Malika, Sergey, Gariashi, Andrew,

Happy Monday! Apologies for the delay getting back to you. I was pulled into an escalation last week and had to fly back home unexpectedly for some personal matters.

First, a huge thank you to Mani for taking the time to meet with us at Sephora HQ last week. We had a fantastic time. The headquarters is seriously impressive and it was great to see firsthand how everything comes together for your team. I hope we get the chance to come back and visit again the next time I am in town, or better yet, when we kick this project off together.

Also, thank you again for everything your team has provided. The source table schemas, the clarification on the output format, all of it was exactly what we needed and we were able to hit the ground running.

We owe you the demo walkthrough we had promised for Friday. The video walks through the full end-to-end process, from uploading the files your team provided, through the agentic workflow running in LangGraph with a custom visualization tool we built to make each step easy to follow. From there it moves into a dashboard view where you can take manual review actions on any flagged items and access past job runs with full detail on what the pipeline did at each stage. The entire workflow runs in under two to three minutes, all on Azure. Here is the video.

https://bayonetechnoadvisors-my.sharepoint.com/:v:/g/personal/cmoore_bayone_com/IQDiqXFCGNiMTLeFPX4zjWQ3AWRsn8c4300v_mABn-WqwjE?e=jlaPj5

If the video looks blurry at all, click the gear icon and select 1080p for the best quality, or download it directly. The link is restricted for security since it involves your data. If anyone on the team needs access, just let us know and we can grant it.

Everything in this demo was built specifically around your DataStage jobs, stored procedures, framework, and source schemas over the last two weeks. Even at the PoC stage and without a great deal of optimization, the multi-agent pipeline is already producing above 97% accuracy on the first pass. The remaining items are not errors. They are small conversion items that get flagged for a quick human review before the pipeline finalizes, things like implicit type casts and performance considerations that are worth a second set of eyes. We are really proud of where this landed and excited for you to see it.

Even for a PoC, we built this production-style, hosted and deployed securely on Azure, and it could be ported over to your environment as well. We also have an option that requires no infrastructure at all. It is slower, but it can enable local developers immediately if there is any expected lag time with IT, which I know has come up in the past.

One thing to note is that right now someone still needs to manually provide the source files and take the generated output to deploy it. Once we have access to your environment, the agents can pull source files and push output directly, making the full workflow autonomous.

For this week, we would love to know what your availability looks like for a live demo. Everything is ready from our end. If it would be helpful, we could also get this deployed on Azure with secure credentials so your team can log in and actually try the workflow themselves. Not just something we are showing on our screen, but a real web application your team can interact with on your own. We would do that at no cost. That could be ready by Thursday, and we could share access with you on Friday. Just let us know what sounds good.

When we spoke with Mani last week, he mentioned the possibility of leveraging one of our existing BayOne resources at Sephora to get access to the Cognos environment. We would love to pursue that as an immediate next step after the PoC to get the pipeline fully autonomous in your ecosystem and remove the manual handoff entirely. Happy to discuss whenever the timing is right.

Really looking forward to hearing back and getting this in front of the team.

All my best,

Colin
