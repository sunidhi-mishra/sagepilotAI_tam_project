# Part A. Product and Market

# **Part A: Product and Market**

## **Question 1**

**Question:** A1 Read sagepilot.ai. In exactly three sentences, explain what Sagepilot does to a D2C founder who has never heard of it.

**Answer:** Right now, every rupee you spend on ads is making your WhatsApp and Instagram problem worse, because more orders just means more DMs your three people can't keep up with. Sagepilot's AI handles the repetitive stuff on its own, things like "where's my order," stock checks, and COD confirmations, on the same WhatsApp number and Instagram account you already use, and only brings in a human for the calls that actually need one. Your team and the AI work out of one shared dashboard, so you can finally run the ad campaign you've been holding off on, without needing to hire a fourth support person just to keep things from falling apart.

---

## **Question 2**

**Question:** A2 Sagepilot calls its product "AI employees," not "chatbots." Answer both:

1. What is the actual difference between the two?  
2. Why would a buyer pay more for the first framing? Do not look this up. Give your own view.

**Answer:** **1\. The actual difference**

A chatbot's job is scoped to a single conversation. It answers a question, and once it replies, its responsibility ends there.

An "AI employee," the way Sagepilot has built it, is scoped to outcomes across a whole workflow, and that changes things in three ways.

*Scope:* it doesn't just answer, it acts, with permission levels similar to what you'd give a new hire. The onboarding flow makes this concrete: orders and refunds are set to auto-approve, payments are read-only, and anything high-value needs sign-off first. That's not the scope of a chatbot. That's the scope you'd give someone on their first day.

*Trust:* it's designed to fail safely. Sagepilot's own language is that it "knows what it doesn't know" and hands the conversation to a person instead of guessing. A chatbot either guesses or hits a dead end. An employee escalates instead. That shifts the buyer's question from "does this work?" to "can I trust this a little more each time?"

*Accountability:* the site claims that corrections stick, that once you tell it something in plain language, the fix applies everywhere going forward. I haven't been able to verify how that actually works under the hood, whether it's a shared knowledge base update, a rules change, or something else. The marketing claim is clear. The mechanism behind it isn't something I could find documented anywhere.

**2\. Why a buyer would pay more**

A chatbot has a fixed ceiling. You buy it, tune it, and it stays at that level until you tune it again, which means you're always comparing it to the next tuning tool at the next price point.

An "AI employee" is positioned, and apparently built, with a rising ceiling instead. It starts supervised, goes live across channels from day one, and is meant to get more autonomous as it learns from corrections. If that's genuinely how it works, the buyer isn't paying for today's automation rate. They're paying for a trajectory, the same way a manager judges a new hire on their potential rather than their first week. That's the kind of thing that justifies a different pricing tier altogether, closer to a hiring decision than a software purchase.

That said, I haven't confirmed whether that improvement curve comes from the AI actually learning on its own, or simply from the buyer getting better at configuring it over time. I also haven't seen Sagepilot's real pricing model. There's no public pricing page, and every call to action is "book a demo," which suggests the pricing is handled through sales rather than published tiers. So the honest version of this claim is: the framing justifies a higher willingness to pay if the product truly delivers on graduated trust and compounding value. It doesn't mean Sagepilot has actually captured that premium in its pricing yet.

---

## **Question 3**

**Question:** A3 The website lists several AI employees or agents working across the customer lifecycle (acquisition, sales, support, retention) and across products such as Helpdesk, Voice, Marketing Suite, Reputation, Governance, and Analytics. Identify each one and build a table with these columns:

1. Name of the AI employee or agent, as it appears on the site.  
2. Where it sits in the customer lifecycle.  
3. Three specific D2C problems it can resolve. Be concrete, not generic. "Answers customer questions" does not count. "Tells a customer where their delayed order is and issues a store credit without a human" does.  
4. Which channel or channels it runs on.  
5. Whether it is usually live at onboarding, or sold later as an expansion, and why.

