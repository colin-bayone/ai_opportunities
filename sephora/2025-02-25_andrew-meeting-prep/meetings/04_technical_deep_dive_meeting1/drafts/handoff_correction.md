# Correction: Priority Order

You've got it backwards.

**MCP is the bigger issue, not YAML vs Scala.**

The original demo scope from Meeting 4 was Cognos with MCP integration. That was the whole point. If we cannot demonstrate MCP, Track A fundamentally changes. It goes from "look at this automated pipeline that connects to Cognos" to "look at us parsing an XML file you exported manually."

The YAML vs Scala thing is a clarification question. We ask, they answer, we build accordingly. It doesn't change whether Track B is viable.

The MCP constraint changes what Track A actually is. That's why it needs to be framed carefully. We're not saying we can't do it. We're saying we can build the connector architecture, but live demonstration requires their environment access, which their security posture may not allow. If they want to see MCP working, they need to provide that access.

This is the context for why the scoping docs matter. Track A's scoping doc explicitly addresses this with a section on "MCP Connectivity Requirements" that lays out what happens with vs without environment access. Track B's scoping doc has the YAML vs Scala clarification as a confirm box.

Both are attached. They can read the details. The email just needs to set up the right framing so they understand what they're looking at.