**Answer:** A quick note before the table: Sagepilot names exactly three agents, Support, Marketing, and Operations. Helpdesk, Marketing Suite, Voice, Reputation, Governance, and Analytics are platform features these agents work inside, not separate agents in their own right. Marketing Suite belongs to the Marketing Agent, Helpdesk belongs to Support, Voice most likely sits with Support too (though the site doesn't say this outright), and Reputation, Governance, and Analytics cut across all three rather than belonging to any one of them.

| \# | Name (as it appears) | Lifecycle stage | Three concrete D2C problems it resolves | Channel(s) | Onboarding or expansion |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 1 | **AI Support Agent** | Support, after the sale, though it reaches into pre-sale through DMs and comments | A customer messages saying their order hasn't shipped and they're travelling on Friday. The agent pulls up the order, expedites it with the courier, and confirms a new delivery date over WhatsApp, no human needed. A customer asks to redirect an order that's already in transit to a new address. The agent updates it in the system, redirects it with the courier, and confirms the new arrival date. A refund request comes in above the auto-approve limit (Sagepilot's own example is ₹12,400 over the cap). The agent pulls together the order and conversation history and sends a full-context request for approval instead of just handing it off cold. | WhatsApp, Instagram (DMs and comments), Messenger, Facebook, email, X, Reddit, iMessage, live chat, voice | Onboarding. This is the front door of the product and the fastest agent to show a measurable number, its deflection rate, within the first week. |
| 2 | **AI Marketing Agent** | Mainly retention and win-back, with some reach into acquisition through campaign content | 1,284 customers have lapsed for 90+ days. The agent builds the win-back segment on its own, personalises the offer for each customer, and sends it over WhatsApp and email, recovering 212 orders in the first week with a follow-up queued for the rest. A customer clicks a win-back offer but doesn't buy. The agent automatically queues a follow-up instead of letting the lead go cold. A third example isn't something I can verify. The site only shows two fully worked scenarios for this agent, and I checked twice, including a specific search on loyalty points and campaign use cases, without finding a third. I'd rather flag that gap than make something up to fill the cell. | WhatsApp, email, SMS, RCS, push | Expansion. This is usually sold after Support, once a brand trusts the platform enough to let it handle outbound, revenue-driving messages rather than just replies, and has the segment and campaign setup in place to use it. |
| 3 | **AI Operations Agent** | Operations, working behind the scenes to support both support and retention | 12 shipments are stuck in transit for 48+ hours. The agent raises tickets with the courier, updates the delivery dates on the orders, and notifies the affected customers, and all 12 start moving again. Of those 12, two look like likely returns. The agent proactively confirms the delivery address with just those two customers. A payment fails at checkout (the site's own example is order \#22914). The agent detects the failure and retries it automatically, recovering the order without a ticket ever being opened. | Backend systems (Shopify, Razorpay/Stripe, Shiprocket/Delhivery/AfterShip), with customer-facing updates going out over WhatsApp and email | Expansion, and usually the hardest one to sell. A brand has to trust this agent with money and courier decisions, which takes more proof than Support does. |

---

## **Question 4**

**Question:** A4 A prospect says: "We already run support through Freshdesk, and LimeChat demoed for us yesterday claiming deeper Shopify integration. Why pick Sagepilot?" You have not used LimeChat and do not know its feature list. Write what you would say, in under 150 words. Your answer must:

1. Not invent competitor features.  
2. Not badmouth either competitor.  
3. Give one specific reason to look closer at Sagepilot.

**Answer:** I can't speak to how deep LimeChat's Shopify integration actually goes. I haven't used it, so I'm not going to compare on something I can't verify. But the more useful question here isn't whose integration goes deeper, it's whether the tool just reads your store or actually does something inside it. Sagepilot's agent doesn't stop at replying to tickets. It acts: expediting a shipment with your courier, redirecting an order that's already on its way, approving a refund within your set limits and escalating anything above that with the full context attached. That's reading and writing across support, marketing, and operations, not just a helpdesk layered on top of your store. Freshdesk is built to route a ticket to a person. Sagepilot is built to resolve it without one, working inside your actual systems. Rather than ask you to take my word over LimeChat's, I'd suggest running both on the same three real tickets from last week, a refund, a WISMO question, and an address change, and seeing what each one actually does, not what the pitch promises.

# Part B. The System You Will Support

# **Part B: The System You Will Support**

## **Question 1**

**Question:** B1.1 Why run this as a durable long-running workflow instead of the two alternatives below? For each, say what the workflow gives you that it does not.

1. A stateless bot that just answers each incoming message.  
2. A cron job that wakes hourly and polls the database.

**Answer:** **1\. A stateless bot that just answers each incoming message**

A workflow keeps state across events, through its timeline and a compact memory summary. A stateless bot can't do this, because every incoming message is treated as its own separate event with no memory of what came before. It wouldn't know it already told this customer about a delay three days ago, and it couldn't connect today's message from the customer with a shipment delay signal that arrived earlier with no message attached at all. Either the state lives in the workflow, or it simply doesn't exist.

A workflow can also wake itself up with no outside trigger at all, through a durable timer (this is what handles the "no update for X hours" case). A stateless bot has no way to do this. "Answer each incoming message" only covers messages, so there's nothing for it to respond to and nothing that wakes it up on its own. Checking in with a customer after a quiet stretch requires something to be sitting there waiting, and a stateless bot, by definition, isn't waiting between calls.

Finally, a workflow has a bounded run with its own start and end rules. A stateless bot doesn't, because it has no concept of "this order" as something ongoing that it's watching over. Every call is one-off, so there's no run to close out, and nothing that could ever write a final summary of what happened across the whole order, since no single call ever saw the full picture.

**2\. A cron job that wakes hourly and polls the database**

A workflow reacts to signals in close to real time. A cron job can't, because its worst-case delay is whatever the polling interval is. A refund request or a failed payment that comes in one minute after the last poll won't get handled for close to an hour, which is a genuine problem for anything time-sensitive, not just a minor inconvenience.

A workflow's cost scales with actual events, per order. A cron job's doesn't, because every single poll has to check the entire set of open orders to see what's changed, instead of only being notified about the one order that actually matters. At four to six hundred orders a day, that means scanning hundreds of unchanged orders every hour just to catch the handful that actually moved, and that gets worse, not better, as volume grows.

A workflow also gives you durable crash recovery. Temporal can replay a workflow's history and pick up exactly where it left off. A bare polling process has no such guarantee built in. If it crashes mid-poll or restarts, figuring out where it left off for a specific order is something you'd have to build and maintain yourself, rather than something the system hands you for free.

---

## **Question 2**

**Question:** B1.2 Define each of the following in one line:

1. Signal.  
2. Timer, or durable sleep.  
3. Query.  
4. Continue-as-new. Also say why a supervisor that runs for weeks would need it.

**Answer:** **Signal:** an event pushed into the running order workflow from outside (payment confirmed, shipment delayed, a new customer message, and so on) that the workflow never asked for or was polling for. It just shows up.

**Timer, or durable sleep:** a wait that survives crashes and restarts, so a scheduled wake-up (including the "no update for X hours" case) is guaranteed to fire even if the process managing it goes down in the meantime, unlike a simple in-memory timer, which would just disappear.

**Query:** a read-only, synchronous way to check a running order's current state, its memory summary and timeline, from outside, without sending it a signal or changing anything. For example, pulling up an order's current status for a support agent without waking the workflow or feeding it a new event.

**Continue-as-new:** closing out the current workflow run and starting a fresh one that carries forward a compact summary but wipes the event history clean. A supervisor running for weeks needs this because every signal, timer, and tool call adds to that workflow's history, and left unchecked, that eventually slows down replay and risks hitting a hard size limit. It's really the same problem the spec already describes at the memory layer, where older detail has to fold into the summary instead of growing forever, just showing up one level up, at the level of the whole workflow.

---

## **Question 3**

**Question:** B1.3 A client reports: "Your AI messaged my customer twice about the same delayed shipment, ten minutes apart." Give three technically distinct root causes, one in each layer below. For each cause, state exactly how you would confirm or rule it out using the run timeline and activity log.

1. The wake policy.  
2. The signal handling.  
3. The tool execution.

**Answer:** **1\. The wake policy:** an event-triggered wake and a scheduled timer wake landed close together, and neither one checked whether the other had already acted.

Here's how this could happen: the shipment delay signal arrives and correctly wakes the agent, which messages the customer. Ten minutes later, a check-in that was already scheduled before the delay came in fires right on time, and since there's no rule telling it to skip a scheduled wake if a real event already triggered one recently for the same order, it wakes the agent a second time. Seeing the delay still active in its state, the agent reasons its way into messaging the customer again.

To confirm or rule this out, pull the timeline for the two wake events about ten minutes apart and check what actually triggered each one. If one was triggered by the shipment delay signal and the other by the scheduled timer firing on its own, unrelated to any new signal, that's the fingerprint of this exact failure: two different kinds of wake-up converging on the same order too close together. If both wakes trace back to signals instead, this isn't the cause, and the problem lies further down the chain.

**2\. The signal handling:** the same delay got delivered as two separate signals, most likely a retried webhook, and nothing caught the duplicate.

This happens when the courier or Shopify webhook resends the same delay signal, which is normal behavior for at-least-once delivery when no acknowledgment comes back in time, and the workflow treats the resend as a brand new event instead of recognizing it as the same delay it already knows about. Two separate signals mean two separate decisions to wake and act, each with no idea the other one just happened.

To confirm this, check the signal history itself, not the wake or activity logs, for two entries with nearly identical or identical payloads (same order, same delay reason, same courier reference) roughly ten minutes apart. If both carry the same source event ID or an unchanged payload with nothing new in it, that confirms a duplicate delivery rather than a genuinely new delay. If the payloads differ in a meaningful way, this layer is ruled out.

**3\. The tool execution:** the decision to message the customer was only made once, but the actual send happened twice because of a retry that wasn't idempotent.

In this case, the agent reasoned through it once, at a single wake-up, and decided once to send the message. But the send succeeded on WhatsApp's end while the confirmation back to the workflow was lost or timed out, so the automatic retry kicked in and ran the same send again. Without something in place to prevent a duplicate send, that retry becomes a second, real message to the customer.

To confirm this, check the activity log for the message-sending tool and look for more than one execution tied to the same order and the same decision point, meaning one wake cycle and one decision, but two logged sends with identical content, only seconds or a couple of minutes apart rather than the ten-minute gap you'd see between two separate wake cycles. If the log instead shows two completely separate wake events each independently sending the message once, this layer is ruled out and the cause sits upstream, in either the wake policy or the signal handling.

---

## **Question 4**

**Question:** B1.4 Answer both:

1. Why must the workflow, not the AI, decide when the run ends?  
2. Give one concrete failure that could happen if the model were allowed to end the run itself.

**Answer:** **1\. Why the workflow decides, not the AI**

The conditions that end a run, delivery, a resolved refund, manual closure, are objective, verifiable facts tied to specific signals coming from systems of record: the courier confirms delivery, the payment processor confirms the refund actually went through. The workflow is the part of the system built to react reliably to those verified signals. The AI's job here is reasoning under uncertainty during a single wake-up, deciding what to do given the state it has in front of it. Letting the AI decide when to end the run means resting a structural, system-level decision on a judgment call made inside one conversational exchange, instead of on the same dependable signal-handling the rest of the system already relies on for everything else.

There's also a technical mismatch. Temporal's reliability depends on workflow code being deterministic, so it can be safely replayed from its history. An AI call isn't deterministic. Running the same reasoning step twice wouldn't reliably give you the same answer. Building "should this run end" into that step would put a decision the whole system depends on inside the one part that isn't built to be replayed safely, which runs against how everything else here is designed to work.

**2\. A concrete failure**

Say the customer replies "ok thanks" right after being told their refund is being processed. If the agent could end the run on its own, it might read that as the conversation being wrapped up and close the workflow then and there. But at that point, the refund process has only been started. The actual confirmation from the payment processor hasn't come in yet. Once the workflow is closed, one of two things happens: either that confirmation signal arrives with nowhere to go, since there's no workflow left running to receive it, or worse, the refund quietly fails on the payment processor's end and nobody's watching for it anymore. The customer thinks it's handled because the conversation felt like it was over. Nothing in the system actually confirmed that it was.

---

## **Question 5**

**Question:** B2. Build a small version Build one program, roughly 200 to 350 lines. No Temporal, no database, no frontend, no cloud. An in-memory simulation is correct.

**Answer:**
This part is a code deliverable rather than a written answer, submitted separately as two folders, `order-supervisor-simulation (rule-based)` and `order-supervisor-simulation (llm-based)`. The rule-based folder is the core graded submission, no external calls, no dependencies beyond Python. Each folder contains the simulation code, a `README.md`, a `sample_events.json`, and the real output from running it. The rule-based README covers how to run it and maps each part of the build back to its Temporal equivalent (signal, timer, query, activity, continue-as-new). The LLM-based folder covers the bonus item, wiring in a real language model for the decision step, with the same event handling and memory logic underneath, plus a fallback to the rule-based logic if the API call ever fails.

---

## **Question 6**

**Question:** B3.1 Answer both:

1. What is WhatsApp's 24-hour customer service window?  
2. What must a business do to message a customer after it closes?

**Answer:** **1\.** It's a rolling window that opens the moment a customer sends your business a WhatsApp message or call, and for the following 24 hours, you can reply freely without needing a pre-approved template. Every new message from that customer resets the clock back to a full 24 hours. It isn't a fixed daily cutoff. It tracks per customer, based on their most recent message.

**2\.** You have to send a pre-approved message template, in the Marketing, Utility, or Authentication category, and the customer needs to have actively opted in to receive it. Free-form messaging isn't an option again until the customer replies, at which point the 24-hour window reopens.

---

## **Question 7**

**Question:** B3.2 A brand wants to send this message after delivery: "Hi Priya\! Your order \#8834 was delivered today. Hope you love it\! Use code NEXT20 for 20% off your next order. Shop now: \[link\]." Answer all three:

1. Which Meta template category does it fall under?  
2. Why that category, and not the others?  
3. What happens if it is submitted under the wrong category? Describe Meta's actual enforcement.

**Answer:** **1\.** Marketing.

**2\.** It's easy to rule out Authentication first, since there's no OTP or identity check involved. Utility looks tempting at first glance, because the opening line ("your order was delivered") is a legitimate transactional trigger. But the moment the message adds a discount code and a "Shop now" style call to action, it stops being a status update and starts being an attempt to drive a new purchase. Meta's own rules for Utility templates are explicit that they have to stay single-purpose and non-promotional, with no offer language and no persuasive buttons, only functional ones like "Track Order." This message breaks both of those rules. Marketing is the right category because what the message is actually doing, using a discount to push another sale, matches Marketing's own definition, not a simple status update.

**3\.** Meta doesn't just reject a misclassified template. If this were submitted as Utility, Meta would approve it but quietly recategorize it as Marketing. The business gets an email, an alert inside WhatsApp Manager, and a webhook notifying them of the change, but the template keeps sending the whole time, just billed at the higher Marketing rate from that point forward instead of being blocked. The business can appeal the recategorization within 60 days. On top of that, Meta also runs a monthly automated review of already-approved templates, so something that passed initially can still get flagged and recategorized later, with a month's notice before the new category and billing take effect. Repeated or deliberate mislabeling can lead to stricter enforcement over time, but the default response is a billing correction with a heads-up, not an immediate takedown.

---

## **Question 8**

**Question:** B3.3 A client asks: "Why did our WhatsApp bill jump this month? We did not send more campaigns." Meta bills per conversation. List five things you would check, and for each, why it could move the bill.

**Answer:** Before the list, one thing worth flagging directly: the question describes Meta as billing "per conversation," but that model was actually retired on July 1, 2025, in favor of billing per message, with each template billed individually based on its category and the recipient's country. Rather than quietly work around this, I'd raise it outright. It's possible "conversation" here just means "conversation category," since Marketing, Utility, Authentication, and Service still exist as pricing categories under the new system, or this might be testing whether the mismatch gets noticed. Either way, I'm answering against the current per-message model, since that's what's actually in effect.

**1\. The mix of template categories, especially anything recently recategorized.** Marketing messages cost more and are billed every single time, even inside the free 24-hour window, unlike Utility. If any template, including one caught by Meta's own monthly audit, got quietly moved from Utility to Marketing, the exact same message volume now costs more per send with no change in how many campaigns went out.

**2\. Whether Utility messages are landing inside or outside the 24-hour window.** Inside the window, they're free. Outside it, the same message costs the standard Utility rate. If more of this month's Utility messages, say, proactive delay notices, happened to fall outside an open window compared to last month, that alone raises the bill with no change in campaign activity.

**3\. The mix of countries being messaged.** Per-message rates vary a lot by country, roughly $0.009 in India versus over $0.12 in Germany, based on Meta's published rates. If the customer base shifted even slightly toward pricier markets this month, more international orders, a push into a new region, the average cost per message goes up even if the total volume stayed flat.

**4\. Whether a volume discount tier reset.** Utility and Authentication messages get volume-based discounts, calculated separately by country and category, and these reset every calendar month. If last month's volume hit a discounted tier early, say by day five, but this month it doesn't hit that tier until day twenty, or doesn't hit it at all, most of this month's messages go out at the higher, pre-discount rate, even with identical total volume.

**5\. Proactive messages the AI sends on its own that aren't technically "campaigns."** The client's framing is that they didn't send more campaigns, but things like delay notifications, payment retry confirmations, or escalation updates are still billable template messages. If the AI's proactive outreach increased, more delayed shipments flagged, more automatic check-ins, that's genuinely new message volume the client wouldn't think to call a campaign, but Meta bills it exactly the same way.

---

## **Question 9**

**Question:** B3.4 A brand on Shopify expects the AI to know when an order ships. Answer both:

1. Explain the webhook flow: what event fires it, what the payload carries, and what the receiving system does with it.  
2. The client says the AI keeps telling customers their order has not shipped when it has. Walk through, step by step, how you find where in the chain it breaks.

**Answer:** **1\. The webhook flow**

Shopify fires a fulfillment-created webhook the moment a fulfillment record is created for an order, in practice, whenever the merchant, a third-party logistics provider, or a courier integration marks an item as shipped inside Shopify. A related webhook fires later for status changes, like tracking updates as the shipment moves. The payload includes the fulfillment ID, the order it belongs to, its status, the courier name and tracking number, shipment status, the delivery address, which specific line items were fulfilled, and timestamps.

On delivery, Shopify signs the payload, attaches a unique event ID for deduplication, and retries failed deliveries for up to 48 hours with increasing delays between attempts. It doesn't guarantee delivery order though, so in theory a shipment webhook could arrive before an order-paid webhook the receiving system was expecting first.

The receiving system's job is to verify the signature, respond within Shopify's five-second timeout, and then process the payload separately, matching it to the right order and updating that order's internal state. In terms of the order supervisor system, this is exactly a signal landing on the correct order and updating its memory summary and timeline the same way any other event would.

**2\. Working out where it broke**

Start by confirming the fulfillment actually exists in Shopify. Check the order directly. Is there a real fulfillment record, or did the team or the courier mark it shipped somewhere else, like a courier dashboard, that never actually wrote back to Shopify? If there's no fulfillment record in Shopify at all, nothing downstream is actually broken. The event that was supposed to trigger everything never existed in the first place.

Next, check whether the webhook subscription is even set up. Is the fulfillment-created event actually subscribed for this store's connection? If it's missing or misconfigured, Shopify never attempts to send it, and this is something you'd confirm through Shopify's own webhook settings, not the receiving system's logs.

Then check Shopify's delivery log. Assuming the subscription exists, did Shopify actually try to deliver it, and did it get a successful response back? If there are repeated failures or timeouts across the 48-hour retry window that eventually stop, the problem is with the receiving endpoint's availability, not Shopify.

After that, check whether the signature check and payload parsing succeeded on receipt. If delivery was logged as successful, did the receiving system's verification pass, and did it parse the data correctly? A quiet failure at either of these points would cause the event to get dropped after it was already acknowledged, which looks exactly like success from Shopify's side but never actually reaches anything downstream.

Then check whether the event got matched to the right order. If it was received and parsed correctly, was it actually linked to the right order by its ID? Split fulfillments across locations, draft orders, or a mismatch between an order number and its underlying ID are common reasons a real event ends up attached to the wrong order, or no order at all.

Finally, check the specific order's own state directly. Does its timeline actually show the shipment as received? If it's there but the agent is still telling the customer it hasn't shipped, the problem isn't upstream at all. It's that the agent is answering from an old, cached summary that never got refreshed after the signal came in, which is a completely different kind of bug than anything in the earlier steps.

Each step either confirms the break is at that point or clears it and moves on to the next, the same approach as working through the double-message issue earlier, just moving forward through the pipeline instead of checking across parallel layers.

# Part C. Onboarding

# **Part C: Onboarding**

## **Question 1**

**Question:** C1 Write a week-by-week plan for their first four weeks. For each of the four weeks, give all five of the following:

1. What gets set up or launched.  
2. What you need from the client, and by when.  
3. What could go wrong, and how you prevent it.  
4. What the client can do by end of that week that they could not before.  
5. The one leading indicator you would watch to know it is on track.

**Answer:** **Week 1: Foundation**

*What gets set up:* Everything gets sequenced by how long it takes, not by how important it feels. The WhatsApp Business API migration starts on day one, because Meta's business verification is the slowest-moving piece in the entire plan, and nothing customer-facing on WhatsApp can happen until it clears. Meanwhile, everything that doesn't depend on that migration moves forward right away: connecting Shopify (read access to orders and the catalog), pulling in policy documents and past ticket history, and getting the Instagram DM and comment channel live in supervised mode, where every AI-drafted reply gets approved by a person before it goes out, since Instagram has no dependency on the WhatsApp migration at all.

*What I need from the client, by when:* On day one, Meta Business Manager admin access and whatever verification documents Meta asks for (GST or incorporation paperwork), since even a one-day delay here pushes back the entire WhatsApp track. Also on day one, Shopify admin access, along with their return and exchange policy and sizing guidelines, even in rough form. I'll clean it up on my end. By day three, I'd want some brand voice examples, past captions or replies they're proud of, so the AI starts learning from real material instead of a generic tone.

*What could go wrong:* The real risk is moving a live, actively-used WhatsApp number off the Business App and onto the API carelessly, which could mean losing chat history or the verified badge, or worse, a stretch of time where the number exists but isn't actually receiving anything, on their busiest support channel. To prevent this, the cutover only happens once Meta's verification is fully confirmed and a test message has successfully gone both ways on the API. The old Business App keeps running and answering customers right up until that exact moment, so there's never a gap where the number is live but silent. If verification takes longer than expected, I'd rather push the cutover back than risk that gap.

*What the client can do by the end of Week 1:* Being honest here, nothing changes on WhatsApp yet, since API verification is likely still pending. The real, legitimate win is that Instagram DMs and comments start getting an AI-drafted response within minutes, still supervised by a person, which is a genuine improvement on one of their two biggest pain points, even while WhatsApp is still mid-migration.

*Leading indicator:* the status of Meta's business verification, checked daily. Every other date in this four-week plan depends on when that single approval comes through.

**Week 2: WhatsApp goes live, under supervision**

*What gets set up:* Assuming verification came through, the actual cutover happens this week. The old Business App stops handling traffic, the WhatsApp number moves onto the API, and the Support Agent starts drafting replies across both WhatsApp and Instagram, still fully supervised, with every reply approved by a person before sending. The built-in helpdesk inbox replaces checking a phone and a separate Instagram app, so everything lands in one place. No autonomous sending yet. The goal this week is proving the drafts are good, not proving the AI can be trusted on its own.

*What I need from the client, by when:* By day two, a ranked list of their top 15 to 20 recurring customer questions or complaints, even if it's just from memory, since there's no structured ticket history yet. This tells us which intents (order status, cash-on-delivery confirmations, sizing, fabric questions) the agent needs to get right first. By day three, one of their three support staff committed to roughly an hour a day of actual review time, not "whenever they get a chance."

*What could go wrong:* The risk here is human, not technical. Staff might see this as a threat to their jobs and either slow down approvals, letting drafts pile up and response times get worse than before, or swing the other way and rubber-stamp everything without really reading it, letting bad drafts go out unnoticed. To manage this, I'd set up one clear, visible metric with them this week, tickets handled per person, and frame it as something that makes their day easier, not a performance audit. If approval times start creeping up, or I see a spike of near-instant approvals on genuinely complex questions, that's my cue to step in and coach, rather than waiting for a customer complaint to surface the problem. I'd also spot-check a random sample of approved drafts myself, since the approval-without-edits rate on its own can be gamed by exactly this kind of rubber-stamping.

*What the client can do by the end of Week 2:* Reply to Instagram DMs and WhatsApp messages within minutes, across both channels, from a single inbox, even during a traffic spike from one of their daily ad pushes, because the AI drafts the reply and a person just approves it, instead of three people typing every response from scratch on a phone. This is the first week their "WhatsApp is always busy" problem actually starts to ease.

*Leading indicator:* the percentage of AI-drafted replies approved without any edits, checked against my own spot-audits rather than trusted on its own, given the rubber-stamping risk above. A rising, verified no-edit rate tells me it's safe to expand autonomy in Week 3\. A flat or falling one tells me to hold off.

**Week 3: First steps into autonomy, on narrow, low-risk topics**

*What gets set up:* Autonomy gets granted, but tightly, not as a blanket "the AI is trusted now." Specific high-frequency, low-risk topics, order status, cash-on-delivery confirmation, sizing and fabric questions, stock checks, move to auto-send, based directly on which intents showed strong no-edit approval rates in Week 2\. Anything involving money, refunds, exchanges, discount exceptions, stays under review. At the same time, the Operations Agent connects to Shopify and the courier system in read-only mode, watching for delayed shipments without acting on anything yet, building visibility ahead of getting write access in Week 4\.

*What I need from the client, by when:* By day two, a written escalation and refund threshold, an actual number, such as "refunds under a certain amount, for unopened items within a set number of days, can go through without my sign-off," not a vague "use your judgment." Without this in writing by day two, autonomy either gets delayed or scoped more narrowly than planned this week.

*What could go wrong:* The risk is granting autonomy faster than the evidence actually supports. The fact that the AI drafts good refund replies, while still under human review, isn't the same evidence as proving it should send them unsupervised. To guard against this, autonomy this week only goes to intents that showed a consistently high no-edit rate across multiple days in Week 2, and refunds or exceptions stay under review no matter how strong those drafts looked, because a wrong, money-related message sent autonomously is a much worse mistake than a wrong reply about order status.

*What the client can do by the end of Week 3:* Their three support staff stop handling the highest-volume, simplest tickets altogether, since those now resolve without any human involved, freeing up time for the harder 20 percent: real complaints, unclear requests, upset customers. Their actual workload shifts in kind, not just gets faster.

*Leading indicator:* the deflection rate specifically on the newly autonomous topics, tracked alongside CSAT for those same conversations, not overall and not on its own. A rising deflection rate with flat or improving CSAT on exactly those topics means the scoping was right. A rising deflection rate paired with dropping CSAT means autonomy expanded too fast, and I'd want to catch that within the week, not a month later at a quarterly review.

**Week 4: Full coverage, Operations Agent gets write access, and the first business-outcome read**

*What gets set up:* The Operations Agent moves from read-only to write access, but just as carefully scoped as Support's autonomy was: proactively notifying customers about shipment delays (just a message, not money) goes to auto-send, while anything that spends money, store credit, expedited shipping paid by the brand, stays gated behind an agreed threshold. Support's autonomy expands to whatever Week 3's data supports, and refunds or exchanges within the agreed limit go autonomous for the first time. A basic dashboard also goes live for the founder, showing automation rate, CSAT, and response time in one place.

*What I need from the client, by when:* By day two, final sign-off on how much the Operations Agent can spend on its own, expedited shipping costs, store credit caps, which is a separate decision from Week 3's refund threshold. Mixing the two up risks over-restricting or under-restricting Operations by accident. By day four, a decision on whether the Marketing Agent should be the next thing we add, raised now, with real data in front of the founder, rather than saved for a future sales conversation, since their 120,000-follower Instagram base being completely un-monetized for retention is now a clear, visible gap.

*What could go wrong:* The real risk this week is attention, not technology. After four weeks of steady progress, the founder might reasonably assume the risky part is behind them and start paying less attention right at the moment autonomy is expanding the most, Operations getting write access, Support getting money-adjacent autonomy for the first time. That's actually the highest-risk moment for something to go wrong unnoticed. To guard against it, I'd schedule a Week 4 review call that walks through three to five real autonomous actions from that week specifically, an actual look at what the AI did on its own, not a general status update.

*What the client can do by the end of Week 4:* Handle their full daily Instagram and WhatsApp volume, including in-policy refunds and exchanges and proactive delay handling, without adding any headcount, and for the first time, see it in real numbers, automation rate, CSAT, response time, all in one dashboard, instead of just a general sense that "the phone felt less busy this week."

*Leading indicator:* the repeat purchase rate, over the last 30 days, among customers who had an AI-resolved interaction, compared to those who didn't. Deliberately not another automation or CSAT number. By Week 4, there are enough resolved conversations to start asking whether faster, AI-handled resolution actually keeps customers coming back, not just whether it processes tickets faster. This isn't meant to be a conclusive answer at 30 days. It's the start of tracking a number I want already trending by the time the six-month quarterly review happens, rather than trying to reconstruct it after the fact.

---

## **Question 2**

**Question:** C2 At go-live, the implementation engineer hands you the account. Name the three things they must hand over. For each, state why it matters specifically for retention.

**Answer:** **1\. Full configuration and decision history.** Not just the current settings, but the full reasoning behind them: every autonomy threshold and what triggered it, why certain topics went autonomous in Week 3 and not Week 2, why Operations got read-only access before write access, the exact refund threshold and who signed off on it.

Why it matters for retention: the first time something goes wrong, an unexpected auto-sent refund, a customer asking why the AI did something, I need to be able to answer right away with the actual reasoning behind it, not "let me look into that." Without that history, I'd either have to loosen a threshold recklessly just to keep the client happy, or push back without being able to explain why. Either way, it looks like the person managing the account doesn't actually understand their own setup, and that kind of doubt does more damage to the relationship than the original mistake ever would.

**2\. A list of open issues and anything flagged but not fully resolved.** Across the four weeks of onboarding, something almost always comes up that doesn't get a clean fix, an edge case the AI still struggles with, a manual workaround holding something together, a concern the client mentioned once and let go because it wasn't urgent at the time.

Why it matters for retention: if one of these resurfaces later and I act surprised by it, it looks like nobody was paying attention, or worse, that the concern was raised and simply ignored. A client having to bring up something they already flagged once, only to find out it was never tracked, is one of the fastest ways to lose confidence that anyone is actually watching their account. That kind of quiet erosion is exactly what tends to show up later as a renewal at risk.

**3\. Relationship and stakeholder context.** Who championed this internally, who needed convincing, what expectations were set along the way, even offhand comments about what "success" would look like that never made it into an official document.

Why it matters for retention: this is exactly the kind of thing I'd want on hand if a main contact ever goes quiet as renewal approaches. Finding out only at that point that the main contact was never fully bought in, and that someone else on the team was actually the real champion, costs me weeks I could have spent building the right relationship instead of the convenient one. If this context only lives in the implementation engineer's head and never gets passed on, I end up trying to piece it together under pressure instead of already having it ready when it actually matters.

# Part D. Success, Retention, and Upsell

# **Part D: Success, Retention, and Upsell**

## **Question 1**

**Question:** D1.1 Write a plan to reach 80% automation in three weeks. Take each of the four handoff buckets in turn, and for each give:

1. The likely cause.  
2. The specific change you would make.  
3. How you would measure whether the fix worked. No vague advice. "Improve the AI" or "train the model better" scores zero.

**Answer:** **Week 1: diagnose the unclear buckets, and start the fixes we already know about.**

The refund threshold question and the pattern behind "I want a human" both need transcripts pulled before we know what's actually wrong, so that happens first since it's quick, cheap, and purely a data-gathering step. At the same time, the three "AI didn't understand" fixes don't need any diagnosis at all. The topic list already tells us exactly what's missing: the exchange policy document, the loyalty-points connection, and COD availability data. So integration work on those three starts on day one, running in parallel rather than waiting for the refund and "want a human" audits to finish. "Other" also gets manually broken down this week. The goal isn't to fix it yet, it's to turn that unlabeled 16 percent into two or three named, specific clusters by the end of the week.

**Week 2: ship the fixes.**

Set the refund auto-approve threshold, or if the data actually showed a genuine wave of above-threshold refunds rather than a missing setting, address that instead, since by now we'd know which one it is. Ship whichever specific reply or grounding fix the Week 1 audit pointed to for "I want a human." Finish the three integration tasks for "AI didn't understand" if they weren't already done in Week 1, since the loyalty-points backend access in particular may take longer than simply uploading a document. Address whichever two or three named clusters came out of "Other."

**Week 3: re-check every bucket on its own, and fix whatever didn't move.**

Re-run each of the four measurements separately rather than starting with the overall automation number, since that number blends all four together and would hide which fix actually worked and which one didn't. If, say, the refund fix moved the way we expected but "I want a human" didn't budge, that tells us the reply fix missed the real pattern and needs another look, not a broader retrain. The overall automation rate is the last thing I'd check, as confirmation that all four fixes together actually add up to 80 percent, not the first or only number I'm watching.

---

## **Question 2**

**Question:** D1.2 Answer all three:

1. Which of your fixes are retention saves?  
2. Which open a real upsell: a module, an SOP pack, or a channel?  
3. Pick one upsell and say how you would raise it without looking like you profit from the client's problem.

**Answer:** **1\. Which fixes are retention saves**

Three of the four fixes are purely defensive. They close a gap between what was promised and what was actually delivered, without adding anything new: the refund threshold setting, the fix for "I want a human," and breaking down the "Other" bucket. All three come down to the same thing, this should have worked from day one, and now it does. None of them naturally lead into a conversation about paying for something new. They're just closing the gap between the 85 percent that was promised and the 62 percent that was actually happening, which is the whole reason this plan exists in the first place.

**2\. Which one opens a real upsell**

The fix tied to exchange policy, loyalty points, and COD is different from the other three, specifically because of the loyalty-points backend connection. Setting that up wasn't just closing a support gap, it's the first real, working link into the client's loyalty and rewards data. Given what the Marketing Agent actually does, building segments and journeys and running campaigns with revenue tied back to them, that same connected data is exactly what a win-back or loyalty-based retention campaign would need. So this one fix leaves something behind that the other three don't: not just a fixed problem, but a live data connection a second module could actually use.

**3\. Raising the upsell without it looking opportunistic**

I wouldn't bring up the Marketing Agent in the same conversation as the fix, or anywhere near the moment the client is frustrated about the gap between 85 percent promised and 62 percent delivered. That's exactly the trap to avoid, fixing something broken and then immediately trying to sell something else reads as manufactured urgency, whether that's the intent or not. I'd wait until automation is visibly back on track, the 80 percent target hit and CSAT recovered, and raise it as its own separate conversation, anchored to something concrete that's already true rather than a pitch: "now that loyalty balances are working inside support, here's what that same connection could do for a win-back campaign on your actual list of lapsed customers, want me to show you what that looks like using your real numbers?" If this ever got pushed on directly, the distinction I'd point to is that the loyalty connection exists because support genuinely needed it. It's an honest byproduct, not something built to set up a sale, and the upsell conversation stands on its own, backed by a real, sizeable lapsed-customer segment shown with their own data, rather than riding on the back of "remember that thing we just fixed for you."

---

## **Question 3**

**Question:** D2.1 List 8 to 10 metrics you would present. For each, give:

1. What it measures.  
2. Why it matters to a D2C brand specifically.  
3. What a healthy number and an unhealthy number look like for this kind of business.

**Answer:** **Group 1: Support health**

**Automation rate**, the percentage of conversations resolved without a person involved. This matters because it directly drives cost per ticket, and it's the number that should be tracking toward whatever was promised during onboarding. A healthy number at six months in is 75 to 85 percent or higher. Unhealthy is anything stalled below 65 percent, or trending downward month over month.

**CSAT specifically on AI-resolved conversations**, kept separate from conversations a human handled. This shows whether automation is trading cost savings for customer trust. Healthy is 4.3 or higher out of 5\. Unhealthy is below 3.8, which is the same threshold that should trigger a deeper look, similar to the earlier diagnostic.

**Breakdown of handoff reasons** (refunds, "I want a human," "didn't understand," other), which shows exactly which knowledge or setup gaps are costing automation. Healthy looks like handoffs concentrated in genuinely new, low-volume issues. Unhealthy looks like handoffs dominated by a known gap that still hasn't been fixed.

**First response time** across WhatsApp and Instagram. Supplement buyers asking whether their order has shipped, or whether a product is safe to take alongside something else, expect a near-instant reply, not a wait measured in hours. Healthy is under a minute. Unhealthy is multiple hours, especially during a campaign spike.

**Group 2: Marketing and revenue, shaped specifically for a supplement brand**

**Repeat purchase or reorder rate**, matched to how the product is actually consumed. This is the metric that should stand out most for this kind of business specifically. Supplements are typically consumed on a set schedule, often a 30-day supply, so the number worth watching is what percentage of customers reorder within roughly 30 to 45 days of running out. Healthy is 40 percent or more reordering within that window. Unhealthy is under 20 percent, which suggests either the product isn't sticking with customers, or nobody's reminding them before they lapse.

**Win-back campaign recovery rate**, the percentage of lapsed customers brought back through win-back messages from the Marketing Agent. Healthy is 5 to 8 percent or higher conversion on a well-targeted lapsed segment. Unhealthy is under 2 percent, which points to poor targeting or customers simply tuning the offers out.

**WhatsApp and Instagram-attributed revenue as a share of total revenue**, which ties engagement spend directly to actual sales rather than just cost savings. Healthy looks like a rising, clearly attributable share, even 10 to 15 percent and growing is meaningful for a channel that didn't exist as a revenue line six months ago. Unhealthy is flat or negligible revenue despite active campaigns going out.

**Group 3: Platform and cost health, the kind of thing a CMO wouldn't think to ask about, but should still see**

**Template category accuracy**, meaning how many templates are correctly filed as Utility versus Marketing, since a misfiled template either gets quietly recategorized (raising cost) or risks enforcement. Healthy is zero flagged recategorizations over the past quarter. Unhealthy is any repeated pattern of templates getting caught in Meta's monthly review, which is real, avoidable spend.

**Messaging cost per resolved conversation**, which ties billing factors (category mix, timing relative to the messaging window, which countries are being messaged) directly to actual unit economics, so cost gets judged against automation gains rather than looked at on its own. Healthy is a number trending down as automation improves and templates stay properly categorized. Unhealthy is a rising cost despite flat or falling message volume.

---

## **Question 4**

**Question:** D2.2 The CMO asks about WhatsApp campaign attribution. In under 100 words, plain enough for a non-technical CMO, answer both:

1. What is the difference between read attribution and click attribution?  
2. Which should they use, and why?

**Answer:** Read attribution credits a sale to anyone who simply opened your WhatsApp message, even if they never tapped anything. It's a bigger number, but some of those people would have bought anyway regardless of the message. Click attribution only counts a sale when someone actually tapped your link, a smaller number, but a much more honest sign that the message itself is what drove the purchase. For deciding whether a campaign is actually working, and where to put budget, use click attribution. It won't make things look better than they are. Read attribution is fine for a rough sense of reach, but not for spending decisions.

---

## **Question 5**

**Question:** D2.3 Write the first three sentences of the QBR, the way a real person opens with a founder. Not corporate language.

**Answer:** "Hey, before we get into any numbers, I just want to say it's been genuinely fun watching your repeat customers start treating the AI more like a person at the brand than a bot. There's some real good news in here, one thing that's still rough and I want to be straight with you about, and one idea I think could actually move revenue, not just cut costs. Let's start with what's actually working, not what looks best on a slide."

---

## **Question 6**

**Question:** D3 Using your table from A3, pick the single best expansion for them. Give all four:

1. The specific problem or opportunity it addresses for this client.  
2. The ROI logic, and the exact data you would pull to prove it.  
3. The one metric you would put in front of them.  
4. The exact message, under 120 words, that opens the conversation.

**Answer:** **1\. The specific problem or opportunity**

This client has already cleared the exact trust bar that determines whether the Marketing Agent makes sense: six months of healthy usage and strong renewals is real evidence they trust the platform with reactive support, even though they've never let it near outbound, revenue-generating messages. The opportunity here isn't "add a feature." It's that every customer who's gone quiet after a support conversation is currently getting little to no re-engagement effort, on a WhatsApp number that's already proven it can hold a good conversation. That's unused potential sitting on infrastructure they already trust, not a brand new ask.

**2\. The ROI logic and the data behind it**

This doesn't need to be a hypothetical case, because six months of real support history already exists in their account. I'd pull the number of customers who had a resolved, positive support interaction and then went quiet for 60 to 90-plus days without reordering. That's concrete, already-true evidence, the same kind of move as the loyalty-points connection mentioned earlier, just using support conversation data instead. The logic is straightforward: these customers didn't leave because something went wrong, their own resolved-ticket history proves that, they simply never had a reason to come back. Even a modest 5 to 8 percent win-back rate on that specific group, measured against their own average order value, is a real, defensible revenue number pulled straight from their own account, not an industry benchmark.

**3\. The one metric to show them**

The number of customers who had a positive, resolved support interaction and haven't reordered in over 60 days. Not an automation number, their support metrics are already strong and don't need re-selling. This one points directly at revenue that's currently sitting on the table, uncaptured.

**4\. The opening message**

"Hey \[Name\], six months in, your support numbers speak for themselves, so I'm not here about that. I pulled one number from your own account: you've got a real chunk of customers who had a good, resolved conversation with support and then just... didn't come back within 60-plus days. Nothing went wrong with them, they just never got a nudge. The same WhatsApp number that's already earning your customers' trust on support could run that re-engagement automatically. Before asking you to commit to anything, I'd rather just run a one-time test send to that exact group so you can see real recovered orders on your own numbers first. Worth trying?"

---

## **Question 7**

**Question:** D4 Write your save plan. Give all four:

1. What you investigate first, and in which data.  
2. Who you talk to internally, and who on the client side.  
3. The reframe you bring to the renewal conversation.  
4. The exact first message you send to reopen the relationship, without sounding alarmed.

**Answer:** **1\. What to investigate first**

Before assuming this is a product problem, I'd rule out anything unrelated first. A login drop, a CSAT dip, and a quiet main contact are just as consistent with someone changing roles, going on leave, or an internal reorg as they are with genuine dissatisfaction. So I'd first check whether the login drop is specific to the main contact or spread across the whole team. If everyone else's activity stayed normal and only this one person dropped off, that points to something personal or organizational rather than a complaint about the product. I'd also check whether the CSAT drift is concentrated in one specific handoff type, like refunds or a spike in "I want a human," or if it's spread thin and low-grade across everything. A concentrated spike usually points to one fixable incident. A broad drift usually points to slower-building frustration. And before any of that, I'd go back to the original handoff notes from onboarding first, not last, to check whether something was already flagged back then that never got properly closed out. If it was, that changes what I lead with entirely.

**2\. Who to talk to**

Internally, I'd talk to whoever has recently handled this account's support history and any escalations, since they'd know about friction I haven't seen yet, and the implementation engineer who ran the original onboarding handoff, specifically to check those stakeholder notes again for anything relevant. On the client side is where the real judgment call is. I wouldn't go straight to the quiet main contact with "we've noticed a drop," since that's exactly the alarmed tone to avoid. If the handoff notes point to a secondary contact from onboarding, someone in operations, or anyone else who championed the rollout alongside or instead of the now-quiet contact, I'd reach out to them with a normal, low-key check-in, not framed as "your colleague's gone quiet," just an ordinary touch base, to get honest context without it looking like I'm going around the main contact. If there's no secondary contact in the notes, I'd go straight to the main contact, but with the light-touch message below, not an investigation.

**3\. The reframe for the renewal conversation**

Not "why haven't you logged in," which sounds accusatory, and not "your contract's up in six weeks," which adds pressure at exactly the wrong moment and makes the whole outreach look self-serving. The real reframe is moving away from usage as a scorecard and renewal as a negotiation, and toward what's actually been delivered so far and what's coming next, treating the renewal date as incidental rather than the reason for the call. The conversation I want to have is "here's what's working, here's what I want to fix, here's what I think is worth doing next quarter," the same conversation I'd want to have at month three just as much as month six, not one that only exists because a contract date is coming up.

**4\. The first message**

"Hey \[Name\], hope things have been good on your end. It's been a few months since we properly checked in, so I wanted to grab 15 minutes whenever's convenient, partly to hear how things are feeling on your side, and partly because I've got an idea for next quarter I think could genuinely move the needle for you. No rush, whenever works."

---

## **Question 8**

**Question:** D5 Write your reply to the client, under 300 words. It must cover all three:

1. At least three specific problems, in either their execution or their measurement.  
2. Why their conclusion is premature.  
3. Concrete changes for the next campaign: segmentation, attribution settings, and timing.

**Answer:** Thanks for sending over the numbers. I want to gently push back on "this failed," because I think the data is actually telling a more specific, more fixable story.

There are three concrete problems here, before we even talk about the channel itself. First, a 71 percent delivery rate means nearly 15,000 contacts never even received the message, which points to a list-hygiene issue, stale or invalid numbers, or a phone number quality problem, not evidence that the channel doesn't work. Second, of everyone who received it, 45 percent read it but only 2.1 percent clicked, and that gap tells us something specific: people saw the message and weren't moved to act, which is about the offer or the creative, not WhatsApp itself. Third, I don't have confirmation this list was actually segmented. If it went out to the full 50,000, including contacts who've been inactive for a long time, that alone would drag down delivery, read, and click rates all at once, making it impossible to tell whether the channel underperformed or we simply messaged the wrong people.

On "this failed" specifically, that conclusion sits inside a contradiction in your own numbers. You already have 1.8 lakh rupees in attributed revenue, checked the morning after, on a 7-day attribution window that hasn't even closed yet. Calling this a failure a few hours in, on a window that's still running, isn't really supported by the same data being used to make that call.

For the next send, three concrete changes: on segmentation, send only to contacts with a genuine recent interaction or purchase, not the full list, so delivery and read rates reflect people who are actually engaged. On attribution, shift primary reporting to click-based rather than read-based, since it's a stricter, more honest signal of real intent, and let the 7-day window fully close before judging results. On timing, test two different send times against a small slice of the list first, since WhatsApp read rates are highly sensitive to timing, and right now we're guessing.

Let's go through the delivery breakdown together this week before we decide anything about the channel itself.

# Part E. Judgment Under Pressure

# **Part E: Judgment Under Pressure**

## **Question 1**

**Question:** E1.1 Write your exact WhatsApp reply to the founder, the way you would actually send it at 9:47 PM.

**Answer:** "Got it, I know they placed that order expecting free shipping, and that's on us to make right, not on you to fight with them about. I'm pulling up the exact conversation right now to see what happened. Within the hour I'll come back to you with what I found and what we're doing about that specific customer's order, at minimum, we'll make the shipping right on our end so they're not the one stuck paying for our mistake. I'm not going quiet on this."

---

## **Question 2**

**Question:** E1.2 Write the internal Slack message you send your team right after.

**Answer:** 🚨 Live client issue, need eyes now

\[Client\]'s founder just messaged me directly at 9:47pm. Their AI Support Agent told a customer "free shipping on all orders," that's not our policy, and the customer already placed an order expecting it.

Need three things in parallel, right now:

1. Pull the exact conversation and decision trace for that reply. Was it grounded in any source at all when it said "free shipping," or did it just make that up?  
2. Check whether this is a one-off or still happening. Search this client's conversations from tonight for anything similar about shipping. If it's said this to more than one customer, the urgency changes a lot.  
3. Pull this client's current shipping policy source. Is it missing entirely, or pointing to something outdated, like an old promo page?

I've already told the founder I'll have an update within the hour. Please move fast, I'll jump on a call if that's quicker than Slack. Tagging whoever owns this client's setup.

---

## **Question 3**

**Question:** E1.3 List, in order, every step you take over the next 12 hours. For each step, say:

1. What you investigate.  
2. Who you talk to.  
3. What you tell the client, and when.

**Answer:** **0 to 15 minutes: stop things from getting worse, before we even know the root cause.** There's nothing conclusive to investigate yet, this is a precaution, not a diagnosis. I talk to whoever owns this client's setup, on whatever channel is fastest, a call if that beats Slack. The action here matters more than communication: regardless of what turns out to be wrong, I put an approval step in place for any shipping-cost or policy claims from this client immediately. If the grounding source is missing or outdated, this stops any further wrong answers from going out while we figure out what happened. I don't tell the client anything yet, it's too early, and taking action matters more right now than sending a premature update.

**15 to 45 minutes: figure out how widespread this is.** I search this client's conversations from tonight for any other instance of a shipping-related claim, to find out if this happened to one customer or several. I'm talking with whoever's already pulling the transcript and grounding sources. Still nothing to the client yet, I'm still inside the one-hour window I already committed to.

**Around the 60-minute mark: the update I promised.** By now I should have the transcript, an answer on scope (one customer or more), and a rough idea of what went wrong. I go straight to the founder, since this is the deadline I set for myself, and going quiet past it would undercut what I already told them. I share what was said, how many customers it reached, my current best guess at the cause, and the stopgap already in place, shipping claims are now gated. I also raise, but don't decide on my own, the question of what happens with the affected customer's order, which leads into the next step.

**60 to 90 minutes: decide what happens with the affected customer's order.** I look at what the order is actually worth, and weigh the cost of honoring the free shipping against the damage to the relationship if the brand goes back on something their own AI told the customer. I bring this to the founder, since it's their call, not mine, but my recommendation is to honor the free shipping, or refund the shipping cost, on this one order regardless of general policy, since the customer acted in good faith on what they were told. Arguing over fine print with one already-upset customer over a single order isn't worth what it costs in goodwill. I share my recommendation as advice, and let the founder make the final call.

**90 minutes to 3 hours: the actual root-cause investigation.** I dig into whether the shipping policy was ever loaded as a grounding source for this client in the first place, and separately, whether there's an enforced rule requiring an ungrounded cost or policy claim to escalate instead of being answered outright. I work with engineering directly on this, looking into the actual grounding setup for this client's workspace.

**By the next morning: the permanent fix, designed and tested.** I work with whoever implements the grounding and escalation rules, and I test it myself before calling it done rather than just assuming a configuration change went in cleanly.

**Around the 12-hour mark: closing the loop with the founder.** Not silence after that first update, a same-day follow-up explaining the root cause in plain terms, confirming the fix has shipped and been tested, and confirming what happened with the affected customer's order.

---

## **Question 4**

**Question:** E1.4 Answer both:

1. What in the agent's setup most likely let it invent "free shipping"?  
2. Sagepilot grounds answers in sources and supports approval gates. Describe the permanent fix, and how you verify it holds.

**Answer:** **1\. What let it happen**

I think it's genuinely both causes, and naming just one would understate how serious this is. The immediate cause is almost certainly that the shipping policy was never loaded in as a grounding source for this client, so when asked directly, the model filled that gap with a plausible-sounding, common industry assumption (free shipping is something a lot of D2C brands offer) instead of an actual fact. But the reason that answer was ever allowed to reach a customer is the second, more serious gap. By Sagepilot's own design, answers are supposed to stay grounded in real sources, never guessed, and hand off to a person when it isn't sure. A properly enforced rule should have caught this regardless of whether the shipping policy document existed, by refusing to make a claim that costs the business money with no traceable source behind it, and escalating instead. The fact that it answered confidently instead of escalating means that safeguard wasn't actually enforced for this kind of claim, and that's the deeper, more important problem to fix. A missing document is just a content gap. A missing safeguard is a systemic one.

**2\. The permanent fix, and how I'd verify it**

The fix has two parts, one for each gap. First, load the client's actual, current shipping policy in as a real grounding source, so there's something true to point to. Second, and this is the more important piece, set up shipping cost, discounts, and any other financially binding claims as a category that requires a citation to a live source before the agent can answer at all. If no source is found, it has to escalate instead, no exceptions, no matter how reasonable its own guess might sound.

To verify this holds, I wouldn't just re-ask the exact same question that caused the problem and call it done. I'd try several differently worded, leading questions designed to trigger the same failure: "do you offer free shipping?", "is shipping included?", "I heard shipping's free right now, is that true?", "what's your shipping policy?" and confirm that every single one either cites the real policy correctly or escalates cleanly, with none of them producing a confident answer that isn't actually grounded in anything. I'd also spot-check a sample of real shipping-related conversations from the following week, not just my own test questions, to make sure the safeguard is actually working in live traffic, not only in the scenarios I happened to think to test myself.

---

## **Question 5**

**Question:** E2.1 Rank all 8 in the order you address them. For each, in two to three sentences, say what you do first and why.

**Answer:** **G, the Meta restriction with WhatsApp fully down.** Every minute this goes on, the damage keeps adding up across their entire business, not just one part of it, and my first move here is light: trigger the escalation and get them a stopgap channel today, not hours of hands-on work, so I can move on to the next fire quickly.

**A, go-live Wednesday with the developer silent since Friday.** This has already been quietly stuck for three days, and the deadline is now only two days away, so the damage has been building even before I noticed it this morning. My first move is a firm, fast call to get a developer actually responding today, not me trying to debug their integration myself.

**C, the CSAT drop the client hasn't noticed yet.** This is a risk I caught on my own, not something they raised, and it's still fresh, from just last week, which means there's still a real window to diagnose and fix it before it turns into something like the next two accounts. Acting today, while it's still recent and specific, is what keeps it from growing into a bigger problem later.

**E, 14 days of silence from an account that used to be very active.** Same category of risk as C, just further along and harder to reverse. I'd still reach out today with something light-touch, but I'm being honest with myself that this one may already be a tougher save than C.

**F, the client who wants to cancel.** This one is explicit and fully out in the open, I already know exactly what's bothering them, so there's no investigating needed, just a same-day, low-pressure message. It's serious, but unlike the four above it, it isn't actively getting worse minute by minute.

**B, the custom Diwali flow due Thursday.** A real deadline that needs actual design and testing work, so it needs attention today to leave enough time, but it's a scheduled deliverable, not a live or quietly worsening risk.

**H, the client asking for 12 SOPs by end of week, for the third time.** This needs a firm, same-day response about scope, but the real issue here is a boundary problem, not any harm to the client, making it the lowest-stakes item that still needs a response today.

**D, the happy client asking about voice AI.** No urgency at all, a warm reply today keeps the momentum going, but it rightly comes last.

---

## **Question 6**

**Question:** E2.2 Which single account is the biggest risk to Sagepilot's revenue? Explain your reasoning in detail.

**Answer:** I want to keep this separate from how I ranked things above, because I don't think the two questions should have the same answer. G sits at the top of my action list because it's the account where doing nothing costs the most per minute, but "most urgent" and "biggest revenue risk" aren't actually the same question, and I think the honest answer here is E, not G, and not F either.

Here's the reasoning. F is loud and completely out in the open, I know exactly what's wrong and have a real, if narrow, chance to fix it, because the client is still talking to me. G is a genuine crisis, but it's something that happened to them, a Meta restriction, not evidence that Sagepilot itself let them down. Once it's resolved, there's no real reason the relationship should be damaged, assuming we fix it fast. E is a different kind of problem entirely: 14 days of silence, an account that used to be active, and, most importantly, no complaint at all. That silence isn't a good sign. The same pattern that shows up with a renewal at risk usually holds here too, quiet disengagement tends to come before quiet churn, and by the time it becomes explicit, a "we're not renewing," the decision has often already been made internally, with nothing left to actually intervene on. F still gives me a chance to make my case. E might mean there's no case left to make by the time I find out something's wrong.

So G is my top priority to act on today, but E is the account I'd actually flag as the biggest risk to revenue, precisely because it's the one where I have the least information and the least time before it becomes something I can't fix.

---

## **Question 7**

**Question:** E2.3 Write the exact WhatsApp message you send Client F on Monday morning. Under 100 words. Keep them, but promise nothing you cannot deliver.

**Answer:** "Hey \[Name\], got your message about the platform feeling like too much to learn, and that's a fair thing to bring up. Before anything else, can we grab 20 minutes this week where I just handle the setup myself, so it's completely off your plate? I'd honestly rather do the work than ask you to learn it. What's a good time Tuesday or Wednesday?"

---

## **Question 8**

**Question:** E3.1 A customer messages on WhatsApp: their dog refused the food, and they want a refund. Write the complete instructions for the agent. Cover every condition and branch, including at least these five edge cases:

1. The customer does not have their order number.  
2. Delivery was exactly 7 days ago.  
3. The bag is already opened, but they demand a refund anyway.  
4. The customer becomes angry and threatens a chargeback.  
5. The point at which the agent must hand off to a human.

**Answer:** **The governing principle, stated plainly to the agent:** the outcome here depends on only two facts, how many days have passed since delivery, and whether the product has been opened. The customer's stated reason (their dog wouldn't eat it) doesn't change which outcome applies. The agent should acknowledge the complaint with genuine empathy, but shouldn't let sympathy override policy, and shouldn't invent an exception for "the product didn't work as expected," since no such exception exists in the actual policy.

**Step 1: confirm the order number and delivery date before committing to anything.** This comes first, always, no exceptions.

If the customer doesn't have their order number, the agent doesn't refuse to help and doesn't guess either. It acknowledges the complaint and asks for the phone number or email the order was placed under, or an approximate order date, to look it up. No outcome, refund, replacement, or otherwise, gets stated until the order is actually identified. If it can't be found through the conversation, it hands off to a person.

**Step 2: once the order and delivery date are confirmed, branch based on how many days have passed.**

On the "exactly 7 days" question: the policy as written doesn't say whether day 7 counts as inside or outside the window. Rather than let the agent quietly decide that on its own in the moment, which is exactly the kind of confident guess on unclear ground that caused the earlier free-shipping incident, this gets settled before the agent ever goes live, by asking the client directly which they mean. I'd suggest the more generous option, counting day 7 as still within the window, as the lower-friction default, but the client makes the final call, and whatever they decide becomes a fixed, unambiguous rule built into the agent's instructions, not something it works out live. Once that's settled, "exactly 7 days ago" stops being an edge case and just becomes a normal one.

If more than 7 days have passed (based on whichever rule the client confirmed), there's no refund and no replacement, regardless of whether the product was opened. State this once, plainly. Offer to log feedback about the product. Don't offer any compensation outside the stated policy, no matter how the complaint is phrased.

If it's within 7 days and the product is unopened and sealed, process a full refund.

If it's within 7 days and the product has been opened, no refund, offer a one-time replacement with a different variant instead.

**Step 3: the customer demands a refund anyway, even though the product's been opened.** Acknowledge their frustration once, restate the policy clearly and just once (opened items get a replacement, not a refund), and offer that replacement as the actual resolution on the table. Don't repeat the denial a second time with stronger language, and don't improvise a partial refund or discount to smooth things over, that's simply not an option here. If they keep pushing after that one clear restatement, hand off to a person.

**Step 4: the customer gets angry or threatens a chargeback.** This doesn't change the outcome being offered. The agent doesn't cave and offer a refund it was never authorized to give, because doing that under pressure would teach every future customer that getting angry is the fastest way around the policy. It does trigger an immediate handoff though: acknowledge the frustration directly, say once that this is being passed to a person on the team, and hand it off with full context attached, order number, delivery date, opened or unopened status, and whatever's already been offered. The agent doesn't keep negotiating past this point.

**Step 5: when the agent must hand off to a human, stated explicitly.**

* The order number or delivery date can't be confirmed through conversation.  
* The customer disputes the delivery date itself, claiming it arrived later than the system shows. The agent doesn't take a side on a factual disagreement like that.  
* The customer becomes angry or threatens a chargeback or legal action.  
* The customer explicitly asks to speak to a person.  
* The customer asks for something outside the four defined outcomes, like a discount code instead of a refund or replacement. The agent doesn't improvise outside what's actually in the policy.

---

## **Question 9**

**Question:** E3.2 Describe how you test this before it goes live. Give both:

1. The specific test cases you run.  
2. What a pass looks like for each, so the agent cannot mis-promise the way the free-shipping agent did.

**Answer:** **1\. Test cases, covering every branch and edge case above**

* Unopened, sealed, delivered 3 days ago. Expect a full refund.  
* Unopened, sealed, delivered exactly 7 days ago, following whichever rule was confirmed. Expect the outcome matching that rule, applied the same way every time.  
* Unopened, sealed, delivered 8 days ago. Expect no refund and no replacement.  
* Opened, delivered 2 days ago. Expect a replacement offered, not a refund.  
* Opened, delivered 2 days ago, customer demands a refund anyway after being told no once. Expect one restatement plus the replacement offer, then a handoff if they keep pushing.  
* Customer has no order number, only gives a first name. Expect the agent to ask for a phone number, email, or approximate date, and not proceed based on a guess.  
* Customer claims delivery was "over a week ago" but the system shows 5 days. Expect a handoff, not the agent picking a side on the disagreement.  
* Customer says "this is fraud, I'm doing a chargeback" mid-conversation. Expect an immediate handoff, with no further offers made.  
* Customer asks for a discount code instead of a refund or replacement. Expect a handoff, not an improvised discount.  
* A leading, ambiguous question with no clean match in policy, taken directly from the lesson in the free-shipping incident: "Can you just cover the cost since my dog got sick from it?" Expect the agent to recognize this isn't covered by any stated branch, since there's no product-safety or liability clause in the policy, and hand off, rather than confidently making up a resolution the way the earlier agent invented free shipping.

**2\. What a pass actually looks like**

A pass needs two things to be true at once, not just "it landed on the right answer." First, the agent's conclusion has to exactly match the correct policy branch for that scenario. Second, and this is the part that actually matters most, the agent must never state a refund, a replacement, or any resolution at all before both the order number and delivery date have been explicitly confirmed in that conversation. A fail is any case where the agent commits to an outcome first and asks clarifying questions afterward, or skips confirmation because the case "seemed obvious." On the exact 7-day case specifically, a pass means the agent applies the one confirmed rule consistently across repeated attempts, not different answers depending on how the question is phrased. And on the last test case, the one shaped like the free-shipping incident, a pass strictly means the agent recognizes that no policy branch covers the request and hands it off. Any confident, sympathetic-sounding answer invented on the spot is a fail, full stop, no matter how reasonable it sounds, because that's exactly the failure this whole exercise is meant to prevent.

